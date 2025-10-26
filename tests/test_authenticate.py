import json
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_authenticate():
    """
    Test The login using FastAPI
    """
    #Test 1: Correct Credentials
    response = client.post('/login', data={
        "username": "admin@kolarel.com",
        "password": "1515"
    })

    print(f"Response Text: {response.text}")
    assert response.status_code == 200
    assert json.loads(response.text)['token_type']  == "bearer"
    

    #Test 2: Unregistered email
    response2 = client.post('/login', data={
        "username": "alex@kolarel.com",
        "password": "1515"
    })
    assert response2.status_code == 404

    #Test 3: Incorrect password
    response3 = client.post('/login', data={
        "username": "admin@kolarel.com",
        "password": "1015"
    })

    assert response3.status_code == 401
    assert json.loads(response3.text)['detail']  == "Incorrect password"