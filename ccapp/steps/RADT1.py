# -*- coding: cp866 -*-

from behave import *
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

#Откроем главную страницу. Передадим в качестве аргумента адрес страницы.
@given('website "{url}"')
def step(context, url):
#Измените строку, для выполнения теста в другом браузере
    context.browser = webdriver.Firefox()
    #context.browser.maximize_window()
    context.browser.get("http://ccapp-test.marpasoft.com/")

#Теперь нажмем на кнопку "Найти"
@Then("enter login and the password")
def step(context):
    WebDriverWait(context.browser, 120).until(EC.element_to_be_clickable((By.XPATH, '//div[@id="tools-nav"]/ul[1]/li[1]/a')))
    context.browser.find_element_by_xpath('//div[@id="tools-nav"]/ul[1]/li[1]/a').click()
    WebDriverWait(context.browser, 120).until(EC.element_to_be_clickable((By.XPATH, '//input[@id="id_username"]')))
    context.browser.find_element_by_xpath('//input[@id="id_username"]').click()
    username = context.browser.find_element_by_id('id_username')
    username.send_keys("zipppt@gmail.com")
    password = context.browser.find_element_by_id('id_password')
    password.send_keys("zipppt2016")
    log = context.browser.find_element_by_id('submit_button')
    log.click()

#Проверим, что мы на странице с результатами поиска, есть некоторый искомый текст
@Then("enter PersonaInformation form Radt1")
def step(context):
    WebDriverWait(context.browser, 120).until(EC.presence_of_element_located((By.XPATH, '//div[@class="row menu"]/div[@class="col-sm-3"][2]/ul[3]/li[2]/a')))
    context.browser.find_element_by_xpath('//div[@class="row menu"]/div[@class="col-sm-3"][2]/ul[3]/li[2]/a').click()
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
@Then("doSubmit")
def step(context):
    element = context.browser.find_element_by_xpath("//input[@id='id_agree']")
    element.click()
    element = context.browser.find_element_by_xpath("//a[@id='submit_button']/span")
    element.click()
    element = context.browser.find_element_by_xpath("//input[@id='id_agree']")
    element.click()
    element = context.browser.find_element_by_xpath("//a[@id='submit_button']/span")
    element.click()
@Then("doRegHis")
def step(context):
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
@Then("doApply")
def step(context):
    element = context.browser.find_element_by_xpath("//a[@id='submit_button']/span")
    element.click()
    element = context.browser.find_element_by_xpath("//input[@id='id_type_0']")
    element.click()
    element = context.browser.find_element_by_xpath("//a[@id='submit_button']/span")
    element.click()
@Then("doClean")
def step(context):
    context.browser.get("http://ccapp-test.marpasoft.com/admin/profiles/profile/148208/")
    element = context.browser.find_element_by_xpath("//input[@id='id_application_set-0-DELETE']")
    element.click()
    element = context.browser.find_element_by_xpath("//input[@class='default']")
    element.click()
