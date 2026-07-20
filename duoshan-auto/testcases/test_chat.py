"""
TestCase — 聊天功能测试（需登录抖音）
"""
import allure
import pytest


@allure.feature("聊天功能")
class TestChat:
    """聊天相关测试（需先登录抖音）"""

    @allure.story("发送消息")
    @allure.title("发送文本消息（需登录）")
    @pytest.mark.skip(reason="需要抖音登录账号")
    def test_send_text_message(self, driver):
        """发送消息测试 - 需先登录"""
        pass

    @allure.story("输入框交互")
    @allure.title("输入框焦点（需登录）")
    @pytest.mark.skip(reason="需要抖音登录账号")
    def test_chat_input_focus(self, driver):
        """输入框交互测试 - 需先登录"""
        pass
