from selenium.webdriver.common.by import By
from appium.webdriver.common.appiumby import AppiumBy
"""
    一、以下为app登录模块配置信息    
"""
#登录方法
app_loginmethod = By.ID,"com.mesh.im:id/item_arrow"
#下拉框选择器
app_login_option = By.ID,"com.mesh.im:id/wheel_picker_option_wheel"
#登录方法确认
app_login_method_confirm = By.ID,"com.mesh.im:id/tv_ui_confirm"
#登录方法取消
app_login_method_cancel = By.ID,'com.mesh.im:id/tv_ui_cancel'
#登录用户名
app_username = By.ID,"com.mesh.im:id/et_account"
#登录密码
app_password = AppiumBy.ID,"com.mesh.im:id/et_password"
#展示登录密码
app_show_password = By.ID,"com.mesh.im:id/text_input_end_icon"
#协议
app_accept = By.ID,"com.mesh.im:id/cb_check"
#登录按钮
app_login = By.ID,"com.mesh.im:id/bt_login"
#账号密码错误弹窗
app_login_error_tip = AppiumBy.XPATH, '//*[contains(@text, "incorrect")]'


"""
    一、以下为app登录之后sync confirmation页面    
"""
app_sync_sync = By.ID,"com.mesh.im:id/btn_sync"
app_sync_cancel = By.ID,"com.mesh.im:id/btn_cancel"

"""
    一、以下为app登录之后chats页面    
"""
#聊天列表搜索框
app_user_search = By.ID,"com.mesh.im:id/iv_so_img"
#聊天列表搜索输入框
app_user_search_input = By.ID,"com.mesh.im:id/et_so_content"
#聊天列表搜索好友结果第一个
app_user_search_list = By.ID,"com.mesh.im:id/tv_nickname"
#聊天列表指定给联系人test发送消息
contact_user = AppiumBy.ANDROID_UIAUTOMATOR,f'new UiSelector().text("test")'
#聊天框标题
contact_title = By.ID,'com.mesh.im:id/title'
#聊天列表指定给群1111111发送消息
contact_group = AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("1111111")'
#聊天列表第一个好友
app_user = By.ID,"com.mesh.im:id/lastMsg"
#聊天输入框
app_message_input = By.ID,"com.mesh.im:id/chatInput"
#聊天对话框空白区域
app_message_black = By.XPATH,'//androidx.recyclerview.widget.RecyclerView[@resource-id="com.mesh.im:id/recycler"]/android.widget.LinearLayout[3]/android.view.ViewGroup/android.widget.LinearLayout'
#聊天输入框发送消息send
app_message_send = By.ID,"com.mesh.im:id/chatSend"
#聊天点击表情包
app_message_emoji  =By.ID,"com.mesh.im:id/emoji_keyboard"
#选择第一个表情包
app_message_emoji_1 = By.XPATH,'//android.widget.GridView[@resource-id="com.mesh.im:id/emoji_recycler"]/android.widget.LinearLayout[1]'
#聊天点击+号
app_message_more = By.ID,"com.mesh.im:id/chatMore"
#聊天点击语音电话
app_voice_call = By.ID,"com.mesh.im:id/btn_call_voice"
#聊天点击视频电话
app_video_call = By.ID,"com.mesh.im:id/ btn_call_video"
#发送成功的标志
app_message_success = By.XPATH,'//android.widget.ImageView[@resource-id="com.mesh.im:id/iv_state"]'
#聊天记录文本消息
app_message_all = By.XPATH, '//android.widget.TextView[@resource-id="com.mesh.im:id/content"]'
#聊天记录表情包
app_emoji = By.XPATH,'//android.widget.TextView[@resource-id="com.mesh.im:id/content" and @text="[emoji_grin]"]'
#文本转语音
app_message_voice_keyboard = By.ID,"com.mesh.im:id/voice_keyboard"
#说话按钮
app_message_voice_say = By.ID,'com.mesh.im:id/touchSay'
#语音消息
app_message_voice = By.XPATH,'//android.widget.TextView[@resource-id="com.mesh.im:id/duration"]'
#语音消息播放
app_message_voice_view = By.XPATH,'//android.widget.LinearLayout[@resource-id="com.mesh.im:id/content"]'
#+号
app_more = By.ID,"com.mesh.im:id/chatMore"

#选择相册
app_album = By.XPATH,'//android.widget.TextView[@resource-id="com.mesh.im:id/menu" and @text="Album"]'
#选择截图相册下拉
app_album_choice = By.XPATH,'//android.widget.ImageView[@resource-id="com.mesh.im:id/ps_iv_arrow"]'
#选择相册
app_album_folder  = By.XPATH,'//androidx.recyclerview.widget.RecyclerView[@resource-id="com.mesh.im:id/folder_list"]/android.widget.RelativeLayout[2]'
#相册第一张文件
app_album_first = By.XPATH,'(//android.widget.TextView[@resource-id="com.mesh.im:id/tvCheck"])[1]'
#相册点击确认选择
app_album_complete = By.ID,"com.mesh.im:id/ps_tv_complete"
#聊天框所有图片
app_message_image = By.XPATH,'//android.widget.ImageView[@resource-id="com.mesh.im:id/content"]'
#点击查看图片
app_message_image_view = By.XPATH,'//android.widget.RelativeLayout[@resource-id="com.mesh.im:id/add"]/android.widget.ImageView'
#图片下载
app_message_image_down = By.XPATH,'//android.widget.ImageView[@resource-id="com.mesh.im:id/btn_down"]'
#查看图片返回
app_message_image_back = By.XPATH,'//android.widget.ImageView[@resource-id="com.mesh.im:id/btn_back"]'


#点击+号选择camera
app_camera = By.XPATH,'//android.widget.TextView[@resource-id="com.mesh.im:id/menu" and @text="Camera"]'
#长按摄像
app_camera_view = By.XPATH,'//android.widget.FrameLayout[@resource-id="com.mesh.im:id/capture_layout"]/android.view.View'
#摄影取消
app_camera_view_cancel = By.XPATH,'//android.widget.FrameLayout[@resource-id="com.mesh.im:id/capture_layout"]/android.view.View[1]'
#摄影确认发送
app_camera_view_send = By.XPATH,'//android.widget.FrameLayout[@resource-id="com.mesh.im:id/capture_layout"]/android.view.View[2]'
#点击播放视频
app_camera_view_play = By.XPATH,'//android.widget.ImageView[@resource-id="com.mesh.im:id/video_play"]'
#视频下载
app_camera_view_down = By.XPATH,'//android.widget.ImageView[@resource-id="com.mesh.im:id/btn_down"]'
#播放视频后返回
app_camera_view_play_back = By.XPATH,'//android.widget.ImageView[@resource-id="com.mesh.im:id/btn_back"]'


#点击+号选择发送文件
app_file = By.XPATH,'//android.widget.TextView[@resource-id="com.mesh.im:id/menu" and @text="File"]'
#文件根目录
app_file_ImageButton = By.XPATH,'//android.widget.ImageButton[@content-desc="显示根目录"]'
#文件目录文档
app_file_doc = By.XPATH ,'//android.widget.TextView[@resource-id="android:id/title" and @text="文档"]'
#文档文件夹
app_file_MeshDownload = By.XPATH,'//android.widget.TextView[@resource-id="android:id/title"]'
#选择发送doc文档
app_file_send = By.ID,'com.google.android.documentsui:id/metadata'
#选择发送文件
app_file_first = By.XPATH,'(//android.widget.LinearLayout[@resource-id="com.google.android.documentsui:id/line2"])[1]'
#查看发送的文件title
app_file_send_doc = By.XPATH,'//android.widget.TextView[@resource-id="com.mesh.im:id/title" and @text="Voip 翻译 加密聊天需求整理_034040.docx"]'
#文件的receive File按钮
app_file_receive = By.XPATH,'//android.widget.Button[@resource-id="com.mesh.im:id/bt_receive"]'
#文件的open file按钮
app_file_open = By.ID,'com.mesh.im:id/bt_open'
#查看文件内容
app_file_open_text = By.XPATH,'//android.webkit.WebView[@text="Preview"]'
#缓存文件内容
app_file_open_2_text = By.XPATH,'	(//android.widget.Image[@text="loading"])[1]'
#查看文件点击返回
app_file_view_back = By.XPATH,'//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.widget.TextView[1]'
app_file_open_back = By.XPATH,'//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.TextView[1]'


#点击+号选择发送名片
app_card = By.XPATH,'//android.widget.TextView[@resource-id="com.mesh.im:id/menu" and @text="Contact Card"]'
#名片页title
app_card_title = By.XPATH,'//android.widget.TextView[@text="Select friends"]'
#选择名片列表
app_card_list = By.ID,'com.mesh.im:id/bt_receive'
#选择Anna的名片
app_card_anna = By.XPATH,'//android.widget.TextView[@resource-id="com.mesh.im:id/nickName" and @text="Anna"]'
#选择名片列表页搜索框
app_card_search = By.XPATH,'//android.widget.EditText[@resource-id="com.mesh.im:id/tv_search"]'
#名片页清除输入框按钮
app_card_input_clear = By.XPATH,'//android.widget.ImageView[@resource-id="com.mesh.im:id/btn_clear"]'
#Anna的搜索结果
app_card_search_result = By.XPATH,'//android.widget.TextView[@resource-id="com.mesh.im:id/nickName"]'
#名片页返回按钮
app_card_back = By.XPATH,'//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.TextView[1]'
#发送名片确认
app_card_confirm = By.ID,'com.mesh.im:id/tv_ui_confirm'
#发送名片取消
app_card_cancel = By.ID,'com.mesh.im:id/tv_ui_cancel'
#聊天记录的名片名称
app_send_card_title = By.XPATH,'//android.widget.TextView[@resource-id="com.mesh.im:id/contact_name"]'
#聊天名片的查看详情
app_send_card_detail = By.XPATH,'//android.widget.TextView[@resource-id="com.mesh.im:id/btn_view_details"]'
#聊天名片查看详情返回
app_send_card_detail_back = By.XPATH,'//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.widget.TextView[1]'
#聊天页面返回到列表
app_message_back = By.XPATH,'//android.widget.ImageView[@resource-id="com.mesh.im:id/iv_back"]'

#语音通话麦克风按钮
app_call_mic = By.ID,'com.mesh.im:id/cb_mic'
#语音通话扬声器按钮
app_call_voice = By.ID,'com.mesh.im:id/cb_voice'
#语音通话挂断电话按钮
app_call_hangup = By.ID,'com.mesh.im:id/iv_hangup2'
#语音通话打开视频按钮
app_call_video = By.ID,'com.mesh.im:id/cb_video'
#语音通话对象名称
app_call_username = By.ID,'com.mesh.im:id/tv_user_name'
#语音通话+人按钮
app_call_add = By.ID,'com.mesh.im:id/iv_add'
#语音通话人数
app_call_usercount = By.ID,'com.mesh.im:id/tv_user_count'
#语音通话缩小窗口按钮
app_call_small_window = By.ID,'com.mesh.im:id/iv_small_window'
#语音通话发起人名称
app_call_user = By.ID,'com.mesh.im:id/tv_user'


#点击我的头像
app_avatar = By.XPATH,'//android.widget.ImageView[@resource-id="com.mesh.im:id/avatar"]'
##关闭头像页面
app_avatar_back = By.XPATH,'//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.TextView[3]'
app_login_out = By.XPATH,'//android.widget.TextView[@text="Log Out"]'
#点击确认登出
app_loginout_confirm = By.ID,'com.mesh.im:id/tv_ui_confirm'
#点击取消登出
app_loginout_cancel = By.ID,'com.mesh.im:id/tv_ui_cancel'


#名片详情页面
#名片name
app_card_showname = By.ID,'com.mesh.im:id/showName'
#名片ID
app_card_ID = By.ID,'com.mesh.im:id/userId'
#名片头像
app_card_avatar = By.ID,'com.mesh.im:id/avatar'
#名片部门
app_card_department = By.XPATH,'//android.widget.TextView[@resource-id="com.mesh.im:id/item_title" and @text="Department"]'
#名片岗位
app_card_position = By.XPATH,'//android.widget.TextView[@resource-id="com.mesh.im:id/item_title" and @text="Position"]'
#名片邮箱
app_card_email = By.XPATH,'//android.widget.TextView[@resource-id="com.mesh.im:id/item_title" and @text="E-mail"]'
#名片邮箱地址
# app_card_email_text = By.Xpath,f'//android.widget.TextView[@text="{email}"]'
#名片电话
app_card_phone = By.XPATH,'//android.widget.TextView[@resource-id="com.mesh.im:id/item_title" and @text="Phone Number"]'
#名片修改备注入口
app_card_edit_contact = By.XPATH,'//android.widget.TextView[@resource-id="com.mesh.im:id/item_title" and @text="Edit Contact"]'
#点击去修改备注
app_card_edit_click = By.XPATH,'(//android.widget.ImageView[@resource-id="com.mesh.im:id/item_arrow"])[1]'
#修改备注页标题
app_card_edit_title = By.XPATH,'//android.widget.TextView[@text="Edit Contact"]'
#修改备注页名称
app_card_edit_name = By.ID,'com.mesh.im:id/tv_name'
#修改备注页ID
app_card_edit_ID = By.ID,'com.mesh.im:id/tv_chatid'
#修改备注页头像
app_card_edit_avatar = By.ID,'com.mesh.im:id/avatar'
#展示Remark
app_card_remark = By.ID,'com.mesh.im:id/tv_remark'
#点击输入备注
app_card_edit_remark = By.ID,'com.mesh.im:id/et_remark'
#修改备注页保存
app_card_edit_save = By.ID,'com.mesh.im:id/bt_save'
#名片分享入口
app_card_share = By.XPATH,'//android.widget.TextView[@resource-id="com.mesh.im:id/item_title" and @text="Share Contact"]'
#点击去分享
app_card_share_click = By.XPATH,'(//android.widget.ImageView[@resource-id="com.mesh.im:id/item_arrow"])[2]'
#隐私
app_card_privacy = By.XPATH,'//android.widget.TextView[@resource-id="com.mesh.im:id/item_title" and @text="Privacy"]'
app_card_privacy_click = By.XPATH,'(//android.widget.ImageView[@resource-id="com.mesh.im:id/item_arrow"])[3]'
#朋友圈入口
app_card_moment = By.XPATH,'//android.widget.TextView[@resource-id="com.mesh.im:id/item_friend_circle_text"]'
app_card_moment_click = By.XPATH,'//android.widget.ImageView[@resource-id="com.mesh.im:id/item_friend_circle_arrow"]'
#去发消息
app_card_send_message = By.XPATH,'//android.widget.TextView[@text="Send Message"]'
#去发语音或视频
app_card_call = By.XPATH,'//android.widget.TextView[@text="Voice or Video Call"]'
#右上角三个。
app_card_more = By.XPATH,'//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.widget.TextView[3]'


#toast引用消息输入框
app_toast_reply = By.ID,'com.mesh.im:id/chatInput'
#引用消息清除
app_toast_reply_clear = By.ID,'com.mesh.im:id/btn_clear'
#消息引用框
app_toast_reply_message = By.XPATH,'//android.view.ViewGroup[@resource-id="com.mesh.im:id/quote_layout"]'
#消息引用回复消息内容
app_toast_reply_content = By.XPATH,'//android.widget.TextView[@resource-id="com.mesh.im:id/content" and @text="回复消息"]'
#消息引用发送emoji内容
app_reply_emoji = By.XPATH,'//android.widget.TextView[@resource-id="com.mesh.im:id/tv_quote" and @text="[emoji_grin]"]'
#消息引用发送文本内容
app_reply_text = By.XPATH,'//android.widget.TextView[@resource-id="com.mesh.im:id/tv_quote"]'
#消息引用发送语音内容
app_reply_voice = By.ID,'com.mesh.im:id/tv_quote'
#消息引用发送图片+视频+文件+名片内容
app_reply_photo = By.XPATH,'//android.widget.TextView[@resource-id="com.mesh.im:id/tv_file_type"]'
#引用文本范围
app_quote_reply = By.ID,'com.mesh.im:id/tv_quote'


#转发消息
#转发消息选择好友页
#标题
app_forward_select = By.XPATH,'//android.widget.TextView[@text="Select a Chat"]'
#转发多选单选切换
app_forward_multiple = By.XPATH,'//android.widget.TextView[@resource-id="com.mesh.im:id/btn_multiple"]'
#转发给指定人admin
app_forward_user = By.XPATH,'//android.widget.TextView[@resource-id="com.mesh.im:id/name" and @text="test2"]'
#复选框选择第一个好友
app_forward_user_1 = By.XPATH,'//android.widget.TextView[@resource-id="com.mesh.im:id/name" and @text="Anna"]'
app_forward_user_2 = By.XPATH,'//android.widget.TextView[@resource-id="com.mesh.im:id/name" and @text="test2"]'
#多选确认
app_forward_multiple_send = By.XPATH,'//android.widget.Button[@resource-id="com.mesh.im:id/btn_send"]'
#搜索框
app_forward_search = By.XPATH,'//android.widget.TextView[@resource-id="com.mesh.im:id/et_so_content"]'
#搜索输入框
app_forward_input = By.XPATH,'//android.widget.EditText[@resource-id="com.mesh.im:id/et_so_content"]'
#清空输入
app_forward_input_cancel = By.XPATH,'//android.widget.TextView[@resource-id="com.mesh.im:id/tv_cancel"]'
#选择搜索结果
app_forward_search_result = By.XPATH,'//android.widget.TextView[@resource-id="com.mesh.im:id/tv_name"]'
#取消搜索，cancel
app_forward_search_cancel = By.XPATH,'//android.widget.TextView[@resource-id="com.mesh.im:id/tv_cancel"]'
#转发确认
app_forward_confirm = By.ID,'com.mesh.im:id/tv_ui_confirm'
#转发取消
app_forward_cancel = By.ID,'com.mesh.im:id/tv_ui_cancel'
#取消后返回
app_forward_cancel_back = By.XPATH,'//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.TextView[1]'
#转发的文本内容
app_forward_text_content = By.XPATH,'//android.widget.TextView[@resource-id="com.mesh.im:id/card"]'
#转发的好友名字
app_forward_chat_name = By.XPATH,'//android.widget.TextView[@resource-id="com.mesh.im:id/nick_name"]'
#转发的标题
app_forward_title = By.XPATH,'//android.widget.TextView[@resource-id="com.mesh.im:id/title"]'
#转发完成之后列表
app_forward_msg = By.XPATH,'//androidx.recyclerview.widget.RecyclerView[@resource-id="com.mesh.im:id/recycler"]'
app_forward_time = By.XPATH,'(//android.widget.TextView[@resource-id="com.mesh.im:id/time"])[1]'


###选择消息
#选择框
app_select = By.XPATH,'//android.widget.CheckBox[@resource-id="com.mesh.im:id/check"]'
#选择后点击转发
app_select_forward = By.XPATH,'//android.widget.ImageView[@resource-id="com.mesh.im:id/btn_forward"]'
#选择后点击删除
app_select_delete = By.XPATH,'//android.widget.ImageView[@resource-id="com.mesh.im:id/btn_delete"]'
#删除二次确认取消
app_select_delete_cancel = By.XPATH,'//android.widget.TextView[@resource-id="com.mesh.im:id/tv_ui_cancel"]'
#删除二次确认确认
app_select_delete_confirm = By.XPATH,'//android.widget.TextView[@resource-id="com.mesh.im:id/tv_ui_confirm"]'

#单聊框的时间
app_message_time = By.XPATH,'//android.widget.TextView[@resource-id="com.mesh.im:id/time"]'

##删除消息
#删除二次确认
app_delete_confirm = By.XPATH,'//android.widget.TextView[@resource-id="com.mesh.im:id/tv_ui_confirm"]'
#删除二次确认取消
app_delete_cancel = By.XPATH,'//android.widget.TextView[@resource-id="com.mesh.im:id/tv_ui_cancel"]'
#删除二次确认提示
app_delete_notice = By.XPATH,'//android.widget.TextView[@resource-id="com.mesh.im:id/tv_message_message"]'


##撤回提示
app_recall_notice = By.XPATH,'//android.widget.TextView[@resource-id="com.mesh.im:id/notice"]'

##编辑消息
#编辑的消息内容
app_edit_message_content = By.XPATH,'//android.widget.TextView[@resource-id="com.mesh.im:id/tv_content"]'
#编辑区域
app_edit_message_input = By.XPATH,'//android.widget.EditText[@resource-id="com.mesh.im:id/chatInput"]'
#点击完成发送
app_edit_done = By.XPATH,'//android.widget.Button[@resource-id="com.mesh.im:id/chatSend"]'
#编辑标志,text是Edited
app_edit = By.XPATH,'//android.widget.TextView[@resource-id="com.mesh.im:id/tv_edit"]'




###添加好友
#聊天列表的+号(入口1）
app_add_menu = By.XPATH,'//android.widget.ImageView[@resource-id="com.mesh.im:id/btn_add_menu"]'
app_add_create_group = By.XPATH,'//android.widget.TextView[@text="Create Group"]'
app_add_friends = By.XPATH,'//android.widget.TextView[@text="Add Friends"]'
app_add_scan = By.XPATH,'//android.widget.TextView[@text="Scan"]'
#点击添加好友首页标题Add Friends
app_add_friends_home_page = By.XPATH,'//android.widget.TextView[@text="Add Friends"]'
app_add_friends_home_item_scan = By.XPATH,'//android.widget.FrameLayout[@resource-id="com.mesh.im:id/item_scan"]'
app_add_friends_home_item_icon = By.XPATH,'//android.widget.ImageView[@resource-id="com.mesh.im:id/item_icon"]'
app_add_friends_home_item_title = By.XPATH,'//android.widget.TextView[@resource-id="com.mesh.im:id/item_title"]'
app_add_friends_home_item_summary = By.XPATH,'//android.widget.TextView[@resource-id="com.mesh.im:id/item_summary"]'
app_add_friends_home_item_mobile_contact = By.XPATH,'//android.widget.FrameLayout[@resource-id="com.mesh.im:id/item_mobile_contact"]'

###聊天列表的搜索框（入口2）
app_chat_list_search = By.XPATH,'//android.widget.TextView[@resource-id="com.mesh.im:id/et_so_content"]'
#搜索输入框
app_chat_list_search_input = By.XPATH,'//android.widget.EditText[@resource-id="com.mesh.im:id/et_so_content"]'
#非好友聊天页面的add按钮
app_chat_add = By.XPATH,'//android.widget.TextView[@resource-id="com.mesh.im:id/tv_add"]'
##取消搜索
app_chat_search_cancel = By.XPATH,'//android.widget.TextView[@resource-id="com.mesh.im:id/tv_cancel"]'


#加好友点击搜索
app_add_friends_search = By.XPATH,'//android.widget.TextView[@resource-id="com.mesh.im:id/tv_search"]'
#加好友搜索输入框
app_add_friends_search_input = By.XPATH,'//android.widget.EditText[@resource-id="com.mesh.im:id/editText"]'
#加好友搜索结果
app_add_friends_search_result = By.XPATH,'//android.widget.TextView[@resource-id="com.mesh.im:id/tv_keyword"]'
#点击搜索结果号码16611111114
app_add_friends_result_phone = By.XPATH,'//android.widget.TextView[@resource-id="com.mesh.im:id/tv_nickname"]'
#点击搜索结果名称test4
app_add_friends_result_name = By.XPATH,'//android.widget.TextView[@resource-id="com.mesh.im:id/tv_name"]'
#点击搜索结果标题Phone Number:
app_add_friends_result_title = By.XPATH,'//android.widget.TextView[@resource-id="com.mesh.im:id/tv_title"]'
# 点击加好友页面
app_add_friends_page = By.XPATH,'//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.LinearLayout'
#点击加好友
app_send_add_friends = By.XPATH,'//android.widget.TextView[@text="Add Friends"]'
#点击发起聊天
app_add_send_message = By.XPATH,'//android.widget.TextView[@text="Send Message"]'
#发送好友请求页面的标题New Friends Apply
app_add_friends_title = By.XPATH,'//android.widget.TextView[@text="New Friends Apply"]'
#发送好友请求的文本内容
app_add_friends_content = By.XPATH,'//android.widget.EditText[@resource-id="com.mesh.im:id/et_content"]'
#发送好友请求页面的备注
app_add_friends_remark = By.XPATH,'//android.widget.EditText[@resource-id="com.mesh.im:id/et_alise"]'
#点击发送好友请求
app_add_friends_send = By.XPATH,'//android.widget.Button[@resource-id="com.mesh.im:id/bt_send"]'
#发送好友请求之后点击返回
app_add_friends_card_back = By.XPATH,'//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.widget.TextView[1]'
#点击返回之后取消搜索
app_add_friends_search_cancel = By.XPATH,'//android.widget.TextView[@resource-id="com.mesh.im:id/cancel"]'
#添加好友搜索页面点击返回
app_add_friends_back = By.XPATH,'//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.widget.TextView[1]'


###新好友验证页面
#contacts页面
app_contacts = By.ID,'com.mesh.im:id/tv_tab_contacts'
#new friends的入口
app_contacts_new_friends = By.XPATH,'//android.widget.TextView[@resource-id="com.mesh.im:id/item_title" and @text="New Friends"]'
#新好友页面标题
app_contacts_new_friends_title = By.XPATH,'//android.widget.TextView[@text="New Friends"]'
#返回按钮
app_contacts_new_friends_back = By.XPATH,'//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.TextView[1]'
#聊天列表chats
app_chats = By.ID,'com.mesh.im:id/tv_tab_chat'
#好友昵称
app_new_friends_name = By.XPATH,'//android.widget.TextView[@resource-id="com.mesh.im:id/nickname"]'
#请求内容
app_new_friends_remark = By.ID,'com.mesh.im:id/remark'
#验证状态Waiting for verification
app_new_friends_handle = By.XPATH,'//android.widget.TextView[@resource-id="com.mesh.im:id/handle"]'


##处理好友请求
#点击去处理
app_friends_request_action = By.ID,'com.mesh.im:id/action'
#同意好友申请
app_friends_accept = By.ID,'com.mesh.im:id/bt_accept'
#拒绝好友申请
app_friends_reject = By.ID,'com.mesh.im:id/bt_refuse'
#好友申请内容
app_friends_content = By.XPATH,'//android.widget.TextView[@resource-id="com.mesh.im:id/hil"]'
#好友申请标题
app_friends_request_title = By.XPATH,'//android.widget.TextView[@text="New Friends Request"]'
#好友处理返回
app_requests_action_back = By.XPATH,'//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.TextView[1]'
#好友处理长按删除
app_request_delete = By.ID,'com.mesh.im:id/_ll_temp'

##好友资料三个...
app_friends_info_more = By.XPATH,'//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.widget.TextView[3]'
app_friends_delete = By.ID,'com.mesh.im:id/bt_delete'
#删好友二次提醒
app_friends_confirm = By.ID,'com.mesh.im:id/tv_ui_confirm'
app_friends_cancel = By.ID,'com.mesh.im:id/tv_ui_cancel'
#删好友二次提醒文案Delete contact "测试添加好友" and the chathistory with that contact.
app_friends_delete_note = By.ID,'com.mesh.im:id/tv_message_message'
#拉黑名单
app_friends_block = By.XPATH,'//android.widget.CheckBox'
#拉黑好友二次提醒
app_friends_block_cancel = By.ID,'com.mesh.im:id/tv_ui_cancel'
app_friends_block_confirm = By.ID,'com.mesh.im:id/tv_ui_confirm'
#拉黑好友提醒文案 When you block this user, you will not receive any messages from them and you will not see each other's Moments updates. Block this user now?
#拉黑后文案展示 This user has been blocked, You will not receive any message from them
app_friends_blocked_notice = By.XPATH,'//android.widget.TextView[@resource-id="com.mesh.im:id/tv_blocked"]'
#主页的拉黑列表
app_block_list = By.XPATH,'//android.widget.FrameLayout[@resource-id="com.mesh.im:id/item_blocked_list"]/android.widget.LinearLayout'
#拉黑列表好友名称 test6
app_clock_list_title = By.ID,'com.mesh.im:id/item_title'
