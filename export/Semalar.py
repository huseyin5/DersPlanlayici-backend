from db import Egitmen, Sinif
from .ma import ma


# Kayıt Ekleme ve Listeleme Şemaları

class EgitmenSema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Egitmen


class SinifSema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Sinif


class DersSema(ma.SQLAlchemyAutoSchema):
    # AutoSchema foreignKey'leri görmezden geliyor bunun için include_fk kullanırız
    class Meta:
        model = Sinif
