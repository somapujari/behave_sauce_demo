from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@then(u'click on product')
def click_on_product(context):
    context.driver.find_element(By.XPATH, "//div[normalize-space()='Sauce Labs Backpack']").click()


@then('click on add to_cart')
def click_add_to_cart(context):
    context.driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']").click()


@then('click on cart logo')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']").click()


@then(u'click on checkout')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//button[@id='checkout']").click()


@then(u'verify add_to_cart page')
def step_impl(context):
    add = context.driver.find_element(By.XPATH, "//span[@class='title']").text
    if add == 'Checkout: Your Information':
        assert True
    else:
        assert False
