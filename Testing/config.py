# coding=utf-8
import os

error = True  # 调试信息打开或关闭
debug = True  # 调试信息打开或关闭
info = True  # 执行信息开关（主要用于log打印；）

base_dir = os.path.dirname(os.path.realpath(__file__)) + os.path.sep

# 日志文件保存地址
log_file_dir = base_dir + "logs"

# 截图图片存储地址
img_shot_dir = base_dir + 'imgs'


# 超时设置
element_find_wait = 15  # until 查找控件元素超时时间time_out（秒）
element_display_wait = 5  # until_display 等待控件元素显示超时时间time_out（秒）