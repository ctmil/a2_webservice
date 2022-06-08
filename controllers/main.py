# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
import json

class LeadSolutions(http.Controller):

    @http.route('/holaecuador', auth='public')
    def hola_ecuador(self, **kwargs):
        return('<h1>Hola Ecuador!!!</h1>')

    @http.route(['/read_partner_data/<x_partner>'], auth='public')
    def read_partner_data(self, db=None, user=None, pwd=None, **kwargs):
        if db and user and pwd:
            uid = request.session.authenticate(db, user, pwd)
            if uid:
                url,params = request.httprequest.url.split('?')
                items = url.split('/')
                partner = items[len(items)-1]
                try:
                    partner_obj = request.env['res.partner'].browse(int(partner))
                    return json.dumps({
                        'name': partner_obj.name,
                        'ref': partner_obj.ref,
                        'email': partner_obj.email,
                    })
                except:
                    return request.render('website.404')
            else:
                return request.render('website.404')



class Todo(http.Controller):

    @http.route('/helloworld', auth='public')
    def hello_world(self, **kwargs):
        return('<h1>Hello World!</h1>')

    @http.route(['/get_partner_data/<x_partner>'], auth='public')
    def partners_json(self, db=None, user=None, pwd=None, **kwargs):
        url,params = request.httprequest.url.split('?')
        items = url.split('/')
        partner = items[len(items)-1]
        if db and user and pwd and partner:
            uid = request.session.authenticate(db, user, pwd)
            if uid:
                partner_obj = request.env['res.partner'].browse(int(partner))
                return json.dumps({
                    'name': partner_obj.name,
                    'ref': partner_obj.ref
                    })
        return json.dumps({
                'test': 'data'
                })
