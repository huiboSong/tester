# coding=utf-8

# 运行时设置
driver_type = "chrome"  # chrome or firefox/ff or ie or opera or phantomjs
run_os = "windows"  # windows or mac or linux
element_find_wait = 15  # 查找控件元素超时时间time_out（秒）


# 测试环境
desired_caps={
    "platformName":"Android",
    # 设备操作系统版本
    "platformVersion":"8.0",
    #设备号
    "deviceName":"PBV0216624004346",
    "appPackage":"com.womai",
    "appActivity":"com.womai.activity.MainActivity"
}
desired={
    "platformName":"Android",
    # 设备操作系统版本
    "platformVersion":"8.0",
    #设备号
    "deviceName":"PBV0216624004346",
    "appPackage":"com.bingofresh.binbox",
    "appActivity":"com.bingofresh.binbox.view.activity.SplashActivity"
}
# 存放购物车ID，cartid
newcart_id = {}
# 加价购商品ID
Add_skuid = {}
# 旧接口下单需要
params = {}



