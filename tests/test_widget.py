from source.widget import *
def test_get_date():
    pass

def test_mask_account_card():
    assert mask_account_card("") == "  "
    assert mask_account_card("Счет 7000792289606361") == "Счет **6361"
    assert mask_account_card("Visa Platinum 7000792289606361") == "Visa Platinum   7000 79** **** 6361"
