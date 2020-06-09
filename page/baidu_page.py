from poium import Page, PageElements,PageElement


class BaiduPage(Page):
    '''
    'css': By.CSS_SELECTOR,
    'id_': By.ID,
    'name': By.NAME,
    'xpath': By.XPATH,
    'link_text': By.LINK_TEXT,
    'partial_link_text': By.PARTIAL_LINK_TEXT,
    'tag': By.TAG_NAME,
    'class_name': By.CLASS_NAME,
    '''
    search_input = PageElement(id_="kw", describe="搜索框")
    search_button = PageElement(id_="su", describe="搜索按钮")
    #settings = PageElement(link_text="设置", describe="设置下拉框",timeout=10)
    settings = PageElement(id_="s-usersetting-top", describe="设置下拉框", timeout=10)
    search_setting = PageElement(link_text="搜索设置", describe="搜索设置选项")
    #save_setting = PageElement(css=".prefpanelgo", describe="保存设置")
    save_setting = PageElement(xpath="//a[text()='保存设置']", describe="保存设置")

    # 定位一组元素
    search_result = PageElements(xpath="//div/h3/a", describe="搜索结果")


