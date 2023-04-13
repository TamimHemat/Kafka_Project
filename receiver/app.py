import json
import datetime
import logging
import logging.config
import uuid
import connexion
from connexion import NoContent
from pykafka import KafkaClient
import yaml
from flask_cors import CORS

def process_event(event, endpoint):
    trace_id = str(uuid.uuid4())
    event['trace_id'] = trace_id

    logger.debug(f'Received {endpoint} event with trace id {trace_id}')
    
    client = KafkaClient(hosts=f"{app_config['events']['hostname']}:{app_config['events']['port']}")

    topic = client.topics[app_config['events']['topic']]

    producer = topic.get_sync_producer()

    dic = {
        "type": endpoint,
        "datetime": datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ'),
        "payload": event
    }

    json_str = json.dumps(dic)

    producer.produce(json_str.encode('utf-8'))
    
    logger.info(f"PRODUCER::producing {endpoint} event")
    
    logger.info(json_str)

    return NoContent, 201

# Endpoints
def buy(body):
    process_event(body, 'buy')
    return NoContent, 201

def sell(body):
    process_event(body, 'sell')
    return NoContent, 201

def health():
    logger.info("Health endpoint called for Receiver")
    return NoContent, 200

app = connexion.FlaskApp(__name__, specification_dir='')
app.add_api("openapi.yml", base_path="/receiver", strict_validation=True, validate_responses=True)
CORS(app.app)

with open('app_conf.yml', 'r') as f:
    app_config = yaml.safe_load(f.read())

with open('log_conf.yml', 'r') as f:
    log_config = yaml.safe_load(f.read())
    logging.config.dictConfig(log_config)

logger = logging.getLogger('basic')

if __name__ == "__main__":
    app.run(port=8080)
