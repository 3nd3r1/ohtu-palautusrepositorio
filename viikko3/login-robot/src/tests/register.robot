*** Settings ***
Resource        resource.robot

Task Setup      Create User And Input Register Command


*** Test Cases ***
Register With Valid Username And Password
    Input Credentials    pete    pete1234
    Output Should Contain    New user registered

Register With Already Taken Username And Valid Password
    Input Credentials    kalle    pete1234
    Output Should Contain    User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials    k    pete1234
    Output Should Contain    Invalid username

Register With Enough Long But Invalid Username And Valid Password
    Input Credentials    pete1    pete1234
    Output Should Contain    Invalid username

Register With Valid Username And Too Short Password
    Input Credentials    pete    pete
    Output Should Contain    Invalid password

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials    pete    petepetepete
    Output Should Contain    Invalid password


*** Keywords ***
Create User And Input Register Command
    Create User    kalle    kalle123
    Input Register Command
