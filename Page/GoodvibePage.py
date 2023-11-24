from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import time
from selenium.webdriver import ActionChains
import random
from Base.Base import Base

class GoodvibePage(Base):
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def find_windows(self):
        print("---------------------------------")
        print("열린 윈도우 정보 : ", self.driver.window_handles)
        print("---------------------------------")
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def move_free_experince(self):
        self.driver.find_element(By.CSS_SELECTOR, ".btn-freetrial-main").click()

    def fill_companyname(self):
        companyName = self.driver.find_element(By.ID, "companyName")
        companyName.click()
        companyName.send_keys("일루미나리안")

    def fill_ceoname(self):
        ceoName = self.driver.find_element(By.ID, "ceoName")
        ceoName.click()
        ceoName.send_keys("김사무엘")

    def select_businesstype(self):
        # select-React-control
        self.driver.find_element(By.ID, "businessType").click()
        businesstype = self.driver.find_element(By.XPATH, "//*[text()='개인']")
        self.driver.execute_script("arguments[0].scrollIntoView();", businesstype)
        businesstype.click()

    def select_scale(self):
        # select-React-control
        self.driver.find_element(By.ID, "scale").click()
        scaleValue = self.driver.find_element(By.XPATH, "//*[text()='501-999명']")
        self.driver.execute_script("arguments[0].scrollIntoView();", scaleValue)
        scaleValue.click()

    def fill_name(self):
        name = self.driver.find_element(By.ID, "name")
        name.click()
        name.send_keys("담당자")

    def fill_email(self):
        email = self.driver.find_element(By.ID, "email")
        email.click()
        email.send_keys("test@test.com")

    def fill_mobile(self):
        mobile = self.driver.find_element(By.ID, "mobile")
        mobile.click()
        mobile.send_keys("01012345678")

    def select_duties(self):
        self.driver.find_element(By.CSS_SELECTOR, ".css-95wmob.el0tj998").click()
        duties = self.driver.find_elements(By.CSS_SELECTOR, ".css-gyjkhp.el0tj996")

        print("-------------------------------")
        print("담당업무 개수 : %d" % len(duties))
        print("첫번째 업무 %s" % duties[0].text)
        print("마지막 번째 업무 %s" % duties[31].text)
        print("-------------------------------")

        a = random.randrange(0,32)
        print("-------------------------------")
        print("선택된 duty명 : ", duties[a].text)
        print("-------------------------------")
        action1 = ActionChains(self.driver)
        action1.move_to_element(duties[a]).perform()
        duties[a].click()

        registration1 = self.driver.find_elements(By.CSS_SELECTOR, ".css-1nz26cm.e5gga9e11")

        i = 0
        while registration1[i].text != "등록":
            print("---------------------------------")
            print("%d 번째 메뉴 : %s" % (i, registration1[i].text))
            print("---------------------------------")
            i += 1

        print("%d 번째 버튼은 %s 버튼입니다." % (i, registration1[i].text))

        action2 = ActionChains(self.driver)
        goFree = self.driver.find_element(By.CSS_SELECTOR, ".btn-freetrial-submit.css-16nv7no.e1oaq22c1")
        action2.move_to_element(goFree).perform()
        registration1[i].click()

        searchInput = self.driver.find_element(By.CSS_SELECTOR, ".css-95wmob.el0tj998")
        searchInput.click()
        searchDuty = self.driver.find_elements(By.CSS_SELECTOR, ".css-gyjkhp.el0tj996")

        b = random.randrange(0, 32)


        while a != b:
            b = random.randrange(0, 32)

        print("---------------------------------")
        print("b = %d" % b)
        print("---------------------------------")
        print("검색어 : %s" % searchDuty[b].text)
        print("---------------------------------")
        searchInput.send_keys(searchDuty[b].text)
        action3 = ActionChains(self.driver)
        action3.move_to_element(searchDuty[b]).perform()
        searchDuty[b].click()

        registration2 = self.driver.find_elements(By.CSS_SELECTOR, ".css-1nz26cm.e5gga9e11")

        i = 0
        while registration2[i].text != "등록":
            print("---------------------------------")
            print("%d 번째 메뉴 : %s" % (i, registration2[i].text))
            print("---------------------------------")
            i += 1

        registration2[i].click()

    def check_agreeTermsOfUse(self):
        self.driver.find_element(By.ID, "agreeTermsOfUse").click()

    def check_agreePrivacyStatement(self):
        self.driver.find_element(By.ID, "agreePrivacyStatement").click()

    def close_registor(self):
        self.driver.find_element(By.CSS_SELECTOR, ".css-jqp98p.e1oaq22c7").click()

    def confirm_cancel(self):
        self.driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(12) > div > div > div > div > div > div > button:nth-child(2)").click()





