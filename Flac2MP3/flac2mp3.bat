@ECHO OFF

FOR %%f IN (*.flac) DO (
    ffmpeg -i "%%f" -ab 320k -map_metadata 0 -id3v2_version 3 "%%~nf.mp3"
    del "%%f"
)

PAUSE