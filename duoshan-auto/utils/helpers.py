"""
工具类 — 辅助函数
"""
import json
import logging
import subprocess
import time

logger = logging.getLogger(__name__)


def get_device_info():
    """通过 ADB 获取连接的设备信息"""
    try:
        result = subprocess.run(
            ["adb", "devices"],
            capture_output=True, text=True, timeout=5
        )
        lines = result.stdout.strip().split("\n")[1:]
        devices = [line.split("\t")[0] for line in lines if "device" in line]
        return devices
    except (subprocess.TimeoutExpired, FileNotFoundError) as e:
        logger.warning(f"获取设备信息失败: {e}")
        return []


def get_android_version():
    """获取 Android 版本号"""
    try:
        result = subprocess.run(
            ["adb", "shell", "getprop", "ro.build.version.release"],
            capture_output=True, text=True, timeout=5
        )
        return result.stdout.strip()
    except (subprocess.TimeoutExpired, FileNotFoundError):
        return "未知"


def dump_ui_xml(save_path="ui_dump.xml"):
    """
    使用 UIAutomator dump 当前页面 XML
    用于分析元素定位
    """
    try:
        subprocess.run(
            ["adb", "shell", "uiautomator", "dump", "/sdcard/ui_dump.xml"],
            capture_output=True, timeout=10
        )
        subprocess.run(
            ["adb", "pull", "/sdcard/ui_dump.xml", save_path],
            capture_output=True, timeout=10
        )
        logger.info(f"UI XML 已保存: {save_path}")
        return save_path
    except subprocess.TimeoutExpired:
        logger.error("UI dump 超时")
        return None


class AppMonitor:
    """
    ADB 进程监控工具
    用于 Monkey / 稳定性测试中的日志采集
    """

    @staticmethod
    def start_logcat(tag="DuoshanTest", save_path="app_log.log"):
        """启动 logcat 日志采集"""
        cmd = f"adb logcat -v time -s {tag} > {save_path} 2>&1 &"
        subprocess.Popen(cmd, shell=True)
        logger.info(f"Logcat 已启动: {save_path}")
        return save_path

    @staticmethod
    def get_mem_info(package_name="com.ss.android.ugc.aweme"):
        """获取 App 内存信息"""
        try:
            result = subprocess.run(
                ["adb", "shell", "dumpsys", "meminfo", package_name],
                capture_output=True, text=True, timeout=10
            )
            return result.stdout
        except subprocess.TimeoutExpired:
            return "获取内存信息超时"

    @staticmethod
    def get_cpu_info(package_name="com.ss.android.ugc.aweme"):
        """获取 App CPU 使用率"""
        try:
            result = subprocess.run(
                ["adb", "shell", "top", "-n", "1", "-p", package_name],
                capture_output=True, text=True, timeout=10
            )
            return result.stdout
        except subprocess.TimeoutExpired:
            return "获取 CPU 信息超时"
