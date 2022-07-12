from selene import have, command
from selene.support.shared import browser
from selene.support.shared.jquery_style import s, ss

from demoqa_tests.controls.date_picker import Datepicker
from demoqa_tests.controls.dropdown import Dropdown
from demoqa_tests.utils import path_to_file
from demoqa_tests.controls.table import Table
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

    date_of_birth = Datepicker(s('#dateOfBirthInput'))
    date_of_birth.select_year(1988)
    date_of_birth.select_month(8)
    date_of_birth.select_day(31)

    subjects = TagsInput(s('#subjectsInput'))
    subjects.add('Chem', autocomplete='Chemistry')
    subjects.autocomplete('Maths')

    hobbies_types = s('#hobbiesWrapper')
    hobbies_types.all('.custom-checkbox').element_by(have.exact_text('Sports')).click()

    s('#uploadPicture').send_keys(path_to_file.resourse('01.jpg'))

    s('#currentAddress').type('Some test address')

    state_element = Dropdown(s('#state input'))
    state_element.autocomplete(option='NCR')

    city_element = Dropdown(s('#city input'))
    city_element.autocomplete(option='Delhi')

    s('#submit').perform(command.js.click)

    s('#example-modal-sizes-title-lg').should(have.exact_text('Thanks for submitting the form'))

    results = Table(s('.modal-content .table'))

    results.cells_of_row(row=1, column=2).should(have.exact_text('Olga Lastname'))
    results.cells_of_row(row=2, column=2).should(have.exact_text('test@test.com'))
    results.cells_of_row(row=3, column=2).should(have.exact_text('Female'))
    results.cells_of_row(row=4, column=2).should(have.exact_text('1111111111'))
    results.cells_of_row(row=5, column=2).should(have.exact_text('31 August,1988'))
    results.cells_of_row(row=6, column=2).should(have.exact_text('Chemistry, Maths'))
    results.cells_of_row(row=7, column=2).should(have.exact_text('Sports'))
    results.cells_of_row(row=8, column=2).should(have.exact_text('01.jpg'))
    results.cells_of_row(row=9, column=2).should(have.exact_text('Some test address'))
    results.cells_of_row(row=10, column=2).should(have.exact_text('NCR Delhi'))

    s('#closeLargeModal').perform(command.js.click)
