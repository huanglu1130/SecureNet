from time import sleep
import allure
import pytest
from pyexpat.errors import messages
from selenium.webdriver.common.by import By
from base.base import Base
import pages
import time
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@allure.epic("好友资料卡片")
@allure.feature("好友资料卡片")
class PageAppFriendsInfo(Base):
    def page_app_friends_info(self,name):
        """验证联系人页面所有元素存在性"""
        elements = {
            "name":'//android.widget.TextView[@resource-id="com.mesh.im:id/showName"]',
            "SecureNet ID": '//android.widget.TextView[@resource-id="com.mesh.im:id/userId"]',
            "Department": '//android.widget.TextView[@resource-id="com.mesh.im:id/item_title" and @text="Department"]',
            "Position": '//android.widget.TextView[@resource-id="com.mesh.im:id/item_title" and @text="Position"]',
            "E-mail": '//android.widget.TextView[@resource-id="com.mesh.im:id/item_title" and @text="E-mail"]',
            "Phone Number": '//android.widget.TextView[@resource-id="com.mesh.im:id/item_title" and @text="Phone Number"]',
            "Edit Contact": '//*[@text="Edit Contact"]',
            "Share Contact": '//*[@text="Share Contact"]',
            "Privacy": '//*[@text="Privacy"]',
            "Moment Share": '//*[@text="Moment Share"]',
            "Send Message": '//*[@text="Send Message"]',
            "Voice/Video Call": '//*[@text="Voice or Video Call"]'
        }
        self.base_click(pages.app_contacts)
        loc = By.XPATH, f'//android.widget.TextView[@resource-id="com.mesh.im:id/nickName" and @text="{name}"]'
        self.base_click(loc)
        for element_name, xpath in elements.items():
            try:
                element =  WebDriverWait(self.driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, xpath)))
                assert element.is_displayed(), f"元素 {element_name} 不可见"
                print(f"✅ 元素存在: {element_name}")
            except Exception as e:
                pytest.fail(f"❌ 元素 {element_name} 未找到: {str(e)}")

    def page_app_block_friends(self):
        self.base_click(pages.app_friends_info_more)
        self.base_click(pages.app_friends_block)
        content = '''When you block this user, you will not receive any messages from them and you will not see each other's Moments updates. Block this user now?'''
        self.assert_element_text(pages.app_friends_delete_note,content)
        sleep(1)
        self.base_click(pages.app_friends_block_cancel)
        self.base_click(pages.app_friends_block)
        sleep(1)
        self.base_click(pages.app_friends_block_confirm)
        sleep(1)
        self.assert_element_text(pages.app_friends_blocked_notice, "This user has been blocked, You will not receive any message from them")
        self.base_click(pages.app_contacts_new_friends_back)

    def verify_block_friends(self,name):
        username = self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            f'new UiSelector().text("{name}")'
        )
        username.click()
        found, position = self.is_image_in_screenshot("D://project/screenshot/screenshot.png", 0.9)
        print(f"图标是{found}")


    def page_app_unblock_friends(self,name):
        self.base_click(pages.app_avatar)
        self.base_click(pages.app_block_list)
        sleep(1)
        # self.assert_element_text(pages.app_clock_list_title,name)
        self.base_click(pages.app_clock_list_title)
        sleep(1)
        self.base_click(pages.app_friends_info_more)
        sleep(1)
        self.base_click(pages.app_friends_block)
        self.base_click(pages.app_contacts_new_friends_back)
        self.base_click(pages.app_contacts_new_friends_back)
        self.base_click(pages.app_avatar_back)






