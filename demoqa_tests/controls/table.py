from selene import have, browser
from selene.core.entity import SeleneElement


def cells_row(elements: SeleneElement, /, index: int, *, option: str):
    elements(int).should(have.text(option))
