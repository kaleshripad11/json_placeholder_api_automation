# conftest.py

import pytest

from utils.api_client_base import Api_Client_Base
from utils.config_reader import get_configs
from utils.read_json_data import read_yaml_data

# Fixtures 
@pytest.fixture(scope="session")
def api_client():
    return Api_Client_Base()

@pytest.fixture(scope="session")
def configs():
    return get_configs()

@pytest.fixture(scope="function")
def api_body():
    return read_yaml_data()