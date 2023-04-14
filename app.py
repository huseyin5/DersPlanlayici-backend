import os

from dotenv import load_dotenv
from flask import Flask

from vt.baglanti import vt, migrate

load_dotenv()

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DB_URL")

vt.init_app(app)
migrate.init_app(app, vt)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
