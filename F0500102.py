# -*- coding: utf-8 -*-

from openerp import models, fields


class AModel1(models.Model):

    _name = 'a.model1.name'
# там где цифры интеджер - сайзов нет, а там где буквы Чар+ сайз, булен там где галочки
    htin = fields.Char(help="######", required=True, size=15) ###
    hpages = fields.Integer(string="Стор.")
    hj = fields.Boolean(string="юридична особа", required=True)
    hf = fields.Boolean(string="фізична особа####", required=True)
    hz = fields.Boolean(string="звітний", required=True)
    hzn = fields.Boolean(string="новий звітний", required=True)
    hzu = fields.Boolean(string="уточнюючий", required=True)
    hname = fields.Char(help="назва юр особи", required=True, size=200)
    ###
    htinsti = fields.Char(string="ідентифікаційний код", required=True, size=8)
    hsti = fields.Char(string="назва органу податкової служби", required=True, size=99)
    hzp = fields.Char(string="звітний період", required=True)
    hzy = fields.Integer(string="звітний рік", required=True)
    r00g01i = fields.Integer(string="працювало у штаті")
    r00g02i = fields.Integer(string="працювало за сумісництвом")
    r00g03i = fields.Integer(string="заповнюється в органі", help="№№№№№№№№")

    r01g03a = fields.Float(string="Сума нарахованого доходу, всього", help="грн.,коп.", digits=(10, 2))
    r01g03 = fields.Float(string="#####################", help="грн.,коп.", digits=(10, 2))
    r01g04a = fields.Float(string="####################, всього", help="грн.,коп.", digits=(10, 2))
    r01g04 = fields.Float(string="#########################, всього", help="грн.,коп.", digits=(10, 2))

    r02g01i = fields.Integer(string="кількість рядків")
    r02g02i = fields.Integer(string="кількість фізичних осіб")
    r02g03i = fields.Integer(string="кількість аркушів")
    hkbos = fields.Integer(string="керівник підприємства", help="ідентифікаційний номер")
    hbos = fields.Char(help="прізвище", size=50)
    htelbos = fields.Char(help="тел", size=20)
    hkbuh = fields.Integer(string="головний бухгалтер", help="ідентифікаційний номер")
    hbuh = fields.Char(help="прізвище", size=50)
    htelbuh = fields.Char(help="тел", size=20)

    hfo = fields.Char(string="фізична особа прізвище", help="прізвище", size=50, required=True)
    htelfo = fields.Char(help="тел", size=20)
    hfill = fields.Date(string="дата подання", help="дд.мм.рррр", required=True)

class AModel2(models.Model):

    _name = 'a.model2.name'

    amodel1_id = fields.Many2one('a.model1.name')

    rxxxxg02 = fields.Integer(string="ідентифікаційний номер")
    rxxxxg03a = fields.Float(string="сума нарахованого доходу", help="грн.,коп.", digits=(10, 2))
    rxxxxg03 = fields.Float(string="сума виплаченого доходу", help="грн.,коп.", digits=(10, 2))
    rxxxxg04a = fields.Float(string="сума утриманого податку, нарахованого", help="грн.,коп.", digits=(10, 2))
    rxxxxg04 = fields.Float(string="сума утриманого податку, перерахованого", help="грн.,коп.", digits=(10, 2))
    rxxxxg05 = fields.Char(string="ознака доходу", size=100)
    rxxxxg06d = fields.Date(string="дата прийняття на роботу", help="дд.мм.рррр")
    rxxxxg07d = fields.Date(string="дата звільнення з роботи", help="дд.мм.рррр")
    rxxxxg08 = fields.Char(string="ознака подат.соц.пільги", size=100)
    rxxxxg09 = fields.Integer(string="ознака", help="(0,1)")

