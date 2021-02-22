import sqlalchemy as db
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import SQLAlchemyError
import pandas as pd
from config import Category_groups

from datetime import datetime, timedelta
from dateutil import relativedelta

# Innit DB connection & innit ORM base class
engine = db.create_engine("sqlite:///db.db")
conn = engine.connect()
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

FIRST_OF_MONTH = datetime.today().replace(day=1)
LAST_OF_MONTH = FIRST_OF_MONTH + relativedelta.relativedelta(months=1) - timedelta(days=1)
LAST_3M_START = FIRST_OF_MONTH - relativedelta.relativedelta(months=3)
LAST_3M_END = FIRST_OF_MONTH - timedelta(days=1)


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
    account_id = db.Column(db.Integer, db.ForeignKey("accounts.id"))
    account = relationship("Account")
    description = db.Column("description", db.String)
    category_id = db.Column(db.Integer, db.ForeignKey("categories.id"))
    category = relationship("Category")
    date = db.Column("date", db.Date, nullable=False)
    amount = db.Column("amount", db.Float, nullable=False)
    billable = db.Column("billable", db.Boolean)
    __table_args__ = (db.UniqueConstraint("account_id", "description", "category_id", "date", "amount", "billable",
                                       name="uq_1"),)


# Create table(s) if not created yet
Base.metadata.create_all(engine)

# input = ["Cash", "Twisto", "Unicredit", "Revolut", "Investments"]
# for i in input:
#     x = Account(accounts=i)
#     session.add(x)
#     session.commit()
#

# for i in input:
#     x = Category(categories=i)
#     session.add(x)
#     session.commit()

# acc = session.query(Account).filter_by(accounts="Unicredit").first()
# test_transaction = Transaction(account=acc, description="Drogy třeba", category_id=3, date=datetime.datetime(2021,1,1), amount=float(45.23), billable=True)
# session.add(test_transaction)
# session.commit()

def preprocess_data(data):
    processed_data = {}

    # Check for ,/. in numeric value
    processed_data["amount"] = data["amount"].replace(",", ".")

    # Check if of account
    processed_data["account"] = session.query(Account).filter_by(accounts=data["fromAccount"]).first()
    processed_data["category"] = session.query(Category).filter_by(categories=data["category"]).first()

    processed_data["date"] = datetime.strptime(data["date"], "%Y-%m-%d")
    processed_data["description"] = data["description"]
    processed_data["billable"] = data["billable"]

    if data["toAccount"]:
        transfer_data = {}
        transfer_data["amount"] = float(processed_data["amount"]) * -1
        transfer_data["account"] = session.query(Account).filter_by(accounts=data["toAccount"]).first()
        transfer_data["category"] = processed_data["category"]
        transfer_data["date"] = processed_data["date"]
        transfer_data["description"] = processed_data["description"]
        transfer_data["billable"] = processed_data["billable"]

        all_data = [processed_data, transfer_data]
    else:
        all_data = [processed_data]
    return all_data


def post_data(processed_data):
    data = preprocess_data(processed_data)
    for i in data:
        post = Transaction(account=i["account"], amount=i["amount"], date=i["date"], category=i["category"],
                           description=i["description"], billable=i["billable"])
        session.add(post)
    session.commit()


def get_bilance():
    q = session.query(Transaction.account_id, db.func.sum(Transaction.amount).label("total")).group_by(Transaction.account_id).all()
    bilance = {}
    bilance["total"] = 0
    for i in q:
        bilance[f"acc_{i.account_id}"] = i.total
        bilance["total"] += i.total
    return bilance


def get_monthly_change():
    q1 = session.query(Transaction, db.func.sum(Transaction.amount).label("change")).filter(
        Transaction.date < FIRST_OF_MONTH).first()
    q2 = session.query(Transaction, db.func.sum(Transaction.amount).label("change")).first()
    change = q2.change - q1.change
    return change

def get_overview():
    df = pd.read_sql_table("transactions", con=engine, columns=["category_id", "date", "amount"])
    df_1m = df[(df["date"] >= FIRST_OF_MONTH) & (df["date"] <= LAST_OF_MONTH)]
    df_3m = df[(df["date"] >= LAST_3M_START) & (df["date"] <= LAST_3M_END)]

    overview = {}
    categories = ["bydleni", "jidlo", "volny_cas", "majetek", "doprava", "sluzby", "rozvoj_vzdelani", "prace_vydaje",
                  "dalsi_vydaje", "prace_prijmy", "freelance", "dalsi_prijmy", "vydaje_total", "prijmy_total"]
    for category in categories:
        i_1m = df_1m[df_1m["category_id"].isin(getattr(Category_groups, category))]
        i_3m = df_3m[df_3m["category_id"].isin(getattr(Category_groups, category))]
        overview[category] = {"this_month": i_1m["amount"].sum(), "last_3M": (i_3m["amount"].sum()/3)}
    return overview
