"""
TestCase — PO 模型与定位方式演示
不依赖登录，展示框架设计思路
"""
import allure
import pytest


@allure.feature("PO 模型与定位方式")
class TestFrameworkDemo:
    """演示框架设计（无需登录）"""

    @allure.story("PO 三层模型")
    @allure.title("项目结构展示")
    def test_project_structure(self):
        """
        展示 PO 三层模型设计（纯文档说明）
        实际代码已按此结构组织
        """
        allure.attach("base/ → base_page.py", name="第一层：基类")
        allure.attach("pages/ → login/home/chat/profile", name="第二层：页面对象")
        allure.attach("testcases/ → test_*.py", name="第三层：测试用例")
        assert True

    @allure.story("定位方式示例")
    @allure.title("5 种元素定位方式代码示例")
    def test_locator_examples(self):
        """
        展示代码中的 5 种定位方式
        """
        examples = """
        ① ID定位:     (AppiumBy.ID, "com.ss.android.ugc.aweme:id/login")
        ② XPath定位:   (AppiumBy.XPATH, "//android.widget.TextView[@text='推荐']")
        ③ ClassName:   (AppiumBy.CLASS_NAME, "android.widget.EditText")
        ④ Accessibility: (AppiumBy.ACCESSIBILITY_ID, "首页，按钮")
        ⑤ UIAutomator:   (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("...")')
        """
        allure.attach(examples, name="5种定位方式", attachment_type=allure.attachment_type.TEXT)
        assert True
