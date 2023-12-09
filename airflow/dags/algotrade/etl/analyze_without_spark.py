import pandas as pd
from datetime import timedelta
from redis import Redis
from loguru import logger

from src.core.config import REDIS_CONFIG, NODES
from src.load.clickhouse import ClickhouseLoader
from src.extract.clickhouse import ClickhouseExtractor
from src.transform.prediction import PredictionTransformer
from src.state.redis import RedisState


def prediction(df: pd.DataFrame):
    for _, elem in df.iterrows():
        yield elem.to_dict()


def run():
    extractor = ClickhouseExtractor(
        host=NODES[0].HOST,
        port=NODES[0].PORT,
        user=NODES[0].USER,
        password=NODES[0].PASSWORD,
        alt_hosts=[f'{NODE.HOST}:{NODE.PORT}' for NODE in  NODES[1:]],
        settings={'use_numpy': True}
    )

    # TODO: Trading algorithm
    query = 'SELECT * FROM default.candles ORDER BY begin DESC'
    df = pd.DataFrame(extractor.extract(query=query))
    
    df['algorithm'] = 'ALG1'
    df['value'] = df['close'] + 10
    df['timestamp'] = df['begin'] + timedelta(minutes=5)
    
    prediction_df = df[['secid', 'algorithm', 'value', 'timestamp']]
    ##

    redis = Redis(
        host=REDIS_CONFIG.HOST, port=REDIS_CONFIG.PORT, password=REDIS_CONFIG.PASSWORD
    )
    state = RedisState(redis=redis)

    logger.info('[*] Loading predictions to clickhouse')

    result_transformer = PredictionTransformer()
    loader = ClickhouseLoader(
        host=NODES[2].HOST,
        port=NODES[2].PORT,
        user=NODES[2].USER,
        password=NODES[2].PASSWORD,
        alt_hosts=[f"{NODE.HOST}:{NODE.PORT}" for NODE in NODES],
        state=state,
    )

    result_data = result_transformer.transform(
        prediction(prediction_df),
        to_dict=True
    )

    result = loader.load(data=result_data, table='predictions')
    logger.info(result)

    logger.info('[+] Success loading predictions to clickhouse')
