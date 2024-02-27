from functions.level_1.four_bank_parser import BankCard, SmsMessage, Expense, parse_ineco_expense

import datetime


def test_parse_ineco_expense():
    assert parse_ineco_expense(SmsMessage('1 000, 1234567890000123 23.02.24 14:13 McDonalds authcode 4488', 'MyBank', 
                                          datetime.datetime(2024,2,23,14,20)), 
                               [BankCard('0120', "Alex Justas"), BankCard('0123', "Arkadiy Volozh")])
    
