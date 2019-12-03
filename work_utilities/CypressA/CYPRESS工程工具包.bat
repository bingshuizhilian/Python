@ECHO OFF & PUSHD %~DP0
title CYPRESS工程工具包
mode con cols=40 lines=28
:menu
cls
color 2F
echo =======================================
echo ===========CYPRESS工程工具包===========
echo =======================================
echo =============ybs@20190919==============
echo =======================================
echo.
echo =======================================
echo 1.合成常规固件
echo.
echo 2.合成带bootloader的固件
echo.
echo 3.合成诊断烧录使用的application固件
echo.
echo 4.合成诊断烧录使用的flash driver固件
echo.
echo 5.修正源代码中WAV声音文件的长度信息
echo.
echo 6.格式化src文件夹下的所有源代码
echo.
echo 7.查看帮助文档
echo.
echo 8.退出
echo =======================================
set /p user_input=请输入数字：
if %user_input% equ 1 echo 请确保源代码中boot功能宏开关改为#if 1 & python ./scripts/DoReleaseFirmware.py & cd.. & start "" "firmware_release" & cd utilities
if %user_input% equ 2 echo 请确保源代码中boot功能宏开关改为#if 0 & python ./scripts/GenerateFirmwareWithBootloader.py & cd.. & start "" "firmware_release\with_bootloader" & cd utilities
if %user_input% equ 3 echo 请确保源代码中boot功能宏开关改为#if 0 & python ./scripts/GenerateApplicationFirmware.py & cd.. & start "" "firmware_release\application_file" & cd utilities
if %user_input% equ 4 echo 请确保midwares文件夹中已经含有Bootloader.srec文件 & python ./scripts/GenerateFlashDriverFile.py & start "" "midwares"
if %user_input% equ 5 python ./scripts/ModifyWAVlength.py
if %user_input% equ 6 %~dp0/scripts/astyle.exe ../src/*.c ../src/*.h ../src/*.cpp ../src/*.hpp --recursive --style=ansi -s4 -S -N -L -m0 -M40 --convert-tabs -n -p -U %f
if %user_input% equ 7 start "" "%~dp0/readme.pdf"
if %user_input% equ 8 exit
pause
goto menu