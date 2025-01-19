import pytest

from tests.utils.docker_utils  import start_database_container



@pytest.fixture(scope="session", autouse=True)
def db_session():
    container = start_database_container()
    yield container
    container.stop()
    container.remove()

def test_database_container(db_session):
    assert db_session.status == "running"