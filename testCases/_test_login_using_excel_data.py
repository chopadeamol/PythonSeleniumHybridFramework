import time
from pageObjects.LoginPage import LoginPage
from utilities.customLogger import LogGenerator
from utilities.readProperties import ReadConfig
from utilities import readExcel

class Test_002_Data_Driven_Test_Login():
    baseURL = ReadConfig.getApplicationUrl()
    excel_file_path = ".\\TestData\\LoginData.xlsx"
    logger = LogGenerator.genLog()

    def test_login_data_driven(self, setup):
        self.logger.info("..........Starting Test_002_Data_Driven_Test_Login............")
        self.driver = setup
        self.logger.info("....................Opening URL...........................................")
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.rows = readExcel.getRowCount(self.excel_file_path, 'sheet1')
        print("Number of Rows are: ", self.rows)
        list_status = []
        for row in range(2, self.rows+1):
            self.user = readExcel.readData(self.excel_file_path, 'sheet1', row, 1)
            self.password = readExcel.readData(self.excel_file_path, 'sheet1', row, 2)
            self.result = readExcel.readData(self.excel_file_path, 'sheet1', row, 3)
            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)
            actual_title = self.driver.title
            expected_title = "Dashboard / nopCommerce administration"
            if actual_title == expected_title:
                if self.result == "Pass":
                    self.logger.info("..............Passed.............")
                    self.lp.clickLogout()
                    list_status.append("Pass")
                elif self.result == "Fail":
                    self.logger.info("............Failed...............")
                    self.lp.clickLogout()
                    list_status.append("Fail")
            elif actual_title != expected_title:
                if self.result == "Pass":
                    self.logger.info("............Failed...............")
                    list_status.append("Fail")
                elif self.result == "Fail":
                    self.logger.info("............Passed................")
                    list_status.append("Pass")
            print(f"The status of the tests are: {list_status}")

        if "Fail" not in list_status:
            self.logger.info("...........Data Driven Login Test Passed............")
            self.driver.close()
            assert True
        else:
            self.logger.error("..............Data Driven Login Test Failed..................")
            self.driver.close()
            assert False

        self.logger.info("..............End of Data Driven Login Test........................")
        self.logger.info("..............Test_002_Data_Driven_Test_Login Finished..........................")