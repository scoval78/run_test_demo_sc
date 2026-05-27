from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import pytest

@pytest.fixture()
def browser():
    chrome_browser = webdriver.Chrome()
    chrome_browser.implicitly_wait(10)
    return chrome_browser

def test_home_page(browser):
    browser.get('https://www.qa-practice.com/')
    assert browser.title == 'QA Practice'
    assert browser.find_element(By.ID, 'id_text_string')

def test_buttons_page(browser):
    browser.get('https://www.qa-practice.com/elements/dutton/simple')
    assert browser.find_element(By.ID, 'submit-id-submit')


def test_alert_page(browser):
    browser.get('https://www.qa-practice.com/elements/alert/alert')
    browser.find_element(By.LINK_TEXT, 'Click').click()
    assert Alert(browser).text == 'I am an alert!'