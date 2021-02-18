import sqlalchemy as db
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

from datetime import datetime

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

# input = ['Bydlení > Nájem', 'Bydlení > Energie', 'Bydlení > Další', 'Jídlo > Nákupy', 'Jídlo > Delivery',
#          'Jídlo > Restaurace', 'Jídlo > Doplňky, nootropika a léky', 'Volný čas > Párty', 'Volný čas > Schůzky',
#          'Volný čas > Kulturní akce', 'Volný čas > Fitness a sport', 'Volný čas > Cigarety a drogy',
#          'Volný čas > Dovolená', 'Volný čas > Další', 'Hygienické potřeby', 'Oblečení', 'Majetek > Elektronika',
#          'Majetek > Nábytek a vybavení', 'Majetek > Další', 'Doprava > MHD', 'Doprava > Vlaky, autobusy a jiné',
#          'Doprava > Další', 'Služby > Holič', 'Služby > Zdravotní náklady', 'Služby > Poplatky a subscriptions',
#          'Služby > Další', 'Rozvoj a vzdělání > Knihy', 'Rozvoj a vzdělání > Přednášky, konference a kurzy',
#          'Rozvoj a vzdělání > Další', 'Práce > OSSZ', 'Práce > VZP', 'Práce > Daně a FÚ', 'Práce > Další', 'AppStores',
#          'Dárky', 'Další výdaje', 'Práce', 'Freelance', 'Bydlení', 'Dary', 'Investiční příjmy', 'Další příjmy']
# for i in input:
#     x = Category(categories=i)
#     session.add(x)
#     session.commit()

# acc = session.query(Account).filter_by(accounts="Unicredit").first()
# test_transaction = Transaction(account=acc, description="Drogy třeba", category_id=3, date=datetime.datetime(2021,1,1), amount=float(45.23), billable=True)
# session.add(test_transaction)
# session.commit()

dummy_data = {'amount': '-454,35', 'fromAccount': 'Twisto', 'toAccount': '', 'category': 'Oblečení',
              'date': '2021-02-18', 'description': 'Ahoj', 'billable': False}

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

def postData(processed_data):
    data = preprocess_data(processed_data)
    for i in data:
        post = Transaction(account=i["account"], amount=i["amount"], date=i["date"], category=i["category"],
                           description=i["description"], billable=i["billable"])
        session.add(post)
    session.commit()
