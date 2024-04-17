Bug Report


1. Errors in Singnup Server API
GET signupsrv/user does not return the correct username when a valid token is used for the API calls.
Description:
The signupsrv/user API doc states that it "Gets user information for the given token" but when a valid token is used in the API call we do not the user name for which the token was generated but instead "test" is the response for all different tokens that were used.
Steps to reproduce:
    * Invoke an API call towards the signupsrv (/api/v1/signupsrv/user) with valid token
Expected result:
    * Success code with correct user name for whom the token was issued
Actual result:
    * Success code 200 with username as "test" always with any valid token.

2. Errors in Weather server API
GET weathersrv/weather returns valid data when a wrong / invalid token is used for API call.

Description: The user authentication is broken as the token data is not used to authenticate / validate the user and thus the API gives response even when the user's identity can be established.

Steps to reproduce:
    * Invoke an API call towards the weathersrv (/api/v1/weathersrv/user) with invalid token
Expected result:
    * Failure code 404 with authentication failure / Bad request as the token does not identify any user
Actual result:
    * Success code 200 with weather info.
