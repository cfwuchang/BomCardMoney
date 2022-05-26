
from odoo import api,fields,models,_
import datetime
class BomCardMoney(models.Model):
	_inherit = "bom.card"

	money = fields.Float(string=u"金额",help='非自动计算值，需要手动填写')
	
	

		
