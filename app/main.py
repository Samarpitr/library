from app.api.endpoints.books import books_router 
from fastapi import FastAPI
# from app.db import db_setup
app = FastAPI()

#including books router
app.include_router(books_router)


#Commented this as integrating alembic for managing the migrations

# @app.on_event("startup") 
# async def on_startup():
#     '''Creates tables on starup of the application'''
#     await db_setup.init_db()

