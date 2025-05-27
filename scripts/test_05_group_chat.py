import allure
class TestAppGroupChat:
    @allure.story("查看好友资料")
    def test_block_friends(self,group_chat):
        group_name = "测试新建群聊"
        group_chat.page_app_create_group(group_name)