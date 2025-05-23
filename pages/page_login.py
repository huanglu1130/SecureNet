from time import sleep
from pages.page_sync_confirmation import PageAppSync
from base.base import Base
import pages
class PageAppLogin(Base):
    #1、点击登录方法
    def page_app_click_method(self):
        self.base_click(pages.app_loginmethod)

    # 2、选择ADlogin方法
    def page_app_click_ADlogin(self):
        self.base_click(pages.app_login_option)
    #3、滑动到local
    def page_app_option(self):
        self.page_app_click_method()
        sleep(5)
        self.base_select_option(pages.app_login_option)
        sleep(2)
        self.page_app_click_confirm()

    #3、点击确认
    def page_app_click_confirm(self):
        self.base_click(pages.app_login_method_confirm)
    #4、输入用户名
    def page_app_input_username(self, username):
        self.base_input(pages.app_username, username)
    #5、点击空白区域
    def page_app_click_blank(self):
        self.base_click_blank(1,2)

    # 5、点击输入密码
    def page_app_click_pwd(self):
        self.base_click(pages.app_password)
    #点击显示输入密码
    def page_app_show_pwd(self):
        self.base_click(pages.app_show_password)
    #5、输入密码
    def page_app_input_pwd(self, pwd):
        print("点击密码输入")
        self.base_input(pages.app_password, pwd)

    #6、点击同意协议
    def page_app_click_accpet(self):
        self.base_click(pages.app_accept)

    #7、点击登录按钮
    def page_app_click_login(self):
        print("点击登录按钮")
        self.base_click(pages.app_login)
    #8、获取toast
    def page_app_toast(self):
        self.base_toast_capture(pages.app_login_error_tip)

    #8、整合登录流程
    def page_app_login(self,username,password):
        # self.page_app_click_method()
        # sleep(5)
        # self.page_app_option()
        # sleep(2)
        # self.page_app_click_confirm()
        self.page_app_input_username(username)
        self.page_app_click_blank()
        self.page_app_input_pwd(password)
        # self.page_app_click_accpet()
        self.page_app_click_login()

    #9.给别人调用的登录方法
    def page_app_login_test(self,username,password):
        self.page_app_option()
        self.page_app_click_accpet()
        self.page_app_login(username,password)
        # PageAppSync(self.driver).page_app_click_sync()
