from behave import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

use_step_matcher("re")

@given('I open contact page')
def step_impl(context):
    context.browser.get("http://www.practiceselenium.com/let-s-talk-tea.html")

@step('I fill the form with values')
def step_impl(context):
    context.browser.find_element_by_name("name").send_keys("Doni")
    context.browser.find_element_by_name("email").send_keys("test@example.com")
    context.browser.find_element_by_name("subject").send_keys("tes")
    context.browser.find_element_by_name("message").send_keys("message")

@step('I hit submit button')
def step_impl(context):
    context.browser.find_element_by_class_name('form-submit').click()

@then('Thank you message appear')
def step_impl(context):
    try:
        element = WebDriverWait(context.browser, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "form-message"))
        )
        print(element.get_attribute("innerHTML"))
        assert "Thank you sending us your information. We will get back to you with your Chai :)" in element.get_attribute("innerHTML")
    except(TimeoutException, StaleElementReferenceException):
        raise Exception('Unable to sumbit form')