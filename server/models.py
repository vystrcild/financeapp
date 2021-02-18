import sqlalchemy as db
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import SQLAlchemyError

import datetime

# Innit DB connection & innit ORM base class
engine = db.create_engine("sqlite:///db.db")
conn = engine.connect()
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class Account(Base):
    """
    DB table - Accounts
    """
    __tablename__ = "accounts"
    id = db.Column("id", db.Integer, primary_key=True, autoincrement=True)
    accounts = db.Column("accounts", db.String, unique=True, nullable=False)


class Category(Base):
    """
    DB table - Categories
    """
    __tablename__ = "categories"
    id = db.Column("id", db.Integer, primary_key=True, autoincrement=True)
    categories = db.Column("categories", db.String, unique=True, nullable=False)


class Transaction(Base):
    """
    DB table - Transactions
    """
    __tablename__ = "transactions"
    id = db.Column("id", db.Integer, primary_key=True, autoincrement=True)
    #account = db.Column("account", db.Integer, db.ForeignKey("accounts.id"), nullable=False)
    account_id = db.Column(db.Integer, db.ForeignKey("accounts.id"))
    description = db.Column("description", db.String)
    #category_id = db.Column("category", db.Integer, db.ForeignKey("categories.id"), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey("categories.id"))
    date = db.Column("date", db.Date, nullable=False)
    amount = db.Column("amount", db.Float, nullable=False)
    billable = db.Column("billable", db.Boolean)
    __table_args__ = (db.UniqueConstraint("account_id", "description", "category_id", "date", "amount", "billable",
                                       name="uq_1"),)


# Create table(s) if not created yet
Base.metadata.create_all(engine)

test_transaction = Transaction(account_id=1, description="Tyvole", category_id=2, date=datetime.datetime(2021,1,1), amount=float(-321.23), billable=True)
session.add(test_transaction)
session.commit()

# input = ["Cash", "Twisto", "Unicredit", "Revolut"]
# for i in input:
#     x = Account(accounts=i)
#     session.add(x)
#     session.commit()

# input = ["Nákupy", "Jídlo", "Bydlení", "Služby"]
# for i in input:
#     x = Category(categories=i)
#     session.add(x)
#     session.commit()