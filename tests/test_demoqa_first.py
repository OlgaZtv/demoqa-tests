import os

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

    s("#uploadPicture").send_keys(os.path.abspath(f'../resources/01.jpg'))

    s('#currentAddress').type('Some test address')

    s('#state input').type('NCR').press_tab()
    s('#city input').type('Delhi').press_tab().press_enter()

    s('#submit').perform(command.js.click)

    s('#example-modal-sizes-title-lg').should(have.exact_text('Thanks for submitting the form'))

    tr = browser.elements("table tr")
    tr.element(1).should(have.text("Olga Lastname"))
    tr.element(2).should(have.text("test@test.com"))
    tr.element(3).should(have.text("Female"))
    tr.element(4).should(have.text(str("1111111111")))
    tr.element(5).should(have.text("31 August,1988"))
    tr.element(6).should(have.text("Maths"))
    tr.element(7).should(have.text("Sports"))
    tr.element(8).should(have.text("01.jpg"))
    tr.element(9).should(have.text("Some test address"))
    tr.element(10).should(have.text("NCR Delhi"))

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

    path_to_new_row = '//*[@class="rt-table"]//*[@class="rt-tbody"]//*[@role="rowgroup"][4]//*[@class="rt-td"]'
    s(f'{path_to_new_row}[1]').should(have.exact_text('Olga'))
    s(f'{path_to_new_row}[2]').should(have.exact_text('Lastname'))
    s(f'{path_to_new_row}[3]').should(have.exact_text('33'))
    s(f'{path_to_new_row}[4]').should(have.exact_text('test@test.ru'))
    s(f'{path_to_new_row}[5]').should(have.exact_text('1500'))
    s(f'{path_to_new_row}[6]').should(have.exact_text('QA'))

    s('#edit-record-2').click()
    s('#firstName').type('Ivan')
    s('#lastName').type('Ivanov')
    s('#userEmail').click().clear()
    s('#userEmail').type('test2@test.ru')
    s('#age').type('25')
    s('#salary').type('1200')
    s('#department').type('QA')
    s('#submit').click()

    path_to_column = '//*[@class="rt-td"]'
    path_to_row = '//*[@class="rt-table"]//*[@class="rt-tbody"]//*[@role="rowgroup"][2]'
    s(f'{path_to_row + path_to_column}[1]').should(have.exact_text('Ivan'))
    s(f'{path_to_row + path_to_column}[2]').should(have.exact_text('Ivanov'))
    s(f'{path_to_row + path_to_column}[3]').should(have.exact_text('25'))
    s(f'{path_to_row + path_to_column}[4]').should(have.exact_text('test2@test.ru'))
    s(f'{path_to_row + path_to_column}[5]').should(have.exact_text('1200'))
    s(f'{path_to_row + path_to_column}[6]').should(have.exact_text('QA'))

    path_to_row = '//*[@class="rt-table"]//*[@class="rt-tbody"]//*[@role="rowgroup"][3]'
    path_to_column = '//*[@class="rt-td"]'
    path_to_delete_button = '#delete-record-3'
    s('.main-header').should(have.exact_text('Web Tables'))
    s(path_to_column + path_to_delete_button).click()

    s(f'{path_to_row + path_to_column}[1]').should(have.exact_text(' '))
    s(f'{path_to_row + path_to_column}[2]').should(have.exact_text(' '))
    s(f'{path_to_row + path_to_column}[3]').should(have.exact_text(' '))
    s(f'{path_to_row + path_to_column}[4]').should(have.exact_text(' '))
    s(f'{path_to_row + path_to_column}[5]').should(have.exact_text(' '))
    s(f'{path_to_row + path_to_column}[6]').should(have.exact_text(' '))



