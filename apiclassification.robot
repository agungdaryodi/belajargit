*** Settings ***
Library             DataDriver          file=apitesting_file.xlsx   sheet_name=Sheet1
Library             APILibrary.py
Test Template       API Excel Input Cases

*** Test Cases ***
Dummy Case
    Comment         NULL

*** Keywords ***
API Excel Input Cases
    [Arguments]     ${file_name}	${expected_spoof}
    Run API for Functional Test         ${file_name}
    API Should Run Successfully
    API Output Should Be                ${expected_spoof}
    Sleep  1s
