from openerp import models, fields


class AModel1(models.Model):

    _name = 'a.model1.name'

    htin = fields.Char(string="ЭДРПОУ", required=True, max_length=18)
    hpages = fields.Char(string="Стор.", required=True, max_length=5)
    hj = fields.Char(string="юридична особа", required=True, max_length=99)
    hf = fields.Char(string="фізична особа", required=True, max_length=99)
    hz = fields.Char(string="звітний", required=True, max_length=15)
    hzn = fields.Char(string="новий звітний", required=True, max_length=15)
    hzu = fields.Char(string="уточнюючий", required=True, max_length=15)
    hname = fields.Char(string="назва юр особи", required=True, max_length=99)
    htinsti = fields.Char(int="ідентифікаційний код", required=True, max_length=8)
    hsti = fields.Char(string="назва органу податкової служби", required=True, max_length=99)
    hzp = fields.Char(string="звітний період", required=True, max_length=10)
    hzy = fields.Char(int="звітний рік", required=True, max_length=4)
    r00g01i = fields.Char(int="працювало у штаті", required=True, max_length=9)
    r00g02i = fields.Char(int="працювало за сумісництвом", required=True, max_length=9)
    r00g03i = fields.Char(int="заповнюється в органі", required=True, max_length=9)
    r02g01i = fields.Char(int="кількість рядків", required=True, max_length=9)
    r02g02i = fields.Char(int="кількість фізичних осіб", required=True, max_length=9)
    r02g03i = fields.Char(int="кількість аркушів", required=True, max_length=9)
    hkbos = fields.Char(int="керівник підприємства ідентифікаційний номер", required=True, max_length=8)
    hbos = fields.Char(string="керівник підприємства прізвище", required=True, max_length=20)
    htelbos = fields.Char(int="керівник підприємства тел", required=True, max_length=12)
    hkbuh = fields.Char(int="головний бухгалтер ідентифікаційний номер", required=True, max_length=8)
    hbuh = fields.Char(string="головний бухгалтер прізвище", required=True, max_length=20)
    htelbuh = fields.Char(int="головний бухгалтер тел", required=True, max_length=12)
    hfill = fields.Char(int="дата подання", required=True, max_length=8)
    hfo = fields.Char(string="фізична особа прізвище", required=True, max_length=20)
    htelfo = fields.Char(int="фізична особа тел", required=True, max_length=12)



class AModel2(models.Model):

    _name = 'a.model2.name'

    rxxxxg02 = fields.Char(int="ідентифікаційний номер", required=True, max_length=8)
    rxxxxg03a = fields.Float(float="сума нарахованого доходу", required=True, max_length=8)
    rxxxxg03 = fields.Float(float="сума виплаченого доходу", required=True, max_length=8)
    rxxxxg04a = fields.Float(float="сума утриманого податку, нарахованого", required=True, max_length=8)
    rxxxxg04 = fields.Float(float="сума утриманого податку, перерахованого", required=True, max_length=8)
    rxxxxg05 = fields.Float(float="ознака доходу", required=True, max_length=8)
    rxxxxg06d = fields.Float(float="дата прийняття на роботу", required=True, max_length=8)
    rxxxxg07d = fields.Float(float="дата звільнення з роботи", required=True, max_length=8)
    rxxxxg08 = fields.Float(float="ознака подат.соц.пільги", required=True, max_length=8)
    rxxxxg09 = fields.Float(float="ознака (0,1)", required=True, max_length=8)

