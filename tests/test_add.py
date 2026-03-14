import allure
import pytest
import requests

BASE_URL = "http://localhost:5000"

@allure.suite("Calculator tests")
@allure.feature("Calculator")
@allure.sub_suite("Add tests")
@pytest.mark.parametrize("title,a,b,expected", [
    ("Positive", 4, 6, "10"),
    ("Negative", -2, -3, "-5"),
    ("Mixed", 10, -3, "7")
])
@allure.title("{title}")
def test_add(title, a, b, expected):
    with allure.step("Send request"):
        r = requests.get(f"{BASE_URL}/add?a={a}&b={b}")
    with allure.step("Verify response"):
        assert r.status_code == 200
        assert r.text == expected
