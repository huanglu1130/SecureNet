import os
import time
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.actions.interaction import POINTER_TOUCH
from selenium.webdriver.common.actions.mouse_button import MouseButton
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import WebDriverException
import subprocess
from selenium.webdriver.common.by import By
import pytesseract
from PIL import Image
import io
import cv2
import numpy as np
from io import BytesIO
from selenium.common.exceptions import NoSuchElementException
from datetime import datetime
pytesseract.pytesseract.tesseract_cmd = r'D:\Tesseract-OCR\tesseract.exe'

class Base:
    # 初始化方法
    def __init__(self, driver):
        self.driver = driver

    # 查找元素方法
    def base_find(self, loc, timeout=10, poll=0.5,retries=3):
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_element(*loc))


    # 点击方法
    def base_click(self, loc):
        self.base_find(loc).click()

    def swipe_down(self,start_y_ratio=0.3, end_y_ratio=0.7):
        """
        在屏幕垂直方向下滑
        :param driver: Appium WebDriver 实例
        :param start_y_ratio: 起始点Y坐标比例 (0-1)
        :param end_y_ratio: 结束点Y坐标比例 (0-1)
        """
        # 获取屏幕尺寸
        window_size = self.driver.get_window_size()
        width = window_size['width']

        # 计算坐标
        start_x = width // 2
        start_y = int(window_size['height'] * start_y_ratio)
        end_x = width // 2
        end_y = int(window_size['height'] * end_y_ratio)

        # 构造 W3C Actions
        actions = [
            {
                "type": "pointer",
                "id": "finger1",
                "actions": [
                    {"type": "pointerMove", "duration": 0, "x": start_x, "y": start_y},
                    {"type": "pointerDowm", "button": 0},
                    {"type": "pause", "duration": 1},  # 按压时间
                    {"type": "pointerMove", "duration": 1, "x": end_x, "y": end_y},  # 滑动持续时间
                    {"type": "pointerUp", "button": 0}
                ]
            }
        ]

        # 执行滑动
        self.driver.execute("actions", {"actions": actions})
        time.sleep(0.5)



    def base_select_option(self,loc,option_index=0):
        # 1. 定位下拉框容器
        try:
            wheel_view = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(loc)
            )
            # print(f"区域元素找到！位置：{wheel_view.location}, 尺寸：{wheel_view.size}")
        except Exception as e:
            print(f"未找到元素，请检查是否正确。错误：{str(e)}")

        # 2. 获取元素位置和尺寸
        location = wheel_view.location
        size = wheel_view.size

        # 3. 计算滑动坐标（从底部滑动到顶部）
        start_x = location['x'] + size['width'] // 2
        start_y = location['y'] + size['height'] * 0.8  # 起始点（底部80%位置）
        end_y = location['y'] + size['height'] * 0.2  # 结束点（顶部20%位置）

        # 4. 创建滑动动作
        actions = ActionBuilder(self.driver)
        finger = actions.add_pointer_input(POINTER_TOUCH, "finger")

        # 动作序列（按下→滑动→释放）
        finger.create_pointer_move(x=start_x, y=start_y)
        finger.create_pointer_down(button=MouseButton.LEFT)
        finger.create_pause(0.3)  # 滑动持续时间（秒）
        finger.create_pointer_move(x=start_x, y=end_y)
        finger.create_pointer_up(button=MouseButton.LEFT)
        # 5. 执行滑动
        actions.perform()

    def base_long_press(self, element, second,slide_distance=300):
        """
        长按元素后下滑取消
        :param driver: WebDriver实例
        :param element: 要长按的元素(如语音按钮)
        :param press_duration: 长按持续时间(毫秒)
        :param slide_distance: 下滑距离(像素)
        """
        # 获取元素位置和尺寸
        location = element.location
        size = element.size

        # 计算元素中心点坐标
        start_x = location['x'] + size['width'] / 2
        start_y = location['y'] + size['height'] / 2

        # 计算滑动终点坐标
        end_x = start_x
        end_y = start_y + slide_distance

        # 创建触摸指针
        touch_input = PointerInput(interaction.POINTER_TOUCH, "finger")

        # 构建动作序列
        actions = ActionChains(self.driver)
        actions.w3c_actions = ActionBuilder(self.driver, mouse=touch_input)

        # 1. 移动到元素中心
        actions.w3c_actions.pointer_action.move_to_location(start_x, start_y)
        # 2. 按下手指
        actions.w3c_actions.pointer_action.pointer_down()
        # 3. 保持按压状态(长按)
        actions.w3c_actions.pointer_action.pause(second)  # 转换为秒
        # 4. 向下滑动
        actions.w3c_actions.pointer_action.move_to_location(end_x, end_y)
        # 5. 释放手指
        actions.w3c_actions.pointer_action.pointer_up()

        # 执行动作序列
        actions.perform()

    def _capture_screenshot(self):
        """获取当前屏幕截图"""
        screenshot = self.driver.get_screenshot_as_png()
        return cv2.cvtColor(np.array(Image.open(io.BytesIO(screenshot))), cv2.COLOR_RGB2BGR)


    # 输入方法
    def base_input(self, loc, value):
        # 获取元素
        el = self.base_find(loc)
        # 清空
        el.clear()
        # el.click()
        time.sleep(1)
        # 输入
        el.send_keys(value)

    #关闭键盘
    def close_keyboard(self):
        actions = ActionBuilder(self.driver)
        actions.w3c_actions.pointer_action.move_to_location(10, 10)  # 点击屏幕空白处
        actions.w3c_actions.pointer_action.click()
        actions.perform()

    #点击空白区域
    def base_click_blank(self,x,y):
        finger = PointerInput("touch", "finger")
        actions = ActionBuilder(self.driver, mouse=finger)
        actions.pointer_action.move_to_location(x, y).click()
        actions.perform()

    # 获取文本方法
    def base_get_text(self, loc):
        return self.base_find(loc).text

    #定位消息元素最后一个
    def base_get_last_message(self,loc):
        try:
            all_messages = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located(
                    (loc)
                )
            )
            last_msg = all_messages[-1]  # 最后一条消息
        except Exception as e:
            print(f"发生错误:{str(e)}")
        return last_msg

     # 定位消息元素最后第二个
    def base_get_message(self, loc):
        try:
            all_messages = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located(
                    (loc)
                )
            )
            last_msg = all_messages[-2]  # 最后一条消息
        except Exception as e:
            print(f"发生错误:{str(e)}")
        return last_msg
    #获取页面所有的消息
    def get_all_message_texts(self,loc):
        """
        获取当前聊天窗口中的所有消息文本内容
        :return: 消息文本列表（按时间顺序，从旧到新）
        """
        # 1. 定位所有消息元素
        message_elements = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located(
                    (loc)
                )
            )  # 微信消息元素的示例ID

        # 2. 提取文本内容
        return [msg.text for msg in message_elements]

    def get_latest_messages(self, loc,num):
        message_elements = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((loc))
        )
        # 反转列表，取最新num条
        return [msg.text for msg in reversed(message_elements)][:num]

    def _is_element_present(self,loc):
        """检查元素是否存在"""
        try:
            self.driver.find_element(*loc)
            return True
        except NoSuchElementException:
            return False

    def check_elements_hierarchy(self, elements, parent=None, timeout=5):
        """
        校验父子层级结构的元素是否存在
        :param driver: WebDriver实例
        :param elements: 元素列表，格式 [
            {"parent": (by, value), "children": [(by1, value1), (by2, value2)]},
            ...
        ]
        :param parent: 最外层父元素（可选）
        :param timeout: 超时时间
        :return: bool 是否全部存在
        """
        current_parent = parent or self.driver
        try:
            for element_group in elements:
                # 1. 定位父元素
                if "parent" in element_group:
                    parent_locator = element_group["parent"]
                    current_parent = WebDriverWait(current_parent, timeout).until(
                        EC.presence_of_element_located(parent_locator))

                # 2. 校验子元素
                for child_locator in element_group.get("children", []):
                    WebDriverWait(current_parent, timeout).until(
                        EC.presence_of_element_located(child_locator))
            return True
        except NoSuchElementException:
            return False

    #定位元素最后一个
    def base_get_last(self,loc):
        try:
            all_messages = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located(
                    (loc)
                )
            )
            last_msg = all_messages[-1]  # 最后一条元素
        except Exception as e:
            print(f"发生错误:{str(e)}")
        return True


    # 获取toast
    def base_toast_capture(self,loc):
        try:
            toast = WebDriverWait(self.driver, 2).until(
                EC.presence_of_element_located((loc))
            )
            print(toast.text)
        except:
            print("未找到Toast元素")
        # toast = self.driver.find_element(loc)
        # print(toast.text)

    # 截图方法
    def base_get_img(self,loc):
        #1.定位截图元素
        file_view = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(loc))
        # 2. 获取图片元素的截图
        # screenshot = file_view.screenshot_as_png
        # image = Image.open(io.BytesIO(screenshot))
        # 3. 使用Tesseract OCR识别图片中的文字
        # custom_config = r'--oem 3 --psm 6'  # OCR引擎模式配置
        # extracted_text = pytesseract.image_to_string(image, config=custom_config, lang='chi_sim+eng')
        # return extracted_text
        max_retries = 3
        for attempt in range(max_retries):
            try:
                screenshot = file_view.screenshot_as_png
            except WebDriverException:
                if attempt == max_retries - 1:
                    raise
                self.reset_uiautomator2()  # 调用下面的重置方法
                time.sleep(2 ** attempt)
            image = Image.open(io.BytesIO(screenshot))
            # 3. 使用Tesseract OCR识别图片中的文字
            custom_config = r'--oem 3 --psm 6'  # OCR引擎模式配置
            extracted_text = pytesseract.image_to_string(image, config=custom_config, lang='chi_sim+eng')
            return extracted_text

    def reset_uiautomator2(self):
        """硬重置UiAutomator2服务"""
        import subprocess
        subprocess.run(["adb", "shell", "am", "force-stop", "io.appium.uiautomator2.server"])
        subprocess.run(["adb", "shell", "am", "force-stop", "io.appium.uiautomator2.server.test"])
        time.sleep(3)

    def base_get_imgtext(self,target_text, timeout=10,poll_interval=0.01):
        end_time = time.time() + timeout
        pytesseract_config = '--psm 6 --oem 3 -c tessedit_char_whitelist=0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        screenshot_count =0
        while time.time() < end_time:
            # img_path = DIR_PATH + os.sep + "img" + os.sep + "{}.png".format(time.strftime("%Y%m%d%H%M%S"))
            # self.driver.get_screenshot_as_file(img_path)
            screenshot_count += 1
            screenshot=self.driver.get_screenshot_as_png()
            image = Image.open(io.BytesIO(screenshot))
            # 3. OCR 识别文字
            custom_config = r'--oem 3 --psm 6'  # OCR引擎模式配置
            text = pytesseract.image_to_string(image, config=custom_config, lang='chi_sim+eng')
            # print(text)
            if target_text.lower() in text.lower():
                print(f"成功匹配 | 截图次数: {screenshot_count} | 识别文本: {text}")
                return text
            time.sleep(poll_interval)
        raise TimeoutError(f"在{timeout}秒内未找到文本: {target_text}")

    def base_get_toast(self,target_text):
        """三重验证Toast"""
        # 方法1：原生DOM检测
        try:
            if self.driver.find_element(By.XPATH, f'//*[contains(@text,"{target_text}")]'):
                return True
        except:
            pass
        # 方法2：ADB日志检测
        try:
            cmd = f'adb shell "logcat -d | grep -i \'{target_text}\'"'
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
            if target_text.lower() in result.stdout.lower():
                return True
        except:
            pass
        # 方法3：OCR兜底（针对系统级Toast）
        screenshot = self.driver.get_screenshot_as_png()
        text = pytesseract.image_to_string(Image.open(io.BytesIO(screenshot)))
        if target_text.lower() in text.lower():
            return True
        raise AssertionError(f"未检测到Toast: {target_text}")

    def assert_element_text(self, locator, expected):
        actual = self.driver.find_element(*locator).text
        assert actual.replace(" ", "") == expected.replace(" ", ""), f"文本断言失败: {actual}"

    def is_image_in_screenshot(self, target_image_path, threshold=0.8, save_failed=True):
        """
        增强版的图像匹配方法（修复版）
        :param target_image_path: 目标图片路径
        :param threshold: 匹配阈值(0-1)
        :param save_failed: 是否保存失败截图
        :return: (bool, (x, y)) 是否匹配及匹配位置
        """
        try:
            # 创建失败截图目录
            if save_failed:
                os.makedirs("failed_screenshots", exist_ok=True)
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

            # 定位最后一个消息元素
            last_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((
                    By.XPATH,
                    '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.mesh.im:id/recycler"]'
                    '/android.widget.LinearLayout[last()]'
                ))
            )

            # # 修正后的滚动操作
            # # 方案1：使用标准滚动参数（推荐）
            # self.driver.execute_script("mobile: scroll", {
            #     "strategy": "xpath",
            #     "selector": '//android.widget.LinearLayout[last()]',
            #     "direction": "down",
            #     "maxSwipes": 1
            # })
            # time.sleep(0.5)

            # 计算物理像素裁剪区域（处理高DPI屏幕）
            with BytesIO(self.driver.get_screenshot_as_png()) as f:
                screenshot_pil = Image.open(f)
                dpr = screenshot_pil.width / self.driver.get_window_size()['width']

                location = last_element.location
                size = last_element.size
                crop_area = (
                    int(location['x'] * dpr),
                    int(location['y'] * dpr),
                    int((location['x'] + size['width']) * dpr),
                    int((location['y'] + size['height']) * dpr)
                )
                cropped_img = screenshot_pil.crop(crop_area)

                # 图像预处理和匹配
                def preprocess(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    gray = cv2.GaussianBlur(gray, (3, 3), 0)
                    return cv2.adaptiveThreshold(
                        gray, 255,
                        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                        cv2.THRESH_BINARY_INV, 11, 2
                    )

                screenshot = cv2.cvtColor(np.array(cropped_img), cv2.COLOR_RGB2BGR)
                target = cv2.imread(target_image_path, cv2.IMREAD_COLOR)

                result = cv2.matchTemplate(
                    preprocess(screenshot),
                    preprocess(target),
                    cv2.TM_CCOEFF_NORMED
                )
                _, max_val, _, max_loc = cv2.minMaxLoc(result)

                # 调试处理
                if max_val >= threshold:
                    h, w = target.shape[:2]
                    debug_img = screenshot.copy()
                    cv2.rectangle(debug_img, max_loc, (max_loc[0] + w, max_loc[1] + h), (0, 255, 0), 2)
                    cv2.imwrite("debug_match.png", debug_img)
                    return True, max_loc
                else:
                    if save_failed:
                        cv2.imwrite(f"failed_screenshots/failed_{timestamp}_screenshot.png", screenshot)
                        cv2.imwrite(f"failed_screenshots/failed_{timestamp}_target.png", target)
                    return False, None

        except Exception as e:
            print(f"图像匹配失败: {str(e)}")
            if save_failed:
                self.driver.save_screenshot(f"failed_screenshots/error_{timestamp}.png")
            return False, None