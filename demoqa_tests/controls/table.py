from selene.core.entity import Element


class Table:

    def __init__(self, element: Element):
        self.element = element

    def path_to_cell(self, row_index: int, column_index: int):
        return self.cells_of_row(row_index)[column_index]

    def cells_of_row(self, index):
        return self.rows[index].all('td')

    @property
    def rows(self):
        return self.element.all('tr')
