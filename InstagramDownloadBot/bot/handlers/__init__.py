from bot.handlers.instagram import insta_router
from bot.handlers.main import *

dp.include_routers(*[
    insta_router,
])