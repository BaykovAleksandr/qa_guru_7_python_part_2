from selene import browser
from selene import be, have


def test_positive(config_browser):
    browser.open('https://demoqa.com/automation-practice-form')
    browser.element('#firstName').should(be.blank).type('Aleksandr')
    browser.element('#lastName').should(be.blank).type('Baykov')
    browser.element('#userEmail').should(be.blank).type('test@yandex.com')
    browser.element('[for="gender-radio-1"]').click()
    browser.element('#userNumber').should(be.blank).type('1234567890')
    browser.element('#dateOfBirthInput').click()
    browser.element(".react-datepicker__month-select>option[value='11']").click()
    browser.element(".react-datepicker__year-select>option[value='1988']").click()
    browser.element('.react-datepicker__day--019').click()
    browser.element('#subjectsInput').should(be.blank).type('Maths').press_enter()
    browser.element("[for='hobbies-checkbox-3']").click()
    browser.element('#currentAddress').type("Moscow Region")
    browser.element('#react-select-3-input').type('ncr').press_enter()
    browser.element('#react-select-4-input').type('delhi').press_enter()
    browser.element('#submit').press_enter()
    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
    browser.element('.table').should(have.text('Aleksandr Baykov' and 'test@yandex.com' and 'Male' and
                                               '1234567890' and '19 December,1988' and 'Maths' and 'Music' and
                                               'Moscow Region' and 'NCR Delhi'))
    print("Выведенные на экран поля соответствуют заполненным")
