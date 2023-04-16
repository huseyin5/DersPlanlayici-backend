from sqlalchemy import Column, Integer, String

from .db import db


class Egitmen(db.Model):
    __tablename__ = "egitmenler"

    egitmen_id = Column(Integer, primary_key=True)
    egitmen_adi = Column(String)
    egitmen_soyadi = Column(String)
    egitmen_alani = Column(String)
