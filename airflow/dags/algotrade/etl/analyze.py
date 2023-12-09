from pyspark.sql import SparkSession
from pyspark.sql.functions import lit
from loguru import logger
from datetime import timedelta

from src.core.config import HDFS_CONFIG, SPARK_CONFIG
from src.schemas.prediction import PREDICTION


spark = SparkSession \
    .builder \
    .master(f'{SPARK_CONFIG.DRIVER}://{SPARK_CONFIG.HOST}:{SPARK_CONFIG.PORT}') \
    .appName('algotrade-predictions-analyze') \
    .getOrCreate()

dataframe = spark.read.schema(PREDICTION).parquet(
    f'{HDFS_CONFIG.DRIVER}://{HDFS_CONFIG.HOST}:{HDFS_CONFIG.PORT}/{HDFS_CONFIG.PATH}/algotrade-candle-clickhouse-to-parquet'
)

dataframe = dataframe.select(
    (dataframe.begin + timedelta(minutes=5)).alias('timestamp'),
    lit('ALG1').alias('algorithm'), 
    (dataframe.close + 10).alias('value')
)

dataframe.write.parquet(
    path=f'{HDFS_CONFIG.DRIVER}://{HDFS_CONFIG.HOST}:{HDFS_CONFIG.PORT}/{HDFS_CONFIG.PATH}/algotrade-predictions',
    mode='overwrite'
)

logger.info('[+] Success analyzing')