from odoo import models, fields

class MrpBom(models.Model):
    _inherit = 'mrp.bom'

    x_under_group = fields.Selection(related='product_tmpl_id.x_under_group', readonly=False, store=True, string='Under Group')
    x_brand = fields.Char(related='product_tmpl_id.x_brand', readonly=False, store=True, string='Brand')
    x_matl_core = fields.Char(related='product_tmpl_id.x_matl_core', readonly=False, store=True, string='Material + Core Details')
    x_micron = fields.Char(related='product_tmpl_id.x_micron', readonly=False, store=True, string='Micron / Specification')
    x_matl_wt = fields.Float(related='product_tmpl_id.x_matl_wt', readonly=False, store=True, string='Material Wt (Grams/Kgs)')
    x_core_wt = fields.Float(related='product_tmpl_id.x_core_wt', readonly=False, store=True, string='Core Wt (Grams/Kgs)')
    x_gr_wgt = fields.Float(related='product_tmpl_id.x_gr_wgt', readonly=False, store=True, string='Gross Wt (Grams/Kgs)')
    x_qtty_box = fields.Float(related='product_tmpl_id.x_qtty_box', readonly=False, store=True, string='Nos per Box/Pack')


class MrpBomLine(models.Model):
    _inherit = 'mrp.bom.line'

    x_finished_product = fields.Many2one(related='bom_id.product_tmpl_id', readonly=True, store=True, string='Finished Product')
    x_under_group = fields.Selection(related='product_id.x_under_group', readonly=True, string='Under Group')
    x_brand = fields.Char(related='product_id.x_brand', readonly=True, string='Brand')
    x_matl_core = fields.Char(related='product_id.x_matl_core', readonly=True, string='Material + Core Details')
    x_micron = fields.Char(related='product_id.x_micron', readonly=True, string='Micron / Specification')
    x_matl_wt = fields.Float(related='product_id.x_matl_wt', readonly=True, string='Material Wt (Grams/Kgs)')
    x_core_wt = fields.Float(related='product_id.x_core_wt', readonly=True, string='Core Wt (Grams/Kgs)')
    x_gr_wgt = fields.Float(related='product_id.x_gr_wgt', readonly=True, string='Gross Wt (Grams/Kgs)')
    x_qtty_box = fields.Float(related='product_id.x_qtty_box', readonly=True, string='Nos per Box/Pack')
