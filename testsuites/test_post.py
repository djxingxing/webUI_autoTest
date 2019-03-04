import time
import unittest
from Discuz_lx1.framework.base_testcase import BaseTestCase
from Discuz_lx1.framework.user_page import UserPage


class post_use(BaseTestCase):

    def test_post(self):
        post_page = UserPage(self.driver)
        post_page.open_url("http://127.0.0.1/forum.php ")
        time.sleep(3)
        post_page.login('Euler','zhu1234..')
        time.sleep(3)

        seaech="haotest"

        post_page.search(seaech)

        try :
            assert "haotest" in self.driver.title
            print("查找成功")
        except Exception as  e:
            print("失败",e)
        time.sleep(3)

        # 用户退出
        post_page.logout()

if __name__ == '__main__':
    unittest.main()

