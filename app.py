import os
from dotenv import load_dotenv
from flask import Flask
from flask_migrate import Migrate
from api import api
from db import db
from export import ma

load_dotenv()

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DB_URL")

db.init_app(app)
ma.init_app(app)
Migrate(app, db)

app.register_blueprint(api, url_prefix="/api")


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
