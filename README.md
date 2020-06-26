<img src="https://raw.githubusercontent.com/vincenzo-gasparo/robotframework-testrail-reporter/master/rftr.png" alt="robotframework-testrail-reporter" class="img-fluid">

# robotframework-testrail-reporter

robotframework-testrail-reporter is a Python library used to publish robotframework test executions to TestRail.
It parses the output.xml file and search tests tagged with a specific testcase id, then it retrieves testcases run id from  TestRailtest suite run id.

### Installation

robotframework-testrail-reporter requires python3+, lxml, and testrail installed and  to run. (and robotframework to execute tests)

```sh
$ pip3 install robotframework-testrail-reporter
$ rf-tr-reporter -f output.xml -t test-case-id -u https://xxx.testrail.io/ -e my@email.com -k pwd_or_apikey -r runid
```

### Methods

| Method | Arguments | README |
| ------ | ------ | ------ |
| find_tests_tagged_by | path, tag | This method parses the output xml generated by robotframework defined by path and finds all test nodes with starting tag tag.<br/>Returns a list of dictionaries with following keys: ['rf_test_name', 'test_id , 'status_id, 'comment', 'elapsed']  **rf_test_name** is the robotframework test name <br/> **test_id** is the numeric value contained in tag<br/>**status_id** is the conversion of test status to testrail standards<br/>**comment** is the test status message<br/>**elapsed** is the test execution time in s, (min 1 second)<br/>Args:<br/>**path** is the path of robotframework xml output file<br/>**tag** is the tag to be found in robotframework tests, it must contain a numeric part which specifies testcase run id, example: test_case_id=123 |
| get_comment | status | This method returns the test execution status message which is the text attribute of test **status** node in output xml, if no text is found it retuns an empty string. Comment maximum length is defined by comment_size_limit variable.<br/>Args:<br/>**status** is the status node found via xpath selector with lxml |
| get_elapsed | status | This method calculates the elapsed test execution time which is endtime - starttime in test **status** node of output XML. Returns a string of test execution seconds. Example: '5s'<br/>Args:<br/>**status** is the status node found via xpath selector with lxml |
| publish_results | api, run_id, results | This method publishes robotframework results to a testrail run<br/>Args:<br/>**api** is an instance of testrail.client.API already logged in<br/>**run_id** is the id of the run to update <br/>**results** is a list of dictionaries that contains test results |
| replace_caseid_with_testid | api, results, run_id | This method parses all results generated by find_tests_tagged_by method and replace all testcases ids with specific testruns ids in test_id key of each result<br/>Args:<br/>**api** is an instance of testrail.client.API already logged in<br/>**results** is a list of dictionaries that contains test results<br/>**run_id** is the id of the run to update |

