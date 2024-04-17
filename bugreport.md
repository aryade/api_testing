# Bug Report

## signupsrv /user API always returning "test" as the username
GET signupsrv/user does not return the correct username when a valid token is used for the API calls.
Description:
The signupsrv/user API doc states that it "Gets user information for the given token" but when a valid token is used in the API call we do not the user name for which the token was generated but instead "test" is the response for all different tokens that were used.

### Steps to reproduce:
    * Invoke an API call towards the signupsrv (/api/v1/signupsrv/user) with valid token
### Expected result:
    * Success code with correct user name for whom the token was issued
### Actual result:
    * Success code 200 with username as "test" always with any valid token.

## signupsrv /validate API Spec has incorrect in parameter text
The documentation for the signupsrv/validate API spec has incorrect text.
Description:
The description in the validate API says,
Validates if Token provided is valid or not. Returns True if valid or False if it is invalid
name: name of the user whose token needs to be renewed

In the above the input is token and not user name and the token is not renewed but a bool is returned to say if the token is valid or not.

## signupsrv /user with invalid token has incorrect return code
GET /user with invalid token return 401 but the spec has 404 with Not Found as the error message.

### steps to recreate
    * Invoke API call towards the singupsrv(/api/v1/signupsrv/user) with invalid token
### Expected result:
    * Failure code 404 with Validation error as the token does not identify any user
### Actual result:
    * Failure code 401

## quotesrv /quote has return codes and error messages not documented in the API spec
GET /quote with invalid token return 401 with error message "token is invalid"
Description:
The API spec has only 200 and 422 as the return code but for invalid token we also get 401

### steps to recreate
    * Invoke API call towards the quotesrv(/api/v1/quotesrv/quote) with invalid token
### Expected result:
    * Failure code 422 with Validation error as the token does not identify any user
### Actual result:
    * Failure code 401.

## weathersrv /weather has no authentication
GET weathersrv/weather returns valid data when a wrong / invalid token is used for API call.

Description: The user authentication is broken as the token data is not used to authenticate / validate the user and thus the API gives response even when the user's identity can be established.

### Steps to reproduce:
    * Invoke an API call towards the weathersrv (/api/v1/weathersrv/user) with invalid token
### Expected result:
    * Failure code 422 with authentication failure / Bad request as the token does not identify any user
### Actual result:
    * Success code 200 with weather info.


In general the API spec return codes do not match the server code as error codes and messages are not properly documented.
The test cases fail as they are verifying the API spec against the server API response.