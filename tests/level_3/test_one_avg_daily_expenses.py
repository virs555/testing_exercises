import decimal
import pytest
import datetime

from functions.level_3.one_avg_daily_expenses import calculate_average_daily_expenses
from functions.level_3.models import Currency, BankCard

def test__calculate_average_daily_expenses__return_daily_expense_for_expenses(create_expense):
    expense_1 = create_expense(amount = decimal.Decimal('10.99'))
    expense_2 = create_expense(amount = decimal.Decimal('11.99'))
    assert calculate_average_daily_expenses([expense_1, expense_2]) == decimal.Decimal('22.98')

@pytest.mark.xfail(reason='Amount does not take into account the difference in the cost of currencies')
def test__calculate_average_daily_expenses__return_daily_expense_for_different_currencies(create_expense):
    expense_rub = create_expense(currency = Currency.RUB, amount = decimal.Decimal('10.99'))
    expense_usd = create_expense(currency = Currency.USD, amount = decimal.Decimal('10.99'))
    assert calculate_average_daily_expenses([expense_rub, expense_usd]) == decimal.Decimal('21.98')

@pytest.mark.xpass(reason='Probably should not work if the bank card number is too long')
def test__calculate_average_daily_expenses__return_daily_expense_if_bank_card_has_more_than_four_digits(create_expense):
    expense_bank_card = create_expense(
        card = BankCard(last_digits='1234567891011121314151617181920', owner='Vladimir Seregin'), 
                        amount=decimal.Decimal('10.98'))
    assert calculate_average_daily_expenses([expense_bank_card]) == decimal.Decimal('10.98')

@pytest.mark.xpass(reason='Probably should not work if the bank card contains not digits')
def test__calculate_average_daily_expenses__return_daily_expense_if_bank_card_has_not_digits(create_expense):
    expense_bank_card = create_expense(
        card = BankCard(last_digits='abcd', owner='Vladimir Seregin'), 
                        amount=decimal.Decimal('10.98'))
    assert calculate_average_daily_expenses([expense_bank_card]) == decimal.Decimal('10.98')

def test__calculate_average_daily_expenses__return_daily_expense_for_empty_spent_in(create_expense):
    expense_spent_in = create_expense(spent_in='', amount = decimal.Decimal('10.98'))
    assert calculate_average_daily_expenses([expense_spent_in]) == decimal.Decimal('10.98')

@pytest.mark.xfail(reason='Date cannot be in the future')
def test__calculate_average_daily_expenses__return_daily_expense_for_dates_from_future(create_expense):
    expense_date = create_expense(spent_at=datetime.datetime(3024, 3, 17, 23, 9), amount = decimal.Decimal('10.98'))
    assert calculate_average_daily_expenses([expense_date]) == decimal.Decimal('10.98')

def test__calculate_average_daily_expenses__return_daily_expense_without_expense_category(create_expense):
    expense_category = create_expense(category = None, amount = decimal.Decimal('10.98'))
    assert calculate_average_daily_expenses([expense_category]) == decimal.Decimal('10.98')