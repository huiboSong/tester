Dim $Window_name

If $CmdLine[1] == "chrome" Then
   $Window_name = "打开"
ElseIf $CmdLine[1] == "firefox" Then
   $Window_name = "文件上传"
Else
   $Window_name = "选择要加载的文件" ;IE
EndIf

;ControlFocus("title","text",controlID) Edit1=Edit instance 1
ControlFocus($Window_name, "","Edit1")


; Wait 10 seconds for the Upload window to appear
  WinWait("[CLASS:#32770]","",10)


; Set the File name text on the Edit field

  ControlSetText($Window_name, "", "Edit1", $CmdLine[2])

  Sleep(500)

; Click on the Open button

  ControlClick($Window_name, "","Button1");