import pytest
from shared.app_logging.factory import init_logger

@pytest.fixture(scope="session", autouse=True)
def init_logger_fixture():
    """
    Initialize the root logger for the test session.

    This fixture is automatically used for the entire test session to ensure that
    logging is configured before any tests are run. It sets up the root logger
    with a stream handler and a file handler, allowing logs to be captured both
    in the console and in a log file.
    """
    init_logger()