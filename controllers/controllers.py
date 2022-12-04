# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
import json


class ToolsControl(http.Controller):
    @http.route('/tools_control/tools_control', auth='public', crf=False)
    def index(self, **kw):
        return "Hello, world"

    # @http.route('/api', auth='public', website=False)
    @http.route('/api', auth='public', website=False, crf=False, type='json', methods=['GET', 'POST'])
    def all_alerts(self, **kw):
        alert_rec = http.request.env['tools_control.tools_control'].sudo.search([])
        alerts = []
        for rec in alert_rec:
            alerts.append({
                'action': rec.action,
                'date': rec.date,
                'area': rec.area,
                'photo': rec.photo,
            })

        return alerts


    @http.route('/get_tools_control', type="json", auth='public', cors='*', methods=['GET', 'POST'], crf=False)
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
