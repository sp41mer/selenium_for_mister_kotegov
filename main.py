# -*- coding: utf-8 -*-
import seismograph
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys


suite = seismograph.Suite(__name__)


@suite.register
def delete_my_own_post(case):
    # --- Авторизация ---
    # Берем бразур
    browser = webdriver.Chrome('/Users/sp41mer/PycharmProjects/parcer/chromedriver')
    url = 'http://ok.ru'
    # Идем по ссылке
    browser.get(url)
    # Ждем пока загрузится хоть какая-нибудь картинка
    WebDriverWait(browser, 10).until(lambda browser: browser.find_element_by_css_selector('img'))
    # Получаем необходимые для авторизации инпуты
    login_input = browser.find_element_by_xpath("//input[@id='field_email']")
    login_input.send_keys('89260665086')
    password_input = browser.find_element_by_xpath("//input[@id='field_password']")
    password_input.send_keys('Gfhjkmlkzjr1488')
    login_button = browser.find_element_by_xpath(
        "//div[@id='loginContentBlock']//div[@class='form-actions']//input[@type='submit']")
    #Логинимся
    login_button.click()
    # Ждем пока загрузится хоть какая-нибудь картинка
    WebDriverWait(browser, 10).until(lambda browser: browser.find_element_by_css_selector('img'))

    # --- Выполнение теста --- #
    status_post = browser.find_element_by_xpath("//div[@class = 'posting-form_itx_w']")
    status_post.click()
    WebDriverWait(browser, 10).until(lambda browser: browser.find_element_by_xpath("//div[@class='form-actions']//input[@type='submit']"))
    status_field = browser.find_element_by_id('posting_form_text_field')
    status_field.send_keys('My first status')
    #как сделать без этого не придумал, какой бы элемент я не ждал, все равно кликаю в пустоту
    time.sleep(3)
    submit_button = browser.find_element_by_xpath("//div[@class='form-actions']//input[@type='submit']")
    submit_button.click()
    # Ждем пока загрузится хоть какая-нибудь картинка
    WebDriverWait(browser, 10).until(lambda browser: browser.find_element_by_css_selector('img'))
    # как сделать без этого не придумал, какой бы элемент я не ждал, все равно кликаю в пустоту
    time.sleep(3)
    #Переходим в свою ленту
    profile_link = browser.find_element_by_xpath("//a[@class = 'mctc_nameLink']")
    profile_link.click()
    # Ждем пока загрузится хоть какая-нибудь картинка
    WebDriverWait(browser, 10).until(lambda browser: browser.find_element_by_css_selector('img'))
    ActionChains(browser).move_to_element(browser.find_element_by_xpath("//div[@class = 'feed h-mod']")).perform()
    case.assertion.equal(1, 1)


@suite.register
def my_second_test(case):
    case.assertion.equal(1, 1)


@suite.register
def my_third_test(case):
    case.assertion.equal(1, 1)


if __name__ == '__main__':
    seismograph.main()
