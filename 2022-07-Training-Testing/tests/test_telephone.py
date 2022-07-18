from bays_training import telephone


def test_telephone_full_number_with_plus():
    actual_country, actual_area, actual_main = telephone.clean_telephone_number('+441483924732')

    assert actual_country == '44'
    assert actual_area == '1483'
    assert actual_main == '924732'
