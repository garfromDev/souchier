# -*- coding: utf-8 -*-

from odoo import models, fields, api

# class openacademy(models.Model):
#     _name = 'openacademy.openacademy'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100
class Emplacement(models.Model):
    _name = 'souchier.emplacement'
    name = fields.Char(string="Emplacement", required=True, index=True)
    occupe_par = fields.many2one(comodel_name='souchier.souche', required=False,
                                 , ondelete='set null')
    
    
class Souche(models.Model):
    _name = 'souchier.souche'
    
    name = fields.Char(string="Souche", required=True, index=True)
    description = fields.Text(string="Description")
    _sql_constraints = [('name', 'unique(name)',
                         "Le nom de la souche doit etre unique")]
    client = fields.many2one(comodel_name='res.users', string="Client",
                             required=True, ondelete='restrict')
    emplacement = fields.many2one(comodel_name='souchier.emplacement',
                                  string="Emplacement master",
                                  ondelete="restrict",
                                  required=True)

    emplacements_WS = fields.one2many(comodel_name='souchier.emplacement',
                                       string="Emplacements working seeds",
                                       ondelete='restrict',
                                      inverse_name='occupe_par',
                                       required=False)
    date_reception = fields.Date(required=True)
    
                        
