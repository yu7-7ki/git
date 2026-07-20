"""
Pages — 首页/主页（抖音 Feed 流）
元素 ID 已通过 Appium Inspector 抓取验证 ✅
"""
import logging

from appium.webdriver.common.appiumby import AppiumBy
from base.base_page import BasePage

logger = logging.getLogger(__name__)


class HomePage(BasePage):
    """抖音首页 — Feed 短视频流"""

    # ============ 顶部频道区 ============

    # 【定位方式②: XPATH】推荐频道（text 匹配）
    TAB_RECOMMEND = (AppiumBy.XPATH, "//android.widget.TextView[@text='推荐']")

    # 【定位方式②: XPATH】关注频道
    TAB_FOLLOWING = (AppiumBy.XPATH, "//android.widget.TextView[@text='关注']")

    # 【定位方式②: XPATH】商城频道
    TAB_SHOP = (AppiumBy.XPATH, "//android.widget.TextView[@text='商城']")

    # ============ 底部导航栏 ============

    # 4 个 Tab 共用一个 resource-id: com.ss.android.ugc.aweme:id/0to
    # 没有 content-desc，使用 text 文本定位

    # 【定位方式④: ACCESSIBILITY_ID】首页 Tab（content-desc）
    TAB_HOME = (AppiumBy.ACCESSIBILITY_ID, "首页，按钮")

    # 【定位方式④: ACCESSIBILITY_ID】朋友 Tab
    TAB_FRIEND = (AppiumBy.ACCESSIBILITY_ID, "朋友，按钮")

    # 【定位方式④: ACCESSIBILITY_ID】消息 Tab
    TAB_MESSAGE = (AppiumBy.ACCESSIBILITY_ID, "消息，按钮")

    # 【定位方式④: ACCESSIBILITY_ID】我 Tab
    TAB_PROFILE = (AppiumBy.ACCESSIBILITY_ID, "我，按钮")

    # 【定位方式①: ID】发布按钮（底部 +）
    PUBLISH_BTN = (AppiumBy.ID, "com.ss.android.ugc.aweme:id/f=q")

    # ============ 右上角操作按钮 ============

    # 【定位方式①: ID】搜索按钮（首页右上角）
    SEARCH_BTN = (AppiumBy.ID, "com.ss.android.ugc.aweme:id/2ix")

    # ============ 页面操作方法 ============

    def browse_feed(self, swipe_count=3):
        """浏览 Feed 流（滑动视频）"""
        logger.info(f"开始浏览 Feed 流，滑动 {swipe_count} 次")
        self.wait_element_visible(self.TAB_HOME)
        for i in range(swipe_count):
            self.swipe_up()
            logger.info(f"第 {i + 1} 次上滑")
        return self

    def switch_to_recommend(self):
        """切换到推荐频道"""
        self.click(self.TAB_RECOMMEND)
        return self

    def switch_to_following(self):
        """切换到关注频道"""
        self.click(self.TAB_FOLLOWING)
        return self

    def click_search(self):
        """点击搜索按钮"""
        self.click(self.SEARCH_BTN)
        return self

    def click_publish(self):
        """点击发布按钮（底部 +）"""
        self.click(self.PUBLISH_BTN)
        return self

    def go_to_tab(self, tab_name: str):
        """切换到底部 Tab（首页/朋友/消息/我）"""
        tab_map = {
            "首页": self.TAB_HOME,
            "朋友": self.TAB_FRIEND,
            "消息": self.TAB_MESSAGE,
            "我": self.TAB_PROFILE,
        }
        locator = tab_map.get(tab_name)
        if locator:
            self.click(locator)
            logger.info(f"切换到底部Tab: {tab_name}")
        return self

    def go_to_profile(self):
        """进入个人主页"""
        self.go_to_tab("我")
        return self

    def go_to_messages(self):
        """进入消息列表"""
        self.go_to_tab("消息")
        return self

    def go_to_friends(self):
        """进入朋友页"""
        self.go_to_tab("朋友")
        return self

    def is_on_home(self) -> bool:
        """判断是否在首页"""
        return self.is_element_present(self.TAB_HOME)
