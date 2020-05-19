import pytest
import requests


@pytest.fixture(scope="session")
def unlogin_fixture():
    s=requests.session()
    return s
