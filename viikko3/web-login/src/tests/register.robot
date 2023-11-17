*** Settings ***
Resource            resource.robot
Resource            login_resource.robot

Suite Setup         Open And Configure Browser
Suite Teardown      Close Browser
Test Setup          Create User And Go To Register Page


*** Test Cases ***
Register With Valid Username And Password
    Set Username    pete
    Set Password    pete1234
    Set Password Confirmation    pete1234
    Submit Register
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username    p
    Set Password    pete1234
    Set Password Confirmation    pete1234
    Submit Register
    Register Should Fail With Message    Invalid username

Register With Valid Username And Invalid Password
    Set Username    pete
    Set Password    petepetepete
    Set Password Confirmation    petepetepete
    Submit Register
    Register Should Fail With Message    Invalid password

Register With Nonmatching Password And Password Confirmation
    Set Username    pete
    Set Password    pete1234
    Set Password Confirmation    pete
    Submit Register
    Register Should Fail With Message    Password and password confirmation do not match

Login After Successful Registration
    Set Username    pete
    Set Password    pete1234
    Set Password Confirmation    pete1234
    Submit Register
    Register Should Succeed
    Go To Login Page
    Set Username    pete
    Set Password    pete1234
    Submit Credentials
    Login Should Succeed

Login After Failed Registration
    Set Username    p
    Set Password    pete1234
    Set Password Confirmation    pete1234
    Submit Register
    Register Should Fail With Message    Invalid username
    Go To Login Page
    Set Username    p
    Set Password    pete1234
    Submit Credentials
    Login Should Fail With Message    Invalid username or password


*** Keywords ***
Submit Register
    Click Button    Register

Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]    ${message}
    Register Page Should Be Open
    Page Should Contain    ${message}

Set Password Confirmation
    [Arguments]    ${password_confirmation}
    Input Password    password_confirmation    ${password_confirmation}

Create User And Go To Register Page
    Create User    kalle    kalle123
    Go To Register Page
    Register Page Should Be Open
