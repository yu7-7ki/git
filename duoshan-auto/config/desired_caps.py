"""
多闪 App — Appium 自动化测试配置
"""
import os

# 项目根目录
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 截图目录
SCREENSHOTS_DIR = os.path.join(ROOT_DIR, "screenshots")
os.makedirs(SCREENSHOTS_DIR, exist_ok=True)

# 测试报告目录
REPORTS_DIR = os.path.join(ROOT_DIR, "reports")
os.makedirs(REPORTS_DIR, exist_ok=True)

# Appium 连接配置
APPIUM_CONFIG = {
    "command_executor": "http://127.0.0.1:4723",  # Appium Server 地址
}

# Desired Capabilities 工厂函数
def get_douyin_caps(platform="android"):
    """获取抖音 App 的 Desired Capabilities"""
    if platform == "android":
        return {
            "platformName": "Android",
            "deviceName": "LDPlayer",                  # 雷电模拟器
            "udid": "127.0.0.1:5555",                  # 雷电模拟器 ADB 端口
            "appPackage": "com.ss.android.ugc.aweme",   # 抖音包名
            "appActivity": ".splash.SplashActivity",     # 启动 Activity
            "noReset": True,                           # 不重置应用数据
            "automationName": "UiAutomator2",          # Android 自动化引擎
            "newCommandTimeout": 300,                  # 命令超时时间
            "autoGrantPermissions": True,              # 自动授予权限
        }
    # iOS 配置预留
    return {}
