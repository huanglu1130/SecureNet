import time
import cv2
import numpy as np
import pytesseract
from PIL import Image
import io
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
import pytest
pytesseract.pytesseract.tesseract_cmd = r'D:\Tesseract-OCR\tesseract.exe'

class BaseToast:
    # 初始化方法
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)



    def _capture_screenshot(self):
        """获取当前屏幕截图"""
        screenshot = self.driver.get_screenshot_as_png()
        return cv2.cvtColor(np.array(Image.open(io.BytesIO(screenshot))), cv2.COLOR_RGB2BGR)



    # def _find_button(self):
    #     try:
    #         screenshot = self.driver.get_screenshot_as_png()
    #         image = Image.open(io.BytesIO(screenshot))
    #         img = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    #         height, width = img.shape[:2]
    #
    #         # 2. 定义ROI区域（底部50%）
    #         roi_y_start = int(height * 0.1)
    #         roi = img[roi_y_start:height, 0:width]
    #
    #         # 3. OCR增强处理
    #         gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    #         _, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)  # 自适应阈值
    #
    #         # 4. 使用Tesseract识别
    #         custom_config = r'--oem 3 --psm 6 -c tessedit_char_whitelist=0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    #         data = pytesseract.image_to_data(binary, config=custom_config, output_type=pytesseract.Output.DICT)
    #         return data
    #     except Exception as e:
    #         print(f"OCR 点击失败: {str(e)}")
    #         self.driver.save_screenshot("ocr_click_failed.png")



    def _find_verify_button_position(self,message_type,target_text):
        """
        使用OCR识别按钮位置
        :param target_text: 要查找的按钮文本(Reply/Forward/Select/Delete)
        :return: (x, y) 坐标元组
        """
        try:
            screenshot = self.driver.get_screenshot_as_png()
            image = Image.open(io.BytesIO(screenshot))
            img = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
            height, width = img.shape[:2]

            # 2. 定义ROI区域（底部50%）
            roi_y_start = int(height * 0.1)
            roi = img[roi_y_start:height, 0:width]

            # 3. OCR增强处理
            gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
            _, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)  # 自适应阈值

            # 4. 使用Tesseract识别
            custom_config = r'--oem 3 --psm 6 -c tessedit_char_whitelist=0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
            data = pytesseract.image_to_data(binary, config=custom_config, output_type=pytesseract.Output.DICT)
            self.verify_toast(data,message_type)
            # 5. 精准坐标计算
            for i, text in enumerate(data['text']):
                if text.strip() and target_text.lower() in text.lower():
                    # 计算ROI内相对坐标
                    rel_x = data['left'][i] + data['width'][i] // 2
                    rel_y = data['top'][i] + data['height'][i] // 2

                    # 转换为屏幕绝对坐标
                    abs_x = rel_x
                    abs_y = roi_y_start + rel_y
                    return self.click_by_coordinates(abs_x, abs_y)
            self.driver.save_screenshot("ocr_click_failed.png")
            raise Exception(f"未找到文本: {target_text}")
        except Exception as e:
            print(f"OCR 点击失败: {str(e)}")
            self.driver.save_screenshot("ocr_click_failed.png")

    def verify_toast(self,data,message_type):
        # 从返回数据中提取按钮文本
        actual_button_texts = data.get('text', [])
        actual_button_texts = [text.strip() for text in actual_button_texts if text.strip()]
        # 预期结果配置
        expected_config = {
            "Text": {
                "expected": ["Reply", "Forward", "Copy", "Edit", "Select", "Recall", "Delete"],
                "unexpected": []
            },
            "File": {
                "expected": ["Reply", "Forward", "Select", "Recall", "Delete"],
                "unexpected": ["Copy", "Edit"]
            },
            "Image": {
                "expected": ["Reply", "Forward", "Select", "Recall", "Delete"],
                "unexpected": ["Copy", "Edit"]
            },
            "Video": {
                "expected": ["Reply", "Forward", "Select", "Recall", "Delete"],
                "unexpected": ["Copy", "Edit"]
            },
            "Card": {
                "expected": ["Reply", "Forward", "Select", "Recall", "Delete"],
                "unexpected": ["Copy", "Edit"]
            },
            "Voice": {
                "expected": ["Reply", "Select", "Recall", "Delete"],
                "unexpected": ["Copy", "Forward", "Edit"]
            }

        }

        # 验证按钮
        config = expected_config[message_type]
        missing_buttons = [btn for btn in config["expected"] if btn not in actual_button_texts]
        unexpected_buttons = [btn for btn in config["unexpected"] if btn in actual_button_texts]

        # 记录结果
        if not missing_buttons and not unexpected_buttons:
            allure.attach(
                f"长按{message_type}消息按钮展示正确",
                f"实际按钮: {actual_button_texts}"
            )
        else:
            pytest.fail(
                f"{message_type}消息按钮不正确\n"
                f"缺少的按钮: {missing_buttons}\n"
                f"不应出现但出现的按钮: {unexpected_buttons}\n"
                f"预期包含: {config['expected']}\n"
                f"预期不包含: {config['unexpected']}\n"
                f"实际结果: {actual_button_texts}"
            )


    def _find_button_position(self,target_text):
        """
        使用OCR识别按钮位置
        :param target_text: 要查找的按钮文本(Reply/Forward/Select/Delete)
        :return: (x, y) 坐标元组
        """
        try:
            screenshot = self.driver.get_screenshot_as_png()
            image = Image.open(io.BytesIO(screenshot))
            img = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
            height, width = img.shape[:2]

            # 2. 定义ROI区域（底部50%）
            roi_y_start = int(height * 0.1)
            roi = img[roi_y_start:height, 0:width]

            # 3. OCR增强处理
            gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
            _, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)  # 自适应阈值

            # 4. 使用Tesseract识别
            custom_config = r'--oem 3 --psm 6 -c tessedit_char_whitelist=0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
            data = pytesseract.image_to_data(binary, config=custom_config, output_type=pytesseract.Output.DICT)
            # print(f"返回所有的按钮为{data['text']}")
            # 5. 精准坐标计算
            for i, text in enumerate(data['text']):
                # if text.strip() and target_text.lower() in text.lower():
                if text.strip() and target_text == text:
                    # 计算ROI内相对坐标
                    rel_x = data['left'][i] + data['width'][i] // 2
                    rel_y = data['top'][i] + data['height'][i] // 2

                    # 转换为屏幕绝对坐标
                    abs_x = rel_x
                    abs_y = roi_y_start + rel_y
                    return self.click_by_coordinates(abs_x, abs_y)
            self.driver.save_screenshot("ocr_click_failed.png")
            raise Exception(f"未找到文本: {target_text}")
        except Exception as e:
            print(f"OCR 点击失败: {str(e)}")
            self.driver.save_screenshot("ocr_click_failed.png")

    def click_by_coordinates(self, x, y):
        """使用 W3C Actions 实现坐标点击"""
        try:
            #创建动作序列
            actions = [
                {"type": "pointer", "id": "finger1", "parameters": {"pointerType": "touch"},"actions": [
                    {"type": "pointerMove", "duration": 100, "x": x, "y": y},
                    {"type": "pointerDown", "button": 0},
                    {"type": "pause", "duration": 300},
                    {"type": "pointerUp", "button": 0}
                ]}
            ]
            # 执行动作
            self.driver.execute("actions", {"actions": actions})
            time.sleep(0.5)
            return True

        except Exception as e:
            print(f"坐标点击失败: {str(e)}")
            self.driver.save_screenshot("click_coordinates_failed.png")
            return False

    def long_press_message(self,message):
        """长按消息打开操作菜单"""
        self.driver.execute_script('mobile: longClickGesture', {
            'elementId': message.id,
            'duration': 2000  # 长按2秒
        })
        time.sleep(1)  # 等待菜单弹出

    def click_toast_first_button(self,element,message_type,button_text):
        """
        点击Toast菜单中的按钮
        :param element:
        :param button_text: 按钮文本(Reply/Forward/Select/Delete)
        """
        # 1.长按消息打开菜单
        self.long_press_message(element)
        # # 2. 点击按钮
        self._find_verify_button_position(message_type,button_text)
        time.sleep(1)  # 等待操作完成

        print(f"已点击按钮: {button_text}")


    def click_toast_button(self,element,button_text):
        """
        点击Toast菜单中的按钮
        :param element:
        :param button_text: 按钮文本(Reply/Forward/Select/Delete)
        """
        # 1.长按消息打开菜单
        self.long_press_message(element)
        # # 2. 点击按钮
        self._find_button_position(button_text)
        time.sleep(1)  # 等待操作完成

        print(f"已点击按钮: {button_text}")


