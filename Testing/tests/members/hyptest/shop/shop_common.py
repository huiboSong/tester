# coding=utf-8

import sys
import comall

from setting.hyptest import el
from setting.hyptest import setting



reload(sys)
sys.setdefaultencoding("utf-8")


def shop_area_select(dr):
    """商城-首页选择地区
    dr: comall实例(webdriver)对象
    tc：unittest testCase对象
    """
    #dr = comall.Comall(setting.driver_type)
    # 打开商城登录页面
    dr.open(setting.login_page_index)
    # 等待页面加载完成
    # dr.until_page_load()
    # 点击区域定位选择框
    dr.until("xpath", el.index_select_address_dropdown_show)
    dr.click("xpath", el.index_select_address_dropdown_show)
    # 移动到测试2级城市，让下面的3级地区显示出来
    dr.move_to_element("xpath", el.index_select_address_select_city)
    # 获得要选择的3级地区名称
    area_name_click = dr.get_text("xpath", el.index_select_address_select_subsite)
    # 点击选择3级地区
    dr.click("xpath", el.index_select_address_select_subsite)
    # 点击【开始购物】按钮
    dr.click("xpath", el.index_select_address_submit)
    # 验证选择地区成功
    #area_name_show = dr.get_text("xpath", el.index_area_selected_dt)
    #tc.assertEqual(area_name_click, area_name_show, "shop_common:shop_area_select选择地区失败")


#if __name__ == "__main__":
   #shop_area_select()
