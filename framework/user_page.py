from Discuz_lx1.framework.base import BasePage
from selenium.webdriver.common.by import By

class UserPage(BasePage):

    #登录用户名，密码框
    username_input_loc=(By.NAME,'username')
    userpwd_input_loc=(By.NAME,'password')

    #登录按钮
    login_button_loc=(By.CSS_SELECTOR,'.fastlg_l button')

    #进入默认版块（可以点击文字进入也可以点击图片进入）
    plant_word_loc = (By.CSS_SELECTOR, '.bm_c h2 a')
    plant_img_loc=(By.CSS_SELECTOR, '.fl_icn img')

    #快速发帖，标题框和文本框
    title_input_loc = (By.XPATH, "//input[@id='subject']")
    content_textarea_loc = (By.XPATH, "//textarea[@name='message']")

    # 发帖按钮
    send_post_loc=(By.NAME,'topicsubmit')

    # 回帖文本框
    reply_text_loc = (By.CSS_SELECTOR, '#fastpostmessage')

    #回帖按钮
    reply_button_loc=(By.CSS_SELECTOR, '#fastpostsubmit')
    # reply_button_loc=(By.NAME,'replysubmit')

    #论坛按钮
    forum_text_loc=(By.ID,'mn_forum')

    # 用户退出按钮
    exit_text_loc=(By.LINK_TEXT,'退出')

    #************************************************************
    #进入默认版块之后，帖子文本
    post_word_loc=(By.XPATH," // th/a[2]")

    #删除主题文本
    del_post_loc=(By.LINK_TEXT,"删除主题")

    #确定按钮
    sure_button_loc=(By.NAME,"modsubmit")

    #管理中心文本
    center_word_loc=(By.LINK_TEXT,"管理中心")

    #论坛文本
    forun_word_loc=(By.LINK_TEXT,'论坛')

    #添加新版块文本
    # new_plant_loc=(By.LINK_TEXT,"添加新版块")
    # new_plant_loc = (By.CSS_SELECTOR, ".addtr")

    new_plant_loc=(By.CSS_SELECTOR,'.lastboard a')
    new_plant_name_loc=(By.NAME,'newforum[1][]')

    #提交按钮

    # submit_button_loc=(By.LINK_TEXT,'提交')
    submit_button_loc = (By.NAME, 'editsubmit')
    # submit_button_loc=(By.ID,'submit_editsubmit')

    #新版块 版块2
    # newplant_name_loc=(By.NAME,'版块2')
    newplant_name_loc = (By.XPATH, " // tbody/tr[2]/td[2]/h2/a")

    #****************************************************************
    # 搜索框
    search_input_loc = (By.XPATH, "//input[@id='scbar_txt']")

    # 搜索按钮
    search_send_loc = (By.CSS_SELECTOR, '.scbar_btn_td button')

    #*****************************************************************
    #发帖按钮
    vote_button_loc=(By.ID,'newspecial')

    #发起投票
    vote_word_loc=(By.LINK_TEXT,'发起投票')

    #投票标题
    vote_input_loc = (By.XPATH, "//input[@name='subject']")

    #投票内容
    vote_center1_loc=(By.CSS_SELECTOR,'.mbm p input ')
    vote_center2_loc = (By.CSS_SELECTOR, '.mbm p:nth-child(2) input ')
    vote_center3_loc = (By.CSS_SELECTOR, '.mbm p:nth-child(3) input')

    #发起投票
    vote_send_loc=(By.XPATH,"//button[@id='postsubmit']")

    #投票选项
    cat_radio_loc=(By.CSS_SELECTOR,'.pslt input')

    dog_radio_loc=(By.XPATH, "  // div[ @class ='pcht'] / table / tbody / tr[6] / td[2]")
    pig_radio_loc=(By.XPATH, " // tbody/tr[4]/td[2]/input")
    # // div[ @class ='pcht'] / table / tbody / tr[6] / td[2]
    # pig_radio_loc = (By.XPATH, " // div[ @class ='pcht'] / table / tbody / tr[6] / td[2]")




    #投票提交
    submit_send_loc=(By.XPATH,"//button[@id='pollsubmit']")

    cat_message_loc=(By.XPATH, "  // div[ @class ='pcht'] / table / tbody / tr[2] / td[2]")
    dog_message_loc=(By.XPATH, "  // div[ @class ='pcht'] / table / tbody / tr[4] / td[2]")
    pig_message_loc = (By.XPATH, "  // div[ @class ='pcht'] / table / tbody / tr[6] / td[2]")

    #投票的主题
    title_vote_loc=(By.ID,'thread_subject')


    def login(self,name,password):
        # 用户密码输入
        self.sendkeys(name,*self.username_input_loc)
        self.sendkeys(password, *self.userpwd_input_loc)

        # 登录
        self.click("登录",*self.login_button_loc)

    def join_plant(self):
        # 进入默认板块
        self.click("默认版块",*self.plant_word_loc)
        # self.click(*self.plant_img_loc)

    def plant_send(self,title,content):

        # 默认板块发帖
        self.sendkeys(title, *self.title_input_loc)
        self.sendkeys(content, *self.content_textarea_loc)
        self.click('发帖',*self.send_post_loc)

    def reply(self,reply_content):

        # 默认板块回帖(写回帖)
        self.sendkeys(reply_content, *self.reply_text_loc)

    def reply_send(self):

        #回帖发送
        self.click("回复",*self.reply_button_loc)

    def logout(self):

        #进入论坛，然后退出用户
        # self.click("论坛",self.forum_text_loc)

        # 用户退出
        self.click("退出",*self.exit_text_loc)


     #删除操作
    def  del_post(self):

        #选中第一个帖子
        self.click("第一个帖子",*self.post_word_loc)
        self.click("删除主题",*self.del_post_loc)
        self.click("确定",*self.sure_button_loc)


    def center(self):
        # 进入管理中心
        self.click("管理中心", *self.center_word_loc)

    def establish_plant(self,name):

        #进入论坛--添加新版块--提交
        self.click("论坛", *self.forun_word_loc)
        self.driver.switch_to.frame(0)
        self.click("添加新版块", *self.new_plant_loc)
        self.clear(*self.new_plant_name_loc)
        self.sendkeys(name, *self.new_plant_name_loc)

        self.click("提交", *self.submit_button_loc)


    def page_switch(self):
        #页面跳转

        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[1])

    def page_close(self):
        #页面关闭
        self.driver.close()

    def join_plant2(self):
        # 进入板块2
        self.click("版块2",*self.newplant_name_loc)


    def search(self,search_title):

        #搜索
        self.sendkeys(search_title,*self.search_input_loc)
        self.click("搜索",*self.search_send_loc)


    def join_vote(self):

        self.click("发贴", *self.vote_button_loc)
        self.click("发起投票", *self.vote_word_loc)

    def vote_initiation(self,title,center1,center2,center3):


        self.sendkeys(title, *self.vote_input_loc)

        self.sendkeys(center1, *self.vote_center1_loc)
        self.sendkeys(center2, *self.vote_center2_loc)
        self.sendkeys(center3, *self.vote_center3_loc)

        self.click('发起投票',*self.vote_send_loc)


    def vote(self):
        self.click("猫",*self.cat_radio_loc)
        self.click('提交',*self.submit_send_loc)

    def vote_message(self):
        print("投票结果：")
        cat_result=self.output_text(*self.cat_message_loc)
        print("猫：  ",cat_result)
        dog_result =self.output_text(*self.dog_message_loc)
        print("狗：  ",dog_result )
        pig_result =self.output_text(*self.pig_message_loc)
        print("猪：  ",pig_result )


        title=self.output_text(*self.title_vote_loc)
        print("投票主题名称：",title)










