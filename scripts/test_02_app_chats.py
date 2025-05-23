# import unittest
# import pytest
# # from parameterized import parameterized
# from base.base import Base
# from pages.page_login import PageAppLogin
import time

from util import GetDriver,GetLog,read_json
# from pages.page_chats import PageAppChats
from datetime import datetime
import allure
import pytest

@allure.feature("单聊模块")
@pytest.mark.usefixtures("app")
class TestAppChat:
    def test_00_send_user(self,app):
        with allure.step("选择发送人"):
            app.page_app_click_user("test")
#
#     @pytest.mark.parametrize("desc,text,expected",
#     [tuple(item.values()) for item in read_json("D:/project/data/app_message.json")]
# )
#     @allure.story("这是发送文本")
#     def test_send_message(self,app,desc,text,expected):
#         try:
#             with allure.step(f"发送{desc}的场景"):
#                 app.page_app_send_message(text)
#                 app.verify_last_message(expected)
#         except Exception as e:
#             pytest.fail(f"发生错误:{str(e)}")
#     @allure.story("这是发送表情包")
#     def test_send_emoji(self,app):
#         with allure.step("发送表情包"):
#             app.page_app_send_emoji()
#         with allure.step("验证表情包"):
#             app.verify_last_message("[emoji_grin]")
#
#     @allure.story("这是发送语音")
#     def test_send_voice(self,app):
#         # app.page_app_click_user("test")
#         with allure.step("发送语音"):
#             app.page_app_send_voice()
#         with allure.step("验证语音"):
#             app.verify_last_voice()
#
#     @allure.story("这是发送图片")
#     def test_send_image(self,app):
#         # app.page_app_click_user("test")
#         with allure.step("发送图片"):
#             app.page_app_send_image()
#         time.sleep(5)
#         with allure.step("验证图片"):
#             app.verify_sent_image()
#
#
#     @allure.story("这是发送视频")
#     def test_send_view(self,app):
#         # app.page_app_click_user("test")
#         with allure.step("发送视频"):
#             app.page_app_send_view()
#         time.sleep(5)
#         with allure.step("验证视频"):
#             app.verify_sent_view()
#
#
#     @allure.story("这是发送文件")
#     def test_send_file(self,app):
#         # app.page_app_click_user("test")
#         with allure.step("发送文件"):
#             app.page_app_send_file()
#         with allure.step("验证文件"):
#             app.verify_file()
#
#     @allure.story("这是搜索好友+取消发送名片")
#     def test_send_card_cancel(self,app):
#         # app.page_app_click_user("test")
#         # print("这是发送名片取消")
#         app.page_app_send_card("Anna","cancel")
#
#     @allure.story("这是搜索好友+发送名片")
#     def test_send_card_confirm(self,app):
#         # app.page_app_click_user("test")
#         with allure.step("发送搜索名片"):
#             app.page_app_send_card("Anna","confirm")
#         with allure.step("验证名片"):
#             app.verify_last_card("Anna")
#     @allure.story("这是固定好友+取消发送名片")
#     def test_send_annacard_cancel(self,app):
#         # app.page_app_click_user("test")
#         # print("这是发送名片取消")
#         app.page_app_send_Annacard("cancel")
#
#     @allure.story("这是固定好友+发送名片")
#     def test_send_annacard_confirm(self,app):
#         # app.page_app_click_user("test")
#         with allure.step("发送固定名片"):
#             app.page_app_send_Annacard("confirm")
#         with allure.step("验证名片"):
#             app.verify_last_card("Anna")
#
#
#     @allure.story("是发送消息+引用回复消息")
#     def test_toast_text_reply(self,app):
#         # app.page_app_click_user("test")
#         with allure.step("发送消息文本"):
#             app.page_app_send_message("先发消息")
#         with allure.step("引用回复消息文本"):
#             app.page_app_text_reply("confirm")
#         with allure.step("验证消息文本内容"):
#             app.verify_quote_reply("text")
#
#         with allure.step("发送表情包"):
#             app.page_app_send_emoji()
#         with allure.step("引用回复表情包"):
#             app.page_app_text_reply("confirm")
#         with allure.step("验证表情包引用回复"):
#             app.verify_quote_reply("emoji")
#
#
#         with allure.step("发送语音"):
#             app.page_app_send_voice()
#         with allure.step("引用语音回复"):
#             app.page_app_voice_reply("confirm")
#         with allure.step("验证语音引用回复"):
#             app.verify_quote_reply("voice")
#
#
#         with allure.step("发送图片"):
#             app.page_app_send_image()
#         with allure.step("引用图片"):
#             app.page_app_image_reply("confirm")
#         with allure.step("验证图片引用回复"):
#             app.verify_quote_reply("image")
#
#
#         with allure.step("发送视频"):
#             app.page_app_send_view()
#         with allure.step("引用视频"):
#             app.page_app_camera_reply("confirm")
#         with allure.step("验证视频引用回复"):
#             app.verify_quote_reply("video")
#
#
#         with allure.step("发送文件"):
#             app.page_app_send_file()
#         with allure.step("引用文件"):
#             app.page_app_file_reply("confirm")
#         with allure.step("验证文件引用回复"):
#             app.verify_quote_reply("file")
#
#
#
#         with allure.step("发送名片"):
#             app.page_app_send_Annacard("confirm")
#         with allure.step("引用名片"):
#             app.page_app_card_reply("confirm")
#         with allure.step("验证名片引用回复"):
#             app.verify_quote_reply("card")
#
#     @allure.story("这是发送消息+取消引用回复消息")
#     def test_toast_reply_cancel(self,app):
#         # app.page_app_click_user("test")
#         # print("这是发送消息+取消引用回复消息")
#         with allure.step("发送消息文本"):
#             app.page_app_send_message("先发消息")
#         with allure.step("取消引用消息"):
#             app.page_app_text_reply("cancel")
    #
    # @allure.story("这是发送文本消息+多选切换单选转发消息")
    # def test_toast_forward_text_confirm(self,app):
    #     # app.page_app_click_user("test")
    #     # print("这是发送消息+转发消息")
    #     message = "先发消息切换选择转发"
    #     with allure.step("发送消息文本"):
    #         app.page_app_send_message(message)
    #     with allure.step("发送消息文本+选择用户转发"):
    #         app.page_app_text_forward_multiple_one("confirm")
    #     with allure.step("查看转发人聊天框消息内容"):
    #         app.verify_last_message(message)
    #     with allure.step("回到聊天列表"):
    #         app.page_app_send_back_click("test")

    # @allure.story("多种消息类型的转发消息场景")
    # @pytest.mark.parametrize("msg_type", ["text", "emoji","image", "video", "card", "file"])
    # # @pytest.mark.parametrize("msg_type", ["emoji"])
    # @pytest.mark.parametrize("selection_type", ["single", "multiple", "search"])
    # @pytest.mark.parametrize("action", ["confirm", "cancel"])
    # def test_forward_message(self,app, msg_type, selection_type, action):
    #     """测试各种消息类型的转发场景"""
    #     with allure.step(f"测试 {msg_type} 消息通过 {selection_type} 方式{action}转发"):
    #         msg = "测试文本消息"
    #         # 1. 发送消息
    #         app.send_message(msg_type,msg)
    #         # 2. 长按消息
    #         text = app.long_press_click_message(msg_type)
    #
    #         # 3. 选择接收人
    #         selected = app.select_recipients(selection_type, text)
    #
    #         # 4. 执行转发/取消
    #         times = app.execute_forward(selection_type,action)
    #         forward_time=times.strftime("%H:%M")
    #         time.sleep(2)
    #         # 5. 验证转发/取消
    #         app.verify_forward_result(msg_type,selected,action,forward_time)
    #         time.sleep(1)
    #
    # def test_switch_account(self,app):
    #     app.page_app_send_back()
    #     msg = ["测试消息3", "测试消息2", "测试消息3"]
    #     app.page_app_switch_account(msg)
    #     app.page_app_click_user("test")
    #
    # @allure.story("发送多条消息")
    # def test_send_select_message(self,app):
    #     app.page_app_click_user("test")
    #     msg = ["测试消息3", "测试消息2", "测试消息3"]
    #     app.page_app_send_more_message(msg)
    #
    # @allure.story("选择消息转发或删除单条以及多条")
    # @pytest.mark.parametrize("action_type", ["forward", "delete"])
    # def test_message_actions(self,app, action_type):
    #     """测试消息操作（转发/删除）"""
    #     # 对两条消息执行相同操作
    #     for type in ["select_one", "select_two"]:
    #         app.app_page_select(type)
    #         app.app_page_select_type(action_type)
    #     message_time = datetime.now()
    #     forward_time = message_time.strftime("%H:%M")
    #     msg = ["测试消息3", "测试消息2", "测试消息3"]
    #     app.verify_select(action_type,msg,forward_time)
    #     app.page_app_send_back_click("test")


    # @allure.story("长按删除消息")
    # def test_delete_message(self,app):
    #     """测试长按删除消息（取消和确认删除）"""
    #     test_msg = "测试删除消息"  # 使用更具描述性的变量名
    #
    #     with allure.step("1. 发送测试消息"):
    #         app.page_app_send_message(test_msg)
    #
    #     with allure.step("2. 测试取消删除"):
    #         app.page_app_delete_message("cancel")
    #         app.verify_delete_message("cancel",test_msg)
    #
    #     with allure.step("3. 测试确认删除"):
    #         app.page_app_delete_message("confirm")
    #         app.verify_delete_message("confirm",test_msg)



    # @allure.story("多种消息类型的撤回消息场景")
    # # @pytest.mark.parametrize("msg_types", ["text", "emoji","image", "video", "card", "file","voice"])
    # def test_recall_message(self,app):
    #     """测试各种消息类型的转发场景"""
    #     msg_types = ["text", "emoji", "image", "video", "card", "file", "voice"]
    #     # msg_types = ["file", "voice"]
    #     keyword = "You recalled a message"
    #     msg = "测试撤回消息"
    #     with allure.step(f"测试 {msg_types} 消息撤回"):
    #         for i, msg_type in enumerate(msg_types, 1):
    #             print(f"现在是测试{msg_type}")
    #             # 1. 发送消息
    #             app.send_message(msg_type,msg)
    #             # 2.撤回消息
    #             app.page_app_recall_message(msg_type)
    #             #3.校验消息是否存在
    #             app.assert_message_recalled(msg,msg_type)
    #             #4.校验撤回标识数量
    #             app.assert_recall_stats(expected_total=i)
    #             #5、校验撤回标识文本内容
    #             app.assert_last_recall_contains(keyword)
    #
    # @allure.story("多种编辑消息场景")
    # def test_edit_message(self, app):
    #     msg = "测试消息"
    #     edit_msg = "编辑测试消息"
    #     with allure.step(f"测试消息编辑"):
    #         # 1. 发送消息
    #         app.page_app_send_message(msg)
    #         # 2.点击编辑消息
    #         app.page_app_edit_message(msg,edit_msg)
    #

    TEST_MESSAGES = [
        {"type": "text", "content": "测试复制消息"},
        {"type": "emoji", "content": "[emoji_grin]"}
    ]
    @allure.story("多种复制消息场景")
    @pytest.mark.parametrize("msg_data",TEST_MESSAGES)
    def test_copy_message(self, app,msg_data):
        """测试各种消息类型的转发场景"""
        with allure.step(f"测试 {msg_data['type']} 消息复制"):
            # 1. 发送消息
            app.send_message(msg_data['type'],msg_data['content'])
            # 2.点击复制消息
            app.page_app_copy_message(msg_data['type'])
            #3.断言复制发送的消息
            app.assert_message_copy(msg_data['content'],msg_data['type'])




