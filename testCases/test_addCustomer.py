import time
import allure
import pytest
from selenium.webdriver.common.by import By
from pageObjects.LoginPage import LoginPage
from pageObjects.AddCustomerPage import AddCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGenerator
from utilities.generalOperations import random_generator
from utilities.generalOperations import currentTimestamp


@allure.feature('Add Customer feature')
@allure.severity(allure.severity_level.NORMAL)
class Test_003_AddCustomer:
    baseURL = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()
    logger = LogGenerator.genLog()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_addCustomer(self, setup):

        self.logger.info(f"Started Test_003_AddCustomer at: {currentTimestamp()}")
        self.driver = setup
        with allure.step("Launching base url"):
            self.driver.get(self.baseURL)

        with allure.step("Maximizing window"):
            self.driver.maximize_window()
        self.lp = LoginPage(self.driver)

        with allure.step("Entering username"):
            self.lp.setUserName(self.username)
        with allure.step("Entering password"):
            self.lp.setPassword(self.password)
        with allure.step("Clicking login button"):
            self.lp.clickLogin()
        with allure.step(f"Login successful:{currentTimestamp()}"):
            pass
        with allure.step(f"Starting Add Customer Test at: {currentTimestamp()}"):
            pass
        self.addCust = AddCustomer(self.driver)
        with allure.step("Clicking main customers menu"):
            self.addCust.clickCutomersMenu()
        time.sleep(3)
        with allure.step("clicking sub customer menu"):
            self.addCust.clickCustomerItem()
        with allure.step("clicking add new button"):
            self.addCust.clickAddNew()
        self.logger.info("Providing Customer Information")
        with allure.step("Entering email"):
            self.email = random_generator() + "@gmail.com"
            self.addCust.setEmail(self.email)
        with allure.step("Entering password"):
            self.addCust.setPassword("Test_321")
        with allure.step("Entering first name of customer"):
            self.addCust.setfirstName("Amol")
        with allure.step("Entering last name of customer"):
            self.addCust.setlastName("Chopade")
        with allure.step("Entering gender of customer"):
            self.addCust.setGender("Male")
        with allure.step("Entering dob"):
            self.addCust.setDob("01/01/1996")
        with allure.step("Entering company name"):
            self.addCust.setCompanyName("UI_Test")
        self.addCust.isTaxExempt()
        self.addCust.setNewsletter("Your store name")
        self.addCust.setCustomerRoles("Registered")
        self.driver.save_screenshot(".\\Screenshots\\" + f"test_AddCustomer1.png:{currentTimestamp()}")
        self.addCust.setManagerVendor()
        self.addCust.setAdminContent("Add Customer for an automation testing: Dummy test")
        self.addCust.clickSave()
        self.logger.info(f"Saving Customer Information:{currentTimestamp()}")
        self.logger.info(f"Add Customer Validation is Started here:{currentTimestamp()}")
        self.message = self.driver.find_element(By.TAG_NAME, "body").text
        print(f"Message is: {self.message}")
        self.flash_message = "customer has been added successfully."
        if self.flash_message in self.message:
            assert True
            self.logger.info("Add Customer Test Passed")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+f"test_AddCustomer.png:{currentTimestamp()}")
            self.logger.info("Add Customer Test Failed")
            assert False
        self.driver.close()
        self.logger.info(f"Add Customer Test Ends Up Here at: {currentTimestamp()}")