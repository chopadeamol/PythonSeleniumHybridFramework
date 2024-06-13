@echo off
call venv\scripts\activate
python -m pytest --html=Reports\report\chrome.html --browser chrome
pause
