from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestCodlesssample():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_codlesssample(self):
        # Test name: codless_sample
        # Step # | name | target | value
        # 1 | open | /en-gb/ |
        self.driver.get("http://selenium1py.pythonanywhere.com/en-gb/")
        # 2 | setWindowSize | 984x588 |
        self.driver.set_window_size(984, 588)
        # 3 | click | id=login_link |
        self.driver.find_element(By.ID, "login_link").click()
        # 4 | click | id=id_registration-email |
        self.driver.find_element(By.ID, "id_registration-email").click()
        # 5 | type | id=id_registration-email | test@registration.com
        self.driver.find_element(By.ID, "id_registration-email").send_keys("test@registration.com")
        # 6 | click | id=id_registration-password1 |
        self.driver.find_element(By.ID, "id_registration-password1").click()
        # 7 | type | id=id_registration-password1 | qqq111!!!
        self.driver.find_element(By.ID, "id_registration-password1").send_keys("qqq111!!!")
        # 8 | click | id=id_registration-password2 |
        self.driver.find_element(By.ID, "id_registration-password2").click()
        # 9 | type | id=id_registration-password2 | qqq111!!!
        self.driver.find_element(By.ID, "id_registration-password2").send_keys("qqq111!!!")
        # 10 | click | name=registration_submit |
        self.driver.find_element(By.NAME, "registration_submit").click()
        # 11 | waitForElementVisible | css=.alertinner | 5000
        WebDriverWait(self.driver, 5000).until(
            expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".alertinner")))
        # 12 | assertText | css=.alertinner | Thanks for registering!
        assert self.driver.find_element(By.CSS_SELECTOR, ".alertinner").text == "Thanks for registering!"

