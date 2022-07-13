from selene import command, have
from selene.core.entity import Element
from selene.support.shared.jquery_style import ss


class Dropdown:

    def __init__(self, element: Element):
        self.element = element

    def select(self, /, *, option: str):
        self.element.perfom(command.js.scroll_into_view).click()
        ss('[id^=react-select-][id*=-option]').element_by(have.exact_text(option)).click()

    def autocomplete(self, /, *, option: str):
        self.element.type(option).press_tab()
