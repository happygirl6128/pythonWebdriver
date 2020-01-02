import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class Challenge3(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.copart.com")
        self.assertIn("Copart", self.driver.title)

    def tearDown(self):
        self.driver.close()

    def test_challenge3forloop(self):
        elements = self.driver.find_elements(By.XPATH, "//*[@id=\"tabTrending\"]/div[1]//a")
        print (len(elements))
        for x in elements:
            print (x.text + ":" + x.get_attribute("href"))

    def test_challenge3whileloop(self):
        elements = self.driver.find_elements(By.XPATH, "//*[@ng-if=\"popularSearches\"]/../div[3]//a")
        print (len(elements))
        x = 0
        while x < len(elements):
            print (elements[x].text + ":" + elements[x].get_attribute("href"))
            x += 1


if __name__ == '__main__':
    unittest.main()
