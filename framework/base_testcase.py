from selenium import webdriver
from Discuz_lx1.framework.browser_engine import BrowserEngine
import unittest

class BaseTestCase(unittest.TestCase):

    def setUp(self):
        '''
        测试的前提准备工作
        '''
        self.driver=webdriver.Chrome('../tools/chromedriver.exe')
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)


    def tearDown(self):

        self.driver.quit()