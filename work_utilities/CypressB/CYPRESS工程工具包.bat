@ECHO OFF & PUSHD %~DP0
title CYPRESS���̹��߰�
mode con cols=40 lines=27
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
echo 4.�ϳ������¼ʹ�õ�flash driver�ļ�
echo.
echo 5.����Դ������WAV�����ļ��ĳ�����Ϣ
echo.
echo 6.��ʽ��src�ļ����µ�����Դ����
echo.
echo 7.�鿴�����ĵ�
echo.
echo 8.�˳�
echo =======================================
set /p user_input=���������֣�
if %user_input% equ 1 echo ��ȷ��Դ������boot���ܺ꿪�ظ�Ϊ#if 1 & %~dp0/tools/cypressutil.exe -r %~dp0/midwares/icmbasicinfo.json %~dp0../Debug/Exe/testTraveo.srec %~dp0../firmware_release/CheryT1E_HC_sw_hw_dt.srec & cd.. & start "" "firmware_release" & cd utilities
if %user_input% equ 2 echo ��ȷ��Դ������boot���ܺ꿪�ظ�Ϊ#if 0 & %~dp0/tools/cypressutil.exe -b %~dp0/midwares/icmbasicinfo.json %~dp0/midwares/Bootloader.srec %~dp0../Debug/Exe/testTraveo.srec %~dp0../firmware_release/with_bootloader/CheryT1E_HC_sw_hw_withBootloader_dt.srec & cd.. & start "" "firmware_release\with_bootloader" & cd utilities
if %user_input% equ 3 echo ��ȷ��Դ������boot���ܺ꿪�ظ�Ϊ#if 0 & %~dp0/tools/cypressutil.exe -a %~dp0/midwares/icmbasicinfo.json %~dp0../Debug/Exe/testTraveo.srec %~dp0../firmware_release/application_file/CheryT1E_HC_sw_hw_applicationFile_dt.srec %~dp0/midwares/FlashDriver.srec %~dp0../firmware_release/application_file/CheryT1E_HC_flashDriverFile.srec & cd.. & start "" "firmware_release\application_file" & cd utilities
if %user_input% equ 4 %~dp0/tools/cypressutil.exe -f %~dp0/midwares/Bootloader.srec %~dp0/midwares/FlashDriver.srec & start "" "midwares"
if %user_input% equ 5 %~dp0/tools/cypressutil.exe -m %~dp0../src/task/Graphics/image_address.h
if %user_input% equ 6 %~dp0/tools/astyle.exe ../src/*.c ../src/*.h ../src/*.cpp ../src/*.hpp --recursive --style=ansi -s4 -S -N -L -m0 -M40 --convert-tabs -n -p -U %f
if %user_input% equ 7 start "" "%~dp0/readme.pdf"
if %user_input% equ 8 exit
pause
goto menu