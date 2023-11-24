import unittest
import time
from Base.Base import Base
from Page.MainPage import MainPage
from Page.WorkPage import WorkPage
from Page.GoodvibePage import GoodvibePage

class Test001(Base):
   # 테스트 Case 작성
   def test_free_experience(self):
       url = "https://illuminarean.com/"
       self.driver.get(url)
       time.sleep(2)

       Main_page = MainPage(self.driver)
       Main_page.close_notice()
       time.sleep(2)
       Main_page.move_menu("Work")
       time.sleep(2)

       Work_Page = WorkPage(self.driver)
       Work_Page.page_scrolling()
       time.sleep(3)
       Work_Page.move_goodvibeworks()
       time.sleep(5)

       Goodvibe_Page = GoodvibePage(self.driver)
       Goodvibe_Page.find_windows()
       time.sleep(5)
       Goodvibe_Page.move_free_experince()
       time.sleep(2)

       Goodvibe_Page.fill_companyname()
       time.sleep(2)
       Goodvibe_Page.fill_ceoname()
       time.sleep(2)
       Goodvibe_Page.select_businesstype()
       time.sleep(2)
       Goodvibe_Page.select_scale()
       time.sleep(2)
       Goodvibe_Page.fill_name()
       time.sleep(2)
       Goodvibe_Page.fill_email()
       time.sleep(2)
       Goodvibe_Page.fill_mobile()
       time.sleep(2)
       Goodvibe_Page.select_duties()
       time.sleep(2)
       Goodvibe_Page.check_agreeTermsOfUse()
       time.sleep(2)
       Goodvibe_Page.check_agreePrivacyStatement()
       time.sleep(2)
       Goodvibe_Page.close_registor()
       time.sleep(5)
       Goodvibe_Page.confirm_cancel()
       time.sleep(5)


if __name__ == "__main__":
    unittest.main()