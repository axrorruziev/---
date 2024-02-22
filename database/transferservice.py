from database.models import UserCard, Transfer

from _datetime import datetime

from database import get_db


def validate_card(card_number, db):
    exact_card = db.query(UserCard).filter_by(card_number=card_number).first

    return exact_card


def create_transaction_db(card_from, card_to, amount):
    db = next(get_db())

    check_card_form = validate_card(card_from, db)
    check_card_to = validate_card(card_to, db)

    if check_card_form and check_card_to:
        if check_card_form.balance >= amount:
            check_card_form.balance -= amount
            check_card_to.balance += amount
            new_transaction = Transfer(check_card_form_id=check_card_form.card_id,
                                       check_card_to_id=check_card_to.card_id,
                                       amount=amount, transaction_date=datetime.now)
            db.add(new_transaction)
            db.commit()
            return 'перевод успешно выполнен'
        else:
            return 'Недостаточно средств'

    else:
        return 'Одна из карт не сущевствует'


def get_history_transaction(card_from_id):
    db = next(get_db())

    card_transaction = db.query(Transfer).filter_by(card_from_id=card_from_id).all()

    if card_transaction:
        return card_transaction
    else:
        return 'нету'


def cancel_transaction_db(card_from, card_to, amount, transfer_id):
    db = next(get_db())

    check_card_form = validate_card(card_from, db)
    check_card_to = validate_card(card_to, db)
    if check_card_form and check_card_to:
        transaction_to_cancel = db.query(Transfer).filter_by(transfer_id=transfer_id).first()
        if transaction_to_cancel:
            check_card_form.balance += amount
            check_card_to.balance -= amount
            transaction_to_cancel.status = False
            db.delete(transaction_to_cancel)
            db.commit()
            return 'перевод отменен'
        else:
            return "указанный перевод не существует"
    else:
        return 'одна из карт не сущевтсвует'


