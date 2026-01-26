from pages.auto_first import AutoFirst

def test_autopage(driver):

    name = 'Kiran Kumar'
    #name = 'Take from excel'
    email = 'Take from excel'
    phone = '000000001'

    auto = AutoFirst(driver)
    actual_name = auto.enter_username(name)
    assert actual_name == name , f"Expected {name}, but the field contains {actual_name}"

    # Email Info
    auto.enter_email(email)

    # Phone Info
    auto.enter_phone(phone)

    # Radio Button
    auto.radio_btn()

    # Provide days
    selected_days = ['thursday', 'friday', 'monday']
    day_result = auto.days_select(*selected_days)
    assert 'monday' in day_result
    print(f'Selected days: {day_result}')



