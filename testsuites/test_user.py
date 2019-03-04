import time
import unittest
from Discuz_lx1.framework.base_testcase import BaseTestCase
from Discuz_lx1.framework.user_page import UserPage


class User_use(BaseTestCase):

    def test_user(self):
        user_page = UserPage(self.driver)
        user_page.open_url("http://127.0.0.1/forum.php ")
        time.sleep(3)
        user_page.login('Euler','zhu1234..')
        time.sleep(3)

        # 点击发帖
        user_page.join_plant()
        title='我的帖子标题'
        content='我的帖子内容'
        user_page.plant_send(title,content)

        time.sleep(15)  # 两次发帖时间间隔不少于15秒

        # 默认板块回帖
        reply='回复我的帖子'
        user_page.reply(reply)

        user_page.reply_send()
        time.sleep(5)

        # 用户退出
        user_page.logout()

if __name__ == '__main__':
    unittest.main()
