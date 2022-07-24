from selene import have, command
from selene.support.shared import browser
from selene.support.shared.jquery_style import ss

from demoqa_tests.model.pages.student_registration_form import StudentRegistrationForm
from demoqa_tests.model.controls.table import Table

form = StudentRegistrationForm()
results = Table()


def given_student_registration_form_opened() -> object:
    browser.open('/automation-practice-form')
    (
        ss('[id^=google_ads][id$=container__]').with_(timeout=10)
        .should(have.size_greater_than_or_equal(2))
        .perform(command.js.remove)
    )
