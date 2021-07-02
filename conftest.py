import pytest


@pytest.fixture(scope="session", autouse=True, )
def url():
    """Base url for tests."""
    return "https://petstore.swagger.io/v2/"
