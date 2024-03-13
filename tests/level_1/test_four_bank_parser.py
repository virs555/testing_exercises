from functions.level_1.four_bank_parser import BankCard, SmsMessage, Expense, parse_ineco_expense

import datetime


def test_parse_ineco_expense():
    assert parse_ineco_expense(SmsMessage('1 000, 1234567890000123 23.02.24 14:13 McDonalds authcode 4488', 'MyBank', 
                                          datetime.datetime(2024,2,23,14,20)), 
                               [BankCard('0120', "Alex Justas"), BankCard('0123', "Arkadiy Volozh")])
    
def test__parse_ineco_expense__return_correct_amount():
    sms = SmsMessage('1000 rub, 1234567890000123 23.02.24 14:13 McDonalds authcode 4488', 'MyBank', 
                                          datetime.datetime(2024,2,23,14,20))
    cards = [BankCard('0120', "Alex Justas"), BankCard('0123', "Arkadiy Volozh")]
    expense = parse_ineco_expense(sms, cards)
    assert expense.amount == 1000

def test__parse_ineco_expense__return_correct_date():
    sms = SmsMessage('1000 rub, 1234567890000123 23.02.24 14:13 McDonalds authcode 4488', 'MyBank', 
                                          datetime.datetime(2024,2,23,14,20))
    cards = [BankCard('0120', "Alex Justas"), BankCard('0123', "Arkadiy Volozh")]
    expense = parse_ineco_expense(sms, cards)
    assert expense.spent_at == datetime.datetime(2024,2,23,14,13)

def test__parse_ineco_expense__return_correct_card():
    sms = SmsMessage('1000 rub, 1234567890000123 23.02.24 14:13 McDonalds authcode 4488', 'MyBank', 
                                          datetime.datetime(2024,2,23,14,20))
    cards = [BankCard('0120', "Alex Justas"), BankCard('0123', "Arkadiy Volozh")]
    expense = parse_ineco_expense(sms, cards)
    assert expense.card == BankCard('0123', "Arkadiy Volozh")

def test__parse_ineco_expense__not_return_incorrect_card():
    sms = SmsMessage('1000 rub, 1234567890000123 23.02.24 14:13 McDonalds authcode 4488', 'MyBank', 
                                          datetime.datetime(2024,2,23,14,20))
    cards = [BankCard('0120', "Alex Justas"), BankCard('0123', "Arkadiy Volozh")]
    expense = parse_ineco_expense(sms, cards)
    assert not expense.card == BankCard('0120', "Alex Justas")