from selene.support.shared import browser
from selene import have, be


def test_search_positive(set_browser_settings):
    input_text = 'selene'
    search_results = 'yashaka/selene: User-oriented Web UI browser tests in'

    browser.element('[name=q]').should(be.blank).type(input_text).press_enter()
    browser.element('[id=search]').should(have.text(search_results))

def test_search_negative(set_browser_settings):
    input_text = 'asdgdasgfdhdfghfg'
    search_results = 'По запросу asdgdasgfdhdfghfg ничего не найдено. '

    browser.element('[name=q]').should(be.blank).type(input_text).press_enter()
    browser.element('[id="topstuff"').should(have.text(search_results))