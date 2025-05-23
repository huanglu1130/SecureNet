from pages.page_add_friends import PageAppAddFriends
from pages.page_login import PageAppLogin
from pages.page_login_out import PageAppLoginOut
from selenium.webdriver.common.by import By
from base.base import Base
from base.base_toast_button import BaseToast
import pages
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from pages.page_friends_info import PageAppFriendsInfo

class PageRequestAction(Base):
    def page_app_request_new(self,add_type,phone,name):
        appaddfriends = PageAppAddFriends(self.driver)
        content = "发起好友请求"
        appaddfriends.page_app_search_friends("+" ,add_type,phone,name)
        ##2.发送添加好友请求
        appaddfriends.page_app_add_friends("+", name,content)
        sleep(1)
        ##4.返回到聊天列表页面
        appaddfriends.page_app_add_friends_back("+")
        sleep(2)
    def page_app_request_action(self,action):
        self.base_click(pages.app_contacts)
        self.base_click(pages.app_contacts_new_friends_title)
        self.base_click(pages.app_friends_request_action)
        if action == "reject":
            self.base_click(pages.app_friends_reject)
        else:
            self.base_click(pages.app_friends_accept)

    def verify_request_status(self,action):
        status = self.base_find(pages.app_new_friends_handle).text
        if action == "reject":
            assert status == "Rejected",f"展示的状态{status}不正确"
        else:
            assert status == "Accepted",f"展示的状态{status}不正确"
        self.base_click(pages.app_contacts_new_friends_back)
        self.base_click(pages.app_chats)


    def page_app_delete_friends(self,name):
        self.base_click(pages.app_contacts)
        element = By.XPATH,f'//android.widget.TextView[@resource-id="com.mesh.im:id/nickName" and @text="{name}"]'
        self.base_click(element)
        self.base_click(pages.app_friends_info_more)
        self.base_click(pages.app_friends_delete)
        content = f'Delete contact "{name}" and the chathistory with that contact.'
        self.assert_element_text(pages.app_delete_notice,content)
        self.base_click(pages.app_delete_cancel)
        self.base_click(pages.app_friends_delete)
        self.base_click(pages.app_delete_confirm)
        self.verify_delete_friends(name)
        self.base_click(pages.app_chats)

    def verify_delete_friends(self,name):
        try:
            # 等待最多 5 秒，直到元素消失才认为删除成功
            WebDriverWait(self.driver, 5).until_not(
                EC.presence_of_element_located((By.XPATH, f'//*[contains(@text, "{name}")]')))
            print(f"✅ 断言成功：'{name}' 已从通讯录删除")
        except NoSuchElementException:
            raise AssertionError(f"好友 '{name}' 仍然存在，删除失败！")


    def page_app_delete_requests(self):
        self.base_click(pages.app_contacts)
        self.base_click(pages.app_contacts_new_friends_title)
        element = WebDriverWait(self.driver, 2).until(
                EC.presence_of_element_located(pages.app_new_friends_handle)
            )
        BaseToast(self.driver).click_toast_button(element,"Delete")
        try:
            # 等待最多 5 秒，直到元素消失才认为删除成功
            WebDriverWait(self.driver, 5).until_not(
                EC.presence_of_element_located((pages.app_new_friends_remark)))
            print(f"✅ 断言成功:已删除")
        except NoSuchElementException:
            raise AssertionError(f"好友申请仍然存在，删除失败！")
