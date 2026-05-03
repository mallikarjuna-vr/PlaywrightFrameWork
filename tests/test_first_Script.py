import pytest
from pages.loginPage import LoginPage
from pages.homePage import HomePage
from pages.cartPage import CartPage
from pages.infoPage import InfoPage
from pages.overviewPage import OverviewPage
from utilites.ExcelData import ExcelData

@pytest.mark.usefixtures("page")
class Test_E2Escenierio1:
    @pytest.mark.smoke
    def test_E2Escenierio3(self, page):
        login_page = LoginPage(page)
        home_page = HomePage(page)
        excel_data = ExcelData()
        username = excel_data.getCellData("testData/userInfo.xlsx", "Sheet1", 2, 1)
        password = excel_data.getCellData("testData/userInfo.xlsx", "Sheet1", 2, 2)

        login_page.login_to_application(username, password)
        home_page.navigate_to_product_details()
        home_page.logout_from_application()


    @pytest.mark.smoke
    def test_E2Escenierio2(self, page):
        login_page = LoginPage(page)
        home_page = HomePage(page)
        excel_data = ExcelData()
        username = excel_data.getCellData("testData/userInfo.xlsx", "Sheet1", 2, 1)
        password = excel_data.getCellData("testData/userInfo.xlsx", "Sheet1", 2, 2)

        login_page.login_to_application(username, password)
        home_page.verify_about_page()
        home_page.logout_from_application()



    @pytest.mark.regression
    def test_E2Escenierio1(self, page):
        login_page = LoginPage(page)
        home_page = HomePage(page)
        cart_page = CartPage(page)
        info_page = InfoPage(page)
        overview_page = OverviewPage(page)
        excel_data = ExcelData()
        username = excel_data.getCellData("testData/userInfo.xlsx", "Sheet1", 2, 1)
        password = excel_data.getCellData("testData/userInfo.xlsx", "Sheet1", 2, 2)

        login_page.login_to_application(username, password)
        home_page.add_first_product_to_cart()
        cart_page.proceed_to_checkout()
        info_page.enter_checkout_information()
        overview_page.placeOrder()
        home_page.logout_from_application()