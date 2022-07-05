from selene import have, command, elements
from selene.support.shared import browser
from selene.support.shared.jquery_style import s, ss

from demoqa_tests.controls import date_picker
from demoqa_tests.controls import dropdown
from demoqa_tests.controls.path_to_file import resourse
from demoqa_tests.controls.table import cells_row
from demoqa_tests.controls.tags_input import TagsInput


def given_student_registration_form_opened():
    browser.open('/automation-practice-form')
    (
        ss('[id^=google_ads][id$=container__]').with_(timeout=10)
        .should(have.size_greater_than_or_equal(2))
        .perform(command.js.remove)
    )


def test_register_student():
    given_student_registration_form_opened()

    s('#firstName').type('Olga')
    s('#lastName').type('Lastname')
    s('#userEmail').type('test@test.com')

    gender = s('#genterWrapper')
    gender.all('.custom-radio').element_by(have.exact_text('Female')).click()

    mobile_number = '#userNumber'
    s(mobile_number).type('1111111111')

    # date_picker.select(s('.react-datepicker__month-select'), option='August')
    # date_picker.select(s('.react-datepicker__year-select'), option='1988')
    date_picker.autocomplete(s('#dateOfBirthInput'), option='31 Aug,1988')

    subjects = TagsInput(browser.element('#subjectsInput'))
    subjects.add('Chem', autocomplete='Chemistry')
    subjects.add('Maths')

    s('#hobbies-checkbox-1').perform(command.js.click)

    s("#uploadPicture").send_keys(resourse('01.jpg'))

    s('#currentAddress').type('Some test address')

    dropdown.autocomplete(s('#state input'), option='NCR')
    dropdown.autocomplete(s('#city input'), option='Deldhi')

    s('#submit').perform(command.js.click)

    s('#example-modal-sizes-title-lg').should(have.exact_text('Thanks for submitting the form'))

    cells_row(ss('table tr'), index=1, option="Olga Lastname")
    cells_row(ss('table tr'), index=2, option="test@test.com")
    cells_row(ss('table tr'), index=3, option="Female")
    cells_row(ss('table tr'), index=4, option="1111111111")
    cells_row(ss('table tr'), index=5, option="31 August,1988")
    cells_row(ss('table tr'), index=6, option="Maths")
    cells_row(ss('table tr'), index=7, option="Sports")
    cells_row(ss('table tr'), index=8, option="01.jpg")
    cells_row(ss('table tr'), index=9, option="Some test address")
    cells_row(ss('table tr'), index=10, option="NCR Delhi")

    s('#closeLargeModal').perform(command.js.click)
