#!/usr/bin/env python
# -*- coding: utf-8 -*-

from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium import webdriver

#Откроем главную страницу. Передадим в качестве аргумента адрес страницы.
@given('website "{url}"')
def step(context, url):
#Измените строку, для выполнения теста в другом браузере
    context.browser = webdriver.Firefox()
    context.browser.maximize_window()
    context.browser.get("http://ya.ru")

#Теперь нажмем на кнопку "Найти"
@When("push button with text '{text}'")
def step(context, text):
    WebDriverWait(context.browser, 120).until(
        EC.element_to_be_clickable((By.XPATH, '//button'))
    )
    context.browser.find_element_by_xpath('//button').click()

#Проверим, что мы на странице с результатами поиска, есть некоторый искомый текст
@Then("page include text '{text}'")
def step(context, text):
    WebDriverWait(context.browser, 120).until(
        EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "%s")]' % text))
    )
    assert context.browser.find_element_by_xpath('//*[contains(text(), "%s")]' % text)
    context.browser.quit()


@given('website "ya\.ru"')
def step_impl(context):
    """
    :type context behave.runner.Context
    """
    pass


@then("push button with text 'Найти'")
def step_impl(context):
    """
    :type context behave.runner.Context
    """
    pass


@then("page include text 'Задан пустой поисковый запрос'")
def step_impl(context):
    """
    :type context behave.runner.Context
    """
    pass


@when("push button with text 'Найти'")
def step_impl(context):
    """
    :type context behave.runner.Context
    """
    pass