from config import db_uri
db_uri.turn_async()

from fastapi import FastAPI
from endpoints import define_end_points
from models.person import Person


app = FastAPI()

app = define_end_points(app)

print('main call __name__', __name__)

