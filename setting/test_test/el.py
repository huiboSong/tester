# coding=utf-8

# xpath
#首页
womai_index_topbtn_login_a = "//*[@id='top_login_span']/li[2]/a"
womai_index_topusername = "//*[@id='top_login_span']/li[1]"
womai_index_topbtn_register_a = "//*[@id='top_login_span']/li[3]/a"

#登录页面
login_username = "//*[@id='cartLoginId']"
login_pwd = "//*[@id='cartPassword']"
login_btn = "//*[@id='login_submit_btn_real']"
login_success = "//*[@id='top_login_span']/li[2]"

#首页登录
login_topusername =" //*[@id='top_login_span']/li[2]/a"


#注册页面
register_MailorPhone = "//*[@id='Email']"
register_loginid = "//*[@id='loginId']"
register_pwd = "//*[@id='password']"
register_pwd2 = "//*[@id='password2']"
register_validateCode = "//*[@id='validateCode']"
register_registerbtn = "//*[@id='submitBtn']"

#我买网首页
index_product = "//*[@id='_gatrack_product_floorproduct_1f_1tabtext3']"
minicart_delete = "//*[@id='_gatrack_delete_mincart_1_delete2']"
minicart = "//*[@id='cartlink']"

minicart_productnum = "//*[@id='smallcart']/div[1]/span[1]/i"

# 选择城市
city_link = "//*[@id='sitename']"
city_sh = "//*[@id='sitecont']/div[1]/div[2]/span[2]/a"
city_gz = "//*[@id='sitecont']/div[1]/div[2]/span[3]/a"


# 商品详情页
# 加入购物车按钮
product_addtocard = "//*[@id='buyBtn']"
# 加入购物车弹层的关闭操作
addtocard_confirm = "//*[@id='showIncludeCart']/div[1]"
# 加入购物车弹层去结算按钮
addtocard_tocard = "//*[@id='showIncludeCart']/div[4]/div[3]/div/a"
# 判断加入购物车是否成功
addtocard_success = "//*[@id='showIncludeCart']/div[4]/div[1]"

# 团购详情页
# 团购加入购物车
tuan_addtocard = "//*[@id='button-buy']"
# 删除商品
tuan_del = "//*[@id='loadshowcart1']/div[2]/div[1]/div[1]/div[3]"
# 确定删除
tuan_del_confirm = "//*[@id='j-alert-confirm999999']"

# 购物车页面
#购物车页面右上角请登录
cart_righttop_login = "//*[@id='top_login_span']/li[1]/a"
#购物车商品数量展示
cart_pronum_text = "//*[@id='amount2_0_565206']"
#购物车页面商品加号
cart_product_add = "//*[@id='p_add2_0']"
#购物车页面商品减号
cart_product_del = "//*[@id='p_dec2_0']"
#购物车页面商品数量输入框
cart_product_num_input = "//*[@id='amount2_0_565206']"
#购物车页面右侧删除单个商品
cart_product_rdel = "//*[@id='loadshowcart1']/div[1]/div[3]/div[1]/div[6]/div/a"
#购物车页面右侧删除单个商品
cart_product_udel = "//*[@id='delSelCartItems1']"
#购物车页面去结算按钮
cart_goto_checkout_btn = "//*[@id='cofcocheck']"
#常温购物车全选复选框
cart_normal_checkall = "//*[@id='all1']"
#常温购物车全选复选框
cart_normalandfresh_checkall = "//*[@id='all_two1']"
#常温购物车页面商品右侧 收藏
cart_favoritesright_a1 = "//*[@id='loadshowcart1']/div[1]/div[3]/div[1]/div[6]/a"
#常温购物车页面商品右侧 收藏提示成功
cart_favoritemes_a1 = "//*[@id='j-alert-popup999999']/div[2]/div[1]/p"
#常温购物车页面商品右侧 收藏提示成功
cart_favoritecon_btn = "//*[@id='j-alert-confirm999999']"
#底部常温购物车页面商品 收藏提示成功
cart_favoriteunder_al = "//*[@id='loadshowcart1']/div[3]/div[1]/div[1]/div[2]/a"

# 卡券页面
# 卡券页面下一步
cardpage_nextstep_btn = "//*[@id='nextStep']"

# 购物车结算
shoppingcard_nextstep_btn = "//*[@id='cofcocheck']"
# 结算中心
checkout_submit_order_btn = "//*[@id='submitOrder']"
# 修改收货地址
update_address = "//*[@id='consignee_show']"
# 增加收货地址
add_address = "//*[@id='qitaaddress']/label"

# 修改我买卡支付金额
update_cardpay = "//*[@id='paymode_show']"
# 取消充抵
cancel_wmpay = "//*[@id='cancelWmCardPayBtn']"
# 输入我买卡金额
input_wmpay = "//*[@id='wmcardCurrentPay303']"
# 输入我买卡密码
input_wmpay_pwd = "//*[@id='payPassword']"



# 提交订单成功页面
ordersucess_page_order_link = "//*[@id='ordernumber']"
ordersucess_page_ordernum = "//*[@id='ordernumber']"

ordersucess_page_msg_bj = "/html/body/div[3]/div/div[1]/div[2]/div[1]"
ordersucess_page_msg_sh = "/html/body/div[4]/div/div[1]/div[2]/div[1]"
orderid = "//*[@id='ordernumber']/strong"

# 订单详情页
#订单详情页取消按钮
orderdetail_cancel_btn = "//*[@id='canCancel']"
orderdetail_cancel_notbuy = "//*[@id='j-big-alert-popup999999'/div[2]/div/div/ul/li[1]"
orderdetail_cancel_notbuy_ok = "//*[@id='j-big-alert-confirm999999']"
orderdetail_cannel_msg = "//*[@id='j-alert-popup999999']/div[2]/div[1]/p"
orderdetail_cannel_cofirm = "//*[@id='j-alert-confirm999999']"

orderdetail_tuancannel_msg = "//*[@id='j-big-alert-popup999999']/div[2]/div/div/ul/li[1]"

# 产地直送
womai_index_seller = "//*[@id='_gatrack_event_topnav_6']"
womai_search_text = "//*[@id='topKeywords']"
womai_search_button = "//*[@id='searchform']/div/div[1]/div[2]/button"
womai_ftest_commodity = "//*[@id='_gatrack_productlist_listpic_607814']/a/img"
womai_sellercheck = "//*[@id='sellercheck']"

# 选择翼支付
checkout_update_paymode = "//*[@id='paymode_show']"
checkout_update_p2mid14125 = "//*[@id='onLinePay14125']/label"
checkout_savaPaymode = "//*[@id='paymode_curlayer']/div[9]/span"
order_mctips_title = "/html/body/div[3]/div/div[1]/div[2]/div[1]"
order_cancel = "//*[@id='j-big-alert-popup999999']/div[2]"

