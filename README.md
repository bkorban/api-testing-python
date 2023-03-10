<h1 align="center">PyRestAPITest</h1>

<p align="center">  
This application is built to do REST API testing using python scripts along with the use of Pytest module as our testing framework.
<br><br>
API being tested: <a href='https://restful-booker.herokuapp.com/apidoc/' target="_blank">restful-booker</a>
</p>

<p align="center">
  <a href="https://opensource.org/licenses/Apache-2.0"><img alt="License" src="https://img.shields.io/badge/License-Apache%202.0-blue.svg"/></a>
</p>

## Languages, libraries and tools used

* __[Python](https://www.python.org/downloads/)__
* __[Pytest](https://docs.pytest.org/en/6.2.x/getting-started.html)__
* __[Requests](https://docs.python-requests.org/en/master/)__
* __[JsonPath](https://pypi.org/project/jsonpath/)__
* __[Pycharm](https://www.jetbrains.com/pycharm/download/)__
* __[Allure](https://pypi.org/project/allure-pytest/)__

Above Features are used to make code simple, generic, understandable, clean and easily maintainable for future development.
Above features inlcude as well Allure reporting for test reporting

## Installation

Install the dependencies and start the testing.

 __Install Pytest__:
```sh
pip install -U pytest
```
 __Install Requests__:
```sh
pip install requests
```

 __Install Json Path__:
```sh
pip install jsonpath
```

<br />
 __Install Allure with Pytest__:
 ```sh
 pip install allure-pytest
 ```

 __Next download the latest allure package zip from [allure-framework GitHub repo](https://github.com/allure-framework/allure2/releases)__
  __Unzip the downloaded zip file__
  __Copyt the path till bin__
  __Add it to the path environment variable__
  __Open the terminal and rin__
  ```sh
  allure --version
  ```

<br />

## Automated tests

__To run a test, you can simply write the following command on Terminal__:
```sh
pytest
```

__To run and get details of all the executed test, you can simply write the following command on Terminal__:
```sh
pytest -rA
```

__To run and generate full HTML details report of all the executed test, you can simply write the following commands on Terminal__:

__But first install [Pytest-HTML](https://pypi.org/project/pytest-html/) by writing the following command on Terminal__
```sh
pip install pytest-html
```
__Then write the following command on Terminal__
```sh
pytest --html==YOUR_REPORT_FILE_NAME.html
```

__To see the reports, open the Project window, and then right-click then click on refresh then right-click on __StationReport.html__ to open the file on the default browser.__


<br />
<br />
__To run and generate Allure reports__

  __In the project directory generate a folder to save allure reports; use the command below to automatically generate this__
  ```sh
  allure generate
  ```

  __This will create a folder named _allure-report_ in your project directory__

  __Now you can run your tests with pytest runner by specifying the directory path to save your allure report__
  ```sh
  pytest --alluredir=allure-report/
  ```

  __Once test execution completes, all the test results would get stored in allure-report directory__

  __The allure report can be viewed in the browser with the command__
  ```sh
  allure serve allure-report/
  ```

  __Link to [allure pytest](https://pypi.org/project/allure-pytest/)__

# Prerequisites
* __Python__
* __Any IDE__

# Built With

* __[Python](https://www.python.org/downloads/)__ - Language used to build the application.
* __[Pycharm](https://www.jetbrains.com/pycharm/download/)__ - The IDE for writing Automation Test Scripts
