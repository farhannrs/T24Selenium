import time
from behave import *
from Helper import seleniumHelper


@given('user navigates to url')
def step_impl(context):
    seleniumHelper.navigate_to_url(context)


@when('user enters "{value}" in "{field}" field')
@when('user enters "{value}" in "{field}"')
def step_impl(context, value, field):
    seleniumHelper.enter_text(context, value, field)


@when('user enters automatic limit_ID in "{field}" to create a new limit')
def step_impl(context, field):
    seleniumHelper.dynamic_limit(context, field)


@when('user clears the auto-populated data from "{field}"')
def step_impl(context, field):
    seleniumHelper.clear_text(context, field)


@when('"{field}" field should be editable')
def step_impl(context, field):
    seleniumHelper.field_editable(context, field)


@then('"{field}" field should be editable')
def step_impl(context, field):
    seleniumHelper.field_editable(context, field)


@when('"{field}" field should not be editable')
def step_impl(context, field):
    seleniumHelper.field_notEditable(context, field)


@then('"{field}" field should not be editable')
def step_impl(context, field):
    seleniumHelper.field_notEditable(context, field)


@when('user clicks on "{button}"')
def step_impl(context, button):
    seleniumHelper.click(context, button)


@when('user clicks on {value} in "{button}" radio button')
def step_impl(context, value, button):
    seleniumHelper.click_radio_button_dynamic(context, value, button)


@when('user clicks on "{value}" from dropdown')
def step_impl(context, value):
    seleniumHelper.click_dropdown_value_dynamic(context, value)


@when("user waits for new window to appear")
def step_impl(context):
    seleniumHelper.switch_window(context)


@when("user goes back to previous screen")
@when("user goes back to previous window")
def step_impl(context):
    seleniumHelper.switch_window_back(context)


@when('user selects by value "{value}" from "{dropdown}"')
def step_impl(context, value, dropdown):
    seleniumHelper.select_dropdown_by_value(context, value, dropdown)


@when('user selects "{value}" from "{dropdown}"')
def step_impl(context, value, dropdown):
    seleniumHelper.select_dropdown(context, value, dropdown)


@given('user is on Temenos Home Screen')
@given('user is present on Home screen')
def step_impl(context):
    seleniumHelper.verify_homepage(context, "Home_HomepageImage")


@then('error message should appear in "{field}"')
@then('completion message should appear in "{field}"')
def step_impl(context, field):
    seleniumHelper.verify_message(context, field)


@given('wait "{secs}"')
@when('wait "{secs}"')
@then('wait "{secs}"')
def step_impl(context, secs):
    time.sleep(int(secs))


@given('wait')
@when('wait')
@then('wait')
def step_impl(context):
    time.sleep(5)


@then('record should appear on screen')
def step_impl(context):
    seleniumHelper.verify_enquiry(context, "Enquiry_ToggleButton")


@then('"{keyword}" should appear on screen')
def step_impl(context, keyword):
    seleniumHelper.verify_enquiry(context, keyword)


@then('"{value}" should be present at position "{position}" in "{keyword}"')
def step_impl(context, value, position, keyword):
    seleniumHelper.verify_account_statement(context, value, position, keyword)


@then('"{value}" should be present in "{keyword}"')
def step_impl(context, value, keyword):
    seleniumHelper.verify_field_value(context, value, keyword)


@then('record should be updated successfully')
def step_impl(context):
    seleniumHelper.verify_enquiry(context, "Action_UpdateGreenFlag")


@when('user clicks on "{button}" tab')
def step_impl(context, button):
    seleniumHelper.click_tab(context, button)


@when('user clicks on "{value}" alert')
def step_impl(context, value):
    seleniumHelper.click_alert(context, value)


@then('"{key}" is saved in context dict from "{field}"')
@when('"{key}" is saved in context dict from "{field}"')
def step_impl(context, key, field):
    seleniumHelper.save_value_in_context(context, key, field)


@when('aaaa "{txt}"')
def step_impl(context, txt):
    seleniumHelper.aaaaaa(context, txt)


@then('"{keyword}" should not be null')
@then('"{keyword}" should be auto populated')
def step_impl(context, keyword):
    seleniumHelper.verify_field_not_empty(context, keyword)


@then('"{key}" is saved in data dict from "{field}"')
@when('"{key}" is saved in data dict from "{field}"')
def step_impl(context, key, field):
    seleniumHelper.save_value_in_data(context, key, field)


@then('write values to file against "{account_status}"')
def step_impl(context, account_status):
    seleniumHelper.write_to_data_gen_file(context, account_status)


@then('error "{error}" for "{field_name}" should appear on screen')
def step_impl(context, error, field_name):
    seleniumHelper.check_mandatory_validation(context, error, field_name)


@when('User scrolls down to the bottom of the page')
def step_user_scrolls_down(context):
    seleniumHelper.step_user_scrolls_down(context)


@when('user updates the value of "{field}"')
def step_impl(context, field):
    seleniumHelper.update_field_value(context, field)