# coding: utf-8
import unittest
from selenium import webdriver

class Base(unittest.TestCase):
    driver = None
    # 기본세팅
    def setUp(self):
        #창없는 크롬 실행
        # options.add_argument('headless')
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        print("WEB Test is started")
        # self.driver.set_window_size(1500, 1000)

    def tearDown(self):
        if self.driver is not None:
            print("-----------------------------")
            print("Tests is finished")
            self.driver.close()
            self.driver.quit()