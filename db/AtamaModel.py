from .db import db


class Atama(db.Model):
    atama_id = db.Column(db.BigInteger, primary_key=True)
    atama_durumu = db.Column(db.Boolen(), default=False)
    atama_tarih = db.Column(db.String(150))
    atama_gun = db.Column(db.Integer)
    atama_sonuc = db.Column(db.String(320000))
