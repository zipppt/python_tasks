# -*- coding: cp866 -*-

from behave import *
#  import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#  import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
#  from selenium.webdriver.common.keys import Keys

LOGIN_LINK_LOCATOR = '//div[@id="tools-nav"]/ul[1]/li[1]/a'


@given('website "{url}"')
def step_impl(context, url):
    context.browser = webdriver.Firefox()
    #  context.browser.maximize_window()
    context.browser.get(url)


@when('enter login "{login}" and password "{password}"')
def step_impl(context, login, password):
    WebDriverWait(context.browser, 120).until(EC.element_to_be_clickable((By.XPATH, LOGIN_LINK_LOCATOR)))
    context.browser.find_element_by_xpath(LOGIN_LINK_LOCATOR).click()
    username_field = context.browser.find_element_by_id('id_username')
    username_field.send_keys(login)
    password_field = context.browser.find_element_by_id('id_password')
    password_field.send_keys(password)
    log = context.browser.find_element_by_id('submit_button')
    log.click()


@then('is logged in as "{username}"')
def step_impl(context, username):
    element = context.browser.find_element_by_xpath("//div[@id='tools-nav']/ul[1]/li[1]/a/strong")
    assert element.text == username

@when("enter RADT-I")
def step_impl(context):
    WebDriverWait(context.browser, 120).until(EC.presence_of_element_located((By.XPATH, '//div[@class="row menu"]/div[@class="col-sm-3"][2]/ul[3]/li[2]/a')))
    context.browser.find_element_by_xpath('//div[@class="row menu"]/div[@class="col-sm-3"][2]/ul[3]/li[2]/a').click()

@then('is RADT-I in as "{name}"')
def step_impl(context, name):
    element = context.browser.find_element_by_xpath("//div[@class='flatblock-content']/h2[2]")
    assert element.text == name

@when("enter PersonaInformation form Radt1")
def step_impl(context):

    element = context.browser.find_element_by_xpath("//div[@class='wrapit']/h4[1]/a")
    element.click()
    element = context.browser.find_element_by_xpath("//div[@id='div_id_personal_info-first_name']/input")
    element.clear()
    element.send_keys("Andrew")
    element = context.browser.find_element_by_xpath("//div[@id='div_id_personal_info-last_name']/input")
    element.clear()
    element.send_keys("Trofimchuk")
    element = context.browser.find_element_by_xpath("//div[@id='div_id_personal_info-middle_name']/input")
    element.clear()
    element.send_keys("Nikola")
    element = context.browser.find_element_by_id('id_personal_info-date_of_birth_month')
    select = Select(element)
    select.select_by_visible_text("July")
    element = context.browser.find_element_by_id('id_personal_info-date_of_birth_day')
    select = Select(element)
    select.select_by_visible_text("6")
    element = context.browser.find_element_by_id('id_personal_info-date_of_birth_year')
    select = Select(element)
    select.select_by_visible_text("1978")
    element = context.browser.find_element_by_xpath("//div[@id='div_id_personal_info-ssn']/input")
    element.clear()
    element.send_keys("2222")
    element = context.browser.find_element_by_xpath("//div[@id='div_id_personal_info-street']/input")
    element.clear()
    element.send_keys("Golosiivska St.")
    element = context.browser.find_element_by_id('id_personal_info-state')
    select = Select(element)
    select.select_by_visible_text("California")
    element = context.browser.find_element_by_xpath("//div[@id='div_id_personal_info-city']/input")
    element.clear()
    element.send_keys("Sacramento")
    element = context.browser.find_element_by_xpath("//div[@id='div_id_personal_info-zip']/input")
    element.clear()
    element.send_keys("11111")
    element = context.browser.find_element_by_xpath("//div[@id='div_id_personal_info-phone']/input")
    element.clear()
    element.send_keys("111-111-1111")
    element = context.browser.find_element_by_xpath("//div[@id='div_id_personal_info-email']/input")
    element.clear()
    element.send_keys("zipppt@gmail.com")
    element = context.browser.find_element_by_xpath("//div[@class='form_block']/a[1]/span")
    element.click()


@when("Submit")
def step_impl(context):
    element = context.browser.find_element_by_xpath("//input[@id='id_agree']")
    element.click()
    element = context.browser.find_element_by_xpath("//a[@id='submit_button']/span")
    element.click()
    element = context.browser.find_element_by_xpath("//input[@id='id_agree']")
    element.click()
    element = context.browser.find_element_by_xpath("//a[@id='submit_button']/span")
    element.click()


@when("RegHis")
def step_impl(context):
    element = context.browser.find_element_by_xpath("//div[@id='div_id_registered']/input")
    element.click()
    element = context.browser.find_element_by_id('id_initial_date_month')
    select = Select(element)
    select.select_by_visible_text("July")
    element = context.browser.find_element_by_id('id_initial_date_day')
    select = Select(element)
    select.select_by_visible_text("6")
    element = context.browser.find_element_by_id('id_initial_date_year')
    select = Select(element)
    select.select_by_visible_text("2015")
    element = context.browser.find_element_by_xpath("//input[@id='id_current_organization_0']")
    element.click()
    element = context.browser.find_element_by_xpath("//input[@id='id_certified']")
    element.click()
    element = context.browser.find_element_by_xpath("//input[@id='id_have_ever_revoked_0']")
    element.click()


@when("Apply")
def step_impl(context):
    element = context.browser.find_element_by_xpath("//a[@id='submit_button']/span")
    element.click()
    element = context.browser.find_element_by_xpath("//input[@id='id_type_0']")
    element.click()
    element = context.browser.find_element_by_xpath("//a[@id='submit_button']/span")
    element.click()


@then("Clean")
def step_impl(context):
    context.browser.get("http://ccapp-test.marpasoft.com/admin/profiles/profile/148208/")
    element = context.browser.find_element_by_xpath("//input[@id='id_application_set-0-DELETE']")
    element.click()
    element = context.browser.find_element_by_xpath("//input[@class='default']")
    element.click()

