import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By


class SlingImages(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.sling.com")

    def tearDown(self):
        self.driver.close()

    def test_slingImagesforloop(self):
        elements = self.driver.find_elements(By.XPATH, "//*[@id=\"channelList\"]//img")
        print (len(elements))
        for x in elements:
            print (x.get_attribute("src") + ":" + x.get_attribute("alt"))

    def test_slingImagewhileloop(self):
        elements = self.driver.find_elements(By.XPATH, "//*[@id=\"channelList\"]//img")
        print (len(elements))
        x = 0
        while x < len(elements):
            print (elements[x].get_attribute("src") + ":" + elements[x].get_attribute("alt"))
            x += 1


if __name__ == '__main__':
    unittest.main()
