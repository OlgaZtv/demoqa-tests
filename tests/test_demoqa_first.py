from selene import have, command
from selene.support.shared import browser
from selene.support.shared.jquery_style import s, ss


def given_opened_text_box():
    browser.open('/automation-practice-form')
    (
        ss('[id^=google_ads][id$=container__]').with_(timeout=10)
        .should(have.size_greater_than_or_equal(2))
        .perform(command.js.remove)
    )


def test_submit_form():
    given_opened_text_box()

    s('#firstName').type('Olga')
    s('#lastName').type('Lastname')
    s('#userEmail').type('test@test.com')
    s('#gender-radio-2').perform(command.js.click)
    s('#userNumber').type('1111111111')
    s('#dateOfBirthInput').perform(command.js.scroll_into_view).click()
    s('[value="1988"]').click()
    s('[value="7"]').click()
    s('div[aria-label="Choose Wednesday, August 31st, 1988"]').click()
    s('#subjectsInput').click().send_keys("Maths").press_enter()
    s('#hobbies-checkbox-1').perform(command.js.click)
    s("#uploadPicture").type('C:/Users/Olga/PycharmProjects/demoqa-tests/images/01.jpg')
    s('#currentAddress').type('Some test address')
    s('#state input').type('NCR').press_tab()
    s('#city input').type('Delhi').press_tab().press_enter()
    s('#submit').perform(command.js.click)

    s('#example-modal-sizes-title-lg').should(have.exact_text('Thanks for submitting the form'))
    ss('[class="table table-dark table-striped table-bordered table-hover"] tr').should(have.exact_texts(
        'Label Values',
        'Student Name Olga Lastname',
        'Student Email test@test.com',
        'Gender Female', 'Mobile 1111111111',
        'Date of Birth 31 August,1988',
        'Subjects Maths',
        'Hobbies Sports',
        'Picture 01.jpg',
        'Address Some test address',
        'State and City NCR Delhi'
    ))
    s('#closeLargeModal').perform(command.js.click)


def test_change_table():
    browser.open('/webtables')
    (
        ss('[id^=google_ads][id$=container__]').with_(timeout=10)
        .should(have.size_greater_than_or_equal(2))
        .perform(command.js.remove)
    )

    s('#addNewRecordButton').click()
    s('#firstName').type('Olga')
    s('#lastName').type('Lastname')
    s('#userEmail').type('test@test.ru')
    s('#age').type('33')
    s('#salary').type('1500')
    s('#department').type('QA')
    s('#submit').click()

    s('#edit-record-2').click()
    s('#firstName').type('Ivan')
    s('#lastName').type('Ivanov')
    s('#userEmail').click().clear()
    s('#userEmail').type('test2@test.ru')
    s('#age').type('25')
    s('#salary').type('1200')
    s('#department').type('QA')
    s('#submit').click()

    s('.main-header').should(have.exact_text('Web Tables'))
    s('#delete-record-3').click()



