from functions.level_1.four_bank_parser import BankCard, SmsMessage, Expense, parse_ineco_expense

import datetime

  
def test__parse_ineco_expense__return_correct_amount(sms_from_bank, bank_cards):
    expense = parse_ineco_expense(sms_from_bank, bank_cards)
    assert expense.amount == 1000

def test__parse_ineco_expense__return_correct_date(sms_from_bank, bank_cards):
    expense = parse_ineco_expense(sms_from_bank, bank_cards)
    assert expense.spent_at == datetime.datetime(2024,2,23,14,13)

def test__parse_ineco_expense__return_correct_card(sms_from_bank, bank_cards):
    expense = parse_ineco_expense(sms_from_bank, bank_cards)
    assert expense.card == BankCard('0123', "Arkadiy Volozh")