from selenium import webdriver
from selenium.webdriver.common.by import By
from Base.Base import Base

class MainPage(Base):
   def __init__(self, driver: webdriver.Chrome):
      # driver 를 Base 클래스에서 생성하기 때문에 받아서 쓰게 수정함
      self.driver = driver

   def close_notice(self):
#      self.driver.find_element(By.CSS_SELECTOR, ".css-1lby940 e1iwydzj0").click()
      self.driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div/div/button[2]").click()

   def move_menu(self, menuTitle):
      getGnb = self.driver.find_element(By.CSS_SELECTOR, ".css-2q6nxg.ev9dfxy1")
      getGnbList = getGnb.find_elements(By.CSS_SELECTOR, ".css-1wzyu4r.ev9dfxy0")
      print("---------------------------------")
      print("getGnbList 길이 : %d" % len(getGnbList))
      print("---------------------------------")

      i = 0
      while getGnbList[i].text != menuTitle:
         print("---------------------------------")
         print("%d 번째 메뉴 : %s" % (i, getGnbList[i].text))
         print("---------------------------------")
         i += 1

      getGnbList[i].click()

      # self.driver.find_element(By.CSS_SELECTOR, ".css-1wzyu4r.ev9dfxy0").click()
      # self.driver.find_element(By.XPATH, "//*[contains(text(), 'Work')]").click()