from fastapi import APIRouter
from card import AddCardValidator
from database.cardservice import check_cart_db, add_cart_db, get_exact_user_card_db, get_exact_card_user_db, \
    delete_card_db

card_router = APIRouter(prefix='/card', tags=['Работа с картами'])


@card_router.post('/add')
async def add_new_card(data: AddCardValidator):
    card_data = data.model_dump()

    checker = check_cart_db(data.card_number)

    if checker:
        result = add_cart_db(**card_data)
        return {'message': result}
    else:
        return {'message': 'Карта с таким номером уже есть в БД'}


@card_router.get('/exact_cards_info')
async def get_user_card_info(user_id: int, card_id: int):
    result = get_exact_card_user_db(user_id=user_id, card_id=card_id)

    if result:
        return {'message': result}
    else:
        return {'message': 'Карта не найдена'}


@card_router.get('/exact-cards')
async def get_user_card(user_id: int):
    result = get_exact_user_card_db(user_id=user_id,)

    if result:
        return {'message': result}
    else:
        return {'message': 'Пользоваетль не найден'}


@card_router.delete('/delete-card')
async def delete_card(card_id: int):
    result = delete_card_db(card_id=card_id)

    if result:
        return {'message': f'Success {result}'}
    else:
        return {'message': 'Нету такой карты '}


