import logging
import logging.config
import connexion
import requests
import yaml
from flask_cors import CORS

statuses = {
    "receiver": "",
    "storage": "",
    "processing": ""
}

def check():
    try:
        # res1 = requests.get("http://receiver:8080/receiver/health")
        res1 = requests.get("http://localhost:8080/receiver/health")
        if res1.status_code == 200:
            statuses["receiver"] = "Running"
    except:
        statuses["receiver"] = "Down"
    try:
        # res2 = requests.get("http://storage:8090/storage/health")
        res2 = requests.get("http://localhost:8090/storage/health")
        if res2.status_code == 200:
            statuses["storage"] = "Running"
    except:
        statuses["storage"] = "Down"
    try:
        # res3 = requests.get("http://processing:8100/processing/health")
        res3 = requests.get("http://localhost:8100/processing/health")
        if res3.status_code == 200:
            statuses["processing"] = "Running"
    except:
        statuses["processing"] = "Down"
    return statuses

app = connexion.FlaskApp(__name__, specification_dir='')
app.add_api("openapi.yml", strict_validation=True, validate_responses=True, base_path="/health")
CORS(app.app)

with open('log_conf.yml', 'r') as f:
    log_config = yaml.safe_load(f.read())
    logging.config.dictConfig(log_config)

logger = logging.getLogger('basic')

if __name__ == "__main__":
    app.run(port=8110)
