from sqlalchemy import Column, Integer, String, ForeignKey

from .db import db


class Ders(db.Model):
    __tablename__ = "dersler"

    ders_id = Column(Integer, primary_key=True)
    ders_adi = Column(String)
    ders_ogretmen_id = Column(Integer, ForeignKey('ogretmenler.ogretmen_id'))
    ders_sinif_id = Column(Integer, ForeignKey('siniflar.sinif_id'))
