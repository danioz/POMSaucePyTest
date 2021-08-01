# POMSaucePyTest
This is an example of a python framework with the page object model.

# Requirements
- selenium 
- pytest
- allure
- webdriver-manager

# Generate Test Report
To generate all tests report using Allure you need to run tests by command first:
```
$ python -m pytest -v -s  --alluredir=<reports directory path>
```
Then you need to use command:
```
$ allure serve <reports directory path>
```
