@echo off
setlocal

:INIT
echo 1. English
echo 2. Czech
echo 3. Danish
echo 4. German
echo 5. Spanish
echo 6. Finnish
echo 7. French
echo 8. Italian
echo 9. Japanese
echo 10. Korean
echo 11. Dutch
echo 12. Norwegian
echo 13. Polish
echo 14. Portuguese
echo 15. Russian
echo 16. Swedish
echo 17. Chinese
echo.
set /P M=Select Language: 
echo.

IF "%M%"=="1" set LCID=en_US& goto INSTALL
IF "%M%"=="2" set LCID=cs_CZ& goto INSTALL
IF "%M%"=="3" set LCID=da_DK& goto INSTALL
IF "%M%"=="4" set LCID=de_DE& goto INSTALL
IF "%M%"=="5" set LCID=es_ES& goto INSTALL
IF "%M%"=="6" set LCID=fi_FI& goto INSTALL
IF "%M%"=="7" set LCID=fr_FR& goto INSTALL
IF "%M%"=="8" set LCID=it_IT& goto INSTALL
IF "%M%"=="9" set LCID=ja_JP& goto INSTALL
IF "%M%"=="10" set LCID=ko_KR& goto INSTALL
IF "%M%"=="11" set LCID=nl_NL& goto INSTALL
IF "%M%"=="12" set LCID=no_NO& goto INSTALL
IF "%M%"=="13" set LCID=pl_PL& goto INSTALL
IF "%M%"=="14" set LCID=pt_BR& goto INSTALL
IF "%M%"=="15" set LCID=ru_RU& goto INSTALL
IF "%M%"=="16" set LCID=sv_SE& goto INSTALL
IF "%M%"=="17" set LCID=zh_TW& goto INSTALL
cls
goto INIT

:INSTALL
SET gdir=%~dp0
cd "%gdir%__Installer"
echo Base game
Touchup.exe install -locale %LCID% -installPath "%gdir%" -autologging
echo DLC's
for /D %%i in ("%gdir%__Installer\DLC\*") do (
cd "%%i\__Installer"
echo %%i"
Touchup.exe pdlcinstall -locale %LCID% -pdlcInstallPath "%gdir%" -autologging
)
echo Done
pause
