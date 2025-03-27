cd "%~dp0"
call .\.venv\Scripts\activate.bat
python -m pytest .\tests -n auto --alluredir .\results
allure serve .\results
pause