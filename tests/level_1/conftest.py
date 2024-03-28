import pytest
from functions.level_1.four_bank_parser import BankCard, SmsMessage
import datetime as dt

@pytest.fixture
def tomorrow():
    return dt.date.today() + dt.timedelta(days=1)

@pytest.fixture
def sms_from_bank():
    sms = SmsMessage('1000 rub, 1234567890000123 23.02.24 14:13 McDonalds authcode 4488', 'MyBank', 
                                          dt.datetime(2024,2,23,14,20))
    return sms

@pytest.fixture
def bank_cards():
    bank_cards = [BankCard('0120', "Alex Justas"), BankCard('0123', "Arkadiy Volozh")]
    return bank_cards