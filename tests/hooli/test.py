__author__ = 'delsk'


import unittest
import time
from macaca import WebDriver

desired_caps = {
    'platformName': 'desktop',
    'browserName': 'electron'
}

server_url = {
    'hostname': 'localhost',
    'port': 3456
}

class MacacaTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = WebDriver(desired_caps, server_url)
        cls.driver.init()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_get_url(self):
        self.driver                     \
          .set_window_size(1280, 800)   \
          .get('https://www.baidu.com')

    def test_search_macaca(self):
        self.driver              \
            .element_by_id('kw') \
            .send_keys('macaca')
        self.driver              \
            .element_by_id('su') \
            .click()
        time.sleep(3)
        html = self.driver.source
        self.assertTrue('macaca' in html)
        self.assertTrue(
          self.driver.element_by_css_selector_if_exists(
            '#head > div.head_wrapper'))
        self.driver                                    \
            .element_by_xpath_or_none('//*[@id="kw"]') \
            .send_keys(' elementByXPath')
        self.driver              \
            .element_by_id('su') \
            .click()
        self.driver.take_screenshot()


if __name__ == '__main__':
    unittest.main()

# chrome 示例
#coding=utf-8
import unittest
from macaca import WebDriver
from time import sleep


desired_caps = {
    'platformName': 'Desktop',  #// iOS, Android, Desktop
    'browserName': 'Chrome',    #// Chrome, Electron
}

# 对应Macaca服务的ip和端口号。
server_url = {
    'hostname': '127.0.0.1',
    'port': 3456
}

class MacacaTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = WebDriver(desired_caps, server_url)
        cls.driver.init()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_get_url(self):
        self.driver.get('https://www.baidu.com')
        self.assertEqual(self.driver.title, '百度一下，你就知道')

    def test_search_macaca(self):
        self.driver.element_by_id("kw").send_keys("macaca")
        self.driver.element_by_id("su").click()
        sleep(2)
        title = self.driver.title
        self.assertTrue('macaca',title)


if __name__ == '__main__':
    unittest.main()
