import os
from dotenv import load_dotenv
from flask import Flask
from flask_migrate import Migrate
from flask_cors import CORS
from api import api
from db import db
from export import ma

load_dotenv()

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DB_URL")

db.init_app(app)
ma.init_app(app)
Migrate(app, db)
CORS(app, supports_credentials=True, resources="*", origins=["http://localhost:5000", "http://localhost:5173"])

app.register_blueprint(api, url_prefix="/api")

if __name__ == '__main__':
    app.run()
