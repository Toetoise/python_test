from selenium import webdriver
import unittest
import time
from test_loginclass import Login
from PIL import Image
import re


class ImageCompare(object):
    def make_regalur_image(self, img, size=(256, 256)):
        # 将图片尺寸强制重置为指定的size大小
        # 然后再将其转换成RGB值
        return img.resize(size).convert('RGB')

    def split_image(self, img, part_size=(64, 64)):
        # 将图片按给定大小切分
        w, h = img.size
        pw, ph = part_size
        assert w % pw == h % ph == 0
        return [img.crop((i, j, i+pw, j+ph)).copy()for i in range(0, w, pw) for j in range(0, h, ph)]

    def hist_similar(self, lh, rh):
        # 统计切分后每部分图片的相似度频率曲线
        assert len(lh) == len(rh)
        return sum(1-(0 if L == r else float(abs(1-r))/max(L, r))for L, r in zip(lh, rh))/len(lh)

    def calc_similar(self, li, ri):
        # 计算两张图片的相似度
        return sum(self.hist_similar(l.histogram(), r.histogram())
                   for l, r in zip(self.split_image(li), self.split_image(ri)))/16.0

    def calc_similar_by_path(self, lf, rf):
        li, ri = self.make_regalur_image(Image.open(lf)), \
                 self.make_regalur_image(Image.open(rf))
        return self.calc_similar(li, ri)


class TestDemo(unittest.TestCase):

    def setUp(self):
        driver_url = r"H:\Python38\msedgedriver.exe"
        self.driver = webdriver.Edge(executable_path=driver_url)
        self.driver.implicitly_wait(10)
        url = "https://www.msyk.cn"
        self.driver.get(url)
        self.driver.maximize_window()
        time.sleep(3)
        Login(self.driver).login("nls_1", "Msyk_741")
        self.IC = ImageCompare()
        time.sleep(3)

    def test_imagecomparison(self):
        # 截取第一次访问搜狗首页的图片,并保存本地
        self.driver.save_screenshot("D:\\Chrome_download\\picture\\msyk1.png")
        self.driver.find_element_by_xpath("//a[@data-toggle='dropdown']").click()
        self.driver.find_element_by_xpath("//a[@href='/logout']").click()
        time.sleep(3)
        Login(self.driver).login("nls_1", "Msyk_741")
        time.sleep(3)
        # 截取的二次访问搜狗首页的图片,并保存本地
        self.driver.save_screenshot("D:\\Chrome_download\\picture\\msyk2.png")
        # 打印两张截图比对后的相似度,100表示完全匹配
        print(self.IC.calc_similar_by_path('D:\\Chrome_download\\picture\\msyk1.png', 'D:\\Chrome_download\\picture\\msyk2.png')*100)

    def test_demo(self):
        line = "全部学生（10）"
        b = re.sub(r'）.*', "", re.sub(r'.*（', "", line))
        e = re.sub(r'\d+', "", line)
        c = re.compile(r'\d+').findall(line)
        print(b)
        print(c)
        print(e)


if __name__ == '__main__':
    unittest.main()