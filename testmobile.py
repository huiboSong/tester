# coding=utf-8
__author__ = 'songhuibo'

from appium.webdriver.connectiontype import ConnectionType
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from core import constants
from appium import webdriver
import config
from core.logger import Logger as api_log
import os
import time
from selenium.webdriver.common.touch_actions import TouchActions

PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))

import sys

# reload(sys)
# sys.setdefaultencoding("utf-8")

class Mobile():
    def __init__(self, desired_caps):
        # 要写入log的目录，这个需要在config中配置
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def execute(self, driver_command, params=None):
        self.driver.execute(driver_command, params)

    def get_element(self, by_type, by_value):
        """获取基本元素对象"""
        if by_type == "id":
            return self.driver.find_element_by_id(by_value)
        elif by_type == "name":
            return self.driver.find_element_by_name(by_value)
        elif by_type == "xpath":
            return self.driver.find_element_by_xpath(by_value)
        elif by_type == "link":
            return self.driver.find_element_by_link_text(by_value)
        elif by_type == "tag":
            return self.driver.find_element_by_tag_name(by_value)
        elif by_type == "css":
            return self.driver.find_element_by_css_selector(by_value)
        elif by_type == "className":
            return self.driver.find_element_by_class_name(by_value)
        elif by_type == "accessibility_id":
            return self.driver.find_element_by_accessibility_id(by_value)
        else:
            return False

    def is_element_exists(self, by_type, by_value):
        u"""判断控件元素是否存在，返回boolean值"""
        flag = False
        try:

            self.get_element(by_type, by_value)
            flag = True
        except  NoSuchElementException as e:
            flag = False

        # '''python2 写法
        # try:
        #     self.get_element(by_type, by_value)
        #
        #     flag = True
        # except NoSuchElementException, e:
        #     flag = False

        return flag

    def until(self, by_type, by_value):
        u"""等待一个元素被找到，超时抛出异常，超时时间在configBase中设置"""
        res = False
        for i in range(1, config.element_find_wait, 1):
            self.debug_info(constants.el_to_wait % (by_type, by_value, str(i)))
            if self.is_element_exists(by_type, by_value):
                res = True
                break
            else:
                res = False
            time.sleep(1)

        if not res:
            raise NameError(constants.el_not_find % (
                by_type, by_value, str(config.element_find_wait)))


    def until_display(self, by_type, by_value):
        u"""等待一个元素显示，超时抛出异常，超时时间在configBase中设置"""
        res = False
        for i in range(1, config.element_display_wait, 1):
            self.debug_info(constants.el_to_wait % (by_type, by_value, str(i)))
            if self.is_display(by_type, by_value):
                res = True
                break
            else:
                res = False
            time.sleep(1)

        if not res:
            raise NameError(constants.el_not_find % (
                by_type, by_value, str(config.element_find_wait)))

    def is_display(self, by_type, by_value):
        """判断element是否显示，返回boolean值"""
        if self.is_element_exists(by_type, by_value):
            return self.get_element(by_type, by_value).is_displayed()


    def get_text(self, by_type, by_value):
        """获得控件元素的文本信息"""
        self.until_display(by_type, by_value)
        return self.get_element(by_type, by_value).text

    def click(self, by_type, by_value):
        """点击操作
        Usage:
        driver.click("xpath",el.login_submit_btn)
        """
        self.until_display(by_type, by_value)
        if self.is_element_exists(by_type, by_value):
            self.get_element(by_type, by_value).click()

    def send_keys(self, by_type, by_value, text):

        """文本输入操作
        Usage:
        driver.send_keys("xpath",el.login_submit_btn,"测试数据")
        """

        self.until_display(by_type, by_value)
        if self.is_element_exists(by_type, by_value):
            el = self.get_element(by_type, by_value)
            el.clear()
            el.send_keys(text)

        def quit(self):
            """
            driver.quit()
            """
            self.driver.quit()

        def click_back(self):
            '''
            点击手机的返回键
            '''
            self.driver.keyevent(4)

        def click_home(self):
            '''
        点击手机的HOME键
        '''
        self.driver.keyevent(3)

    def get_size(self):
        # 获得机器屏幕大小x,y
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return (x, y)

    # 屏幕滑动
    def swipe(self, start_x, start_y, stop_x, stop_y, t):
        """
        屏幕滑动
        :param start_x:开始滑动的x坐标
        :param start_y:开始滑动的y坐标
        :param stop_x:结束点x坐标
        :param stop_y:结束点y坐标
        :param t:滑动时间
        """
        self.driver.swipe(int(start_x), int(start_y), int(stop_x), int(stop_y), t)


    def swipe_left(self):
        '''
         # 向左滑动 适用启动页面滑动等
        :return:
        '''
        stat_x = self.get_size()[0] * 0.9
        stat_y = self.get_size()[1] * 0.5
        stop_x = self.get_size()[0] * 0.1
        self.swipe(stat_x, stat_y, stop_x, stat_y, 1000)

    def swipe_right(self):
        '''
         # 向右侧滑动 适用启动页面滑动等
        :return:
        '''
        stat_x = self.get_size()[0] * 0.1
        stat_y = self.get_size()[1] * 0.5
        stop_x = self.get_size()[0] * 0.9
        self.swipe(stat_x, stat_y, stop_x, stat_y, 1000)

    def swipe_top(self):
        '''
          # 向上侧滑动 适用于上拉加载更多
        :return:
        '''

        stat_x = self.get_size()[0] * 0.5
        stat_y = self.get_size()[1] * 7 / 8
        stop_y = self.get_size()[1] / 8
        self.swipe(stat_x, stat_y, stat_x, stop_y, 1000)


    def swipe_down(self):
        '''
            # 向下侧滑动 适用于下拉刷新
        :return:
        '''

        stat_x = self.get_size()[0] * 0.5
        stat_y = self.get_size()[1] / 8
        stop_y = self.get_size()[1] * 7 / 8
        self.swipe(stat_x, stat_y, stat_x, stop_y, 1000)

    def get_current_activity(self):

        '''
        获取当前页面的Activity：就是布满整个窗口或者悬浮于其他窗口上的交互界面
        :return: 当前界面的名称
        '''

        return self.driver.current_activity

    def get_context(self):
        '''
         获取当前页面的context上下文：
        :return:当前界面的上下文
        '''
        return self.driver.current_context

    def get_contexts(self):
        '''
         获取当前页面的context上下文：
        :return:当前界面的上下文
        '''
        return self.driver.contexts

    def switch_to_web(self):
        '''
        原生应用跳转到移动web
        :return:
        '''

        self.driver.switch_to.context('WEBVIEW')
        # self.driver.switch_to.context(context)

    def switch_to_nat(self):
        '''
        移动web跳转到原生应用
        :return:
        '''
        self.driver._switch_to.context("NATIVE_APP")

    def zoom(self, el, percent=200, steps=50):
        '''
        控件el 放大
        :param el: 控件
        :param percent: 放大百分比
        :param steps:
         :return:
        '''
        self.driver.zoom(el, percent, steps)

    def pinch(self, el, percent=200, steps=50):
        '''
        控件el 缩小
        :param el: 控件
        :param percent: 缩小百分比
        :param steps:
        :return:
        '''
        self.driver.pinch(el, percent, steps)


    def move(self):
        '''
        NATIVE_APP使用
        tap_and_hold手指按住某个坐标点并且保持这个动作
        move 想某个坐标点移动
        release 在某个左边点保持松开
        :return:
        '''

        TouchActions(self.driver).tap_and_hold(700, 600).move(300, 600).release(300, 600).perform()

    def is_app_installed(self, package):
        '''
         #
        :param package: 包名
        :return:
        '''

        return self.driver.is_app_installed(package)

    def install_app(self, app_path):
        '''
         # 检查应用是否已经安装
        :param package: 安装地址
        :return:
        '''
        self.driver.install_app(app_path)

    def remove_app(self, package):
        '''
         # 从设备中删除一个应用
        :param package:
        :return:
        '''
        self.driver.remove_app(package)

    def close_app(self):
        '''
         # 关闭应用
        :return:
        '''
        self.driver.close_app()


    def screen_shot(self, name_screen_shot):

        path = PATH(config.img_shot_dir)
        if not os.path.isdir(PATH(path)):
            os.makedirs(path)
        return self.driver.get_screenshot_as_file(path + '\\' + name_screen_shot  + '.png')

    def assert_equal(self, unittest, first, second, msg, name_screen_shot):
        """
        :param first: 第一个比较字符串
        :param second: 第二个比较字符串
        :param msg: 断言信息
        :param name_ScreenShot:截图名称
        :return:
        """
        try:
            unittest.assertEqual(first, second, msg)
        # except Exception:
        # pass
        finally:
            self.switch_to_nat()
            self.screen_shot(name_screen_shot)
            time.sleep(5)
            pass

    def background_app(self):
        '''
        # 把当前应用放到后台去
        :return:
        '''
        self.driver.background_app(5)

    def hide_keyboard(self):
        '''
        # 收起键盘
        :return:
        '''
        self.driver.hide_keyboard()


    def set_network(self, type):
        '''

        :param type: 设置网络连接方式  0：飞行名师，1：数据流量模式 ，2：WiFi模式 ,3:数据流量模式和WiFi都开始 ，如果都不匹配。默认WiFi模式
        :return:
        '''
        if str(type) == "0":
            self.driver.set_network_connection(ConnectionType.AIRPLANE_MODE)
        elif str(type) == "1":
            self.driver.set_network_connection(ConnectionType.DATA_ONLY)
        elif str(type) == "2":
            self.driver.set_network_connection(ConnectionType.WIFI_ONLY)
        elif str(type) == "3":
            self.driver.set_network_connection(ConnectionType.ALL_NETWORK_ON)
        else:
            self.driver.set_network_connection(ConnectionType.WIFI_ONLY)

    def js(self, script):
        """
        Execute JavaScript scripts.
        Usage:
        driver.js("window.scrollTo(200,1000);")
        """
        return self.driver.execute_script(script)

    def tap(self, location, time=100):
        # driver.context("NATIVE_APP");
        # WebElement e = driver.findElementByAccessibilityId("登录");
        res = self.driver.tap(location, time)
        return res

    def move_to_element(self, by_type, by_value):
        """鼠标移动到指定元素"""
        el = self.get_element(by_type, by_value)
        self.until_display(by_type, by_value)
        ActionChains(self.driver).move_to_element(el).perform()

    def page_source(self):
        return self.driver.page_source

    def debug_info(self, text):
        """调试信息是否打印，在config文件设置"""
        if config.debug:
            print (text)

    @staticmethod
    def log(info_type, message):
        t = api_log()
        if info_type == "info":
            t.info(message)
        if info_type == "error":
            t.error(message)
        if info_type == "debug":
            t.debug(message)
        return True



