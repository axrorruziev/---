from fastapi import APIRouter
from database.transferservice import create_transaction_db, cancel_transaction_db, get_history_transaction

from transaction import CreateTransactionValidator, CancelTransactionValidator

trans_router = APIRouter(prefix='/transfers', tags=['transaction'])


@trans_router.post('/cretae')
async def add_new_transaction(data: CreateTransactionValidator):
    transaction_data = data.model_dump()
    result = create_transaction_db(**transaction_data)
    if result:
        return {'message': result}
    else:
        return {'message': 'Ошибка брат'}


@trans_router.get('/history')
async def history_transaction(card_id: int):
    result = get_history_transaction(card_from_id=card_id)
    if result:
        return result
    else:
        return {'message': 'Ошибка '}


@trans_router.post('/cansel')
async def cansel_transaction(data: CancelTransactionValidator):
    cansel_data = data.model_dump()
    result = cancel_transaction_db(**cansel_data)

    if result:
        return {'message': result}
    else:
        return {'message': 'ошибка '}
