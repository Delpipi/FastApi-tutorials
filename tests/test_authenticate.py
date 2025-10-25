import requests

headers = {'Content-Type': 'application/json'}

def test_authenticate():
    """
        Test the login process works by making post request and compare
        the status code and response 's body against the expected value
    """
    #Test 1: Correct Credentials
    response = requests.post('http://localhost:8000/login', json={
        "email": "admin@kolarel.com",
        "password": "1515"
    }, headers=headers)

    assert response.status_code == 200
    assert response.json()['name'] == 'Alexandre Paul'

    #Test 2: Unregistered email
    response2 = requests.post('http://localhost:8000/login', json={
        "email": "alex@kolarel.com",
        "password": "1515"
    }, headers=headers)
    assert response2.status_code == 404

    #Test 3: Incorrect password
    response3 = requests.post('http://localhost:8000/login', json={
        "email": "admin@kolarel.com",
        "password": "1015"
    }, headers=headers)

    assert response3.status_code == 200
    assert response3.json() == False