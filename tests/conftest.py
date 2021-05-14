import os
from tests.utils import login_util
from flask import Flask, Response
from flask.wrappers import Request
import pytest
from src.app import create_app

os.environ["ALLOW_EXPIRED_TOKENS"] = "1"


@pytest.fixture
def client():
    return create_app().test_client()


@pytest.fixture
def new_casting_assistant_token():
    username = os.getenv("CASTING_ASSISTANT_USER")
    password = os.getenv("CASTING_ASSISTANT_PWD")
    return login_util(username, password)


@pytest.fixture
def new_casting_director_token():
    username = os.getenv("CASTING_DIRECTOR_USER")
    password = os.getenv("CASTING_DIRECTOR_PWD")
    return login_util(username, password)


@pytest.fixture
def new_executive_producer_token():
    username = os.getenv("EXECUTIVE_PRODUCER_USER")
    password = os.getenv("EXECUTIVE_PRODUCER_PWD")
    return login_util(username, password)


@pytest.fixture
def casting_assistant_headers():
    expired_token = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ilk1S3MwNE5KTGhfcWl4eC1Mc3AzVSJ9.eyJpc3MiOiJodHRwczovL2hhcHB5MjAwMC51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjA5OGEyODQ5MjAxMzkwMDY4ZWQxYWVmIiwiYXVkIjoiaHR0cDovL2xvY2FsaG9zdC86NTAwMCIsImlhdCI6MTYyMDk2NDA0NywiZXhwIjoxNjIwOTcxMjQ3LCJhenAiOiJrN1pFcU95Qm9QVXMyenF3NXhCSGgxeXRNcnpwbWE2NyIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiXX0.Ae1Xxby-c4dnItyOzC3v9VG_dH9kf3cYwe1TH9uyKeSAgJLKGqfx_-CiuB70Ed8Eb7I2_vzR8uitRAwWjDHGUVNFE1UnYXd03tIVrtH9ycSQ7QTAREUiORE3csajGa2htDLWGGDFRTF9FnbADxPcozW3z8j-hjYC7xb4qntj1O4rQMxovfAjEtuc6D9hHlnxc3aM-Ib2RftxAsnwJTK5f5fwgjPyd_iSjWMWZMnV1IKHWOcEZu5IrcPrA1NlDu77y2cRQwa8NNalYNX-SYaL9qrvqR4DtvunDG5dzCwuVy_tK5hLdLx9QyF3taI2vDep8KRDTPMhQ_q_vN68WLIX5w'
    headers = {
        "Authorization": f"Bearer {expired_token}"
    }
    return headers


@pytest.fixture
def casting_director_token():
    username = os.getenv("CASTING_DIRECTOR_USER")
    password = os.getenv("CASTING_DIRECTOR_PWD")
    return login_util(username, password)


@pytest.fixture
def executive_producer_token():
    username = os.getenv("EXECUTIVE_PRODUCER_USER")
    password = os.getenv("EXECUTIVE_PRODUCER_PWD")
    return login_util(username, password)
