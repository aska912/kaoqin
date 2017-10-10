
@set BUILD_FILE_NAME=main
@set PYINSTALLER_ROOT="D:\Program Files\Python27\Scripts"
@set UPX_ROOT="D:\Program Files\upx391w"


%PYINSTALLER_ROOT%\pyinstaller.exe --noconfirm --onefile --clean %BUILD_FILE_NAME%.py

@Pause
