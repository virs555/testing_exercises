from functions.level_3.four_fraud import find_fraud_expenses

def test__find_fraud_expenses__return_transactions_which_look_like_fraud(create_expense):
    expenses_history = [
        create_expense(amount = 1000),
        create_expense(amount = 1000),
        create_expense(amount = 1000),
        create_expense(amount = 2000),
    ]
    assert find_fraud_expenses(expenses_history) == [create_expense(amount = 1000),
                                                     create_expense(amount = 1000),
                                                     create_expense(amount = 1000),
                                                     ]

def test__find_fraud_expenses_dont_return_transactions_when_chain_less_than_three(create_expense):
    expenses_history = [
        create_expense(amount = 10000)
    ]
    assert find_fraud_expenses(expenses_history) == []

def test__find_fraud_expenses_dont_return_transactions_when_amount_less_than_5000(create_expense):
    expenses_history = [
        create_expense(amount = 1000),
        create_expense(amount = 2000),
        create_expense(amount = 3000),
    ]
    assert find_fraud_expenses(expenses_history) == []

def test__find_fraud_expenses_dont_return_transactions_when_spent_at_is_different(create_expense):
    expenses_history = [
        create_expense(spent_at = 'netflix', amount = 1000),
        create_expense(spent_at = 'appstore', amount = 1000),
        create_expense(spent_at = 'yandex', amount = 1000),
    ]
    assert find_fraud_expenses(expenses_history) == []