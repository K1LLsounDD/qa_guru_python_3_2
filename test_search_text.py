from selene.support.shared import browser
from selene import have, be


def test_search_positive(set_browser_settings):
    browser.element('[name=q]').should(be.blank).type('selene').press_enter()
    browser.element('[id=search]').should(have.text('yashaka/selene: User-oriented Web UI browser tests in'))
