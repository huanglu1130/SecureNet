from time import sleep
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from appium.webdriver.common.appiumby import AppiumBy
from unicodedata import normalize
from base.base import Base
from base.base_toast_button import BaseToast
import pages
from pages.page_select_friends import PageSelectFriends
from pages.page_select_chat import PageSelectAChat
from pages.page_login_out import PageAppLoginOut
from pages.page_login import PageAppLogin
from pages.page_sync_confirmation import PageAppSync
import allure
import pytest
from datetime import datetime
from selenium.common.exceptions import NoSuchElementException

@allure.epic("单聊模块功能")
@allure.feature("聊天框功能")
class PageAppChats(Base):
    # 1、点击指定好友列表进入聊天框
    @allure.story("聊天列表点击聊天对象")
    def page_app_click_user(self,user):
        username = self.driver.find_element(
        AppiumBy.ANDROID_UIAUTOMATOR,
        f'new UiSelector().text("{user}")'
        )
        username.click()
        title = self.base_find(pages.contact_title)
        assert title.text == user, f"不是和{user}聊天'，识别到的好友：{title.text}"



    # 2、输入文字
    def page_app_input_text(self,value):
        self.base_input(pages.app_message_input,value)

    #3、点击发送文本
    def page_app_click_send(self):
        with allure.step("点击发送消息"):
            self.base_click(pages.app_message_send)

    #4、消息发送成功
    def page_app_send_success(self):
        try:
            if self.base_get_last(pages.app_message_success) is True:
                return True
        except Exception as e:
            return False

    #整合发送文本消息
    @allure.title("发送文本消息")
    def page_app_send_message(self, message):
        """发送消息通用方法"""
        self.page_app_input_text(message)
        self.page_app_click_send()

    #整合发送文本消息
    @allure.title("发送多条文本消息")
    def page_app_send_more_message(self, test_messages):
        """发送消息通用方法"""
        for msg in test_messages:
            self.page_app_send_message(msg)

    #发送表情包
    @allure.title("发送表情包")
    def page_app_send_emoji(self):
        self.base_click(pages.app_message_emoji)
        #选择第一个表情包
        self.base_click(pages.app_message_emoji_1)
        #点击send
        self.page_app_click_send()
        self.base_click(pages.app_message_back)


    # 3、点击发送语音消息
    @allure.title("发送语音消息")
    def page_app_send_voice(self):
        # 点击语音键盘
        self.base_click(pages.app_message_voice_keyboard)
        sleep(2)
        voice_btn = self.base_find(pages.app_message_voice_say)
        self.base_long_press(voice_btn,3)
        print("微信语音消息发送成功")
        # self.base_click(pages.app_message_back)


    # 3、点击发送相册图片
    @allure.title("发送图片消息")
    def page_app_send_image(self):
        try:
            #点击+号
            self.base_click(pages.app_message_more)
            #选择相册
            self.base_click(pages.app_album)
            self.base_click(pages.app_album_choice)
            self.base_click(pages.app_album_folder)
            first_image =  WebDriverWait(self.driver, 2).until(
                EC.presence_of_element_located(pages.app_album_first)
                )
            if first_image:
                first_image.click()
            else:
                print("元素未找到")
            self.base_click(pages.app_album_complete)
            sleep(2)
            self.base_click(pages.app_message_back)
            # self.base_select_option(pages.app_message_black)
        except Exception as e:
            pytest.fail(f"图片发送失败: {str(e)}")

        # 3、点击摄影发送

    @allure.title("发送视频消息")
    def page_app_send_view(self):
         # 点击+号
         self.base_click(pages.app_message_more)
        #选择camera
         self.base_click(pages.app_camera)
         view_btn = self.base_find(pages.app_camera_view)
         self.base_long_press(view_btn,5)
         self.base_click(pages.app_camera_view_send)
         sleep(10)
         self.base_click(pages.app_message_back)
         print("视频拍摄发送成功")
         # self.base_select_option(pages.app_message_black)

    #4、点击文件，选择文件发送
    @allure.title("发送文件消息")
    def page_app_send_file(self):
        # 点击+号
        self.base_click(pages.app_message_more)
        # 选择file
        self.base_click(pages.app_file)
        #选择file文件
        self.base_click(pages.app_file_ImageButton)
        sleep(0.5)
        self.base_click(pages.app_file_doc)
        self.base_click(pages.app_file_MeshDownload)
        sleep(0.5)
        self.base_click(pages.app_file_send)
        sleep(5)
        self.base_click(pages.app_message_back)
        # self.base_select_option(pages.app_message_black)

    #搜索名片选择发送
    @allure.title("搜索好友+发送名片消息")
    def page_app_send_card(self,contact_name,action):
        select_friends = PageSelectFriends(self.driver)
        common_steps = [
            # ("选择联系人",lambda:self.page_app_click_user(name)),
            ("打开更多功能", lambda: self.base_click(pages.app_message_more)),
            ("选择名片功能", lambda: self.base_click(pages.app_card)),
            # ("输入联系人", lambda: self.base_input(pages.app_card_search, value=contact_name)),
            ("检查选择联系人列表",lambda :select_friends.page_show_select_friends()),
            ("输入查询条件+清空", lambda: select_friends.page_search_user_clear()),
            ("输入联系人", lambda: select_friends.page_search_user(contact_name))
            # ("点击联系人",lambda:self.base_click(pages.app_card_search_result))
        ]
        try:
            # 执行公共步骤
            for step_name, step_action in common_steps:
                step_action()
                sleep(0.5)  # 适当等待
            if action == "confirm":
                self.base_click(pages.app_card_confirm)
                result_msg = f"成功发送{contact_name}的名片"
            elif action == "cancel":
                self.base_click(pages.app_card_cancel)
                result_msg = "已取消发送名片"
            else:
                raise ValueError("action参数必须是'confirm'或'cancel'")
            self.base_click(pages.app_message_back)
            return True, action
        except Exception as e:
            pytest.fail(f"名片操作失败: {str(e)}")
            # self.driver.save_screenshot(f"error_card_{action}.png")

        # 选择名片发送
    @allure.title("发送固定好友名片消息")
    def page_app_send_Annacard(self, action):
        common_steps = [
            # ("选择联系人", lambda: self.page_app_click_user(name)),
            ("打开更多功能", lambda: self.base_click(pages.app_message_more)),
            ("选择名片功能", lambda: self.base_click(pages.app_card)),
            ("选择Anna联系人", lambda: self.base_click(pages.app_card_anna))
        ]
        try:
            # 执行公共步骤
            for step_name, step_action in common_steps:
                step_action()
                sleep(0.5)  # 适当等待
            if action == "confirm":
                self.base_click(pages.app_card_confirm)
                result_msg = f"成功发送Anna的名片"
            elif action == "cancel":
                self.base_click(pages.app_card_cancel)
                result_msg = "已取消发送名片"
            else:
                raise ValueError("action参数必须是'confirm'或'cancel'")
            print(result_msg)
            # self.base_select_option(pages.app_message_black)
            self.base_click(pages.app_message_back)
        except Exception as e:
            pytest.fail(f"名片操作失败: {str(e)}")
            # self.driver.save_screenshot(f"error_card_{action}.png")


    @allure.title("发起语音通话")
    def page_app_send_call(self):
        print("这是发起语音通话")
        #点击发起语音通话
        self.base_click(pages.app_voice_call)
        # 等待通话建立
        sleep(5)

    @allure.title("挂断语音通话")
    def page_app_end_call(self):
        print("挂断语音通话")
        #点击挂断按钮
        self.base_click(pages.app_call_hangup)
        # 等待返回聊天界面
        sleep(3)

    @allure.story("引用消息")
    def page_app_reply(self,loc,message_type,action):
        # 点击列表好友
        # self.page_app_click_user(name)
        sleep(2)
        text = self.base_get_last_message(loc)
        try:
            BaseToast(self.driver).click_toast_first_button(text,message_type,"Reply")
            if action == "confirm":
                self.base_input(pages.app_toast_reply,"回复消息")
                self.base_click(pages.app_message_send)
            elif action == "cancel":
                self.base_input(pages.app_toast_reply, "取消引用了回复消息")
                self.base_click(pages.app_toast_reply_clear)
                self.base_click(pages.app_message_send)
            else:
                raise ValueError("action参数必须是'confirm'或'cancel'")
            return True
        except Exception as e:
            pytest.fail(f"reply按钮测试失败: {str(e)}")
            # self.driver.save_screenshot("reply_button_failed.png")

    @allure.title("引用文本消息")
    def page_app_text_reply(self, action):
        print("这是文本回复消息")
        self.page_app_reply(pages.app_message_all,"Text", action)

    @allure.title("引用图片消息")
    def page_app_image_reply(self, action):
        self.page_app_reply(pages.app_message_image,"Image", action)

    @allure.title("引用语音消息")
    def page_app_voice_reply(self, action):
        self.page_app_reply(pages.app_message_voice,"Voice", action)

    @allure.title("引用文件消息")
    def page_app_file_reply(self, action):
        print("这是文件回复消息")
        self.page_app_reply(pages.app_file_send_doc,"File", action)

    @allure.title("引用视频消息")
    def page_app_camera_reply(self, action):
        print("这是视频回复消息")
        self.page_app_reply(pages.app_camera_view_play, "Video",action)

    @allure.title("引用名片消息")
    def page_app_card_reply(self, action):
        print("这是名片回复消息")
        self.page_app_reply(pages.app_send_card_title,"Card", action)

        # 消息类型参数化配置

    MESSAGE_TYPES = {
        "text": {
            "locator": pages.app_message_all,
            "content": "测试文本消息"
        },
        "emoji":{
            "locator": pages.app_emoji,
            "content": "[emoji_grin]"
        },
        "image": {
            "locator": pages.app_message_image,
            "content": "Image"
        },
        "video": {
            "locator": pages.app_camera_view_play,
            "content": "Video"
        },
        "card": {
            "locator": pages.app_send_card_title,
            "content": "[Card]"
        },
        "file": {
            "locator": pages.app_file_send_doc,
            "content": "[File]"
        },
        "voice": {
            "locator": pages.app_message_voice,
            "content": "[Voice]"
        }
    }

    @allure.step("发送 {msg_type} 消息")
    def send_message(self, msg_type: str,msg):
        """发送指定类型的消息"""
        if msg_type == "text":
            self.page_app_send_message(msg)
        if msg_type == "emoji":
            self.page_app_send_emoji()
        # 各类型特有操作
        elif msg_type == "image":
            self.page_app_send_image()
        elif msg_type == "video":
            self.page_app_send_view()
        elif msg_type == "card":
            self.page_app_send_Annacard("confirm")
        elif msg_type == "file":
            self.page_app_send_file()
        elif msg_type == "voice":
            self.page_app_send_voice()


    @allure.step("长按消息点击转发")
    def long_press_click_message(self, msg_type: str):
        """长按指定类型的消息"""
        locators = self.MESSAGE_TYPES[msg_type]["locator"]
        locator = self.base_get_last_message(locators)
        text = self.MESSAGE_TYPES[msg_type]["content"]
        BaseToast(self.driver).click_toast_button(locator, "Forward")
        return text


    # @allure.step("点击转发按钮")
    # def click_forward_button(self):
    #     forward_btn = (AppiumBy.XPATH, "//*[@text='转发']")
    #     self.wait.until(EC.element_to_be_clickable(forward_btn)).click()

    @allure.step("选择接收人: {selection_type}")
    def select_recipients(self,selection_type: str,text):
        """
        选择消息接收人
        :param selection_type: single|multiple|search
        :param names: 可选，指定要选择的好友名称列表
        :return: 选择的好友名称元组
        """
        select_chat = PageSelectAChat(self.driver)
        if selection_type == "search":
            select_chat.page_search_chat_clear()
            select_chat.page_search_chat("Anna")
            select_chat.verify_sent_to(text, "Anna")
            return 'Anna'

        elif selection_type == "multiple":
            selected = []
            name1,name2 = select_chat.page_multiple_chat()
            select_chat.verify_sent_to_title()
            select_chat.verify_sent_to_content(text)
            return name1,name2

        else:  # single
            name_element = self.base_find(pages.app_forward_user)
            name = name_element.text.strip()
            self.base_click(pages.app_forward_user)
            select_chat.verify_sent_to(text, name)
            return name

    @allure.step("执行转发操作")
    def execute_forward(self,selection_type, action: str):
        select_chat = PageSelectAChat(self.driver)
        """执行发送或取消操作"""
        if action == "confirm":
            select_chat.page_send_chat_confirm()
        else:
            if selection_type == "search":
                select_chat.page_send_chat_cancel()
                self.base_click(pages.app_forward_search_cancel)
                self.base_click(pages.app_forward_cancel_back)
            else:
                select_chat.page_send_chat_cancel()
                self.base_click(pages.app_forward_cancel_back)
        return datetime.now()


    @allure.step("验证转发结果")
    def verify_forward_result(self, msg_type: str, recipients, action: str,forward_time):
        """验证转发是否成功"""
        if action == "confirm":
            self.page_app_send_back()
            # 验证消息列表更新
            if isinstance(recipients, str):
                recipients = [recipients]
            for name in recipients:
                print(f"接收人{name}")
                if msg_type == "text":
                    self.verify_forward(name,"测试文本消息",forward_time)
                # # 各类型特有操作
                elif msg_type == "emoji":
                    self.verify_forward(name,"[emoji_grin]",forward_time)
                elif msg_type == "image":
                    self.verify_forward(name,"[Photo]",forward_time)
                elif msg_type == "video":
                    self.verify_forward(name,"[Video]",forward_time)
                elif msg_type == "card":
                    self.verify_forward(name,"[Contact Card]",forward_time)
                elif msg_type == "file":
                    self.verify_forward(name,"[File]",forward_time)
            self.page_app_click_user("test")
        else:
            print("取消转发")
            # 验证停留在选择界面
            # assert WebDriverWait(self.driver, 10).until(
            #                 EC.presence_of_element_located(pages.app_forward_cancel_back)
            # )), "取消转发后应仍停留在选择界面"



    def verify_forward(self, name,expected_content,forward_time):
        # 1. 返回聊天列表
        # self.page_app_send_back()
        # 2. 定位目标聊天项
        chat_item = self._find_chat_item(name)
        # 3. 验证消息内容
        actual_content = chat_item.find_element(By.XPATH, './/*[@resource-id="com.mesh.im:id/lastMsg"]').text
        # print("找到了消息"+actual_content)
        msg_time = chat_item.find_element(
            By.XPATH, './/android.widget.TextView[@resource-id="com.mesh.im:id/time"]').text
        time = msg_time.split()[1]
        print("需要验证消息" + expected_content)
        content_ok = expected_content in actual_content
        time_ok = forward_time in time
        return content_ok,time_ok

    def _find_chat_item(self,contact_name):
            app_list_item = f'//android.view.ViewGroup[.//*[@resource-id="com.mesh.im:id/name" and @text="{contact_name}"]]'

            return WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.XPATH, app_list_item)))



    @allure.step("退出登录，其他账号给该账号发消息")
    def page_app_switch_account(self,test_messages):
        loginout = PageAppLoginOut(self.driver)
        login = PageAppLogin(self.driver)
        loginout.page_app_loginout_confirm()
        sleep(5)
        login.page_app_option()
        login.page_app_click_accpet()
        login.page_app_login("16611111111","123456")
        sleep(10)
        self.page_app_click_user("admin")
        for msg in test_messages:
            self.page_app_send_message(msg)
        self.base_click(pages.app_message_back)
        sleep(3)
        loginout.page_app_loginout_confirm()
        login.page_app_option()
        login.page_app_click_accpet()
        login.page_app_login("16621254498", "123456")
        sleep(5)


    @allure.step("长按消息点击选择")
    def app_page_select(self,type):
        """长按指定类型的消息"""
        # 点击列表好友
        # self.page_app_click_user(name)
        sleep(2)
        try:
            text = self.base_get_last_message(pages.app_message_all)
            sleep(2)
            BaseToast(self.driver).click_toast_button(text, "Select")
            # 执行选择操作
            if type == "select_one":
                self.base_get_last_message(pages.app_select).click()
            else:
                 self.base_get_last_message(pages.app_select).click()
                 self.base_get_message(pages.app_select).click()
        except Exception as e:
            pytest.fail(f"Select按钮测试失败: {str(e)}")


    @allure.step("选择转发或者删除")
    def app_page_select_type(self,type):
        select_chat = PageSelectAChat(self.driver)
        if type == "forward":
            self.base_click(pages.app_select_forward)
            self.base_click(pages.app_forward_user)
            select_chat.page_send_chat_confirm()
        else:
            self.base_click(pages.app_select_delete)
            self.base_click(pages.app_select_delete_cancel)
            self.base_click(pages.app_select_delete)
            self.base_click(pages.app_select_delete_confirm)

    @allure.step("检查消息是否转发成功或者删除成功")
    def verify_select(self,type,text,forward_time):
        if type == "forward":
            self.page_app_send_back_click("test2")
            message_content = self.get_all_message_texts(pages.app_message_all)
            message_time_list = self.get_latest_messages(pages.app_message_time,3)
            # print(f"所有的消息是 {message_content}")
            for msg in text:
                assert msg in message_content, f"消息 '{msg}' 未被成功转发"
            # 转换为 datetime 对象
            forward = self.time_str_to_datetime(forward_time)
            message_times = [self.time_str_to_datetime(t) for t in message_time_list]
            # print(f"所有的消息是 {message_times}")
            # 检查每个时间差是否 <= 10 秒
            for msg_time in message_times:
                print(f"消息时间是 {msg_time}")
                time_diff = abs((forward - msg_time).total_seconds())
                # print(f"时间差是 {time_diff}")
                assert time_diff <= 10, f"时间差 {time_diff} 秒超过 10 秒限制（{forward} vs {msg_time.strftime('%H:%M')}）"
            print("断言成功：所有时间差均不超过 10 秒")
            self.page_app_send_back_click("test")
        else:
            message_content = self.get_all_message_texts(pages.app_message_all)
            for msg in text:
                assert msg not in message_content, f"消息 '{msg}' 未被成功删除"

    def time_str_to_datetime(self,time_str):
        """将 'HH:MM' 格式的时间字符串转为 datetime 对象"""
        return datetime.strptime(time_str, "%H:%M")




    @allure.title("多选好友切换到单选好友转发消息")
    def page_app_forward_multiple_to_one(self, loc, text, action):
                # 点击列表好友
                # self.page_app_click_user(name)
        select_chat = PageSelectAChat(self.driver)
        try:
            BaseToast(self.driver).click_toast_button(loc, "Forward")
            select_chat.page_show_select_chat()
            if action == "confirm":
                name1 = select_chat.page_multiple_to_one_chat()
                sleep(3)
                select_chat.verify_sent_to(text,name1)
                select_chat.page_send_chat_confirm()
                sleep(2)
                self.page_app_send_back_click(name1)
            elif action == "cancel":
                name1 = select_chat.page_multiple_to_one_chat()
                sleep(3)
                select_chat.verify_sent_to(text,name1)
                select_chat.page_send_chat_cancel()
            else:
                raise ValueError("action参数必须是'confirm'或'cancel'")
        except Exception as e:
            pytest.fail(f"forward按钮测试失败: {str(e)}")
            # self.driver.save_screenshot("reply_button_failed.png")


    @allure.title("多选切换单选转发文本消息")
    def page_app_text_forward_multiple_one(self,action):
        element = self.base_get_last_message(pages.app_message_all)
        text = element.text
        self.page_app_forward_multiple_to_one(element,text,action)

    @allure.step("长按删除消息")
    def page_app_delete_message(self,action_type):
        element = self.base_get_last_message(pages.app_message_all)
        try:
            BaseToast(self.driver).click_toast_button(element, "Delete")
            notice_text = self.base_find(pages.app_delete_notice).text
            assert notice_text in "Are you sure to delete?",f"二次确认提示语{notice_text}不正确"
            if action_type == "confirm":
                self.base_click(pages.app_delete_confirm)
            else:
                self.base_click(pages.app_delete_cancel)
        except Exception as e:
            pytest.fail(f"delete按钮测试失败: {str(e)}")

    @allure.step("长按删除消息断言")
    def verify_delete_message(self, action_type,text):
        message_content = self.get_all_message_texts(pages.app_message_all)
        if action_type == "confirm":
            assert text not in message_content, f"消息 '{text}' 没有被成功删除"
        else:
            assert text in message_content, f"消息 '{text}' 取消删除没有成功"

    @allure.step("长按消息点击撤回")
    def page_app_recall_message(self, msg_type: str):
        """长按指定类型的消息"""
        locators = self.MESSAGE_TYPES[msg_type]["locator"]
        locator = self.base_get_last_message(locators)
        BaseToast(self.driver).click_toast_button(locator, "Recall")

    @allure.step("校验撤回消息是否存在")
    def assert_message_recalled(self, text, msg_type):
        """断言消息已撤回"""
        # 1. 原消息不应存在
        if msg_type == "text":
            assert not self._is_element_present((By.XPATH,f'//android.widget.TextView[@resource-id="com.mesh.im:id/content" and @text="{text}"]'))
        else:
            locators = self.MESSAGE_TYPES[msg_type]["locator"]
            sleep(2)
            assert not self._is_element_present(locators)


    @allure.step("取当前所有撤回标识元素")
    def get_recall_notices(self):
        """获取当前所有撤回标识元素"""
        recall_notice = self.driver.find_elements(*pages.app_recall_notice)
        return recall_notice

    @allure.step("断言撤回统计")
    def assert_recall_stats(self, expected_total):
        current_notices = self.get_recall_notices()
        print(f"当前撤回数量是{len(current_notices)}")
        print(f"预期撤回数量是{expected_total}")
        assert len(current_notices) == expected_total, (
            f"总撤回数不符！预期: {expected_total}，实际: {len(current_notices)}"
        )
    @allure.step("断言最新撤回标识包含关键词")
    def assert_last_recall_contains(self, keyword):
        """断言最新撤回标识包含关键词"""
        last_notice = self.get_recall_notices()[-1].text
        assert keyword in last_notice, f"最新撤回标识未包含'{keyword}'"




    @allure.step("长按消息点击编辑")
    def page_app_edit_message(self,msg,edit_msg):
        """长按指定类型的消息"""
        element = self.base_get_last_message(pages.app_message_all)
        #点击编辑按钮
        BaseToast(self.driver).click_toast_button(element, "Edit")
        sleep(3)
        #断言需要编辑的消息内容
        self.assert_edit_content(msg)
        #编辑框输入消息
        self.base_input(pages.app_edit_message_input,edit_msg)
        #点击完成
        self.base_click(pages.app_edit_done)
        #断言编辑标志
        self.assert_edited_sign()

    def assert_edit_content(self,msg):
        edit_content = self.base_find(pages.app_edit_message_content).text
        assert edit_content == msg,f"编辑引用的消息内容{edit_content}不正确，应为{msg}"

    def assert_edited_sign(self):
        edit_sign = self.base_get_last_message(pages.app_edit).text
        assert edit_sign == "Edited",f"编辑后的消息标志{edit_sign}不正确"

    @allure.step("长按消息点击copy")
    def page_app_copy_message(self,msg_type):
        """长按指定类型的消息"""
        locators = self.MESSAGE_TYPES[msg_type]["locator"]
        locator = self.base_get_last_message(locators)
        BaseToast(self.driver).click_toast_button(locator, "Copy")
        element = self.base_find(pages.app_message_input)
        BaseToast(self.driver).click_toast_button(element, "Paste")
        sleep(1)
        self.page_app_click_send()


    @allure.step("断言消息复制有没有成功发送")
    def assert_message_copy(self,expected_text,msg_type):
        """验证消息是否发送成功"""
        try:
            # 定位最后一条消息（假设最新消息在列表末尾）
            locators = self.MESSAGE_TYPES[msg_type]["locator"]
            first_text = self.base_get_last_message(locators)
            # 精确匹配文本内容
            assert first_text.text == expected_text, (
                f"消息发送失败！预期: '{expected_text}'，实际: '{first_text.text}'")
            # 定位最后第二条条消息（假设最新消息在列表末尾）
            second_text = self.base_get_message(locators)
            # 精确匹配文本内容
            assert second_text.text == expected_text, (
                f"消息发送失败！预期: '{expected_text}'，实际: '{second_text.text}'")
            print("✔ 消息发送验证成功")
        except NoSuchElementException:
            raise AssertionError("未找到发送的消息")







    def page_app_send_back(self):
        self.base_click(pages.app_message_back)

    def page_app_send_back_click(self,name):
        self.base_click(pages.app_message_back)
        sleep(2)
        self.page_app_click_user(name)



    @allure.step("验证最后一条消息内容")
    def verify_last_message(self, expected):
        # 定位最后一条消息元素
        last_msg = self.base_get_last_message(pages.app_message_all)
        with allure.step("验证消息内容"):
            if expected not in last_msg.text:
                error_msg = f"验证失败！\n预期包含: '{expected}'\n实际内容: '{last_msg.text}'"
                pytest.fail(error_msg)
        with allure.step("检查消息发送状态"):
            if self.base_get_last(pages.app_message_success) is True:
                allure.attach("发送消息成功")
            else:
                pytest.fail("消息发送失败")
        return True

    @allure.step("验证最后一条语音内容")
    def verify_last_voice(self):
        last_voice = self.base_get_last_message(pages.app_message_voice)
        with allure.step("验证语音消息秒数"):
            if last_voice.text == "3''":
                if self.base_get_last(pages.app_message_success) is True:
                    allure.attach("语音消息发送成功")
            else:
                pytest.fail("语音消息发送失败")
        #播放语音消息
        elements= self.base_get_last_message(pages.app_message_voice_view)
        with allure.step("验证语音消息秒数"):
            if elements:
                elements.click()
            else:
                pytest.fail("元素未找到")
        # self.base_click(pages.app_message_voice_view)
        sleep(5)
        return True

    @allure.step("验证最后一条图片内容")
    def verify_sent_image(self):
        """验证已发送消息中的图片元素"""
        expected_text = "测 试 创 建 时 间"
        try:
            # 定位已发送的图片元素
            image_element = self.base_get_last_message(pages.app_message_image)
            # # 验证关键属性
            # assert image_element.is_displayed(), "图片未显示"
            #验证尺寸
            with allure.step("验证图片尺寸"):
                size = image_element.size
                assert size['width'] > 50 and size['height'] > 50, "图片尺寸过小"
            #点击查看图片
            with allure.step("验证图片内容文字"):
                image_element.click()
                extracted_text = self.base_get_img(pages.app_message_image_view)
            # 4. 断言是否包含预期文字
                assert expected_text in extracted_text, f"图片中未找到文字'{expected_text}'，识别到的文字：{extracted_text}"
                print(f"成功验证图片中包含文字: {expected_text}")
            #下载图片
            with allure.step("下载图片"):
                self.base_click(pages.app_message_image_down)
                sleep(1)
            # text = self.base_get_imgtext("success")
            # if 'Save success' in text:
            #     print("图片下载成功")
            # else:
            #     print("图片下载失败")
            #查看图片之后点击返回到聊天框
            with allure.step("验证图片发送状态"):
                self.base_click(pages.app_message_image_back)
                if self.base_get_last(pages.app_message_success) is True:
                    allure.attach("图片消息发送成功")
                else:
                    allure.attach("图片消息发送失败")
            return True
        except Exception as e:
            pytest.fail(f"❌ 图片验证失败: {str(e)}")
# 验证发送的视频
    @allure.step("验证最后一条视频内容")
    def verify_sent_view(self):
        try:
            view_element = self.base_get_last_message(pages.app_camera_view_play)
            with allure.step("验证视频是否存在可点击，可以下载"):
                if view_element:
                    view_element.click()
                else:
                   print("元素未找到")
                sleep(5)
                self.base_click(pages.app_camera_view_down)
                self.base_click(pages.app_camera_view_play_back)
                self.page_app_send_success()
            return True
        except Exception as e:
            pytest.fail(f"❌ 播放视频或者发送失败: {str(e)}")
    #验证发送的文件
    @allure.step("验证最后一条文件内容")
    def verify_file(self):
        file_name = 'Voip 翻译 加密聊天需求整理_034040.docx'
        expected_text = "1 VOIP 功 能"
        try:
            with allure.step("验证文件title是否一致，是否存在可点击，可以打开，打开内容是否一致"):
                last_file = self.base_get_last_message(pages.app_file_send_doc)
                assert file_name in last_file.text, f"发送的文件名不匹配，期望: {file_name}, 实际: {last_file.text}"
                if self.base_get_last(pages.app_message_success) is True:
                    print("文件发送成功")
                else:
                    pytest.fail("文件发送失败")
                last_file.click()
            # receive_file = self.base_find(pages.app_file_receive)
            # if self.base_find(pages.app_file_receive):
            #     print("点击接收文件")
            #     self.base_click(pages.app_file_receive)
                if self.base_find(pages.app_file_open):
                    print("点击打开文件")
                    self.base_click(pages.app_file_open)
                    sleep(5)
            #截图返回文本
                print("截图对比文字")
                locators = [pages.app_file_open_text, pages.app_file_open_2_text]
                for loc in locators:
                    try:
                        extracted_text = self.base_get_img(loc)
                        break
                    except:
                        print("第一次截图失败")
                        continue
                else:
                    raise Exception("所有方式均失败")
                # extracted_text = self.base_get_img(pages.app_file_open_text)
                sleep(2)
            # 4. 断言是否包含预期文字
                assert expected_text in extracted_text, f"图片中未找到文字'{expected_text}'，识别到的文字：{extracted_text}"
                allure.attach(f"成功验证图片中包含文字: {expected_text}")
                sleep(2)
                self.base_click(pages.app_file_view_back)
                sleep(2)
                self.base_click(pages.app_file_open_back)
            return True
        except AssertionError as e:
            pytest.fail(str(e))


    @allure.step("验证最后一条名片内容")
    def verify_last_card(self, expected):
        # 定位最后一条消息元素
        sleep(2)
        last_msg_title = self.base_get_last_message(pages.app_send_card_title)
        last_msg_detail = self.base_get_last_message(pages.app_send_card_detail)
        self.page_app_send_success()
        with allure.step("验证名片title是否一致，是否存在View Details按钮，可以点击"):
            if expected not in last_msg_title.text:
                pytest.fail(f"验证失败！\n预期包含: '{expected}'\n实际内容: '{last_msg_title.text}'")
            if last_msg_detail.text == "View Details":
                last_msg_detail.click()
            else:
                pytest.fail(f"没有展示View Details,展示{last_msg_detail.text}")
        #返回到聊天对话框
            self.base_click(pages.app_send_card_detail_back)

    def transfer_text(self):
        file_text = self.base_get_last_message(pages.app_reply_photo).text
        normalized_text = normalize('NFKC', file_text).strip()  # 合并空白/转换全角
        return normalized_text

    @allure.step("验证引用消息内容")
    def verify_quote_reply(self,type):
        try:
            with allure.step("验证引用内容是否正确，引用回复内容是否正确"):
            # """验证引用回复是否正确显示"""
                if type == "text":
                    assert self.base_get_last_message(pages.app_reply_text).text == "先发消息", "文本引用回复消息内容不匹配"
                elif type == "emoji":
                    assert self.base_get_last_message(pages.app_reply_emoji).text == "[emoji_grin]", "表情包引用回复消息内容不匹配"
                elif type == "voice":
                    assert self.base_get_last_message(pages.app_reply_text).text == "[Voice] 3''", "语音引用回复消息内容不匹配"
                elif type == "image":
                    assert self.transfer_text() == "[Photo]", "图片引用回复消息内容不匹配"
                elif type == "video":
                    assert self.transfer_text() == "[Video]", "视频引用回复消息内容不匹配"
                elif type == "file":
                    assert self.transfer_text() == "[File]", "文件引用回复消息内容不匹配"
                elif type == "card":
                    assert self.transfer_text() == "[Contact Card]", "名片引用回复消息内容不匹配"
                else:
                    pytest.fail("回复的类型不存在")
            # 获取最后一条消息元素
                last_msg = self.base_get_last_message(pages.app_toast_reply_content)
                assert last_msg.text == "回复消息", "回复消息内容不匹配"
                self.page_app_send_success()
                print("引用回复断言通过")
            return True
        except Exception as e:
            pytest.fail(f"❌ 消息引用断言失败: {str(e)}")

    # @allure.step("验证自己发送的消息长按之后出现的按钮")
    # def verify_long_press_toast(self, message_type):
    #     # 定位最后一条消息元素
    #     sleep(2)
    #     with allure.step(f"验证长按{message_type}消息的按钮展示"):
    #         # 获取最后一条消息元素
    #         locators = {
    #             "Text": pages.app_message_all,
    #             "File": pages.app_file_send_doc,
    #             "Image": pages.app_message_image,
    #             "Video":pages.app_camera_view_play,
    #             "Card":pages.app_send_card_title
    #         }
    #         loc = self.base_get_last_message(locators[message_type])
    #
    #         # 长按消息并获取按钮数据
    #         BaseToast(self.driver).long_press_message(loc)
    #         data = BaseToast(self.driver)._find_button()
    #
    #         # 从返回数据中提取按钮文本
    #         actual_button_texts = data.get('text', [])
    #         actual_button_texts = [text.strip() for text in actual_button_texts if text.strip()]
    #         # 预期结果配置
    #         expected_config = {
    #             "Text": {
    #                 "expected": ["Reply", "Forward", "Copy", "Edit", "Select", "Recall", "Delete"],
    #                 "unexpected": []
    #             },
    #             "File": {
    #                 "expected": ["Reply", "Forward", "Select", "Recall", "Delete"],
    #                 "unexpected": ["Copy", "Edit"]
    #             },
    #             "Image": {
    #                 "expected": ["Reply", "Forward", "Select", "Recall", "Delete"],
    #                 "unexpected": ["Copy", "Edit"]
    #             },
    #             "Video": {
    #                 "expected": ["Reply", "Forward", "Select", "Recall", "Delete"],
    #                 "unexpected": ["Copy", "Edit"]
    #             },
    #             "Card": {
    #                 "expected": ["Reply", "Forward", "Select", "Recall", "Delete"],
    #                 "unexpected": ["Copy", "Edit"]
    #             }
    #         }
    #
    #         # 验证按钮
    #         config = expected_config[message_type]
    #         missing_buttons = [btn for btn in config["expected"] if btn not in actual_button_texts]
    #         unexpected_buttons = [btn for btn in config["unexpected"] if btn in actual_button_texts]
    #
    #         # 记录结果
    #         if not missing_buttons and not unexpected_buttons:
    #             allure.attach(
    #                 f"长按{message_type}消息按钮展示正确",
    #                 f"实际按钮: {actual_button_texts}"
    #             )
    #         else:
    #             pytest.fail(
    #                 f"{message_type}消息按钮不正确\n"
    #                 f"缺少的按钮: {missing_buttons}\n"
    #                 f"不应出现但出现的按钮: {unexpected_buttons}\n"
    #                 f"预期包含: {config['expected']}\n"
    #                 f"预期不包含: {config['unexpected']}\n"
    #                 f"实际结果: {actual_button_texts}"
    #             )






    def verify_call_interface(self,username):
        assert self.driver.find_element(pages.app_call_mic).is_displayed(), "麦克风按钮未显示"
        assert self.driver.find_element(pages.app_call_voice).is_displayed(), "扬声器按钮未显示"
        assert self.driver.find_element(pages.app_call_video).is_displayed(), "切换视频按钮未显示"
        call_username = self.base_find(pages.app_call_username)
        if call_username.text == username:
            print(f"拨打正确，是{username}的语音电话")
        else:
            print(f"拨打的是{call_username.text}的语音电话")
        assert self.driver.find_element(pages.app_call_add).is_displayed(), "+人按钮未显示"
        assert self.driver.find_element(pages.app_call_usercount).is_displayed(), "通话人数量未显示"
        assert self.driver.find_element(pages.app_call_small_window).is_displayed(), "缩小窗口按钮未显示"



