from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data.urls import BASE_URL,FEED

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def get_text(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    def wait_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_invisible(self, locator):
        return self.wait.until(EC.invisibility_of_element_located(locator))

    def scroll_to(self, locator):
        element = self.wait_visible(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        return element
    
    def find_elements(self, locator):
        return self.driver.find_elements(*locator)
    
    def get_feed_page(self):
        self.driver.get(BASE_URL + FEED)
    
    def get_current_url(self):
        return self.driver.current_url