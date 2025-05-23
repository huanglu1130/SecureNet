import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.page_friends_request import PageRequestAction
from pages.page_add_friends import PageAppAddFriends
from util import GetDriver, GetLog  # 修正导入语法
from pages.page_chats import PageAppChats
from pages.page_login import PageAppLogin
from pages.page_login_out import PageAppLoginOut
from pages.page_friends_info import PageAppFriendsInfo
import pytest
import time
from pathlib import Path
from typing import Dict, Any
import datetime

@pytest.fixture(scope="module")
def app_driver():
    """提供Appium驱动实例"""
    driver = GetDriver.get_app_driver()
    yield driver


def save_debug_screenshot(driver):
    """保存调试截图"""
    try:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        driver.save_screenshot(f"error_{timestamp}.png")
    except:
        pass

@pytest.fixture
def app(app_driver):  # 依赖app_driver fixture
    """提供应用实例"""
    app = PageAppChats(app_driver)  # 传入driver
    yield app
#     # 不需要app.quit()，因为app_driver会处理

@pytest.fixture
def applogin(app_driver):  # 依赖app_driver fixture
    """提供应用实例"""
    applogin = PageAppLogin(app_driver)  # 传入driver
    yield applogin

@pytest.fixture
def apploginout(app_driver):  # 依赖app_driver fixture
    """提供应用实例"""
    apploginout = PageAppLoginOut(app_driver)  # 传入driver
    yield apploginout

@pytest.fixture
def appaddfriends(app_driver):  # 依赖app_driver fixture
    """提供应用实例"""
    appaddfriends = PageAppAddFriends(app_driver)  # 传入driver
    yield appaddfriends


@pytest.fixture
def request_action(app_driver):  # 依赖app_driver fixture
    """提供应用实例"""
    request_action = PageRequestAction(app_driver)  # 传入driver
    yield request_action

@pytest.fixture
def friends_info(app_driver):  # 依赖app_driver fixture
    """提供应用实例"""
    friends_info= PageAppFriendsInfo(app_driver)  # 传入driver
    yield friends_info


import pytest
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException

@pytest.fixture(autouse=True)  # autouse=True 自动应用于所有测试用例
def back_to_home(request, app_driver):
    """每个用例执行后，尝试回到首页"""
    yield  # 先执行测试用例
    try:
        time.sleep(1)
        for _ in range(5):
            app_driver.press_keycode(4) # 4 = Android 返回键
            if check_is_home(app_driver):
                break
            time.sleep(1)
    except Exception as e:
        print(f"返回首页失败: {e}")
        app_driver.reset_app()  # 终极方案：重置应用

def check_is_home(app_driver):
    """检查当前是否在首页"""
    try:
        element = WebDriverWait(app_driver, 5).until(
            EC.element_to_be_clickable((AppiumBy.ID, 'com.mesh.im:id/tv_tab_chat'))
        )
        element.click()
        return True
    except NoSuchElementException:
        return False