import allure

from demoqa_tests.model import app
from demoqa_tests.utils.attach import add_screenshots, add_logs, add_html, add_video


@allure.description('Test sign up form')
@allure.title("Successful fill form")
@allure.tag('UI')
def test_register_student(setup_browser):
    browser = setup_browser

    with allure.step("Open registrations form"):
        app.given_student_registration_form_opened()

    with allure.step("Fill form"):
        (app.form \
         .set_first_name('Olga') \
         .set_last_name('Lastname') \
         .set_email('test@test.com') \
         .set_mobile('1111111111') \
         .set_gender('Female') \
         .set_birth_date(1988,
                         8,
                         31) \
         .select_subjects('Chemistry',
                          'Maths', ) \
         .select_hobbies('Sports') \
         .upload('01.jpg') \
         .set_address('Some test address') \
         .set_state_city('NCR', 'Delhi'))

    app.form.submit()

    app.form.check_modal_visible('Thanks for submitting the form')

    with allure.step("Check form results"):
        (app.results \
         .assert_texts(1, 1, 'Olga Lastname') \
         .assert_texts(2, 1, 'test@test.com') \
         .assert_texts(3, 1, 'Female') \
         .assert_texts(4, 1, '1111111111') \
         .assert_texts(5, 1, '31 August,1988') \
         .assert_texts(6, 1, 'Chemistry, Maths') \
         .assert_texts(7, 1, 'Sports') \
         .assert_texts(8, 1, '01.jpg') \
         .assert_texts(9, 1, 'Some test address') \
         .assert_texts(10, 1, 'NCR Delhi'))

    app.form.close_dialog()

    add_screenshots(browser)
    add_logs(browser)
    add_html(browser)
    add_video(browser)
