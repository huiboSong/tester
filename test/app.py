import time,os
import testmobile
from setting.test_test import setting
from setting.test_test import el
from setting.test_test import data
import unittest
PATH=lambda p:os.path.abspath(os.path.join(os.path.dirname(__file__),p))
class TestCase(unittest.TestCase):

    def test(self):
        self.dir = testmobile.Mobile(setting.desired_caps)
        test = self.dir
        time.sleep(1)
        test.swipe_left()
        time.sleep(2)
        test.click('id','com.womai:id/guide_start_next')
        # test.click('id','com.womai:id/tutorial_img')
        # test.click('id','com.womai:id/tutorial_img')
        test.click("id","com.android.packageinstaller:id/permission_allow_button")
        time.sleep(3)
        test.click('id','com.womai:id/selectcitylist_item_lin')
        time.sleep(3)
        test.click('id','com.android.packageinstaller:id/permission_allow_button')
        test.click('id','com.womai:id/dialog_close')
        # test.click('id','com.womai:id/tvLoginTip')
        # test.click("id","com.womai:id/ivClose")
        test.send_keys("id","com.womai:id/navigate_bar_more")
        test.click('id','com.womai:id/tvLoginTip')
        test.click('id','com.womai:id/radio_normal')
        test.send_keys('id','com.womai:id/login_edit_username','mobile_ceshi')
        test.send_keys("id","com.womai:id/login_edit_password","songbo1220")
        test.click("id","com.womai:id/login_btn")
        time.sleep(5)
        test.close_app()


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCase)
    result = unittest.TextTestRunner(verbosity=2).run(suite)