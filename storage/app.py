import json
import datetime
import logging
import logging.config
from threading import Thread
import yaml
import mysql.connector
import pymysql
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pykafka
from pykafka import KafkaClient
from pykafka.common import OffsetType
import connexion
from connexion import NoContent
from flask_cors import CORS
from base import Base
from buy import Buy
from sell import Sell

with open('app_conf.yml', 'r') as f:
    app_config = yaml.safe_load(f.read())

with open('log_conf.yml', 'r') as f:
    log_config = yaml.safe_load(f.read())
    logging.config.dictConfig(log_config)

logger = logging.getLogger('basic')

DB_ENGINE = create_engine(f"mysql+pymysql://{app_config['user']}:{app_config['password']}@{app_config['hostname']}:{app_config['port']}/{app_config['db']}", pool_pre_ping=True)
Base.metadata.bind = DB_ENGINE
DB_SESSION = sessionmaker(bind=DB_ENGINE)

# Endpoints
def buy(body):
    with DB_SESSION.begin() as session:
        buy = Buy(body['buy_id'], body['item_name'], body['item_price'], body['buy_qty'], body['trace_id'])
        session.add(buy)
    return NoContent, 201

def get_buys(timestamp):
    session = DB_SESSION()
    rows = session.query(Buy).filter(Buy.date_created >= timestamp)
    data = []
    for row in rows:
        data.append(row.to_dict())
    session.close()
    logger.debug(f"get_buys called with timestamp {timestamp} and returned {len(data)} results")
    return data, 200

def sell(body):
    with DB_SESSION.begin() as session:
        sell = Sell(body['sell_id'], body['item_name'], body['item_price'], body['sell_qty'], body['trace_id'])
        session.add(sell)
    return NoContent, 201

def get_sells(timestamp):
    session = DB_SESSION()
    rows = session.query(Sell).filter(Sell.date_created >= timestamp)
    data = []
    for row in rows:
        data.append(row.to_dict())
    session.close()
    logger.debug(f"get_sells called with timestamp {timestamp} and returned {len(data)} results")
    return data, 200

def process_messages():
    client = KafkaClient(hosts=f"{app_config['events']['hostname']}:{app_config['events']['port']}")
    topic = client.topics[app_config['events']['topic']]
    messages = topic.get_simple_consumer(
        reset_offset_on_start = False,
        auto_offset_reset = OffsetType.LATEST
    )
    for msg in messages:
        msg_str = msg.value.decode('utf-8')
        msg = json.loads(msg_str)
        payload = msg['payload']
        msg_type = msg['type']
        with DB_SESSION.begin() as session:
            logger.info("CONSUMER::storing buy event")
            logger.info(msg)
            if msg_type == "buy":
                item = Buy(**payload)
            elif msg_type == "sell":
                item = Sell(**payload)
            session.add(item)
    messages.commit_offsets()

def health():
    logger.info("Health endpoint called for Storage")
    return NoContent, 200

app = connexion.FlaskApp(__name__, specification_dir='')
app.add_api('openapi.yml', base_path="/storage", strict_validation=True, validate_responses=True)
CORS(app.app)

if __name__ == "__main__":
    tl = Thread(target=process_messages)
    tl.daemon = True
    tl.start()
    app.run(port=8090)
