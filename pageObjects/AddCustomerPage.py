import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

class AddCustomer:
    link_customers_menu_xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
    link_customers_item_xpath = "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    button_add_new_xpath = "//a[@class='btn btn-primary']"
    text_email_xpath = "//input[@id='Email']"
    text_password_xpath = "//input[@id='Password']"
    text_first_name_xpath = "//input[@id='FirstName']"
    text_last_name_xpath = "//input[@id='LastName']"
    radio_gender_male_xpath = "//input[@id='Gender_Male']"
    radio_gender_female_xpath = "//input[@id='Gender_Female']"
    text_dob_xpath = "//input[@id='DateOfBirth']"
    text_company_xpath = "//input[@id='Company']"
    check_tax_xpath = "//input[@id='IsTaxExempt']"
    text_newsletter_xpath = "//*[@id='customer-info']/div[2]/div[9]/div[2]/div/div[1]/div/span/span[1]/span/ul/li/input"
    list_item_Test_store_2_news_xpath = "//li[contains(text(),'Test store 2')]"
    list_item_Your_store_name_news_xpath = "//li[contains(text(),'Your store name')]"
    text_customer_role_xpath = "//*[@id='customer-info']/div[2]/div[10]/div[2]/div/div[1]/div/span/span[1]/span/ul/li/input"
    list_item_administrator_xpath = "//li[contains(text(),'Administrators')]"
    list_item_forumModerators_xpath = "//li[contains(text(),'Forum Moderators')]"
    list_item_registered_xpath = "//li[contains(text(),'Registered')]"
    list_item_guests_xpath = "//li[contains(text(),'Guests')]"
    list_item_vendors_xpath = "//li[contains(text(),'Vendors')]"
    dd_vendor_manager_xpath = "//*[@id='VendorId']"
    text_adminContent_xpath = "//textarea[@id='AdminComment']"
    button_save_xpath = "//button[@name='save']"
    vendor_manage = "//select//option"

    def __init__(self, driver):
        self.driver = driver

    def clickCutomersMenu(self):
        self.driver.find_element(By.XPATH,self.link_customers_menu_xpath).click()

    def clickCustomerItem(self):
        self.driver.find_element(By.XPATH, self.link_customers_item_xpath).click()

    def clickAddNew(self):
        self.driver.find_element(By.XPATH, self.button_add_new_xpath).click()

    def setEmail(self, email):
        self.driver.find_element(By.XPATH, self.text_email_xpath).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element(By.XPATH, self.text_password_xpath).send_keys(password)

    def setfirstName(self, firstname):
        self.driver.find_element(By.XPATH, self.text_first_name_xpath).send_keys(firstname)

    def setlastName(self, lastname):
        self.driver.find_element(By.XPATH, self.text_last_name_xpath).send_keys(lastname)

    def setGender(self, gender):
        if gender == "Male":
            self.driver.find_element(By.XPATH, self.radio_gender_male_xpath).click()
        elif gender == "Female":
            self.driver.find_element(By.XPATH, self.radio_gender_female_xpath).click()

    def setDob(self, dob):
        self.driver.find_element(By.XPATH, self.text_dob_xpath).send_keys(dob)

    def setCompanyName(self, company):
        self.driver.find_element(By.XPATH, self.text_company_xpath).send_keys(company)

    def isTaxExempt(self):
        self.driver.find_element(By.XPATH, self.check_tax_xpath).click()

    def setNewsletter(self, newsletter):
        self.driver.find_element(By.XPATH, self.text_newsletter_xpath).click()
        time.sleep(4)
        if newsletter == "Test store 2":
            self.driver.find_element(By.XPATH, self.list_item_Test_store_2_news_xpath).click()
        elif newsletter == "Your store name":
            self.driver.find_element(By.XPATH, self.list_item_Your_store_name_news_xpath).click()

    def setCustomerRoles(self, role):
        self.driver.find_element(By.XPATH, self.text_customer_role_xpath).click()
        time.sleep(4)
        if role == "Administrators":
            self.driver.find_element(By.XPATH, self.list_item_administrator_xpath).click()
        elif role == "Forum Moderators":
            self.driver.find_element(By.XPATH, self.list_item_forumModerators_xpath).click()
        elif role == "Registered":
            self.driver.find_element(By.XPATH, self.list_item_registered_xpath).click()
        elif role == "Guests":
            self.driver.find_element(By.XPATH, self.list_item_guests_xpath).click()
        elif role == "Vendors":
            self.driver.find_element(By.XPATH, self.list_item_vendors_xpath).click()

    def setManagerVendor(self):
        variable = "Vendor 2"
        elements = self.driver.find_elements(By.XPATH, self.vendor_manage)
        for link_text in elements:
            if variable in link_text.text:
                link_text.click()
                break

    def setAdminContent(self, content):
        self.driver.find_element(By.XPATH, self.text_adminContent_xpath).send_keys(content)

    def clickSave(self):
        self.driver.find_element(By.XPATH, self.button_save_xpath).click()


