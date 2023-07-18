from behave import *
from selenium.webdriver.common.by import By


@then('enter first_name "{name}" and last_name "{last_name}" and zip "{zipcode}"')
def enter_name_zip(context, name, last_name, zipcode):
    context.driver.find_element(By.XPATH, "//input[@id='first-name']").send_keys(name)
    context.driver.find_element(By.XPATH, "//input[@id='last-name']").send_keys(last_name)
    context.driver.find_element(By.XPATH, "//input[@id='postal-code']").send_keys(zipcode)


@then('click on continue')
def click_continue(context):
    context.driver.find_element(By.XPATH, "//input[@id='continue']").click()


@then('verify total')
def verify_total(context):
    ve = context.driver.find_element(By.XPATH, "//div[@class='summary_info_label summary_total_label']").text
    print(ve)
    if 'Total: $32.39' in ve:
        assert True
    else:
        assert False


@then('click on finish')
def click_finish(context):
    context.driver.find_element(By.XPATH, "//button[@id='finish']").click()


@then('verify order')
def verify_order(context):
    content = context.driver.find_element(By.XPATH, '//body').text
    if 'Thank you for your order!' in content:
        assert True
        context.driver.save_screenshot(
            r'C:\Users\Dell\PycharmProjects\behavesaucedemo\screenshots\orderconformpass.png')
    else:
        context.driver.save_screenshot(r'C:\Users\Dell\PycharmProjects\behavesaucedemo\screenshots\orderconformfail.png')
        assert False
