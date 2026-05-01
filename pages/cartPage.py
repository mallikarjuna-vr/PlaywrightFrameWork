from playwright.sync_api import Page, expect
from utilites.ConfigReader import ConfigReader

class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.checkout_button = page.get_by_role("button", name="Checkout")

    def proceed_to_checkout(self):
        try:
            self.checkout_button.click()
            config = ConfigReader()
            check = config.readConfig("basic info", "checkoutURL")
            self.page.wait_for_url(check)
            expect(self.page).to_have_url(check)
        except:
            print("Checkout button is not working or URL did not match.")




