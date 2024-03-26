import pytest

import decimal
import datetime
from functions.level_3.models import Currency, BankCard, ExpenseCategory, Expense


@pytest.fixture()
def create_expense():
    def expense(
        amount: decimal.Decimal = decimal.Decimal('10.99'),
        currency: Currency = Currency.USD,
        card: BankCard = BankCard(last_digits='4488', owner='Vladimir Seregin'),
        spent_in: str = 'Apple Music',
        spent_at: datetime.datetime = datetime.datetime(2024, 3, 17, 23, 9),
        category: ExpenseCategory | None = ExpenseCategory.ONLINE_SUBSCRIPTIONS,
    ):
        return Expense(
            amount = amount,
            currency = currency,
            card = card,
            spent_in = spent_in,
            spent_at = spent_at,
            category = category,
        )
    
    return expense