from app import app
from chalice.test import Client
import pytest
import json
import logging


def test_pass():
    assert 0 == 0


# @pytest.mark.skip
def test_get():
    logging.debug('Test pre-signed URL')
    with open('tests/pre-signed-url.json', ) as f:
        data = json.load(f)
    with Client(app, stage_name='dev') as client:
        result = client.lambda_.invoke('handler', data)
        logging.debug("result %s", result.payload)


