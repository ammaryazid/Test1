from odoo import _, api, fields, models
from odoo.exceptions import ValidationError, UserError


class ResPartner(models.Model):
    _inherit = 'res.partner'
    
    is_customer = fields.Boolean('Is Customer')
    is_vendor = fields.Boolean('Is Vendor')
    supplier_site = fields.Char('Supplier Site')

    state = fields.Selection([
        ('draft', 'Draft'),
        ('waiting_approval', 'Waiting Approval'),
        ('approved', 'Approved'),
    ], string='Status', default='draft')
    
    # approval_history_ids = fields.One2many('approval.matrix.history', 'res_partner_id', string='Approval History')

    def action_request_for_approval(self):
        for rec in self:
            rec.write({'state': 'waiting_approval'})

    def action_approve(self):
        for rec in self:
            rec.write({'state': 'approved', 'active': True})
            rec.supplier_rank += 1

    def action_draft(self):
        for rec in self:
            rec.write({'state': 'draft'})

    # DYNAMIC APPROVAL FUNCTIONS
    # def dynamic_action_request_approval(self):
    #     for rec in self:
    #         try:
    #             self.env['approval.matrix'].create_approval_history(record=rec, fk='res_partner_id')
    #         except UserError as e:
    #             raise
    #         rec.action_request_for_approval()

    # def dynamic_action_approve(self):
    #     for rec in self:
    #         approval_status = False
    #         params = {
    #             "status": "approved",
    #         }
    #         try:
    #             approval_status = self.env['approval.matrix'].update_approval_history(record=rec, fk='res_partner_id', params=params)
    #         except UserError as e:
    #             raise

    #         if approval_status == "approved":
    #             return rec.action_approve()

    # def dynamic_action_reject(self):
    #     for rec in self:
    #         approval_status = False
    #         params = {
    #             "status": "rejected",
    #             "approval_note": "Rejected by %s" % self.env.user.name
    #         }
    #         try:
    #             approval_status = self.env['approval.matrix'].update_approval_history(record=rec, fk='res_partner_id', params=params)
    #         except UserError as e:
    #             raise

    #         if approval_status == "rejected":
    #             return rec.action_draft()
