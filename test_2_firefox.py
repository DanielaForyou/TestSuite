import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

class Firefox(unittest.TestCase):
    COOKIES=(By.ID,'ez-accept-all')
    ADD_REMOVE_URL=(By.XPATH,'//a[contains(text(),"Add")]')
    ADD_ELEMENT_BUTTON=(By.XPATH,'//button')
    DELETE_BUTTON=(By.CLASS_NAME, 'added-manually')

    def setUp(self):
        self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get('https://the-internet.herokuapp.com/')

    def tearDown(self):
        self.driver.quit()

    @unittest.skip
    def test_right_url(self):
        self.driver.find_element(*self.ADD_REMOVE_URL).click()
        actual=self.driver.find_element(By.XPATH,'//h3').text
        expected='Add/Remove Elements'
        self.assertEqual(actual,expected,'Numele paginii nu corespunde')

    @unittest.skip
    def test_add_element(self):
        self.driver.find_element(*self.ADD_REMOVE_URL).click()
        self.driver.find_element(*self.ADD_ELEMENT_BUTTON).click()
        delete_button=self.driver.find_element(*self.DELETE_BUTTON)
        self.assertTrue(delete_button.is_displayed(),'Nu s-a adaugat butonul delete')

    # @unittest.skip
    def test_delete_button(self):
        self.driver.find_element(*self.ADD_REMOVE_URL).click()
        self.driver.find_element(*self.ADD_ELEMENT_BUTTON).click()
        self.driver.find_element(*self.DELETE_BUTTON).click()
        try:
            self.driver.find_element(*self.DELETE_BUTTON)
        except:
            print('Butonul delete a disparut, as expected')










