from bot.handlers.main import main_router
from bot.handlers.menu import menu_router
from bot.handlers.work_place import work_place_router
from bot.handlers.language import language_router
from dispatcher import dp

dp.include_routers(
    *[language_router,
      main_router ,
      work_place_router,
      menu_router]
)