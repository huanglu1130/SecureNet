from pages.page_add_friends import PageAppAddFriends
from pages.page_login import PageAppLogin
from pages.page_login_out import PageAppLoginOut
from selenium.webdriver.common.by import By
from base.base import Base
from base.base_toast_button import BaseToast
import pages
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
class PageGroupChat(Base):
    def page_app_create_group_chat(self,group_name):
        self.base_click(pages.app_add_menu)
        self.base_click(pages.app_add_create_group)
        self.base_input(pages.app_group_chat_name,group_name)
        self._is_element_present(pages.app_group_name_title)
        self.base_click(pages.app_group_chat_name_done)


    def page_app_select_member(self):
        sleep(2)
        self.base_click(pages.app_group_chat_member_1)
        self.base_click(pages.app_group_chat_member_2)
        self.base_click(pages.app_group_chat_done)

    def page_app_create_group(self,group_name):
        self.page_app_create_group_chat(group_name)
        self.page_app_select_member()
        self.verify_group(group_name)

    def verify_group(self,group_name):
        try:
            # 1. 构建动态定位器（处理特殊字符）
            group_locator = (By.XPATH,
                             f'//android.widget.TextView['
                             f'@resource-id="com.mesh.im:id/name" '
                             f'and normalize-space(@text)={repr(str(group_name).strip())}'
                             f']'
                             )

            # 2. 显式等待元素存在且可点击
            group_element = WebDriverWait(self.driver, 5).until(
                lambda d: (
                    element if (element := d.find_element(*group_locator)).is_displayed()
                    else None
                ))
            # 4. 点击进入群聊
            group_element.click()
        except TimeoutException:
            raise AssertionError(
                f"未找到群聊 '{group_name}' 或进入失败\n"
            )
