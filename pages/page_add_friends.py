from time import sleep
import allure
import pytest
from selenium.webdriver.common.by import By
from base.base import Base
import pages
import time



@allure.epic("添加好友功能")
@allure.feature("加好友功能")
class PageAppAddFriends(Base):
    def page_app_click_add_menu(self):
        # self.base_click(pages.app_chats)
        self.base_click(pages.app_add_menu)
        self.base_click(pages.app_add_friends)
        self.verify_add_friends_homepage()



    def page_app_search_friends(self,entrance,add_type,content,name):
        if entrance == "+":
            self.page_app_click_add_menu()
            self.base_click(pages.app_add_friends_search)
            self.base_input(pages.app_add_friends_search_input, content)
            self.base_click(pages.app_add_friends_search_result)
        else:
            self.base_click(pages.app_chat_list_search)
            self.base_input(pages.app_chat_list_search_input, content)
        time.sleep(2)
        self.verify_search_result(entrance,add_type,content,name)
        self.base_click(pages.app_add_friends_result_phone)


    def page_app_add_friends(self,entrance,name,request_content):
        if entrance == "+":
            self.base_click(pages.app_send_add_friends)
        else:
            self.base_click(pages.app_chat_add)
        self.verify_add_friends_page(name,request_content)
        self.base_click(pages.app_add_friends_send)

    def page_app_add_friends_back(self,entrance):
        if entrance == "+":
            self.base_click(pages.app_add_friends_card_back)
            sleep(1)
            self.base_click(pages.app_add_friends_search_cancel)
            sleep(1)
            self.base_click(pages.app_add_friends_back)
        else:
            self.base_click(pages.app_message_back)
            sleep(1)
            self.base_click(pages.app_chat_search_cancel)

    def page_app_new_friends(self,name,request_content,status):
        self.base_click(pages.app_contacts)
        self.base_click(pages.app_contacts_new_friends_title)
        self.verify_new_friends(name,request_content,status)
        # self.base_click(pages.app_contacts_new_friends_back)
        # self.base_click(pages.app_chats)


    def verify_new_friends(self,name,request_content,status):
        try:
            self._is_element_present(pages.app_contacts_new_friends_title)
            self.assert_element_text(pages.app_new_friends_name,name)
            self.assert_element_text(pages.app_new_friends_remark,request_content)
            self.assert_element_text(pages.app_new_friends_handle,status)
        except Exception as e:
            pytest.fail(f"好友验证失败: {str(e)}")


    def verify_add_friends_toast(self, target_text):
        self.base_get_toast(target_text)

    def verify_add_friends_page(self,name,request_content):
        ##断言发送好友标题是否正确
        title = self.base_find(pages.app_add_friends_title)
        assert title.text == 'New Friends Apply',f"发送好友请求页面的标题{title.text}不正确"
        ##断言发送好友默认请求内容是否正确以及更改内容
        content = self.base_find(pages.app_add_friends_content).text
        assert content == "I'm admin", f"发送好友请求页面的标题{content}不正确"
        self.base_input(pages.app_add_friends_content,request_content)
        ##断言发送好友请求默认备注是否正确以及更改备注
        remark = self.base_find(pages.app_add_friends_remark).text
        assert remark == name, f"发送好友请求页面的标题{remark}不正确"
        self.base_input(pages.app_add_friends_remark,"测试添加好友")

    def verify_search_result(self,entrance,add_type,phone,name):
        ## 校验搜索标题
        if entrance == "+":
            title = self.base_find(pages.app_add_friends_result_title)
        else:
            loc = (By.XPATH,f'//android.widget.TextView[@resource-id="com.mesh.im:id/tv_title" and @text="{add_type}"]')
            title = self.base_find(loc)
        assert add_type in title.text,f"发送好友请求页面的标题{title.text}不正确"
        ## 校验搜索号码
        number = self.base_find(pages.app_add_friends_result_phone)
        assert number.text == phone, f"发送好友请求页面的标题{number.text}不正确"
        ## 校验搜索昵称
        tv_name = self.base_find(pages.app_add_friends_result_name)
        assert tv_name.text == name, f"发送好友请求页面的昵称{tv_name.text}不正确"

    def verify_add_friends_homepage(self):
        #校验添加好友首页标题
        page_title = self.base_find(pages.app_add_friends_home_page).text
        assert page_title == "Add Friends",f"添加好友首页标题{page_title}不正确"
        elements_to_check = [
            {
                "parent": (pages.app_add_friends_home_item_scan),  # 最外层父级
                "children": [
                    pages.app_add_friends_home_item_icon,  # 图标
                    pages.app_add_friends_home_item_title,  # 文本
                    pages.app_add_friends_home_item_summary # 箭头
                ]
            }
        ]
        # 执行校验
        assert self.check_elements_hierarchy(elements_to_check), "界面元素层级校验失败"
        print("校验首页元素通过")