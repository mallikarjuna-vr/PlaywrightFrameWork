from playwright.sync_api import Page, expect
from utilites.ConfigReader import ConfigReader

class HomePage:
    def __init__(self, page: Page):
        self.page = page
        self.add_to_cart_button = page.get_by_role("button", name="Add to cart")
        self.shopping_cart_icon = page.locator(".shopping_cart_container")
        self.menu_button = page.get_by_role("button", name="Open Menu")
        self.logout_link = page.get_by_role("link", name="Logout")
        self.about_link = page.get_by_role("link", name="About")
        self.all_products_title = page.locator(".inventory_item_name")
        self.product_description = page.locator(".large_size")

    def add_first_product_to_cart(self):
        try:
            self.add_to_cart_button.first.click()
            self.shopping_cart_icon.click()
            config = ConfigReader()

            cart_url = config.readConfig("basic info","cartURL")
            self.page.wait_for_url(cart_url)
            expect(self.page).to_have_url(cart_url)
        except:
            print("Failed to add product to cart or navigate to cart page.")


    def logout_from_application(self):
        try:
            self.menu_button.click()
            self.logout_link.click()
        except:
            print("Failed to logout from application.")

    def verify_about_page(self):
        try:
            self.menu_button.click()
            self.about_link.click()
            config = ConfigReader()
            about_url = config.readConfig("basic info","aboutURL")
            self.page.wait_for_url(about_url)
            expect(self.page).to_have_url(about_url)
            self.page.go_back()
        except:
            print("Failed to navigate to about page.")

    def navigate_to_product_details(self):
        try:
          for product in self.all_products_title.all():
              product.first.click()
              expect(self.product_description).to_be_visible()
              print(self.product_description.inner_text())
              self.page.go_back()

        except:
            print("Failed to navigate to product details page.")