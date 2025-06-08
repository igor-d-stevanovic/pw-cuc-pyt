Feature: Login

  Scenario: Unsuccessful login with invalid credentials
    Given the user is on the login page
    When the user logs in with username "invalid_user" and password "wrong_password"
    Then an error message "Epic sadface: Username and password do not match any user in this service" should be displayed

  Scenario: Unsuccessful login with empty username
    Given the user is on the login page
    When the user logs in with username "<empty>" and password "some_password"
    Then an error message "Epic sadface: Username is required" should be displayed

  Scenario: Unsuccessful login with empty password
    Given the user is on the login page
    When the user logs in with username "standard_user" and password "<empty>"
    Then an error message "Epic sadface: Password is required" should be displayed