from functions.level_3.two_expense_categorizer import guess_expense_category, is_string_contains_trigger
from functions.level_3.models import ExpenseCategory

def test__guess_expense_category__returns_correct_category_for_known_trigger(create_expense):
    expense = create_expense(spent_in = 'zoom.us')
    assert guess_expense_category(expense) == ExpenseCategory.ONLINE_SUBSCRIPTIONS

def test__guess_expense_category__returns_none_for_unknown_trigger(create_expense):
    expense = create_expense(spent_in = 'unknown')
    assert guess_expense_category(expense) is None

def test__is_string_contains_trigger__returns_true_ignore_case(trigger):
    assert is_string_contains_trigger('NETFLIX', trigger)

def test__is_string_contains_trigger__returns_true_for_when_separator_before_trigger(trigger):
    assert is_string_contains_trigger('netflix Russia', trigger)

def test__is_string_contains_trigger__returns_true_for_when_separator_after_trigger(trigger):
    assert is_string_contains_trigger('discount/netflix', trigger)

def test__is_string_contains_trigger__returns_true_for_when_separatos_on_both_sides_of_trigger(trigger):
    assert is_string_contains_trigger('oneline\\netflix- Russia', trigger)