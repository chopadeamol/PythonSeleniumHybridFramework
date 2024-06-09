import time

import pytest
from selenium.webdriver.common.by import By
from pageObjects.LoginPage import LoginPage
from pageObjects.AddCustomerPage import AddCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGenerator
from utilities.generalOperations import random_generator

class Test_003_AddCustomer:
    baseURL = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()
    logger = LogGenerator.genLog()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_addCustomer(self, setup):

        self.logger.info("...........Started Test_003_AddCustomer..................")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("............Login Successful.............")

        self.logger.info("............Starting Add Customer Test................")
        self.addCust = AddCustomer(self.driver)
        self.addCust.clickCutomersMenu()
        time.sleep(5)
        self.addCust.clickCustomerItem()
        self.addCust.clickAddNew()

        self.logger.info(".........Providing Customer Information.................")
        self.email = random_generator() + "@gmail.com"
        self.addCust.setEmail(self.email)
        self.addCust.setPassword("Test_321")
        self.addCust.setfirstName("Amol")
        self.addCust.setlastName("Chopade")
        self.addCust.setGender("Male")
        self.addCust.setDob("01/01/1996")
        self.addCust.setCompanyName("UI_Test")
        self.addCust.isTaxExempt()
        self.addCust.setNewsletter("Your store name")
        self.addCust.setCustomerRoles("Registered")
        self.driver.save_screenshot(".\\Screenshots\\" + "test_AddCustomer1.png")
        self.addCust.setManagerVendor()
        self.addCust.setAdminContent("Add Customer for an automation testing: Dummy test")
        self.addCust.clickSave()
        self.logger.info(".................Saving Customer Information..................")

        self.logger.info("...............Add Customer Validation is Started here.....................")
        self.message = self.driver.find_element(By.TAG_NAME, "body").text
        print(f"Message is: {self.message}")
        self.flash_message = "customer has been added successfully."
        if self.flash_message in self.message:
            assert True
            self.logger.info(".....Add Customer Test Passed.....")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_AddCustomer.png")
            self.logger.info("........Add Customer Test Failed...........")
            assert False
        self.driver.close()
        self.logger.info("...........Add Customer Test Ends Up Here...............")

