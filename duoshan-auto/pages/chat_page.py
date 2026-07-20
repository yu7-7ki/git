"""
Pages — 聊天页面（多闪核心功能）
"""
import logging

from appium.webdriver.common.appiumby import AppiumBy
from base.base_page import BasePage

logger = logging.getLogger(__name__)


class ChatPage(BasePage):
    """多闪聊天页面"""

    # ============ 元素定位器 ============

    # 【定位方式①: ID】聊天输入框
    CHAT_INPUT = (AppiumBy.ID, "com.ss.android.ugc.aweme:id/chat_input")

    # 【定位方式④: ACCESSIBILITY_ID】发送按钮
    SEND_BTN = (AppiumBy.ACCESSIBILITY_ID, "发送")

    # 【定位方式②: XPATH】聊天消息列表
    MESSAGE_LIST = (
        AppiumBy.XPATH,
        "//android.widget.FrameLayout[@resource-id='com.ss.android.ugc.aweme:id/chat_list']",
    )

    # 【定位方式②: XPATH】最近一条消息
    LAST_MESSAGE = (
        AppiumBy.XPATH,
        "(//android.widget.TextView[@resource-id='com.ss.android.ugc.aweme:id/message_text'])[last()]",
    )

    # 【定位方式②: XPATH】聊天列表中的联系人
    CONTACT_ITEM = (AppiumBy.XPATH, "//android.widget.TextView[@text='好友']")

    # ============ 页面操作方法 ============

    def send_text_message(self, text: str):
        """发送文本消息"""
        logger.info(f"发送消息: {text}")
        self.input_text(self.CHAT_INPUT, text)
        self.click(self.SEND_BTN)
        return self

    def get_last_message_text(self) -> str:
        """获取最近一条消息的文本"""
        try:
            return self.get_text(self.LAST_MESSAGE)
        except:
            logger.warning("获取最后一条消息失败")
            return ""

    def is_message_sent(self, expected_text: str, timeout=10) -> bool:
        """验证消息是否发送成功"""
        import time
        time.sleep(2)
        last_text = self.get_last_message_text()
        result = expected_text in last_text
        logger.info(f"消息验证: 期望='{expected_text}', 实际='{last_text}', 结果={result}")
        return result
