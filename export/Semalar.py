from db import Ogretmen, Sinif
from .ma import ma


# Kayıt Ekleme ve Listeleme Şemaları

class OgretmenSema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Ogretmen


class SinifSema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Sinif


class DersSema(ma.SQLAlchemyAutoSchema):
    # AutoSchema foreignKey'leri görmezden geliyor bunun için include_fk kullanırız
    class Meta:
        model = Sinif
        include_fk = True
