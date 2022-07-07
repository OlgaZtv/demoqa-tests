from selene import command, have
from selene.core.entity import Element


class Datepicker:

    def __init__(self, element: Element):
        self.element = element

    def select(self, /, *, option: str):
        self.element.perfom(command.js.scroll_into_view).click()
        self.element_by(have.exact_text(option)).click()

    def autocomplete(self, /, *, option: str):
        self.element.perform(command.js.set_value(option))
