"""
@author:  虫师
@data: 2019-10-17
@function pytest 参数使用
"""
import sys
import json
from time import sleep
import pytest
from os.path import dirname, abspath

base_path = dirname(dirname(abspath(__file__)))
file_path=base_path + "/test_dir/data/data_file.json"
sys.path.insert(0, base_path)
from page.baidu_page import BaiduPage


def get_testdata(file_path):
    testdata = []
    with(open(file_path, "r")) as f:
        dict_data = json.loads(f.read())
        for i in dict_data:
            testdata.append(tuple(i.values()))
    return testdata

class TestCase:
    @pytest.mark.parametrize(
        "name, search_key",
        [("1", "Selenium"),
         ("2", "pytest文档"),
         ("3", "pytest-html"),
         ],
        ids=["case1", "case2", "case3"]
    )
    def test_baidu_search1(self,name, search_key, browser, base_url):
        '''
        测试parametrize参数化
        :param name:
        :param search_key:
        :param browser:
        :param base_url:
        :return:
        '''
        page = BaiduPage(browser)
        page.get(base_url)
        page.search_input = search_key
        page.search_button.click()
        sleep(2)
        assert browser.title == search_key + "_百度搜索"

    # @classmethod
    # def get_testdata(cls,file_path):
    #     testdata = []
    #     with(open(file_path, "r")) as f:
    #         dict_data = json.loads(f.read())
    #         for i in dict_data:
    #             testdata.append(tuple(i.values()))
    #     return testdata

    @pytest.mark.parametrize(
        "name, search_key",
        get_testdata(file_path)
    )
    def test_baidu_search2(self,name, search_key, browser, base_url):
        '''
        :param name:
        :param search_key:
        :param browser:
        :param base_url:
        :return:
        '''

        page = BaiduPage(browser)
        page.get(base_url)
        page.search_input = search_key
        page.search_button.click()
        sleep(2)
        assert browser.title == search_key + "_百度搜索"
