#############################################################
# THIS IS A PRODUCT OF A COOPERATION AGREEMENT BETWEEN
# AITIC S.A.S. AND MASTERCORE S.A.S.
#
# Maintainers: odoo-dev@mastercore.net
#############################################################

from odoo import api, fields, models
from odoo.exceptions import UserError, ValidationError
from odoo.tests import Form
from dateutil.relativedelta import relativedelta
from odoo.tools.translate import _


class StockPicking(models.Model):
    _inherit = 'stock.book'

    pre_printed = fields.Boolean(string="it's a pre-printed book?")
    cai = fields.Char(string='C.A.I')
    cai_due_date = fields.Date(string='Fecha Vto CAI')
