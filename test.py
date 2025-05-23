from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import time
from appium.options.android import UiAutomator2Options

# appium服务监听地址
server = 'http://127.0.0.1:4723/wd/hub'

def start_app():
    # app启动参数
    desired_caps = {
              'platformName': 'Android', # 平台名称
              'platformVersion': '12',  # 系统版本号
              'deviceName': 'itel_S662LCN',  # 设备名称
              'appPackage': 'com.mesh.im',  # apk的包名
              'appActivity': '.ui.SplashActivity',
               'automationName': 'UiAutomator2',
              'noReset': True,
         }
    options = UiAutomator2Options().load_capabilities(desired_caps)
    try:
        driver = webdriver.Remote(command_executor=server, options=options)
        time.sleep(10)
        print("APP启动成功！")
        time.sleep(10)
    except Exception as e:
        print(f"启动发生错误:{str(e)}")


if __name__ == '__main__':
    start_app()