自动化测试框架搭建说明：

==========================================
安装设置:
1、修改testl.bak.pth文件为testl.pth，打开并修改里面的目录为testl.py所在目录
   copy新的testl.pth文件到python的Lib\site-packages下
   例如我的是：E:\python27\Lib\site-packages

==========================================
1、目录结构说明（配置好了python环境，安装好了selenium；设置了系统环境变量PYTHONPATH到frame_code当前目录；）

|frame_code                                                        --根目录
            |----core                                             --扩展功能库
                          |----databaseDriver.py                  --数据库操作类
                          |----logger.py                          --日志记录类
            |----setting                                             --测试配置目录（对象库，测试数据，测试配置）
                          |----carrefour                             --测试配置目录
                                           |----el.py                        --测试配置目录--对象库文件（elements）
                                           |----setting.py              --测试配置目录--测试配置文件
                                           |----test_data.py          --测试配置目录--测试数据文件
                                           |----__init__.py                  --python包说明文件（空文件）
                          |----example                                    --其他项目配置目录(名字尽量规范)
                                           |----elements_list.py
                                           |----setting.py
                                           |----test_data.py
                                           |----__init__.py                     --python包说明文件（空文件）
                          |----__init__.py
            |----tests                                                              --测试脚本目录
                          |----carrefour                                            测试脚本目录
                                           |----test_all.py                         --脚本执行主文件
                                           |----test-reports                    --xml报告存储目录（用于Jenkins，脚本自动生成）
                                           |----login                                       登录模块--脚本目录
                                                            |----testLogin.py               登录模块--登录（login）测试脚本
                                                            |----testLogout.py              --登录模块--登出测试脚本
                                                            |----__init__.py                             --python包说明文件（空文件，不可删）
                                           |----common                                       --通用模块测试用例
                                                            |----common.py                   --后台通用测试脚本
                                                            |----shop_common.py          --前台PC商城，通用测试脚本
                          |----example_tests
                                           |----test_all.py
                                           |----module
                                                            |----testModule.py
                                                            |----__init__.py                --python包说明文件（空文件）
            |----tools                                                                         --第三方工具目录
                          |----fileupload.exe                                          --web上传选择windows窗口的exe（autoit3生成）
                          |----test_file_upload.au3                                 --autoit3脚本
                          |----README.md                                              --tools目录说明
            |----testl.py                      --主框架文件（继承于pyse.py，用于扩展；增加了api接口测试的calss）
            |----config.py                      --主配置文件
            |----README.md                      --框架说明文档
            |----testl.bak.pth                 --copy到python安装根目录，用于命令行调试脚本使用


==========================================
2、测试脚本编写
   A、在测试模块（例如order_management）目录下，复制一个新的testModule.py，起名为你的脚本名（例如订单新增：order_add.py）
   B、修改import中，引用data、el、setting的包名；（例如松鼠squirrels的修改example的引用为from setting.squirrels import el）
   C、修改脚本中的class名称为要测试的名称(order_add)
   D、新增def测试方法（一个测试方法对应一个case），方法名要求以“test_”开头，例如：test_order_add_01、test_order_add_02
   E、在每个def下，增加注释，说明case测试内容，并编写具体的测试操作步骤

==========================================
3、脚本调试

==========================================
 ****************移 动 端*****************
==========================================
|frame_code                                                        --根目录
            |----setting                                             --测试配置目录（对象库，测试数据，测试配置）
                          |----zx_test                             ----测试配置目录
                                           |----el.py                        ----测试配置目录--对象库文件（elements）
                                           |----setting.py               ----测试配置目录--测试配置文件
                                           |----test_data.py          ----测试配置目录--测试数据文件
                                           |----__init__.py                  --python包说明文件（空文件）

                          |----__init__.py                                   --python包说明文件（空文件）

            |----tests                                                      --测试脚本目录
                          |----zx_test                                          --测试脚本目录
                                           |----mobile_test                         --测试脚本目录
                                                               |----test.py                      --脚本执行主文件
                                                               |----__init__.py                  --python包说明文件（空文件）
            |----testlMobile.py                      --移动端主框架文件（appium的封装）
            |----config.py                      --主配置文件
            |----README.md                      --框架说明文档
==========================================



==========================================
增加json的key必须验证和key的type验证,使用方法:

安装jsonschema
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple jsonschema

步骤:
1,目前只试用于接口测试返回的restful的json格式验证;
2,在testlapi类初始化时,可以选择填写参数[json_schema_file],只要填写了json_schema_file就会验证json格式的有效性
3,json_schema_file是一个json文件的完整路径,使用python的jsonschema库,需要事先编写json文件

jsonschema的验证文件编写方法:

[示例]
被验证的接口返回的json
{
  "name": "qiguojie",
  "age": 37,
  "sex": 1,
  "title": "manager",
  "members":
    [{
      "name": "heyanping",
      "age": 27
    },
      {
        "name": "ningxiaohua",
        "age": 25
      }
    ]

}

验证json编写
{
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "age": {"type": "number"},
        "sex": {"type": "number"},
        "title": {"type": "string"},
        "members": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "name": "string",
                    "age": "number"
                    },
                "required": ["name","age"]
                }
            }
    },
    "required": ["sex", "name", "age", "title", "members"]
}

验证方法说明:
[type]验证数据类型,可以验证string\number\array\object,如果数据类型不符合,则抛出异常:
jsonschema.exceptions.ValidationError: u'xxxxxx' is not of type 'number'

[properties]验证当前对象的子节点

[required]验证当前节点的数据项key必须存在,值为数组,如果数组中有值不存在,则抛出异常:
jsonschema.exceptions.ValidationError: 'xxxxx' is a required property