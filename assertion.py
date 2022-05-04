import unittest
from selenium import webdriver


class MyTestCase(unittest.TestCase):

    def test_title(self) -> None:
        """Page open"""
        driver = webdriver.Chrome(executable_path ='./chromedriver')
        driver.get('https://demoqa.com/text-box')
        self.assertEqual("ToolsQA" == driver.title, True)

    def test_submit(self):
        """Submitted"""
        self.assertTrue(id, 'output')
        self.assertTrue("//input[@id='userName']", 'Julia')
        self.assertTrue("//input[@id='userName']", 'ahj.23@gmail.com')
        self.assertTrue("//input[@id='userName']", '3232 Thompson Ave')
        self.assertTrue("//input[@id='userName']", '555 Lower Detroit Rd')


if __name__ == '__main__':
    unittest.main()
