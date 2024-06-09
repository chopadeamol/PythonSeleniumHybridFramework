import pytest
from selenium import webdriver
from pytest_metadata.plugin import metadata_key

@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        driver = webdriver.Chrome()
        print("Launching chrome browser................................")
        return driver
    elif browser == "firefox":
        driver = webdriver.Firefox()
        print("Launching firefox browser................................")
        return driver
    elif browser == "edge":
        driver = webdriver.Edge()
        print("Launching edge browser...................................")
        return driver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


def pytest_configure(config):
    config.stash[metadata_key]['Project Name'] = "nop Commerce"
    config.stash[metadata_key]['Module Name'] = "Customers"
    config.stash[metadata_key]['Tester'] = "Amol-Chopade"


#@pytest.mark.optionalhook   (This is depricated decorator)
@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("plugins", None)





