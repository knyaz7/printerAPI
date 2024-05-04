from database import db
from marshmallow import Schema, fields


class Print(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    printer_id = db.Column(db.Integer, db.ForeignKey('printer.id'), nullable=False)
    defect = db.Column(db.Integer, nullable=False)
    img_path = db.Column(db.String(127), nullable=False)
    quality = db.Column(db.Integer, nullable=False)

    def __init__(self, printer_id, defect, img_path, quality):
        self.printer_id = printer_id
        self.defect = defect
        self.img_path = img_path
        self.quality = quality

    def __repr__(self):
        return '<Print %r>' % self.printer_id


class PrintSchema(Schema):
    id = fields.Integer(dump_only=True)
    printer_id = fields.Integer(required=True)
    defect = fields.Integer(required=True)
    img_path = fields.String()
    quality = fields.Integer(required=True)
