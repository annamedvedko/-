import pytest
from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"


def test_button_add_to_basket(browser):
    browser.implicitly_wait(5)
    browser.get(link)
    button_text_elt = browser.find_element_by_class_name('btn-primary')
    button_text = button_text_elt.text

    assert  "Добавить в корзину" == button_text, f"{button_text}" 

