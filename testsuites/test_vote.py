import time
import unittest
from Discuz_lx1.framework.base_testcase import BaseTestCase
from Discuz_lx1.framework.user_page import UserPage


class Vote_use(BaseTestCase):

    def test_user(self):
        user_page = UserPage(self.driver)
        user_page.open_url("http://127.0.0.1/forum.php ")
        time.sleep(3)
        user_page.login('Euler','zhu1234..')
        time.sleep(3)

        # 进入默认版块
        user_page.join_plant()
        user_page.join_vote()

        title='喜欢的宠物'
        animal1 = '猫'
        animal2 = '狗'
        animal3 = '猪'

        user_page.vote_initiation(title,animal1,animal2,animal3)

        #进行投票
        user_page.vote()
        user_page.vote_message()


        time.sleep(5)

        # 用户退出
        user_page.logout()

if __name__ == '__main__':
    unittest.main()
