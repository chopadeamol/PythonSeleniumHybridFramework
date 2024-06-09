import pytest
from pageObjects.LoginPage import LoginPage
from utilities.customLogger import LogGenerator
from utilities.readProperties import ReadConfig

class Test_001_Login:
    baseURL = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()
    logger = LogGenerator.genLog()

    @pytest.mark.regression
    def test_HomePageTitle(self,setup):
        self.logger.info("...............Test_001_Login.....................")
        self.logger.info("...............Home Page Title Page Test is started..................")
        self.driver = setup
        self.logger.info("....................Opening URL...........................................")
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        actual_title = self.driver.title
        if actual_title == "Your store. Login":
            self.logger.info("..........Home Page Title Test Passed............")
            self.driver.close()
            assert True
        else:
            self.logger.error(".........Home Page Title Test Failed............")
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homePageTitle.png")
            self.driver.close()
            assert False

    def test_login(self, setup):
        self.logger.info(".......Started Login Test..........")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        actual_title = self.driver.title
        if actual_title == "Dashboard / nopCommerce administration":
            self.logger.info("......Login Test Passed........")
            self.driver.close()
            assert True
        else:
            self.logger.info(".........Login Test Failed........")
            self.driver.save_screenshot(".\\Screenshots\\"+"test_HomePageTitle.png")
            self.driver.close()
            assert False


