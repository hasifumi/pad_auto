rem @echo off

SETLOCAL

call C:\ProgramData\Anaconda3\Scripts\activate.bat

rem call conda -V

call activate test_py36

start python run_scrcpy.py

call python C:\Users\hasif\Project\pad_auto\pyautogui\test_pyautogui.py

start python C:\Users\hasif\Project\pad_auto\pad_auto.py

pause
