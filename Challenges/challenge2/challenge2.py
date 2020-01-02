import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Challenge2(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self): self.driver.close()

    def test_challenge2(self):
        self.driver.get("https://www.copart.com")
        element = self.driver.find_element(By.ID, "input-search")
        element.send_keys("exotic")
        searchBtn = self.driver.find_element(By.XPATH, "//button[@data-uname='homepageHeadersearchsubmit']")
        searchBtn.click()
        html = self.driver.page_source
        datawait = WebDriverWait(self.driver, 10)
        datawait.until(
            expected_conditions.presence_of_element_located((By.XPATH, "//*[@id=\"serverSideDataTable\"]//td")))
        datatable = self.driver.find_element(By.XPATH, "//*[@id=\"serverSideDataTable\"]")
        print (datatable.text)
        self.assertIn("PORSCHE", datatable.text)


if __name__ == '__main__':
    unittest.main()
