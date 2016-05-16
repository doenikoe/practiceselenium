from behave import *

@given('I open check out form')
def step_impl(context):
    context.browser.get("http://www.practiceselenium.com/check-out.html")

@step('I hit place order button without entered any information')
def step_impl(context):
    context.browser.find_element_by_xpath("//button[contains(text(), 'Place Order')]").click()

@then('I unable to submit the form and I still at the same page')
def step_impl(context):
    assert "Check Out" in context.browser.title