import uvicorn

from starlette.applications import Starlette
from starlette.middleware import Middleware
from starlette.middleware.sessions import SessionMiddleware
from starlette_admin.contrib.sqla import Admin, ModelView

from db.config import engine
from db.models import User, Book, Category

from web.provider import UsernameAndPasswordProvider

app = Starlette()  # FastAPI()

# Create admin
admin = Admin(
    engine,
    title="Example: SQLAlchemy",
    base_url='/',
    auth_provider=UsernameAndPasswordProvider(),
    middlewares=[Middleware(SessionMiddleware, secret_key="qewrerthytju4")],
)

class BookModelView(ModelView):
    # fields = ['title']
    exclude_fields_from_create = ["created_at" , 'updated_at']
    exclude_fields_from_list = ["created_at" , 'updated_at']

admin.add_view(ModelView(User))
admin.add_view(BookModelView(Book))
admin.add_view(ModelView(Category))

admin.mount_to(app)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
