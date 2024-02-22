from fastapi import FastAPI

app = FastAPI(docs_url='/')

from starlette.templating import Jinja2Templates
template = Jinja2Templates(directory='templates')
from card.cardapi import card_router
from users.user_api import user_router
from transaction.transfersapi import trans_router
from database import Base, engine
from currency.currencyapi import currency_router
from html_example.html_show import html_router
Base.metadata.create_all(bind=engine)
app.include_router(html_router)
app.include_router(card_router)
app.include_router(user_router)
app.include_router(currency_router)
app.include_router(trans_router)
