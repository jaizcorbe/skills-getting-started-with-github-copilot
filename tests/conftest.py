import copy

import pytest
from fastapi.testclient import TestClient

import src.app as app_module


@pytest.fixture(scope="session")
def client():
    """A TestClient for the FastAPI app."""
    return TestClient(app_module.app)


@pytest.fixture(autouse=True)
def reset_activities():
    """Reset the in-memory activities store after each test."""
    original = copy.deepcopy(app_module.activities)
    yield
    app_module.activities = original
