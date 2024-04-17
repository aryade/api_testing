import requests

quote_api_url = "http://127.0.0.1:8080/api/v1/quotesrv"
user_api_url = "http://127.0.0.1:8080/api/v1/signupsrv"

username = "newUser"
passwd = "testPass"

def test_getquotes():
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
    response = requests.get(quote_api_url+"/quote", params=data)
    assert response.status_code == 200

    data = response.json()
    assert data != ""

def test_getquotes_invalid_token():
    data = {
        "token": "wrong token"
    }
    print(data)
    response = requests.get(quote_api_url+"/quote", params=data)
    assert response.status_code == 401
    data=response.json()
    assert data['detail'] == "token is invalid"

def test_getquote_no_token():
    response = requests.get(quote_api_url+"/quote")
    assert response.status_code == 422
    data = response.json()
    assert data['detail'][0]['msg'] == "field required"