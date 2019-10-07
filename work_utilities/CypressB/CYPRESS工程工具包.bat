@ECHO OFF & PUSHD %~DP0
title CYPRESS工程工具包
mode con cols=40 lines=25
:menu
cls
color 2F
echo =======================================
echo ===========CYPRESS工程工具包===========
echo =======================================
echo =============ybs@20191007==============
echo =======================================
echo.
echo =======================================
echo 1.合成常规固件
echo.
echo 2.合成带bootloader的固件
echo.
echo 3.合成诊断烧录使用的application固件
echo.
echo 4.修正源代码中WAV声音文件的长度信息
echo.
echo 5.格式化src文件夹下的所有源代码
echo.
echo 6.查看帮助文档
echo.
echo 7.退出
echo =======================================
set /p user_input=请输入数字：
if %user_input% equ 1 echo 请确保源代码中boot功能宏开关改为#if 1 & %~dp0/tools/cypressutil.exe -r %~dp0/midwares/icmbasicinfo.json %~dp0../Debug/Exe/testTraveo.srec %~dp0../firmware_release/CheryT1E_HC_sw_hw_dt.srec & cd.. & start "" "firmware_release" & cd utilities
if %user_input% equ 2 echo 请确保源代码中boot功能宏开关改为#if 0 & %~dp0/tools/cypressutil.exe -b %~dp0/midwares/icmbasicinfo.json %~dp0/midwares/Bootloader.srec %~dp0../Debug/Exe/testTraveo.srec %~dp0../firmware_release/with_bootloader/CheryT1E_HC_sw_hw_withBootloader_dt.srec & cd.. & start "" "firmware_release\with_bootloader" & cd utilities
if %user_input% equ 3 echo 请确保源代码中boot功能宏开关改为#if 0 & %~dp0/tools/cypressutil.exe -a %~dp0/midwares/icmbasicinfo.json %~dp0../Debug/Exe/testTraveo.srec %~dp0../firmware_release/application_file/CheryT1E_HC_sw_hw_applicationFile_dt.srec %~dp0/midwares/FlashDriver.srec %~dp0../firmware_release/application_file/CheryT1E_HC_flashDriverFile.srec & cd.. & start "" "firmware_release\application_file" & cd utilities
if %user_input% equ 4 %~dp0/tools/cypressutil.exe -m %~dp0../src/task/Graphics/image_address.h
if %user_input% equ 5 %~dp0/tools/astyle.exe ../src/*.c ../src/*.h ../src/*.cpp ../src/*.hpp --recursive --style=ansi -s4 -S -N -L -m0 -M40 --convert-tabs -n -p -U %f
if %user_input% equ 6 start "" "%~dp0/readme.pdf"
if %user_input% equ 7 exit
pause
goto menu