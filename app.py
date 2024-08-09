from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
import os


from models import db
from web import web_page
from helpers import get_index_page_data

from models import (
    db,
    Title,
    Description,
    Photo,
    Post,
    PublishTime,
)


app = Flask(__name__)
app.config.from_object('settings')

db.init_app(app=app)
CORS(app)
migrate = Migrate(app=app, db=db)


app.register_blueprint(web_page)

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5432, debug=True)
