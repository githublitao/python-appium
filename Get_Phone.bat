

REM 将当运行时间点做为日志文件名

SET logfilename=Phone_Info


REM 创建当天日期目录及测试APP日志保存目录

IF NOT EXIST %~dp0   md %~dp0

SET logdir="%~dp0\%appEnName%%appversion%"

IF NOT EXIST %logdir% (

    ECHO.[ Exec ] 创建目录：%appEnName%%appversion%

    md %logdir%

)

REM 获得手机信息，显示并保存

adb shell cat /system/build.prop>phone.info

FOR /F "tokens=1,2 delims==" %%a in (phone.info) do (

    IF %%a == ro.build.version.release SET androidOS=%%b

    IF %%a == ro.product.model SET model=%%b

    IF %%a == ro.product.brand SET brand=%%b

)

del /a/f/q phone.info

ECHO.[ INFO ] 读取Phone信息

ECHO.         手机品牌: %brand%

ECHO.         手机型号: %model%

ECHO.         系统版本: %androidOS%

ECHO.[Phone]>"%logdir%\%logfilename%.ini"

ECHO.Phone_Brand = %brand%>>"%logdir%\%logfilename%.ini"

ECHO.Phone_Model = %model%>>"%logdir%\%logfilename%.ini"

ECHO.System_Version = %androidOS%>>"%logdir%\%logfilename%.ini"
