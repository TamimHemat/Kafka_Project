import json
import datetime
import requests
import yaml
import logging
import logging.config
from flask_cors import CORS
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import connexion
from connexion import NoContent
from apscheduler.schedulers.background import BackgroundScheduler
from base import Base
from stats import Stats

DB_ENGINE = create_engine("sqlite:///stats.sqlite")
Base.metadata.bind = DB_ENGINE
DB_SESSION = sessionmaker(bind=DB_ENGINE)

def get_latest_stats():
    with DB_SESSION() as session:
        result = session.query(Stats).order_by(Stats.last_updated.desc()).first()
        if result:
            return result.to_dict(), 200
        return NoContent, 201

def populate_stats():
    timestamp = datetime.datetime.now() - datetime.timedelta(days=1)
    timestamp = timestamp.strftime('%Y-%m-%dT%H:%M:%SZ')
    last_updated = timestamp
    logger.debug(f'Beginning processing with timestamp: {last_updated}',)
    with DB_SESSION.begin() as session:
        result = session.query(Stats).order_by(Stats.last_updated.desc()).first()
        if result:
            result = result.to_dict()
            last_updated = result['last_updated']
        else:
            result = {
                "max_buy_price": 9.99,
                "num_buys": 0,
                "max_sell_price": 14.99,
                "num_sells": 0,
                "last_updated": timestamp
            }
        # res = requests.get(f"http://storage:8090/storage/buy?timestamp={last_updated}")
        res = requests.get(f"http://localhost:8090/storage/buy?timestamp={last_updated}")
        res = json.loads(res.text)
        if len(res) > 0:
            for item in res:
                if item['item_price'] > result["max_buy_price"]:
                    result["max_buy_price"] = item['item_price']
        # res2 = requests.get(f"http://storage:8090/storage/sell?timestamp={last_updated}")
        res2 = requests.get(f"http://localhost:8090/storage/sell?timestamp={last_updated}")
        res2 = json.loads(res2.text)
        if len(res2) > 0:
            for item in res2:
                if item['item_price'] > result["max_sell_price"]:
                    result["max_sell_price"] = item['item_price']
        len1 = len(res)
        len2 = len(res2)
        if len1 == 0 and len2 == 0:
            new_stats = Stats(result["max_buy_price"],
                            result["num_buys"],
                            result["max_sell_price"],
                            result["num_sells"], timestamp)
        elif len1 == result["num_buys"] and len2 == result["num_sells"]:
            new_stats = Stats(result["max_buy_price"],
                            result["num_buys"],
                            result["max_sell_price"],
                            result["num_sells"], timestamp)
        elif len1 > result["num_buys"] and len2 > result["num_sells"]:
            new_stats = Stats(result["max_buy_price"],
                                len1,
                                result["max_sell_price"],
                                len2, timestamp)
        elif len1 > result["num_buys"] and len2 == result["num_sells"]:
            new_stats = Stats(result["max_buy_price"],
                                len1,
                                result["max_sell_price"],
                                result["num_sells"], timestamp)
        elif len1 == result["num_buys"] and len2 > result["num_sells"]:
            new_stats = Stats(result["max_buy_price"],
                                result["num_buys"],
                                result["max_sell_price"],
                                len2, timestamp)
        else:
            new_stats = Stats(result["max_buy_price"],
                                result["num_buys"],
                                result["max_sell_price"],
                                result["num_sells"], timestamp)           
        session.add(new_stats)
    return NoContent, 201

def health():
    logger.info("Health endpoint called for Processing")
    return NoContent, 200

def init_scheduler():
    sched = BackgroundScheduler(daemon=True)
    sched.add_job(populate_stats, 'interval', seconds=app_config['period'])
    sched.start()

app = connexion.FlaskApp(__name__, specification_dir='')
app.add_api("openapi.yml", base_path="/processing",strict_validation=True,validate_responses=True)
CORS(app.app)

with open('app_conf.yml', 'r') as f:
    app_config = yaml.safe_load(f.read())

with open('log_conf.yml', 'r') as f:
    log_config = yaml.safe_load(f.read())
    logging.config.dictConfig(log_config)

logger = logging.getLogger('basic')

if __name__ == "__main__":
    init_scheduler()
    app.run(port=8100, use_reloader=False)
