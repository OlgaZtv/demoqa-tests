from selene import command, have
from selene.core.entity import SeleneElement
from selene.support.shared.jquery_style import ss


def select(element: SeleneElement, /, *, option: str):
    element.perfom(command.js.scroll_into_view).click()
    ss('[id^=react-select-][id*=-option]').element_by(have.exact_text(option)).click()


def autocomplete(element: SeleneElement, /, *, option: str):
    element.type(option).press_tab().press_enter()
