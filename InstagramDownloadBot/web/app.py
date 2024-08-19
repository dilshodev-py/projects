from typing import Dict, Any

import uvicorn
from starlette.applications import Starlette
from starlette.middleware import Middleware
from starlette_admin.contrib.sqla import Admin, ModelView
from db.models.base import db
from db import User, Referal
from web.provider import UsernameAndPasswordProvider
from starlette.middleware.sessions import SessionMiddleware
from config import conf

middleware = [
    Middleware(SessionMiddleware, secret_key=conf.web.SECRET_KEY)
]

app = Starlette(middleware=middleware)

logo_url = 'https://telegra.ph/file/f7aadb6d595a7d210b206.png'
admin = Admin(
    engine=db._engine,
    title="Aiogram Web Admin",
    logo_url=logo_url,
    auth_provider=UsernameAndPasswordProvider(),
    middlewares=middleware
)



admin.add_view(ModelView(User))
admin.add_view(ModelView(Referal))

# Mount admin to your app
admin.mount_to(app)

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8080)
