import time,os
import testmobile
from setting.test_test import setting
import unittest
PATH=lambda p:os.path.abspath(os.path.join(os.path.dirname(__file__),p))
class TestCase(unittest.TestCase):

    def test(self):
        self.dir = testmobile.Mobile(setting.desired)
        test = self.dir
        time.sleep(1)
        test.click('id','com.android.packageinstaller:id/permission_allow_button')
        test.click('id','com.android.packageinstaller:id/permission_allow_button')
        test.click('id','com.android.packageinstaller:id/permission_allow_button')
        time.sleep(6)
        test.close_app()
if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCase)
    result = unittest.TextTestRunner(verbosity=0).run(suite)