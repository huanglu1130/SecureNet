from time import sleep
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base import Base
import pages

class PageSelectFriends(Base):
    def page_show_select_friends(self):
        title = self.base_find(pages.app_card_title)
        if title.text == "Select friends":
            print("标题正确")
        else:
            print(f"选择名片标题错误，为{title.text}")
        search_title = self.base_find(pages.app_card_search)
        if search_title.text == "Search":
            print("搜索框标题正确")
        else:
            print(f"搜索框标题错误，为{search_title.text}")

    def page_search_user(self,name):
        self.base_input(pages.app_card_search,name)
        nickname = self.base_find(pages.app_card_search_result)
        if nickname.text == name:
            print("搜索结果正确")
            nickname.click()
        else:
            print(f"搜索结果不正确，为{nickname.text}")
    def page_search_user_clear(self):
        self.base_input(pages.app_card_search, "test2")
        self.base_click(pages.app_card_input_clear)

    def page_send_contact_cancel(self):
        self.base_click(pages.app_card_cancel)

    def page_send_contact_confirm(self):
        self.base_click(pages.app_card_confirm)
