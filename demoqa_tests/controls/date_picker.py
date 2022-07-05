from selene import command, have
from selene.core.entity import SeleneElement
from selene.support.shared.jquery_style import ss, s


def select(element: SeleneElement, /, *, option: str):
    element.perfom(command.js.scroll_into_view).click()
    s('#dateOfBirthInput').element_by(have.exact_text(option)).click()


def autocomplete(element: SeleneElement, /, *, option: str):
    element.perform(command.js.set_value(option))
