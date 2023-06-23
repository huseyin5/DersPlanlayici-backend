from flask import Blueprint
from flask_cors import CORS

from api.genel_api import genel_api_olustur
from db import Egitmen, Ders, Sinif, Atama
from export.Semalar import EgitmenSema, DersSema, SinifSema, AtamaSema

v1 = Blueprint('v1', __name__)
v1.register_blueprint(genel_api_olustur("egitmen", Egitmen, EgitmenSema), url_prefix="/egitmen")
v1.register_blueprint(genel_api_olustur("ders", Ders, DersSema), url_prefix="/ders")
v1.register_blueprint(genel_api_olustur("sinif", Sinif, SinifSema), url_prefix="/sinif")
v1.register_blueprint(genel_api_olustur("atama", Atama, AtamaSema), url_prefix="/atama")

api = Blueprint('api', __name__)
api.register_blueprint(v1, url_prefix="/v1")

CORS(api)
