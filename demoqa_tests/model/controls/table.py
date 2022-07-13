from selene.core.entity import Element
from selene.support.conditions import have
from selene.support.shared import browser


class Table:

    def __init__(self, element: Element = ...):
        self.element = element if element is not ... else browser.element('.modal-content .table')

    def assert_texts(self, row_index: int, column_index: int, *values: str):
        for value in values:
            self.element.all('tr')[row_index].all('td')[column_index].should(have.text(value))
        return self
