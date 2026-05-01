from playwright.sync_api import Page, expect
from utilites.random_Data import RandomData
from utilites.ConfigReader import ConfigReader
class InfoPage:
    def __init__(self, page: Page):
        self.page = page
        self.first_name_field = page.get_by_placeholder("First Name")
        self.last_name_field = page.get_by_placeholder("Last Name")
        self.postal_code_field = page.get_by_placeholder("Zip/Postal Code")
        self.continue_button = page.get_by_role("button", name="Continue")

    def enter_checkout_information(self):
        try:
            random_data = RandomData()
            first_name = random_data.get_first_name()
            last_name = random_data.get_last_name()
            postal_code = random_data.get_zipcode()
            self.first_name_field.fill(first_name)
            self.last_name_field.fill(last_name)
            self.postal_code_field.fill(postal_code)
            self.page.wait_for_timeout(4000)
            self.continue_button.click()
            config = ConfigReader()
            overview_url = config.readConfig("basic info" , "overviewURL")
            self.page.wait_for_url(overview_url)
            expect(self.page).to_have_url(overview_url)
        except:
            print("Error while entering checkout information")