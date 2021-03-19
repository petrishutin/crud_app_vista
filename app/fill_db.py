from models import Note
from models.db import Session
from faker import Faker

def fill_db():
    fake = Faker()
    for _ in range(5):
        Session.add(Note(fake.text()))
    try:
        Session.commit()
    finally:
        Session.close()


if __name__ == '__main__':
    fill_db()
