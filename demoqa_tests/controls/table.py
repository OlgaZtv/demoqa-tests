from selene.core.entity import Element


class Table:

    def __init__(self, element: Element):
        self.element = element

    def cells_of_row(self, index):
        return self.element.all('tbody tr')[index].all('td')
