from odoo import models, fields

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    x_under_group = fields.Selection([
        ('finished_goods', 'Finished Goods'),
        ('raw_material', 'Raw Material'),
        ('packaging_products', 'Packaging Products'),
        ('pvc_cling_film', 'PVC Cling Film'),
        ('export_items', 'Export Items'),
        ('aluminium_foil', 'Aluminium Foil'),
        ('bopp_tape', 'BOPP Tape'),
        ('tissue_paper', 'Tissue Paper'),
        ('disposables', 'Disposables'),
    ], string='Under Group', help="Categorize product under specific business groups")

    x_brand = fields.Char(string='Brand', help="E.g., Naman, My Foil, Home One, Freshwrap")
    x_matl_core = fields.Char(string='Material + Core Details', help="E.g., 900 + 100")
    x_micron = fields.Char(string='Micron / Specification', help="E.g., 11 Micron, 18 X 295")
    x_matl_wt = fields.Float(string='Material Wt (Grams/Kgs)')
    x_core_wt = fields.Float(string='Core Wt (Grams/Kgs)')
    x_gr_wgt = fields.Float(string='Gross Wt (Grams/Kgs)')
    x_qtty_box = fields.Float(string='Nos per Box/Pack')
