from odoo import models, fields, api

class FiltroFechaExistencias(models.Model):
    _name = 'filtro.fecha.existencias' 

    date = fields.Date(string='Date')
    location_id = fields.Many2one('stock.location', string="Location")

    @api.depends('date', 'location_id')
    def _compute_stock_quants(self):
        for record in self:
            if record.date and record.location_id:
                try:
                    stock_quants_grouped = self.env['stock.quant'].read_group([
                        ('location_id', '=', record.location_id.id),
                        ('product_id', '!=', False),
                        ('date', '=', record.date),
                    ], ['location_id', 'product_id', 'quantity'], ['location_id', 'product_id'])

                    record.stock_data = stock_quants_grouped 
                except Exception as e:
                    record.stock_data = []  # Set to empty list on errors 
            else:
                record.stock_data = []

    stock_data = fields.One2many(comodel_name='filtro.fecha.existencias.line', 
                                 inverse_name='filtro_id', 
                                 string="Stock Data")

class FiltroFechaExistenciasLine(models.Model):
    _name = 'filtro.fecha.existencias.line'

    filtro_id = fields.Many2one('filtro.fecha.existencias')
    location_id = fields.Many2one('stock.location', string="Location")
    product_id = fields.Many2one('product.product', string="Product")
    quantity = fields.Float(string="Quantity")
