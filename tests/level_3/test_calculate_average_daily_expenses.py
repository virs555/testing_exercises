from functions.level_3.one_avg_daily_expenses import calculate_average_daily_expenses
import decimal

def test__calculate_average_daily_expenses__return_daily_expense_for_expenses(create_expense):
    expense_1 = create_expense(amount = decimal.Decimal('10.99'))
    expense_2 = create_expense(amount = decimal.Decimal('11.99'))
    assert calculate_average_daily_expenses([expense_1, expense_2]) == decimal.Decimal('22.98')