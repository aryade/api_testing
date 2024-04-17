import requests

api_url = "http://127.0.0.1:8080/api/v1/weathersrv"
user_api_url = "http://127.0.0.1:8080/api/v1/signupsrv"

username = "newUser"
passwd = "testPass"

def test_getweather():
    data = {
        "name": username,
        "passwd": passwd,
    }
    response = requests.post(user_api_url+"/signup", params=data)
    assert response.status_code == 200 # Make sure that API response is successful
    data = response.json() # Make sure that the response is not empty
    assert data != ""
    
    splitLines = data.splitlines()
    splieString = splitLines[0].split()
    token = splieString[1]
    print(token)

    # Token should not be empty
    assert token != ""
    data = {
        "token": token
    }
    print(data)
    response = requests.get(api_url+"/weather", params=data)
    assert response.status_code == 200

    data = response.json()
    assert data != ""

def test_getweather_incorrect_token():
    data = {
        "token": "wrong token"
    }
    print(data)
    response = requests.get(api_url+"/weather", params=data)
    
    #  we shouldnt get response status code as "200", when we running with the wrong token. but the code is buggy.
    assert response.status_code == 422
    data = response.json()
    #assert data != ""
    assert data['detail'][0]['msg'] == "field required"

def test_getweather_no_token():
    response = requests.get(api_url+"/weather")
    assert response.status_code == 422
    data = response.json()
    assert data['detail'][0]['msg'] == "field required"