
===========fileupload.exe================
autoit生成的windows窗口选择，解决浏览器打开win窗口无法识别和操作的问题

传入2个参数，第一个参数是浏览器名称（chrome\firefox），其他则默认是IE；第二个参数是上传文件的完整路径。

例如：fileupload.exe chrome D:/1.txt

无需调用，使用comall框架中的file_upload_window方法即可：

例如：dr.file_upload_window(file_path, setting.driver_type)

===========test_file_upload.au3=============
AutoIt的编辑脚本，可以用au2oexe工具生成exe可以执行文件
