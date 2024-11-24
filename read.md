To run the tests in parallel:
python -m pytest -n=4 --html=Reports\report\chrome.html --browser chrome

To run the tests sequentially:
python -m pytest --html=Reports\report\chrome.html --browser chrome

To view allure report, hit the following command in your project directory path:
allure serve allureReports




