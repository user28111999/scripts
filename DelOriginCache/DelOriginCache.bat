del /f /q "%USERPROFILE%\AppData\local\Origin\*.*" 
FOR /D %%p IN ("%USERPROFILE%\AppData\local\Origin\*.*") DO rmdir "%%p" /s /q
del /f /q "%USERPROFILE%\AppData\roaming\Origin\*.*" 
FOR /D %%p IN ("%USERPROFILE%\AppData\roaming\Origin\*.*") DO rmdir "%%p" /s /q
del /f /q "%ALLUSERSPROFILE%\Origin\*.*"
FOR /D %%p IN ("%ALLUSERSPROFILE%\Origin\*.*") DO rmdir "%%p" /s /q      
