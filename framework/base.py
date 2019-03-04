# coding=utf-8
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Discuz_lx1.framework.logger import Logger
import time
import os.path

logger = Logger(logger="BasePage").getlog()

class BasePage():

    def __init__(self, driver):
        self.driver = driver


    def open_url(self, url):
        self.driver.get(url)     #打开浏览器

    def quit(self):
        self.driver.quit()       #关闭浏览器

    def close(self):
        try:
            self.driver.close()
            logger.info('Closing and quit the browser.')
        except Exception as e:
            logger.error("Failed to quit the browser with %s" % e)    #关闭当前页面

    def find_element(self, *loc):            #找页面元素
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)
            logger.info('找到页面元素-->', loc)

        except:
            logger.error('%s页面中未找到页面元素%s' % (self, loc))

    def get_windows_img(self):              #失败的截图保存在screenshots文件夹中

        file_path = os.path.dirname(os.path.abspath(',')) + '/screenshots/'
        rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        screen_name = file_path + rq + '.png'
        try:
            self.driver.get_screenshot_as_file(screen_name)
            logger.info('Had take screenshot and save to folder :/screenshots ')
        except Exception as e:
            self.get_windows_img()
            logger.error('Failed to take screenshot! %s' % e)

    def sendkeys(self, text, *loc):     #键盘输入发送
        el = self.find_element(*loc)
        el.clear()
        try:
            el.send_keys(text)
            logger.info('输入内容' + text)
        except Exception as e:
            logger.error('Failed to type in input box with %s' % e)
            self.get_windows_img()

    def clear(self, *loc):       #清除
        el = self.find_element(*loc)
        try:
            el.clear()
            logger.info('清空所有内容')
        except Exception as e:
            logger.error('Failed to type in input box with %s' % e)

    def click(self,title="", *loc):       #点击
        el = self.find_element(*loc)
        try:
            el.click()
            logger.info('点击:'+title)
        except Exception as e:
            logger.error('Failed to type in input box with %s' % e)


    def output_text(self,*loc):
        el = self.find_element(*loc)
        try:
            return el.text
            logger.info('文本内容:',el.text )
        except Exception as e:
            logger.error('Failed to type in input box with %s' % e)


