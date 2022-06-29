import time
import math
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

links = ["https://stepik.org/lesson/236895/step/1",
"https://stepik.org/lesson/236896/step/1",
"https://stepik.org/lesson/236897/step/1",
"https://stepik.org/lesson/236898/step/1",
"https://stepik.org/lesson/236899/step/1",
"https://stepik.org/lesson/236903/step/1",
"https://stepik.org/lesson/236904/step/1",
"https://stepik.org/lesson/236905/step/1"]

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(20)
    yield browser
    print("\nquit browser..")
    browser.quit()



@pytest.mark.parametrize('link', links)
def test_guest_should_see_correct_feedback(browser, link):
    browser.get(link)
    answer_field = browser.find_element(By.TAG_NAME, "textarea")
    answer = str(math.log(int(time.time())))
    answer_field.send_keys(answer)
    button = browser.find_element(By.CSS_SELECTOR, ".submit-submission")
    button.click()
    feedback = browser.find_element(By.CLASS_NAME, "smart-hints__hint").text

    assert feedback == "Correct!", feedback
