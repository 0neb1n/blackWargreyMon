import json
import pytest
from app import app

@pytest.fixture
def client(request):
    test_client = app.test_client()

    def teardown():
        pass

    request.addfinalizer(teardown)
    return test_client

def test_builds(client):
    response = client.post("/builds", data={"text": "jenkins_slack_command"})
    assert response.status_code == 200
    assert b"jenkins_slack_command" in response.data
