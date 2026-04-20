import allure
from pages.constructor_page import ConstructorPage

class TestConstructor:
    @allure.title("Счётчик ингредиента увеличивается")
    def test_ingredient_counter(self,driver):

        page = ConstructorPage(driver)

        before = page.get_counter()

        page.add_ingredient_to_order()

        after = page.get_counter()

        assert after > before