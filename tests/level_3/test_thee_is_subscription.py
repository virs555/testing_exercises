from functions.level_3.three_is_subscription import is_subscription
import datetime

def test__is_subscription__returns_true_when_like_subscription(create_expense):
    expense = create_expense(spent_in = 'netflix')
    expense_history = [create_expense(spent_in = 'netflix', spent_at = datetime.date(28, 1, 10)),
                       create_expense(spent_in = 'netflix', spent_at = datetime.date(28, 2, 10)),
                       create_expense(spent_in = 'netflix', spent_at = datetime.date(28, 3, 10)),
                       ]
    assert is_subscription(expense, expense_history)

def test__is_subscription__returns_false_when_insufficient_unique_months(create_expense):
    expense = create_expense(spent_in = 'netflix')
    expense_history = [create_expense(spent_in = 'netflix', spent_at = datetime.date(28, 1, 10)),
                       create_expense(spent_in = 'netflix', spent_at = datetime.date(28, 1, 11)),
                       create_expense(spent_in = 'netflix', spent_at = datetime.date(28, 1, 12)),
                       ]
    assert is_subscription(expense, expense_history) is False

def test__is_subscription__returns_false_when_insufficient_transactions_for_service(create_expense):
    expense = create_expense(spent_in = 'netflix')
    expense_history = [create_expense(spent_in = 'netflix', spent_at = datetime.date(28, 1, 10)),
                       create_expense(spent_in = 'apple', spent_at = datetime.date(28, 2, 10)),
                       create_expense(spent_in = 'yandex', spent_at = datetime.date(28, 3, 10)),
                       ]
    assert is_subscription(expense, expense_history) is False