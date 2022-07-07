from selene import have, command
from selene.support.shared import browser
from selene.support.shared.jquery_style import ss


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

    path_to_new_row = '//*[@class='rt-table']//*[@class='rt-tbody']//*[@role='rowgroup'][4]//*[@class='rt-td']'
    s(f'{path_to_new_row}[1]').should(have.exact_text('Olga'))
    s(f'{path_to_new_row}[2]').should(have.exact_text('Lastname'))
    s(f'{path_to_new_row}[3]').should(have.exact_text('33'))
    s(f'{path_to_new_row}[4]').should(have.exact_text('test@test.ru'))
    s(f'{path_to_new_row}[5]').should(have.exact_text('1500'))
    s(f'{path_to_new_row}[6]').should(have.exact_text('QA'))

    s('#edit-record-2').click()
    s('#firstName').click().clear().type('Ivan')
    s('#lastName').click().clear().type('Ivanov')
    s('#userEmail').click().clear().type('test2@test.ru')
    s('#age').click().clear().type('25')
    s('#salary').click().clear().type('1200')
    s('#department').click().clear().type('QA')
    s('#submit').click()

    path_to_column = '//*[@class='rt-td']'
    path_to_row = '//*[@class='rt-table']//*[@class='rt-tbody']//*[@role='rowgroup'][2]'
    s(f'{path_to_row + path_to_column}[1]').should(have.exact_text('Ivan'))
    s(f'{path_to_row + path_to_column}[2]').should(have.exact_text('Ivanov'))
    s(f'{path_to_row + path_to_column}[3]').should(have.exact_text('25'))
    s(f'{path_to_row + path_to_column}[4]').should(have.exact_text('test2@test.ru'))
    s(f'{path_to_row + path_to_column}[5]').should(have.exact_text('1200'))
    s(f'{path_to_row + path_to_column}[6]').should(have.exact_text('QA'))

    s('.main-header').should(have.exact_text('Web Tables'))
    path_to_row = '//*[@class='rt-table']//*[@class='rt-tbody']//*[@role='rowgroup'][4]'
    path_to_column = '//*[@class='rt-td']'
    path_to_delete_button = '//*[@title='Delete']'
    s(path_to_column + path_to_delete_button).click()

    s(f'{path_to_row + path_to_column}[1]').should(have.exact_text(' '))
    s(f'{path_to_row + path_to_column}[2]').should(have.exact_text(' '))
    s(f'{path_to_row + path_to_column}[3]').should(have.exact_text(' '))
    s(f'{path_to_row + path_to_column}[4]').should(have.exact_text(' '))
    s(f'{path_to_row + path_to_column}[5]').should(have.exact_text(' '))
    s(f'{path_to_row + path_to_column}[6]').should(have.exact_text(' '))



