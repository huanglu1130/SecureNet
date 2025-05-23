import allure
import pytest
from time import sleep
from pages.page_friends_request import PageRequestAction
from pages.page_login_out import PageAppLoginOut
from pages.page_login import PageAppLogin
class TestAppFriendsInfo:
    @allure.story("查看好友资料")
    def test_block_friends(self,friends_info):
        name = "test6"
        ## 进入好友资料页
        friends_info.page_app_friends_info(name)
        ## 拉黑好友
        friends_info.page_app_block_friends()
        friends_info.verify_block_friends("admin")
    def test_unblock_friends(self,friends_info):
        # 解除拉黑
        friends_info.page_app_unblock_friends("test6")
