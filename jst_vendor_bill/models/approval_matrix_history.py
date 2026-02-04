from odoo import _, api, fields, models

class ApprovalMatrixHistory(models.Model):
    _inherit = 'approval.matrix.history'
    _description = 'Approval Matrix History'
    
    account_move_id = fields.Many2one('account.move', string='Move')