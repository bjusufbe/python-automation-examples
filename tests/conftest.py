# conftest.py - special file for pytest which is used for defining fixtures which will be used across all tests which are calling them
import pytest
import yaml
from selenium import webdriver

@pytest.fixture
def define_inputs():
    return [10, 15]

@pytest.fixture
def input_value():
    input = 10
    return input

@pytest.fixture(scope="class")
def setup(request):
    print("Initializing driver")
    config = {}
    driver = None
    with open("./config/environment.yaml", "r") as stream:
        try:
            config = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)

    if config['browser'] == "chrome":
        driver = webdriver.Chrome()
    else:
        driver = webdriver.Firefox()
    driver.get(config['environments']['qa']['url'])
    driver.maximize_window()
    request.cls.driver = driver
    yield driver
    driver.close()