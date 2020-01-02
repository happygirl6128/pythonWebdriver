import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class SlingSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://help.sling.com")

    def tearDown(self): self.driver.close()

    def test_slingSearch(self):
        element = self.driver.find_element(By.ID, "support-search-input")
        element.send_keys("ROKU")
        searchBtn = self.driver.find_element(By.XPATH, "//*[@id=\"hc-search-form\"]//button")
        searchBtn.click()
        element= self.driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div/div[1]/div[2]/ul")
        self.assertIn("Roku", element.text)
        # for x in elements:
        #     print (x.get_attribute("href"))


if __name__ == '__main__':
    unittest.main()
