from odoo import tools, models, fields, api, _
from odoo.exceptions import ValidationError
import openpyxl
import base64
from datetime import date,datetime
import csv
import json
import os
from odoo.tools.safe_eval import safe_eval

class ResCurrency(models.Model):
    _inherit = 'res.currency'

    @api.model
    def cron_res_currency(self):
        param_directory = self.env['ir.config_parameter'].get_param('LEADSOLUTIONS_DIRECTORY','/tmp/')
        if not param_directory.endswith('/'):
            param_directory = param_directory + '/'
        if not os.path.isdir(param_directory):
            os.mkdir(param_directory)
        f = open(param_directory + 'archivo.csv','w')
        employee_writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        employee_writer.writerow(['John Smith', 'Accounting', 'November'])
        employee_writer.writerow(['Erica Meyers', 'IT', 'March'])
        f.close()
