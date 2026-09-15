from odoo import models, fields, api

class MrpProduction(models.Model):
    _inherit = 'mrp.production'

    x_under_group = fields.Selection(related='product_id.x_under_group', readonly=True, store=True, string='Under Group')
    x_operator = fields.Char(string='Operator', help='Operator Name / Shift Lead')
    x_machine = fields.Char(string='Machine / Line', help='Machine Number / Workcenter, e.g. Machine 1, Machine 2, Machine 3, Machine 5')
    x_brand = fields.Char(string='Brand', compute='_compute_custom_weights', store=True, readonly=False)
    x_matl_core = fields.Char(string='Material + Core Details', compute='_compute_custom_weights', store=True, readonly=False)
    x_micron = fields.Char(string='Micron / Specification', compute='_compute_custom_weights', store=True, readonly=False)
    x_matl_wt = fields.Float(string='Material Wt (Grams/Kgs)', compute='_compute_custom_weights', store=True, readonly=False)
    x_core_wt = fields.Float(string='Core Wt (Grams/Kgs)', compute='_compute_custom_weights', store=True, readonly=False)
    x_gr_wgt = fields.Float(string='Gross Wt (Grams/Kgs)', compute='_compute_custom_weights', store=True, readonly=False)
    x_qtty_box = fields.Float(string='Nos per Box/Pack', compute='_compute_custom_weights', store=True, readonly=False)

    x_total_net_wt = fields.Float(string='Total Net Material Wt', compute='_compute_total_production_weights', store=True, readonly=False, help="Total Net Material Weight (Qty * Material Wt)")
    x_total_core_wt = fields.Float(string='Total Core Wt', compute='_compute_total_production_weights', store=True, readonly=False, help="Total Core Weight (Qty * Core Wt)")
    x_total_gross_wt = fields.Float(string='Total Gross Wt', compute='_compute_total_production_weights', store=True, readonly=False, help="Total Gross Weight (Qty * Gross Wt)")
    x_scrap_loss_wt = fields.Float(string='Scrap / Wastage Wt (Kgs)', default=0.0, help="Actual scrap/trimming/wastage weight in Kgs during production run")

    @api.depends('product_id')
    def _compute_custom_weights(self):
        for record in self:
            if record.product_id:
                record.x_brand = getattr(record.product_id, 'x_brand', '') or ''
                record.x_matl_core = record.product_id.x_matl_core or ''
                record.x_micron = record.product_id.x_micron or ''
                record.x_qtty_box = record.product_id.x_qtty_box or 0.0
                record.x_matl_wt = record.product_id.x_matl_wt or 0.0
                record.x_core_wt = record.product_id.x_core_wt or 0.0
                record.x_gr_wgt = record.product_id.x_gr_wgt or 0.0
            else:
                record.x_brand = ''
                record.x_matl_core = ''
                record.x_micron = ''
                record.x_qtty_box = 0.0
                record.x_matl_wt = 0.0
                record.x_core_wt = 0.0
                record.x_gr_wgt = 0.0

    @api.depends('product_qty', 'qty_producing', 'x_matl_wt', 'x_core_wt', 'x_gr_wgt')
    def _compute_total_production_weights(self):
        for record in self:
            qty = record.qty_producing if (record.qty_producing and record.qty_producing > 0) else (record.product_qty or 0.0)
            record.x_total_net_wt = qty * (record.x_matl_wt or 0.0)
            record.x_total_core_wt = qty * (record.x_core_wt or 0.0)
            record.x_total_gross_wt = qty * (record.x_gr_wgt or 0.0)
