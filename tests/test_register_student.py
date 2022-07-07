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
    subjects.add('Maths')

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

    results = Table(s('.modal-dialog'))

    results.cells_of_row(0).should(have.exact_text('Student Name Olga Lastname'))
    results.cells_of_row(1).should(have.exact_text('Student Email test@test.com'))
    results.cells_of_row(2).should(have.exact_text('Gender Female'))
    results.cells_of_row(3).should(have.exact_text('Mobile 1111111111'))
    results.cells_of_row(4).should(have.exact_text('Date of Birth 31 August,1988'))
    results.cells_of_row(5).should(have.exact_text('Subjects Chemistry, Maths'))
    results.cells_of_row(6).should(have.exact_text('Hobbies Sports'))
    results.cells_of_row(7).should(have.exact_text('Picture 01.jpg'))
    results.cells_of_row(8).should(have.exact_text('Address Some test address'))
    results.cells_of_row(9).should(have.exact_text('State and City NCR Delhi'))

    s('#closeLargeModal').perform(command.js.click)
