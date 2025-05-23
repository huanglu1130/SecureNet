import unittest
# from parameterized import parameterized
from base.base import Base
from util import GetDriver,GetLog,read_json
from pages.page_login import PageAppLogin
import time
import pytest
import allure
@allure.feature("登录模块")
class TestAppLogin:
    @pytest.mark.parametrize("desc,username,password,expected",
    [tuple(item.values()) for item in read_json("D:/project/data/app_login.json")])
    def test_login(self,applogin,desc,username,password,expected):
        print("这是username"+username+"这是密码"+password)
        if desc =="登录环境为AD Login":
            print("登录环境为AD Login的场景")
            applogin.page_app_click_accpet()
            applogin.page_app_login(username,password)
            toast_text = applogin.base_get_imgtext("Username or password is incorrect")
            assert expected in toast_text.replace("\n", " "), \
                f"未找到错误提示文本，实际OCR结果: {toast_text.replace("\n", " ")}"
        elif desc =="账号密码不匹配":
            try:
                applogin.page_app_option()
                print("错误账号或者密码的场景")
                applogin.page_app_login(username,password)
                toast_text = applogin.base_get_imgtext("Username or password is incorrect")
                assert expected in toast_text.replace("\n", " "), \
                    f"未找到错误提示文本，实际OCR结果: {toast_text.replace("\n", " ")}"
            except Exception as e:
                print(f"发生错误:{str(e)}")
        elif desc == "账号为空":
            try:
                print("账号为空的场景")
                applogin.page_app_login(username, password)
                toast_text = applogin.base_get_imgtext("Please enter Phone number/SecureNet ID")
                assert expected in toast_text.replace("\n", " "), \
                    f"未找到错误提示文本，实际OCR结果: {toast_text.replace("\n", " ")}"
            except Exception as e:
                print(f"发生错误:{str(e)}")
        elif desc == "密码为空":
            try:
                print("密码为空的场景")
                applogin.page_app_login(username, password)
                toast_text = applogin.base_get_imgtext("Please enter password")
                assert expected in toast_text.replace("\n", " "), \
                    f"未找到错误提示文本，实际OCR结果: {toast_text.replace("\n", " ")}"
            except Exception as e:
                print(f"发生错误:{str(e)}")
        else:
            try:
                print("登录成功的场景")
                applogin.page_app_login(username, password)
                time.sleep(20)
                # toast_text = self.app.base_get_imgtext("Please enter password")
                # assert expected in toast_text.replace("\n", " "), \
                #     f"未找到错误提示文本，实际OCR结果: {toast_text.replace("\n", " ")}"
            except Exception as e:
                print(f"发生错误:{str(e)}")


#
# class TestAppLogin(unittest.TestCase):
#     def setUp(self):
#         self.driver = GetDriver.get_app_driver()
#         self.app = PageAppLogin(self.driver)
#         self.log = GetLog()  # 初始化日志
#
#     def tearDown(self):
#         self.driver.quit()  # 关闭driver

    # def tearDown(self):
    #     try:
    #         # 优先尝试标准方法
    #         self.driver.close_app()
    #         self.driver.launch_app()
    #     except Exception as e:
    #         print(f"标准方法失败: {e}")

    # @parameterized.expand(read_json("app_login.json"))
    # def test_login(self,desc,username,password,expected):
    #     print("这是username"+username+"这是密码"+password)
    #     if desc =="账号密码不匹配" or desc =="登录环境为AD Login":
    #         try:
    #             print("错误账号或者密码的场景")
    #             self.app.page_app_login(username,password)
    #             toast_text = self.app.base_get_imgtext("Username or password is incorrect")
    #             assert expected in toast_text.replace("\n", " "), \
    #                 f"未找到错误提示文本，实际OCR结果: {toast_text.replace("\n", " ")}"
    #         except Exception as e:
    #             print(f"发生错误:{str(e)}")
    #     elif desc == "账号为空":
    #         try:
    #             print("账号为空的场景")
    #             self.app.page_app_login(username, password)
    #             toast_text = self.app.base_get_imgtext("Please enter Phone number/SecureNet ID")
    #             assert expected in toast_text.replace("\n", " "), \
    #                 f"未找到错误提示文本，实际OCR结果: {toast_text.replace("\n", " ")}"
    #         except Exception as e:
    #             print(f"发生错误:{str(e)}")
    #     elif desc == "密码为空":
    #         try:
    #             print("密码为空的场景")
    #             self.app.page_app_login(username, password)
    #             toast_text = self.app.base_get_imgtext("Please enter password")
    #             assert expected in toast_text.replace("\n", " "), \
    #                 f"未找到错误提示文本，实际OCR结果: {toast_text.replace("\n", " ")}"
    #         except Exception as e:
    #             print(f"发生错误:{str(e)}")
    #     else:
    #         try:
    #             print("登录成功的场景")
    #             self.app.page_app_login(username, password)
    #             time.sleep(20)
    #             # toast_text = self.app.base_get_imgtext("Please enter password")
    #             # assert expected in toast_text.replace("\n", " "), \
    #             #     f"未找到错误提示文本，实际OCR结果: {toast_text.replace("\n", " ")}"
    #         except Exception as e:
    #             print(f"发生错误:{str(e)}")









