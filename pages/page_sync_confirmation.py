import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from base.base import Base
import pages

class PageAppSync(Base):
    # 1、点击同步消息
    def page_app_click_sync(self):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(pages.app_sync_sync)
            )
            element.click()
            print(f"成功点击元素: {pages.app_sync_sync}")
            time.sleep(20)
            return True
        except NoSuchElementException:
            print("没有出现sync按钮")
            return False