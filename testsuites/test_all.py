import unittest,HTMLTestRunner,os
from Discuz_lx1.testsuites.test_user import User_use
from Discuz_lx1.testsuites.test_switch_user import Switch_user
from Discuz_lx1.testsuites.test_post import post_use
from Discuz_lx1.testsuites.test_vote import Vote_use
import sys
sys.path.append('D:/UIzdh/Discuz_lx1')



#设置报告文件保存路径
cur_path=os.path.dirname(os.path.realpath(__file__))
report_path=os.path.join(cur_path,"report")
if not os.path.exists(report_path):os.mkdir(report_path)


#构造测试套件
suite=unittest.TestSuite()
suite.addTest(unittest.makeSuite(User_use))
suite.addTest(unittest.makeSuite(Switch_user))
suite.addTest(unittest.makeSuite(post_use))
suite.addTest(unittest.makeSuite(Vote_use))

if __name__=='__main__':

    html_report=report_path+r'\result.html'
    fp=open(html_report,"wb")

    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, verbosity=2,
                                           title="单元测试报告", description="用例执行情况")
    runner.run(suite)