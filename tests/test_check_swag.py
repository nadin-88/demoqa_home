from pages.swag_labs import SwagLabs

def test_check_all_swaglab(browser):
    swag_labs = SwagLabs (browser)
    swag_labs.visit()
    assert swag_labs.exist_icon()
    assert swag_labs.exist_name_field()
    assert swag_labs.exist_password_field()










