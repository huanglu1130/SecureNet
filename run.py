# import os
# import unittest
# from htmltestreport import HTMLTestReport
# from config import DIR_PATH
#
# suite = unittest.defaultTestLoader.discover("./scripts/", pattern='test_02_app_chats.py')
# file_path = DIR_PATH + os.sep + "report" + os.sep + "log.html"
# HTMLTestReport(file_path).run(suite)


# !/usr/bin/env python3


# run.py
import os
import subprocess
import sys
import pytest
import sys
print("Python路径:", sys.executable)
print("sys.path:", sys.path)


# 使用绝对路径
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
REPORT_DIR = os.path.join(BASE_DIR, "allure-report")
ALLURE_RESULTS = os.path.join(BASE_DIR, "allure-results")
# TEST_FILE = os.path.join(BASE_DIR, "scripts", "test_02_app_chats.py")
# TEST_FILE = os.path.join(BASE_DIR, "scripts", "test_01_app_login.py")
# TEST_FILE = os.path.join(BASE_DIR, "scripts", "test_03_app_loginout.py")
# TEST_FILE = os.path.join(BASE_DIR, "scripts", "test_03_add_friends.py")
TEST_FILE = os.path.join(BASE_DIR, "scripts", "test_04_friends_info.py")



def run_tests():
    """执行测试并生成Allure报告"""
    # 清理旧的报告数据
    if os.path.exists(ALLURE_RESULTS):
        for file in os.listdir(ALLURE_RESULTS):
            os.remove(os.path.join(ALLURE_RESULTS, file))
    os.makedirs(ALLURE_RESULTS, exist_ok=True)

    # 方法1：使用系统命令（100%可靠）
    command = [
        "pytest",
        TEST_FILE,
        "-v",
        "--alluredir=" + ALLURE_RESULTS,
        "--capture=no"
    ]

    exit_code = subprocess.run(command).returncode
    # 方法2：或者使用subprocess（更灵活）
    # import subprocess
    # exit_code = subprocess.call(command)

    # 生成Allure报告
    if exit_code in [0, 1]:  # 成功或部分失败时生成
        os.system(f"allure generate {ALLURE_RESULTS} -o {REPORT_DIR} --clean")
        print(f"\n✅ 报告已生成: file://{REPORT_DIR}/index.html")
    else:
        print("\n❌ 测试执行失败")


if __name__ == "__main__":
    run_tests()