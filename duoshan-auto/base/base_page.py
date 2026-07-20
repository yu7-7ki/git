"""
BasePage — PO 模型的基类
封装 Appium 通用操作：元素定位、等待、截图、手势等

定位方式使用示例（≥3种）:
  1. ID 定位          — find_element(By.ID, "android:id/title")
  2. XPATH 定位       — find_element(By.XPATH, "//android.widget.TextView[@text='登录']")
  3. CLASS_NAME 定位  — find_element(By.CLASS_NAME, "android.widget.Button")
  4. ACCESSIBILITY_ID — find_element(By.ACCESSIBILITY_ID, "compose")
  5. AndroidUIAutomator — find_element(by=By.ANDROID_UIAUTOMATOR, value=...)
"""
import logging
import os
from datetime import datetime

import allure
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import (
    NoSuchElementException,
    TimeoutException,
)
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from config.desired_caps import SCREENSHOTS_DIR

logger = logging.getLogger(__name__)


class BasePage:
    """页面基类，所有 Page 对象继承此类"""

    # ---- 默认超时时间 ----
    IMPLICIT_WAIT = 10          # 隐式等待（秒）
    EXPLICIT_WAIT = 15          # 显式等待（秒）

    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(self.IMPLICIT_WAIT)

    # ============================================================
    # 1. 元素定位（支持多种策略）
    # ============================================================

    def find_element(self, locator):
        """
        定位单个元素
        :param locator: 元组 (By 策略, 定位值)
        :用法: self.find_element((AppiumBy.ID, "com.xxx:id/btn_login"))
        """
        try:
            return self.driver.find_element(*locator)
        except NoSuchElementException:
            self.log_and_screenshot(f"元素未找到: {locator}")
            raise

    def find_elements(self, locator):
        """定位一组元素"""
        return self.driver.find_elements(*locator)

    # ---- 具体定位方式示例 ----

    def find_by_id(self, element_id: str):
        """【定位方式①】ID 定位"""
        return self.find_element((AppiumBy.ID, element_id))

    def find_by_xpath(self, xpath: str):
        """【定位方式②】XPATH 定位"""
        return self.find_element((AppiumBy.XPATH, xpath))

    def find_by_class(self, class_name: str):
        """【定位方式③】CLASS_NAME 定位"""
        return self.find_element((AppiumBy.CLASS_NAME, class_name))

    def find_by_accessibility_id(self, aid: str):
        """【定位方式④】Accessibility ID 定位（content-desc）"""
        return self.find_element((AppiumBy.ACCESSIBILITY_ID, aid))

    def find_by_uiautomator(self, ui_selector: str):
        """【定位方式⑤】Android UIAutomator 定位（强大灵活）"""
        # 示例: 'new UiSelector().text("登录").className("android.widget.Button")'
        return self.find_element((AppiumBy.ANDROID_UIAUTOMATOR, ui_selector))

    # ============================================================
    # 2. 等待机制
    # ============================================================

    def wait_element_visible(self, locator, timeout=None):
        """显式等待 — 元素可见"""
        timeout = timeout or self.EXPLICIT_WAIT
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
        except TimeoutException:
            self.log_and_screenshot(f"等待元素可见超时: {locator}")
            raise

    def wait_element_clickable(self, locator, timeout=None):
        """显式等待 — 元素可点击"""
        timeout = timeout or self.EXPLICIT_WAIT
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(locator)
            )
        except TimeoutException:
            self.log_and_screenshot(f"等待元素可点击超时: {locator}")
            raise

    def wait_element_disappear(self, locator, timeout=None):
        """等待元素消失（常用于加载弹窗）"""
        timeout = timeout or self.EXPLICIT_WAIT
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.invisibility_of_element_located(locator)
            )
        except TimeoutException:
            self.log_and_screenshot(f"等待元素消失超时: {locator}")

    # ============================================================
    # 3. 常用操作
    # ============================================================

    def click(self, locator):
        """点击元素"""
        el = self.wait_element_clickable(locator)
        el.click()
        logger.info(f"点击元素: {locator}")

    def input_text(self, locator, text: str):
        """输入文本（先清空再输入）"""
        el = self.wait_element_visible(locator)
        el.clear()
        el.send_keys(text)
        logger.info(f"输入文本 [{text}]: {locator}")

    def get_text(self, locator) -> str:
        """获取元素文本"""
        el = self.wait_element_visible(locator)
        return el.text

    def is_element_present(self, locator) -> bool:
        """判断元素是否存在"""
        try:
            self.driver.implicitly_wait(2)
            self.driver.find_element(*locator)
            return True
        except NoSuchElementException:
            return False
        finally:
            self.driver.implicitly_wait(self.IMPLICIT_WAIT)

    # ============================================================
    # 4. 手势操作（滑动、长按等 — 适合多闪的 Feed 流）
    # ============================================================

    def swipe_up(self, duration=500):
        """向上滑动（多闪 Feed 流浏览）"""
        size = self.driver.get_window_size()
        start_x = size["width"] * 0.5
        start_y = size["height"] * 0.8
        end_y = size["height"] * 0.2
        self.driver.swipe(start_x, start_y, start_x, end_y, duration)
        logger.info("向上滑动")

    def swipe_down(self, duration=500):
        """向下滑动"""
        size = self.driver.get_window_size()
        start_x = size["width"] * 0.5
        start_y = size["height"] * 0.2
        end_y = size["height"] * 0.8
        self.driver.swipe(start_x, start_y, start_x, end_y, duration)
        logger.info("向下滑动")

    def scroll_to_text(self, text: str):
        """滚动到包含指定文本的元素（UiAutomator2 方式）"""
        ui_selector = f'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text("{text}"))'
        return self.find_by_uiautomator(ui_selector)

    # ============================================================
    # 5. 截图
    # ============================================================

    def take_screenshot(self, name=None):
        """截图保存"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{name or 'screenshot'}_{timestamp}.png"
        filepath = os.path.join(SCREENSHOTS_DIR, filename)
        self.driver.save_screenshot(filepath)
        logger.info(f"截图保存: {filepath}")
        # Attach to Allure 报告
        allure.attach.file(filepath, name=name or "截图", attachment_type=allure.attachment_type.PNG)
        return filepath

    def log_and_screenshot(self, msg: str):
        """错误时记录日志并截图"""
        logger.error(msg)
        self.take_screenshot(name="error")

    # ============================================================
    # 6. 页面导航辅助
    # ============================================================

    def get_page_source(self) -> str:
        """获取当前页面 XML 源码（用于调试元素定位）"""
        return self.driver.page_source

    def press_back(self):
        """按返回键"""
        self.driver.back()
        logger.info("按下返回键")

    def press_home(self):
        """按 Home 键"""
        self.driver.press_keycode(3)  # KEYCODE_HOME = 3
        logger.info("按下 Home 键")
