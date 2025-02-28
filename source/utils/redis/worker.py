import yaml
from flask_redis import FlaskRedis
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

with open('config.yml', 'r') as file:
    config = yaml.safe_load(file)

def SetupRedis(app):
    redis_client = FlaskRedis(app)
    limiter = Limiter(
        get_remote_address,
        app=app,
        storage_uri=f"redis://{config['redis']['ip']}:{config['redis']['port']}",
        storage_options={"socket_connect_timeout": 30},
        strategy="fixed-window",
    )

    return redis_client, limiter