from db import Egitmen, Sinif, Ders
from .ma import ma


# Kayıt Ekleme ve Listeleme Şemaları

class EgitmenSema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Egitmen


class SinifSema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Sinif


class DersSema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Ders
