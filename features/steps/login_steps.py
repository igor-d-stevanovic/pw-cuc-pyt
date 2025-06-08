from behave import given, when, then
from pages.login_page import LoginPage

@given("the user is on the login page")
def step_open_login_page(context):
    context.login_page = LoginPage(context.page)
    context.login_page.open()

@when('the user logs in with username "{username}" and password "{password}"')
def step_login(context, username, password):
    # Convert <empty> to empty string
    if username == "<empty>":
        username = ""
    if password == "<empty>":
        password = ""
    context.login_page.login(username, password)

@then('an error message "{message}" should be displayed')
def step_verify_error_message(context, message):
    context.login_page.verify_error_message(message)