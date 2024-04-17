# How to Run the tests
The tests are done in python and can be executed by running pytest on the root folder once the `docker-compose up -d` is done and all the container are up and running locally.

## Python packages
The test case uses "request" library to make the API calls and get the data from the server. 
"random" library is used to generate random user info.

## Test case execution
pytest execution in the terminal will run all the test files with test_ and give the results.

## command for run
go to the root file and run the test by executing 'pytest'