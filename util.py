import os, json
from pathlib import Path
from appium.options.android import UiAutomator2Options
from pytesseract.pytesseract import cleanup
from appium import webdriver
import appium.webdriver
import logging.handlers
from config import DIR_PATH
import time
from selenium.common.exceptions import WebDriverException
import subprocess

class GetDriver:
    @classmethod
    # 获取App Driver
    def get_app_driver(cls):
        desired_caps = {
              'platformName': 'Android', # 平台名称
              'platformVersion': '12',  # 系统版本号
              'deviceName': 'itel_S662LCN',  # 设备名称
              'appPackage': 'com.mesh.im',  # apk的包名
              'appActivity': '.ui.SplashActivity',
               'automationName': 'UiAutomator2',
               'appium:noReset': True,
              'enableToastNotificationListener':True,
               'autoGrantPermissions': True,
              'uiautomator2ServerLaunchTimeout':9000,
              'uiautomator2ServerInstallTimeout': 60000,
              'appium:newCommandTimeout': 120

         }
        options = UiAutomator2Options().load_capabilities(desired_caps)
        try:
            driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', options=options)
            print("APP启动成功！")
            time.sleep(5)
            return driver
        except Exception as e:
            print(f"APP启动失败。错误：{str(e)}")



# 读取json工具
def read_json(file_name):
    """安全读取JSON文件（自动处理路径）"""
    # 获取项目根目录（假设此文件在project/utils/下）
    project_root = Path(__file__).resolve()
    # 构建完整路径（JSON文件放在project/data/）
    json_path = project_root / "data" / file_name

    if not json_path.exists():
        raise FileNotFoundError(f"JSON文件不存在: {json_path}")

    with open(json_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def write_json(value):
    file_path = DIR_PATH + os.sep + "data" + os.sep + "expect.json"
    with open(file_path, "w", encoding="utf-8")as f:
        data = {"expect": [{"desc": "app订单编号", "order_no": value}]}
        json.dump(data, f)



# 日志封装
class GetLog:
    __log = None

    @classmethod
    def get_log(cls):
        if cls.__log is None:
            # 获取日志器
            cls.__log = logging.getLogger()
            # 设置入口级别
            cls.__log.setLevel(logging.INFO)
            # 获取处理器
            filename = DIR_PATH + os.sep + "log" + os.sep + "tpshop_auto.log"
            tf = logging.handlers.TimedRotatingFileHandler(filename=filename,
                                                           when="midnight",
                                                           interval=1,
                                                           backupCount=3,
                                                           encoding="utf-8")
            # 获取格式器
            fmt = "%(asctime)s %(levelname)s [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s"
            fm = logging.Formatter(fmt)
            # 将格式器添加到处理器
            tf.setFormatter(fm)
            # 将处理器添加到日志器
            cls.__log.addHandler(tf)
        # 返回日志器
        return cls.__log
