from flask import Blueprint, request, jsonify

from db import db
from utility import filtrele


def genel_api_olustur(isim, db_sinifi, sema_sinifi):
    bp = Blueprint(isim, __name__)

    @bp.route("/", methods=["GET"])
    def tumu():
        kayitlar = filtrele(db_sinifi)
        sema = sema_sinifi()
        return sema.dump(kayitlar)

    @bp.route("/<int:id>", methods=["GET"])
    def detay(id):
        detay = db.get_or_404(db_sinifi, id)
        sema = sema_sinifi()
        return sema.dump(detay)

    @bp.route("/", methods=["POST"])
    def ekle():
        yeni_kayit = request.json
        yeni = db_sinifi(**yeni_kayit)
        db.session.add(yeni)
        db.session.commit()
        sema = sema_sinifi()
        return sema.dump(yeni)

    @bp.route("/<int:id>", methods=["PUT", "PATCH"])
    def guncelle(id):
        kayit = db.get_or_404(db_sinifi, id)
        kayit_bilgileri = request.json
        sema = sema_sinifi()
        yeni_kayit = sema.load(kayit_bilgileri, instance=kayit, session=db.session)
        db.session.commit()
        return sema.dump(yeni_kayit)

    @bp.route("/<int:id>", methods=["DELETE"])
    def sil(id):
        kayit = db.get_or_404(db_sinifi, id)
        db.session.delete(kayit)
        db.session.commit()
        return jsonify({"sonuc": "TAMAM"})

    return bp
