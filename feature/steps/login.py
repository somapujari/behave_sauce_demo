from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given('launch chrome browser')
def launch_chrome(context):
    context.driver = webdriver.Chrome()


@when('open url "https://www.saucedemo.com/"')
def url_open(context):
    context.driver.get('https://www.saucedemo.com/')


@when(u'wait for some period')
def wait(context):
    context.driver.implicitly_wait(20)


@when('enter username "{user}" and password  "{pwd}"')
def enter_user_password(context, user, pwd):
    context.driver.find_element(By.ID, 'user-name').send_keys(user)
    context.driver.find_element(By.ID, 'password').send_keys(pwd)


@when('click on login button')
def click_login(context):
    context.driver.find_element(By.ID, 'login-button').click()


@then('user verify title')
def verify(context):
    te = context.driver.find_element(By.XPATH, "//span[@class='title']").text
    if te == 'Products':
        assert True
        context.driver.save_screenshot(r'C:\Users\Dell\PycharmProjects\behavesaucedemo\screenshots\loginpass.png')
    else:
        context.driver.save_screenshot(r'C:\Users\Dell\PycharmProjects\behavesaucedemo\screenshots\loginfail.png')
        assert False


@then('close browser')
def close_browser(context):
    context.driver.close()
