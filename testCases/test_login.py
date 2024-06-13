import pytest
from pageObjects.LoginPage import LoginPage
from utilities.customLogger import LogGenerator
from utilities.readProperties import ReadConfig
import allure

@allure.feature('Login feature')
@allure.severity(allure.severity_level.NORMAL)
@allure.description("This contains two tests: 1.Verify home page title, 2. Verify login credentials")
class Test_001_Login:
    baseURL = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()
    logger = LogGenerator.genLog()

    @pytest.mark.regression
    def test_home_page_title(self,setup):
        self.logger.info("Test_001_Login")
        self.logger.info("Home Page Title Page Test is started")
        self.driver = setup
        self.logger.info("Opening URL")

        with allure.step("Fetching URL and opening browser window"):
            self.driver.get(self.baseURL)

        with allure.step("Maximizing window"):
            self.driver.maximize_window()

        with allure.step("Validating title of the web page"):
            actual_title = self.driver.title

        if actual_title == "Your store. Login":
            allure.attach(self.driver.get_screenshot_as_png(), name="Login Happy Scr", attachment_type=allure.attachment_type.PNG)
            self.logger.info("Home Page Title Test Passed")
            self.driver.close()
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="Login Failed Scr", attachment_type=allure.attachment_type.PNG)
            self.logger.error("Home Page Title Test Failed")
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homePageTitle.png")
            self.driver.close()
            assert False

    def test_login(self, setup):
        self.logger.info("Started Login Test")
        self.driver = setup

        with allure.step("Fetching URL and opening browser window....."):
            self.driver.get(self.baseURL)

        with allure.step("Maximizing window"):
            self.driver.maximize_window()
        self.lp = LoginPage(self.driver)

        with allure.step("Entering username to login to page"):
            self.lp.setUserName(self.username)

        with allure.step("Entering password to login to page"):
            self.lp.setPassword(self.password)

        with allure.step("Clicking login button"):
            self.lp.clickLogin()

        with allure.step("Validating title of the web page"):
            actual_title = self.driver.title

        if actual_title == "Dashboard / nopCommerce administration":
            allure.attach(self.driver.get_screenshot_as_png(), name="Login Title validation Passed",
                          attachment_type=allure.attachment_type.PNG)
            self.logger.info("Login Test Passed")
            self.driver.close()
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="Login Title validation Failed",
                          attachment_type=allure.attachment_type.PNG)
            self.logger.info("Login Test Failed")
            self.driver.save_screenshot(".\\Screenshots\\"+"test_HomePageTitle.png")
            self.driver.close()
            assert False