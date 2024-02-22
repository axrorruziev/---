from database.models import UserCard

from datetime import datetime

from database import get_db


def add_cart_db(user_id, card_number, card_name, balance, exp_date):
    db = next(get_db())

    new_card = UserCard(user_id=user_id, card_number=card_number, card_name=card_name, balance=balance,
                        exp_date=exp_date)

    if new_card:
        db.add(new_card)
        db.commit()
        return 'карта успешно добавлена!!!'
    else:
        return 'ошибка брат'


def get_exact_user_card_db(user_id):
    db = next(get_db())

    exact_user_card = db.query(UserCard).filter_by(user_id=user_id).first()

    if exact_user_card:
        return exact_user_card
    else:
        return 'нету такого пользователя'


def get_exact_card_user_db(user_id, card_id):
    db = next(get_db())

    exact = db.query(UserCard).filter_by(user_id=user_id, card_id=card_id).first()

    if exact:
        return exact
    else:
        return 'нету такой карты или такого пользователя'


def check_cart_db(card_number):
    db = next(get_db())

    checker = db.query(UserCard).filter_by(card_number=card_number).first()

    if checker:
        return checker
    else:
        return 'нету такой карты в бд'


def delete_card_db(card_id):

    db = next(get_db())

    delete_card = db.query(UserCard).filter_by(card_id=card_id).first()

    if delete_card:
        db.delete()
        db.commit()
        return 'все прошло успешно'
    else:
        return 'карта не найдена'


