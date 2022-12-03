# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class ToolsControl(http.Controller):
    @http.route('/tools_control/tools_control', auth='public', crf=False)
    def index(self, **kw):
        return "Hello, world"

    @http.route('/get_tools_control', type="json", auth='public', cors='*', crf=False)
    def get_all_alert(self):
        alert_rec = request.env['tools_control.tools_control'].sudo.search([])
        alerts = []
        for rec in alert_rec:
            print('rec.photo', type(rec.photo))
            vals = {
                'id': rec.id,
                'action': rec.action,
                'date': rec.date,
                'area': rec.area,
                'photo': rec.photo,
            }
            alerts.append(vals)
        data = {
            'status': '200',
            'message': 'success',
            'response': alerts
        }
        return data

    @http.route('/tools_control/tools_control/objects', auth='public', crf=False)
    def list(self, **kw):
        return http.request.render('tools_control.listing', {
            'root': '/tools_control/tools_control',
            'objects': http.request.env['tools_control.tools_control'].search([]),
        })

    @http.route('/tools_control/tools_control/objects/<model("tools_control.tools_control"):obj>', auth='public', crf=False)
    def object(self, obj, **kw):
        return http.request.render('tools_control.object', {
            'object': obj
        })
