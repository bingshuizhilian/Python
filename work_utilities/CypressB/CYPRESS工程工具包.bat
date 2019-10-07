@ECHO OFF & PUSHD %~DP0
title CYPRESS���̹��߰�
mode con cols=40 lines=25
:menu
cls
color 2F
echo =======================================
echo ===========CYPRESS���̹��߰�===========
echo =======================================
echo =============ybs@20191007==============
echo =======================================
echo.
echo =======================================
echo 1.�ϳɳ���̼�
echo.
echo 2.�ϳɴ�bootloader�Ĺ̼�
echo.
echo 3.�ϳ������¼ʹ�õ�application�̼�
echo.
echo 4.����Դ������WAV�����ļ��ĳ�����Ϣ
echo.
echo 5.��ʽ��src�ļ����µ�����Դ����
echo.
echo 6.�鿴�����ĵ�
echo.
echo 7.�˳�
echo =======================================
set /p user_input=���������֣�
if %user_input% equ 1 echo ��ȷ��Դ������boot���ܺ꿪�ظ�Ϊ#if 1 & %~dp0/tools/cypressutil.exe -r %~dp0/midwares/icmbasicinfo.json %~dp0../Debug/Exe/testTraveo.srec %~dp0../firmware_release/CheryT1E_HC_sw_hw_dt.srec & cd.. & start "" "firmware_release" & cd utilities
if %user_input% equ 2 echo ��ȷ��Դ������boot���ܺ꿪�ظ�Ϊ#if 0 & %~dp0/tools/cypressutil.exe -b %~dp0/midwares/icmbasicinfo.json %~dp0/midwares/Bootloader.srec %~dp0../Debug/Exe/testTraveo.srec %~dp0../firmware_release/with_bootloader/CheryT1E_HC_sw_hw_withBootloader_dt.srec & cd.. & start "" "firmware_release\with_bootloader" & cd utilities
if %user_input% equ 3 echo ��ȷ��Դ������boot���ܺ꿪�ظ�Ϊ#if 0 & %~dp0/tools/cypressutil.exe -a %~dp0/midwares/icmbasicinfo.json %~dp0../Debug/Exe/testTraveo.srec %~dp0../firmware_release/application_file/CheryT1E_HC_sw_hw_applicationFile_dt.srec %~dp0/midwares/FlashDriver.srec %~dp0../firmware_release/application_file/CheryT1E_HC_flashDriverFile.srec & cd.. & start "" "firmware_release\application_file" & cd utilities
if %user_input% equ 4 %~dp0/tools/cypressutil.exe -m %~dp0../src/task/Graphics/image_address.h
if %user_input% equ 5 %~dp0/tools/astyle.exe ../src/*.c ../src/*.h ../src/*.cpp ../src/*.hpp --recursive --style=ansi -s4 -S -N -L -m0 -M40 --convert-tabs -n -p -U %f
if %user_input% equ 6 start "" "%~dp0/readme.pdf"
if %user_input% equ 7 exit
pause
goto menu