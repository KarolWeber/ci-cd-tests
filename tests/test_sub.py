import allure
import pytest
import requests

BASE_URL = "http://localhost:5000"

@allure.suite("Calculator tests")
@allure.feature("Calculator")
@allure.sub_suite("Sub tests")
@pytest.mark.parametrize("title,a,b,expected", [
    ("Positive", 7, 5, "2"),
    ("Negative", -8, -4, "-4"),
    ("Mixed", 1, -7, "8")
])
@allure.title("{title}")
def test_sub(title, a, b, expected):
    with allure.step("Send request"):
        r = requests.get(f"{BASE_URL}/sub?a={a}&b={b}")
    with allure.step("Verify response"):
        assert r.status_code == 200
        assert r.text == expected
