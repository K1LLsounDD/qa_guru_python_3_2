import pytest
from selene.support.shared import browser

base_url = 'https://www.google.com/'


@pytest.fixture()
def set_browser_settings():
    browser.config.window_height = 1366
    browser.config.window_width = 768
    browser.open(base_url)
