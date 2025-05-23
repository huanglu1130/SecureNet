from time import sleep

from base.base import Base
import pages
class PageAppLoginOut(Base):
    #1、点击我的头像
    def page_app_loginout_cancel(self):
        self.base_click(pages.app_avatar)
        self.base_click(pages.app_login_out)
        self.base_click(pages.app_loginout_cancel)

    def page_app_loginout_confirm(self):
        self.base_click(pages.app_avatar)
        self.base_click(pages.app_login_out)
        self.base_click(pages.app_loginout_confirm)


