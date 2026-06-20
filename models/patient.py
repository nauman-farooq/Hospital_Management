from odoo import api, fields, models

class HospitalPatient(models.Model):
    # Following line creates a model automatically in Odoo which is linked to the PostGres table
    _name = 'hospital.patient'
    _description = 'Patient Master'

    # we have imported fields class at line one, so that's why we used in following fields.
    name = fields.Char(string="Patient Name", required=True)
    date_of_birth = fields.Date(string="DOB", required=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string="Gender")
