from pydantic import BaseModel


class AddCardValidator(BaseModel):
    user_id: int
    card_number: int
    card_name: str
    balance: float
    exp_date: int
