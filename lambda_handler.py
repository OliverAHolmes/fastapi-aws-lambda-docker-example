from mangum import Mangum
from api import app


def lambda_handler(event, context):
    mangum_handler = Mangum(app, lifespan="off")

    return mangum_handler(event, context)
