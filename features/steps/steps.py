# -*- coding: cp866 -*-

from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium import webdriver

#��஥� ������� ��࠭���. ��।���� � ����⢥ ��㬥�� ���� ��࠭���.
@given('website "{url}"')
def step(context, url):
#������� ��ப�, ��� �믮������ ��� � ��㣮� ��㧥�
    context.browser = webdriver.Firefox()
    #context.browser.maximize_window()
    context.browser.get("http://ya.ru")

#������ ������ �� ������ "����"
@Then("push button with text '{text}'")
def step(context, text):
    WebDriverWait(context.browser, 120).until(
        EC.element_to_be_clickable((By.XPATH, '//button'))
    )
    context.browser.find_element_by_xpath('//button').click()

#�஢�ਬ, �� �� �� ��࠭�� � १���⠬� ���᪠, ���� ������� �᪮�� ⥪��
@Then("page include text '{text}'")
def step(context, text):
    WebDriverWait(context.browser, 120).until(
        EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "%s")]' % text))
    )
    assert context.browser.find_element_by_xpath('//*[contains(text(), "%s")]' % text)
    context.browser.quit()

