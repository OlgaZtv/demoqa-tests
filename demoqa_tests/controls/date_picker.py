from selene import command, have
from selene.core.entity import Element
from selene.support.shared import browser


class Datepicker:

    def __init__(self, element: Element):
        self.element = element

    def select(self, /, *, option: str):
        self.browser.all(option).element_by(have.exact_text(option)).click()

    def autocomplete(self, /, *, option: str):
        self.element.perform(command.js.set_value(option)).click()

    def select_year(self, option: int):
        self.element.click()
        browser.element('.react-datepicker__year-select').element(f'[value="{option}"]').click()

    def select_month(self, option: int):
        self.element.click()
        browser.element('.react-datepicker__month-select').element(f'[value="{option}"]').click()

    def select_day(self, option: int):
        browser.element(f'.react-datepicker__day--0{option}').click()




