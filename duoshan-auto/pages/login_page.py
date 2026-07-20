"""
Pages — 登录页面（多闪真实 UI 元素）
"""
import logging

from appium.webdriver.common.appiumby import AppiumBy
from base.base_page import BasePage

logger = logging.getLogger(__name__)


class LoginPage(BasePage):
    """多闪登录页面"""

    # ============ 元素定位器（从实际 App 抓取）============

    # 【定位方式①: ID】页面标题
    PAGE_TITLE = (AppiumBy.ID, "com.ss.android.ugc.aweme:id/title")

    # 【定位方式①: ID】手机号输入框
    PHONE_INPUT = (AppiumBy.ID, "com.ss.android.ugc.aweme:id/lhb")

    # 【定位方式①: ID】密码输入框（密码登录页）
    PASSWORD_INPUT = (AppiumBy.ID, "com.ss.android.ugc.aweme:id/lc0")

    # 【定位方式①: ID】区号 +86
    COUNTRY_CODE = (AppiumBy.ID, "com.ss.android.ugc.aweme:id/c80")

    # 【定位方式①: ID】"密码登录" 链接（主登录页底部）
    PASSWORD_LOGIN_LINK = (AppiumBy.ID, "com.ss.android.ugc.aweme:id/jm4")

    # 【定位方式①: ID】"验证码登录" 链接（密码登录页底部）
    SMS_LOGIN_LINK = (AppiumBy.ID, "com.ss.android.ugc.aweme:id/jm7")

    # 【定位方式①: ID】"验证并登录" 按钮（主登录页）
    VERIFY_LOGIN_BTN = (AppiumBy.ID, "com.ss.android.ugc.aweme:id/fpx")

    # 【定位方式①: ID】"登录" 按钮（密码登录页）
    LOGIN_BTN = (AppiumBy.ID, "com.ss.android.ugc.aweme:id/login")

    # 【定位方式①: ID】协议勾选框
    AGREEMENT_CHECKBOX = (AppiumBy.ID, "com.ss.android.ugc.aweme:id/miy")

    # 【定位方式②: XPATH】协议文本（通过部分文本匹配）
    AGREEMENT_TEXT = (
        AppiumBy.XPATH,
        "//android.widget.TextView[contains(@text, '已阅读并同意')]",
    )

    # 【定位方式①: ID】返回按钮
    BACK_BTN = (AppiumBy.ID, "com.ss.android.ugc.aweme:id/hr3")

    # 【定位方式①: ID】帮助按钮
    HELP_BTN = (AppiumBy.ID, "com.ss.android.ugc.aweme:id/nkc")

    # 【定位方式④: ACCESSIBILITY_ID】显示密码切换开关
    SHOW_PASSWORD_SWITCH = (AppiumBy.ACCESSIBILITY_ID, "展示密码")

    # ============ 页面操作方法 ============

    def get_title(self) -> str:
        """获取页面标题"""
        return self.get_text(self.PAGE_TITLE)

    def input_phone(self, phone: str):
        """输入手机号"""
        self.input_text(self.PHONE_INPUT, phone)
        return self

    def input_password(self, pwd: str):
        """输入密码"""
        self.input_text(self.PASSWORD_INPUT, pwd)
        return self

    def click_password_login_link(self):
        """点击"密码登录"切换到密码登录页"""
        self.click(self.PASSWORD_LOGIN_LINK)
        logger.info("切换到密码登录页")
        return self

    def click_sms_login_link(self):
        """点击"验证码登录"切换回验证码登录页"""
        self.click(self.SMS_LOGIN_LINK)
        return self

    def click_login(self):
        """点击登录按钮（密码登录页）"""
        self.click(self.LOGIN_BTN)
        return self

    def click_verify_login(self):
        """点击验证并登录按钮（验证码登录页）"""
        self.click(self.VERIFY_LOGIN_BTN)
        return self

    def check_agreement(self):
        """勾选协议"""
        self.click(self.AGREEMENT_CHECKBOX)
        return self

    def click_back(self):
        """点击返回按钮"""
        self.click(self.BACK_BTN)
        return self

    def click_help(self):
        """点击帮助"""
        self.click(self.HELP_BTN)
        return self

    def is_on_login_page(self) -> bool:
        """判断是否在登录页（通过标题判断）"""
        try:
            title = self.get_title()
            return "登录多闪" in title or "手机号密码登录" in title
        except:
            return False

    def login_with_password(self, phone: str, password: str):
        """
        密码登录完整流程
        演示 PO 链式调用
        """
        logger.info("执行密码登录流程")
        self.click_password_login_link() \
            .input_phone(phone) \
            .input_password(password)
        # 按钮需要填完内容才可用，点击登录
        self.click_login()
        logger.info(f"密码登录完成: phone={phone}")
        return self
