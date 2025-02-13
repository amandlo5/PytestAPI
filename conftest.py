import json

import pytest
from datetime import datetime
import os

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    report_dir = 'reports'
    # Ensure the reports directory exists
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")  # Adjusted the datetime format
    config.option.htmlpath = os.path.join(report_dir, f"report_{now}.html")



@pytest.fixture(scope='session',autouse=True)
def setup_teardown():
    print('Start request')
    yield
    print('End Request')

@pytest.fixture()
def load_user_data():
    json_file_path = os.path.join(os.path.dirname(__file__),"data","data.json")
    with open(json_file_path,'r') as json_file:
        data = json.load(json_file)
    return data

@pytest.fixture()
def load_res_data():
    json_file_path = os.path.join(os.path.dirname(__file__),"data","response.json")
    with open(json_file_path,'r') as json_file:
        data = json.load(json_file)
    return data