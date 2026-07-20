"""
Pages — 个人主页/设置页面
"""
import logging

from appium.webdriver.common.appiumby import AppiumBy
from base.base_page import BasePage

logger = logging.getLogger(__name__)


class ProfilePage(BasePage):
    """多闪个人主页"""

    # ============ 元素定位器 ============

    # 【定位方式②: XPATH】用户昵称
    USERNAME = (
        AppiumBy.XPATH,
        "//android.widget.TextView[@resource-id='com.ss.android.ugc.aweme:id/user_name']",
    )

    # 【定位方式②: XPATH】粉丝数
    FANS_COUNT = (
        AppiumBy.XPATH,
        "//android.widget.TextView[contains(@text, '粉丝')]",
    )

    # 【定位方式④: ACCESSIBILITY_ID】设置按钮
    SETTINGS_BTN = (AppiumBy.ACCESSIBILITY_ID, "设置")

    # 【定位方式⑤: UIAutomator】退出登录（滚动查找）
    LOGOUT_BTN = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiScrollable(new UiSelector().scrollable(true))'
        '.scrollIntoView(new UiSelector().text("退出登录"))',
    )

    # 【定位方式②: XPATH】确认退出
    CONFIRM_LOGOUT = (
        AppiumBy.XPATH,
        "//android.widget.Button[@text='确定']",
    )

    # ============ 页面操作方法 ============

    def get_username(self) -> str:
        """获取用户昵称"""
        return self.get_text(self.USERNAME)

    def get_fans_count(self) -> str:
        """获取粉丝数"""
        return self.get_text(self.FANS_COUNT)

    def go_to_settings(self):
        """进入设置页面"""
        self.click(self.SETTINGS_BTN)
        return self

    def logout(self):
        """退出登录"""
        self.go_to_settings()
        self.scroll_to_text("退出登录")
        self.click(self.LOGOUT_BTN)
        self.click(self.CONFIRM_LOGOUT)
        logger.info("已退出登录")
        return self

    def take_profile_screenshot(self):
        """截取个人主页"""
        return self.take_screenshot(name="个人主页")
