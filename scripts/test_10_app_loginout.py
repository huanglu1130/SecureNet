import time
import pytest
import allure
@allure.feature("退出登录模块")
class TestAppLoginOut:
    def test_loginout(self,apploginout):
        apploginout.page_app_loginout_confirm()
        time.sleep(5)

