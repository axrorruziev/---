from pydantic import BaseModel


class CreateTransactionValidator(BaseModel):
    card_from: int
    card_to: int
    amount: float


class CancelTransactionValidator(BaseModel):
    card_from: int
    card_to: int
    amount: float
    transfer_id: int
