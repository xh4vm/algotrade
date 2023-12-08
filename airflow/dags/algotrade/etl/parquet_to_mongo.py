import asyncio
from pyspark.sql import SparkSession
from loguru import logger

from src.core.config import MONGO_CONFIG, HDFS_CONFIG, SPARK_CONFIG
from src.transform.prediction import PredictionTransformer
from src.load.mongo import AsyncMongoLoader, AsyncMongoClient
from src.schemas.prediction import PREDICTION


spark = SparkSession \
    .builder \
    .master(f'{SPARK_CONFIG.DRIVER}://{SPARK_CONFIG.HOST}:{SPARK_CONFIG.PORT}') \
    .appName('algotrade-predictions-load_to_mongo') \
    .getOrCreate()

dataframe = spark.read.schema(PREDICTION).parquet(
    f'{HDFS_CONFIG.DRIVER}://{HDFS_CONFIG.HOST}:{HDFS_CONFIG.PORT}/{HDFS_CONFIG.PATH}/algotrade-predictions'
)

logger.info('[*] Loading predictions to mongo')

result_transformer = PredictionTransformer()
loader = AsyncMongoLoader(client=AsyncMongoClient(settings=MONGO_CONFIG))

result_data = result_transformer.transform(
    (elem.asDict() for elem in dataframe.rdd.toLocalIterator()),
    to_dict=True
)

result = asyncio.run(loader.load(
    db_name=MONGO_CONFIG.DB_NAME,
    collection_name=MONGO_CONFIG.COLLECTION_NAME,
    data=result_data
))
logger.info(result)

logger.info('[+] Success loading predictions to mongo')