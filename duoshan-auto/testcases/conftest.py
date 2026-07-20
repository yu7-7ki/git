"""
pytest 全局配置 — Appium Driver 初始化与清理
"""
import logging
import os

import allure
import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options

from config.desired_caps import APPIUM_CONFIG, get_douyin_caps, SCREENSHOTS_DIR

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)
logger = logging.getLogger(__name__)


@pytest.fixture(scope="function")
def driver():
    """
    每个测试函数启动一个 Appium Session
    yield driver 给测试用，测试结束后自动退出
    """
    caps = get_douyin_caps()
    logger.info(f"连接 Appium Server: {APPIUM_CONFIG['command_executor']}")
    logger.info(f"Desired Capabilities: {caps}")

    options = UiAutomator2Options()
    options.load_capabilities(caps)
    driver = webdriver.Remote(APPIUM_CONFIG["command_executor"], options=options)
    logger.info("Appium Session 已创建")

    yield driver  # 测试在这里执行

    # 测试结束后清理
    logger.info("关闭 Appium Session")
    driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    测试失败时自动截图并附加到 Allure 报告
    """
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        # 获取 driver 对象（从 fixture 中）
        driver = item.funcargs.get("driver")
        if driver:
            screenshot_path = os.path.join(SCREENSHOTS_DIR, f"{item.name}_失败.png")
            driver.save_screenshot(screenshot_path)
            allure.attach.file(
                screenshot_path,
                name=f"{item.name}_失败截图",
                attachment_type=allure.attachment_type.PNG,
            )
            logger.error(f"测试 [{item.name}] 失败，截图已保存: {screenshot_path}")
