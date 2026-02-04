from odoo import _, api, fields, models

class AccountMove(models.Model):
    _inherit = 'account.move'

    approval_history_ids = fields.One2many('approval.matrix.history', 'account_move_id', string='Approval History')
    