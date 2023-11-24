from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from Base.Base import Base

class WorkPage(Base):
    def __init__(self, driver: webdriver.Chrome):
      # driver 를 Base 클래스에서 생성하기 때문에 받아서 쓰게 수정함
      self.driver = driver

    def page_scrolling(self):
        temp = self.driver.find_element(By.XPATH, "//*[contains(text(), 'GOODVIBE WORKS 바로가기')]")
        action = ActionChains(self.driver)
        action.move_to_element(temp).perform()

    def move_goodvibeworks(self):
        self.driver.find_element(By.XPATH, "//*[contains(text(), 'GOODVIBE WORKS 바로가기')]").click()