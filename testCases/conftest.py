import pytest
from selenium import webdriver
from pytest_metadata.plugin import metadata_key
from utilities.customLogger import LogGenerator
from selenium.webdriver.chrome.options import Options
import subprocess
logger = LogGenerator.genLog()

@pytest.fixture()
def setup(browser):
    logger.info(f"============Test Case Started=============")
    if browser == "chrome":
        # driver = webdriver.ChromeOptions()
        options = Options()
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        prefs = {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False
        }
        options.add_experimental_option("prefs", prefs)
        options.add_argument("--headless")
        driver = webdriver.Chrome(options=options)
        print("Launching chrome browser")
        yield driver
        logger.info("Test case execution completed")
        driver.quit()



    elif browser == "firefox":
        options = webdriver.FirefoxOptions()
        # options.add_experimental_option('excludeSwitches', ['disable-popup-blocking'])
        options.add_argument("--disable-blink-features=AutomationControlled")
        # options.add_experimental_option("excludeSwitches", ["enable-automation"])
        # options.add_experimental_option('useAutomationExtension', False)
        options.add_argument("--disable-extensions")
        driver = webdriver.Firefox(options=options)
        print("Launching firefox browser")
        return driver
    elif browser == "Edge":
        options = webdriver.EdgeOptions()
        options.add_experimental_option('excludeSwitches', ['disable-popup-blocking'])
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        options.add_argument("--disable-extensions")
        driver = webdriver.Edge(options=options)
        print("Launching edge browser")
        return driver
    yield




def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


def pytest_configure(config):
    config.stash[metadata_key]['Project Name'] = "nop Commerce"
    config.stash[metadata_key]['Module Name'] = "Customers"
    config.stash[metadata_key]['Tester'] = "Amol-Chopade"



@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("plugins", None)

@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep

# def pytest_runtest_teardown(item, nextitem):
#     logger.info(f"============Test Case Finished==============")
#     command = ["allure serve", "D:\\PythonSeleniumHybridFramework\\allureReports"]
#     result = subprocess.run(command, capture_output=True, text=True, shell=True)
# def pytest_sessionfinish(session, exitstatus):
#     logger.info("==============All Tests are finished===============")
#     if exitstatus == 0:
#         print("==========All Tests Passed==============")
#     else:
#         print("==========Some Tests Failed=============")
#     subprocess.Popen("cmd.exe /k C: && cd && C:\\Users\\apcam && allure && serve && D:\\PythonSeleniumHybridFramework")
#     logger.info(f"============Test Case Finished==============")
    # Open the command prompt
    # process = subprocess.Popen("cmd.exe", stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
    #                            text=True)
    # # Send multiple commands to the command prompt
    # commands = "C:\n"
    # commands += "echo cd\n"
    # commands += "echo C:\\Users\\apcam\n"
    # commands += "echo allure serve D:\\PythonSeleniumHybridFramework\\allureReports\n"
    # process.stdin.write(commands)
    # process.stdin.flush()
    # Read the output
    # output, error = process.communicate()
    # print("Output:\n", output)
    # print("Error:\n", error)
    # command = ["allure serve", "D:\\PythonSeleniumHybridFramework\\allureReports"]
    # result = subprocess.run(command, capture_output=True, text=True, shell=True)