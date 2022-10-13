# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class nahereplenishmentbutton(models.Model):
     _inherit = 'res.currency.rate'
     
     def action_update_replenishment_cost(self, default=None):
          
          self.env['product.template'].cron_update_cost_from_replenishment_cost()
          return True