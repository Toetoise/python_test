from selenium import webdriver
from test_loginclass import Login
from Upload_file import Upload
# from PIL import Image
import time
import unittest


class TestVisitMsykByEdge(unittest.TestCase):
    def setUp(self):
        driver_url = r"H:\Python38\msedgedriver.exe"
        self.driver = webdriver.Edge(executable_path=driver_url)
        self.driver.implicitly_wait(10)
        url = "https://www.msyk.cn/"
        self.driver.get(url)
        self.driver.maximize_window()
        Login(self.driver).login("nls_1", "Msyk_741")

    def test_Sucaiku(self):
        self.driver.find_element_by_id("material").click()
        ppt_path = open("C:\\Users\\Tortoise\\Desktop\\ppt_path.txt", encoding='utf-8')
        filepaths = ppt_path.readline()
        while filepaths:
            print(filepaths, end='')
            filepath = filepaths.rstrip('\n')    # strip函数去除行末readline函数输出的行末的换行符
        #     快速上传
        #     self.driver.find_element_by_id("all-ppt-upload").click()
        #     self.driver.find_element_by_id("ppt-upload-local").click()
        #     time.sleep(1)
        #     print(filepath)
        #     Upload(self.driver).upload_file(filepath)
        #     time.sleep(1)
        #     优质上传
            self.driver.find_element_by_id("all-ppt-upload").click()
            self.driver.find_element_by_id("ppt-hight-upload").click()
            time.sleep(1)
            print(filepath)
            Upload(self.driver).upload_file(filepath)
            time.sleep(1)
            filepaths = f.readline()
        print("上传完成")
        f.close()

    def tearDownClass(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
