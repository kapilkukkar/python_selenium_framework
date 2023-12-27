import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from utlities import readconfig


@pytest.fixture()
def log_on_failure(request, setup_browser):
    yield
    item = request.node
    if item.rep_call.failed:
        allure.attach(setup_browser.get_screenshot_as_png(), name="failed_test", attachment_type=AttachmentType.PNG)


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)


@pytest.fixture
def setup_browser(request):
    browser = readconfig.read_data("basic info", "browser")
    url = readconfig.read_data("basic info", "url")
    if browser.lower() == "chrome":
        driver = webdriver.Chrome()
    elif browser.lower() == "firefox":
        driver = webdriver.Firefox()
    elif browser.lower() == "edge":
        driver = webdriver.Edge()
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    driver.maximize_window()
    driver.get(url)
    driver.implicitly_wait(60)
    request.cls.driver = driver
    yield driver

    driver.quit()
