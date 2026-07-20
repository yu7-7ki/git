"""
TestCase — Appium 自动化框架验证
不依赖登录状态，只验证框架本身可用
"""
import allure
import pytest
import time

from pages.home_page import HomePage


@allure.feature("Appium 自动化框架验证")
class TestAppiumFramework:
    """验证 Appium 测试框架能否正常工作"""

    @allure.story("环境验证")
    @allure.title("Appium 连接设备并启动 App")
    @pytest.mark.smoke
    def test_appium_connect(self, driver):
        """
        验证核心环境：
        1. Appium Server 正常
        2. ADB 连接设备正常
        3. Appium Session 创建成功
        4. 截图功能正常
        """
        with allure.step("等待 App 加载"):
            time.sleep(3)

        with allure.step("获取当前页面信息"):
            activity = driver.current_activity
            package = driver.current_package
            allure.attach(f"Package: {package}, Activity: {activity}",
                         name="当前页面", attachment_type=allure.attachment_type.TEXT)

        with allure.step("截图当前状态"):
            path = HomePage(driver).take_screenshot(name=f"当前页面_{activity}")
            assert path, "截图应成功保存"

        with allure.step("获取页面源码（验证能读取 UI 树）"):
            source = driver.page_source
            assert len(source) > 100, "页面源码应包含内容"
            allure.attach(str(len(source)), name="页面源码大小")

    @allure.story("框架功能验证")
    @allure.title("BasePage 公共方法验证")
    def test_base_page_utils(self, driver):
        """
        验证 BasePage 封装的公共方法
        不依赖特定页面元素
        """
        page = HomePage(driver)
        time.sleep(2)

        with allure.step("获取窗口大小（验证 driver 正常）"):
            size = driver.get_window_size()
            assert size["width"] > 0
            assert size["height"] > 0
            allure.attach(f"{size['width']}x{size['height']}",
                         name="屏幕分辨率")

        with allure.step("截图方法验证"):
            path = page.take_screenshot(name="BasePage截图测试")
            assert path, "截图应保存成功"

        with allure.step("元素判断方法验证（不关心结果）"):
            # 尝试查找任意可见元素，不强制断言
            from appium.webdriver.common.appiumby import AppiumBy
            elements = driver.find_elements(AppiumBy.XPATH, "//*[@enabled='true']")
            allure.attach(str(len(elements)), name="页面可用元素数量")

    @allure.story("设备信息")
    @allure.title("获取测试设备信息")
    def test_device_info(self, driver):
        """获取并记录测试设备信息"""
        with allure.step("获取设备信息"):
            info = {
                "platform": driver.capabilities.get("platformName"),
                "device": driver.capabilities.get("deviceName"),
                "udid": driver.capabilities.get("udid"),
                "appPackage": driver.capabilities.get("appPackage"),
                "appActivity": driver.capabilities.get("appActivity"),
                "automation": driver.capabilities.get("automationName"),
            }
            for k, v in info.items():
                allure.attach(str(v), name=k)
