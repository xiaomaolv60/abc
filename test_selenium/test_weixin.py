'''
使用cookie 登录企业微信，完成导入联系人，加上断言验证
'''
import shelve
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestDemo1():
    def setup_method(self, method):
        # 复用浏览器
        option = Options()
        option.debugger_address = "localhost:9222"
        # self.driver = webdriver.Chrome(options=option)
        self.driver = webdriver.Chrome()
        # 隐式等待
        self.driver.implicitly_wait(5)

    def teardown_method(self, method):
        self.driver.quit()

    def test_contact(self):
        # self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        self.driver.find_element(By.ID,"menu_contacts").click()

    def test_cookie(self):
        #通过复用浏览器登录的方式获取cookies
        # cookies = self.driver.get_cookies()
        # print(cookies)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        cookies = [{'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False, 'value': '1688850209891798'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False, 'value': 'sNzYigI6ix2TW_d98aNQlIg1vTA4cPKmrVq5SM-ALflFozqmUl9OHQazM0HK-XFJMYJt1AojuQ4mD8faG8NQZAiDFIU7nTw4xFeujMSaAolwmL7zoqObuvGyXIf5CCSeKQ2p6Vh9zrytMRuH0IG0Fng8VC93qY9lzKSVB051JAWmzUoSt8yR14ytFaI3qk5Miv44gMllJmZ0HgDgBh7YZaGGgSZ0JkDAdkPk955hDhILbxw94FLTC5tvPaJFFfpDoO9_IUTnWI1q-vXpo90Ysw'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False, 'value': '1688850209891798'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False, 'value': '1970325033156632'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False, 'value': 'direct'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False, 'value': 'a3347807'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False, 'value': '1wE3WExlQuZLhYVjC9r-OTbYSLVHHxyS6PdwkTcwggW0HaQQ7wlWPwWbSr96Rlzx'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False, 'value': '2094127837506169'}, {'domain': '.qq.com', 'expiry': 1598443717, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.206805239.1598355187'}, {'domain': 'work.weixin.qq.com', 'expiry': 1598386719, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/', 'secure': False, 'value': 'h9537i'}, {'domain': '.qq.com', 'expiry': 1598357367, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.qq.com', 'expiry': 1661429317, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.1060984187.1598355187'}, {'domain': '.work.weixin.qq.com', 'expiry': 1629891183, 'httpOnly': False, 'name': 'wwrtx.c_gdpr', 'path': '/', 'secure': False, 'value': '0'}, {'domain': '.work.weixin.qq.com', 'expiry': 1600949338, 'httpOnly': False, 'name': 'wwrtx.i18n_lan', 'path': '/', 'secure': False, 'value': 'zh-cn'}]

        for cookie in cookies:
            if 'expiry' in cookie.keys():
                cookie.pop('expiry')
            self.driver.add_cookie(cookie)

        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        self.driver.find_element(By.ID, "menu_contacts").click()

    def test_cookie1(self):
        db = shelve.open("mydb/logincookies")
        cookies = [
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False,
             'value': '1688850209891798'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False,
             'value': 'sNzYigI6ix2TW_d98aNQlIg1vTA4cPKmrVq5SM-ALflFozqmUl9OHQazM0HK-XFJMYJt1AojuQ4mD8faG8NQZAiDFIU7nTw4xFeujMSaAolwmL7zoqObuvGyXIf5CCSeKQ2p6Vh9zrytMRuH0IG0Fng8VC93qY9lzKSVB051JAWmzUoSt8yR14ytFaI3qk5Miv44gMllJmZ0HgDgBh7YZaGGgSZ0JkDAdkPk955hDhILbxw94FLTC5tvPaJFFfpDoO9_IUTnWI1q-vXpo90Ysw'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False,
             'value': '1688850209891798'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False,
             'value': '1970325033156632'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False,
             'value': 'direct'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False,
             'value': '1'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False,
             'value': 'a3347807'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False,
             'value': '1wE3WExlQuZLhYVjC9r-OTbYSLVHHxyS6PdwkTcwggW0HaQQ7wlWPwWbSr96Rlzx'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False,
             'value': '2094127837506169'},
            {'domain': '.qq.com', 'expiry': 1598443717, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False,
             'value': 'GA1.2.206805239.1598355187'},
            {'domain': 'work.weixin.qq.com', 'expiry': 1598386719, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/',
             'secure': False, 'value': 'h9537i'},
            {'domain': '.qq.com', 'expiry': 1598357367, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False,
             'value': '1'},
            {'domain': '.qq.com', 'expiry': 1661429317, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False,
             'value': 'GA1.2.1060984187.1598355187'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1629891183, 'httpOnly': False, 'name': 'wwrtx.c_gdpr',
             'path': '/', 'secure': False, 'value': '0'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1600949338, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
             'path': '/', 'secure': False, 'value': 'zh-cn'}]

        db['cookie'] = cookies
        cookies = db['cookie']
        db.close()

        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        for cookie in cookies:
            if 'expiry' in cookie.keys():
                cookie.pop('expiry')
            self.driver.add_cookie(cookie)

        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        self.driver.find_element(By.ID, "menu_contacts").click()

    def test_importcontact(self):
        db = shelve.open("mydb/logincookies")
        cookies = db['cookie']
        db.close()
        # 需要先访问需要访问的页面
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")

        for cookie in cookies:
            if 'expiry' in cookie.keys():
                cookie.pop('expiry')
            self.driver.add_cookie(cookie)

        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        self.driver.find_element(By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(2)").click()
        #上传文件使用send_keys()方法，将需要上传的文件的绝对路径传入
        sleep(2)
        self.driver.find_element(By.ID, "js_upload_file_input").send_keys("C:/Users/14917/Desktop/python_practise/test_selenium/test_selenium_file.xlsx")
        myfilename = self.driver.find_element(By.ID, "upload_file_name").text
        assert "test_selenium_file.xlsx" == myfilename

