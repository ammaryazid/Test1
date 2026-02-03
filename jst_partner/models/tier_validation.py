from odoo import _, api, fields, models


class TierValidation(models.AbstractModel):
    _inherit = 'tier.validation'

    def request_validation(self):
        if self._name == "res.partner":
            for rec in self:
                rec.action_request_for_approval()

        res = super().request_validation()

        return res

    def validate_tier(self):
        self.ensure_one()
        res = super().validate_tier()
        if self._name == "res.partner" and self.validated:
            self.action_approve()

        return res

    def restart_validation(self):
        res = super().restart_validation()
        if self._name == "res.partner":
            self.action_draft()

        return res
