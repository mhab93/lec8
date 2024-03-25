from selenium import webdriver
import pytest

def test_title():
    # setup
    driver = webdriver.Chrome()

    # test
    driver.get('https://www.google.com')
    assert driver.title == 'Google'
    print('Passed Title:', driver.title)
    
    # teardown
    driver.quit()

#example 1
    
from selenium import webdriver
import pytest
import random

def test_random():
    assert 1 == random.randint(1,2)

def test_title():
    # setup
    driver = webdriver.Chrome()

    # test
    driver.get('https://www.google.com')
    assert driver.title == 'Google'

    # teardown
    driver.quit()