rem @echo off

SETLOCAL

call C:\ProgramData\Anaconda3\Scripts\activate.bat

rem call conda -V

call activate test_py27

start python run_scrcpy.py

call python C:\Users\hasif\Project\pad_auto\pyautogui\test_pyautogui.py


pause
