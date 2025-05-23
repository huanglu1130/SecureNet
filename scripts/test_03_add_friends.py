import allure
import pytest
from time import sleep
from pages.page_friends_request import PageRequestAction
from pages.page_login_out import PageAppLoginOut
from pages.page_login import PageAppLogin
class TestAppAddFriends:
    # TEST_MESSAGES = [
    #     {"type": "Phone Number", "content": "16611111114","name":"test4"},
    #     {"type": "SecureNet ID:", "content": "J3jOYs1382","name":"test4"},
    #     {"type": "E-mail", "content": "123456789@qq.com", "name": "test4"}
    # ]
    #
    # @pytest.mark.parametrize("msg_data", TEST_MESSAGES)
    # @pytest.mark.parametrize("entrance",["+","page"])
    # # @pytest.mark.parametrize("entrance", ["page"])
    # def test_add_friends(self,back_to_home,appaddfriends,msg_data,entrance, request):
    #     """通过pytest的request对象获取当前测试序号"""
    #     test_index = request.node.name.split("[")[-1].split("]")[0]  # 获取参数化索引如0/1/2
    #     request_content = f"我在测试，发送好友请求{test_index}"
    #     ##1.搜索好友信息
    #     appaddfriends.page_app_search_friends(entrance,msg_data['type'],msg_data['content'],msg_data['name'])
    #     ##2.发送添加好友请求
    #     appaddfriends.page_app_add_friends(entrance,msg_data['name'],request_content)
    #     ##3.校验是否发起请求成功
    #     appaddfriends.verify_add_friends_toast("Successfully Sent")
    #     ##4.返回到聊天列表页面
    #     appaddfriends.page_app_add_friends_back(entrance)
    #     ##5.查看好友请求页面
    #     status = "Waiting for verification"
    #     content = "Me:"+request_content
    #     print(f"发送内容{content}")
    #     appaddfriends.page_app_new_friends(msg_data['name'],content,status)

    # @allure.story("删除好友关系+添加好友")
    # @pytest.mark.parametrize("action_type", ["reject","accept"])
    # def test_request_action(self,back_to_home,apploginout,applogin,request_action,action_type,delete_friends):
    #     ## A账号发起好友请求
    #     request_action.page_app_request_new("Phone Number", "16611111115", "test5")
    #     #退出登录+登录B账号
    #     apploginout.page_app_loginout_confirm()
    #     applogin.page_app_login_test("16611111115", "123456")
    #     #查看好友请求页面
    #     request_action.page_app_request_action(action_type)
    #     request_action.verify_request_status(action_type)
    #     if action_type == "accept":
    #         request_action.page_app_delete_friends("admin")
    #     # 退出登录+登录A账号
    #     apploginout.page_app_loginout_confirm()
    #     applogin.page_app_login_test("16621254498", "123456")
    #     if action_type == "accept":
    #         request_action.page_app_delete_friends("测试添加好友")

    # @allure.story("删除好友关系")
    # def test_delete_friends(self,request_action):
    #     request_action.page_app_delete_friends("test5")

    @allure.story("删除好友请求")
    def test_delete_request(self,back_to_home,request_action):## A账号发起好友请求
        request_action.page_app_request_new("Phone Number", "16611111114", "test4")
        request_action.page_app_delete_requests()


