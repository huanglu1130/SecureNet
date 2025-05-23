import pytest

from base.base import Base
import pages
import time

class PageSelectAChat(Base):
    def page_show_select_chat(self):
        title = self.base_find(pages.app_forward_select)
        if title.text == "Select a Chat":
            print("转发选择页面标题正确")
        else:
            print(f"选择名片标题错误，为{title.text}")
        search_title = self.base_find(pages.app_forward_search)
        if search_title.text == "Search":
            print("搜索框标题正确")
        else:
            print(f"搜索框标题错误，为{search_title.text}")

    def page_search_chat(self,name):
        try:
            time.sleep(1)
            self.base_click(pages.app_forward_search)
            self.base_input(pages.app_forward_input,name)
            nickname = self.base_find(pages.app_forward_search_result)
            if nickname.text == name:
                print("搜索结果正确")
                nickname.click()
            else:
                print(f"搜索结果不正确，为{nickname.text}")
            return True
        except Exception as e:
            pytest.fail("搜索选择好友失败")



    def verify_sent_to_name(self,name):
        try:
            if self.base_find(pages.app_forward_chat_name).text == name:
                print("确认转发页面转发对象正确")
            else:
                print("确认转发页面转发对象不正确")
            return True
        except Exception as e:
            pytest.fail("断言失败")

    def verify_sent_to_title(self):
        try:
            if self.base_find(pages.app_forward_title).text == "Sent to:":
                print("确认转发页面标题正确")
            else:
                print(f"转发标题不正确{self.base_find(pages.app_forward_title).text}")
            return True
        except Exception as e:
            pytest.fail("断言失败")
    def verify_sent_to_content(self,message):
        try:
            content = self.base_find(pages.app_forward_text_content)
            if message in content.text :
                print("转发消息内容一致")
            else:
                print("转发消息内容不一致")
            return True
        except Exception as e:
            pytest.fail("断言失败")

    def verify_sent_to(self,message,name):
        self.verify_sent_to_content(message)
        self.verify_sent_to_title()
        self.verify_sent_to_name(name)


    def page_multiple_chat(self):
        try:
            self.base_click(pages.app_forward_multiple)
            name1_element = self.base_find(pages.app_forward_user_1)
            name1 = name1_element.text
            self.base_click(pages.app_forward_user_1)

            name2_element = self.base_find(pages.app_forward_user_2)
            name2 = name2_element.text
            self.base_click(pages.app_forward_user_2)

            self.base_click(pages.app_forward_multiple_send)
            title_element = self.base_find(pages.app_forward_title)
            self.verify_sent_to_title()
            return name1,name2
        except Exception as e:
            print(f"多选好友失败，错误详情：{str(e)}")
            # 失败时截图
            # self.driver.save_screenshot("multiple_chat_fail.png")

    def page_multiple_to_one_chat(self):
        try:
            self.base_click(pages.app_forward_multiple)

            self.base_click(pages.app_forward_user_1)
            self.base_click(pages.app_forward_user_2)
            time.sleep(1)
            self.base_click(pages.app_forward_user_1)
            self.base_click(pages.app_forward_user_2)
            self.base_click(pages.app_forward_multiple)
            name1_element = self.base_find(pages.app_forward_user_1)
            name1 = name1_element.text
            self.base_click(pages.app_forward_user_1)
            return name1
        except Exception as e:
            print("多选切单选失败")

    def page_search_chat_clear(self):
        self.base_click(pages.app_forward_search)
        self.base_input(pages.app_forward_input, "test2")
        self.base_click(pages.app_forward_input_cancel)


    def page_send_chat_cancel(self):
        self.base_click(pages.app_forward_cancel)

    def page_send_chat_confirm(self):
        self.base_click(pages.app_forward_confirm)