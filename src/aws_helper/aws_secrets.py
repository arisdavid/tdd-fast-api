import logging

import boto3
from botocore.exceptions import ClientError
from decouple import config

logging.basicConfig(level=logging.INFO)


def get_secret():
    secret = None
    secret_name = config("DB_NAME")
    region_name = config("AWS_DEFAULT_REGION")

    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(service_name="secretsmanager", region_name=region_name)

    try:
        get_secret_value_response = client.get_secret_value(SecretId=secret_name)
    except ClientError:
        logging.exception("Unable to retrieve secret")
    else:
        if "SecretString" in get_secret_value_response:
            secret = get_secret_value_response["SecretString"]
    return secret
