from db import Egitmen, Sinif, Ders
from .ma import ma


# Kayıt Ekleme ve Listeleme Şemaları

class EgitmenSema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Egitmen
        load_instance=True


class SinifSema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Sinif
        load_instance=True



class DersSema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Ders
        load_instance=True

