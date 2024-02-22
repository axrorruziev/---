from fastapi import APIRouter, Request
from main import template

html_router = APIRouter(prefix='/web', tags=['Html example'])


@html_router.get('/home')
async def hello_page(request: Request):
    return template.TemplateResponse('index.html',
                                     context={'request': request})

