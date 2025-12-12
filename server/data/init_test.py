from .db import get_session
from stock.models import Stock, StockEntry
from user.models import User

def create_test_data(num_users: int = 5, num_stocks: int = 3):
    session = next(get_session())

    for i in range(num_users):
        User(username=f'user{i}', password="test", balance=10000.0).save(session)

    for i in range(num_stocks):
        stock = Stock(name=f'Stock {i}', category='Test')
        stock.save(session)
        StockEntry(stock_id=stock.uid, value=5000.0).save(session)