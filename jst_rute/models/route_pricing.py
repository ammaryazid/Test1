from odoo import _, api, fields, models


class RoutePricing(models.Model):
    _name = 'route.pricing'
    _description = 'Route Pricing'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Name')
    origin_id = fields.Many2one('res.partner', string='Origin')
    destination_id = fields.Many2one('res.partner', string='Destination')
    distance_mil = fields.Float(string='Distance (Mil)')
    moq_wmt = fields.Float(string='MOQ (WMT)')
    margin = fields.Float(string='Margin (%)')
    sale_price_unit = fields.Float(string='Sale Price Unit')
    currency_id = fields.Many2one(
        'res.currency',
        string='Currency',
        default=lambda self: self.env.company.currency_id
    )

    line_ids = fields.One2many(
        'route.pricing.line',
        'route_id',
        string='Structure Price'
    )


class RoutePricingLine(models.Model):
    _name = 'route.pricing.line'
    _description = 'Route Pricing Line'

    route_id = fields.Many2one('route.pricing', string='Route', ondelete='cascade')
    category_id = fields.Many2one('product.category', string='Category')
    product_id = fields.Many2one('product.product', string='Component')
    qty = fields.Float(string='Qty', default=1.0)
    uom_id = fields.Many2one('uom.uom', string='UoM')
    price = fields.Float(string='Price')

    subtotal = fields.Float(
        string='Subtotal',
        compute='_compute_subtotal',
        store=True
    )

    cost_wmt = fields.Float(
        string='Cost/WMT',
        compute='_compute_cost_wmt',
        store=True
    )

    @api.depends('qty', 'price')
    def _compute_subtotal(self):
        for line in self:
            line.subtotal = line.qty * line.price

    @api.depends('subtotal', 'route_id.moq_wmt')
    def _compute_cost_wmt(self):
        for line in self:
            if line.route_id.moq_wmt:
                line.cost_wmt = line.subtotal / line.route_id.moq_wmt
            else:
                line.cost_wmt = 0.0
