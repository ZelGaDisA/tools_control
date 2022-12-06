# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
import json


class ToolsControl(http.Controller):
    @http.route('/tools_control/tools_control', auth='public', crf=False)
    def index(self, **kw):
        return "Hello, world"

    @http.route('/api', auth='public', website=False, crf=True, cors='*', type='json', methods=['GET'])
    def all_alerts(self, **kw):
        alert_rec = http.request.env['tools_control.tools_control'].sudo().search([])
        alerts = []
        for rec in alert_rec:
            alerts.append({
                'action': rec.action,
                'date': rec.date,
                'area': rec.area,
                'photo': rec.photo,
            })

        return alerts

    @http.route('/create_alert', auth="public", type='json')
    def create(self, **rec):
        if http.request.render:
            if rec['action']:
                vals = {
                    'action': rec['action'],
                    'date': rec['date'],
                    'area': rec['area'],
                    'photo': rec['photo'],
                }
                new_alert = request.env['tools_control.tools_control'].sudo().create(vals)
                args = {'success': True, 'message': 'Success', 'ID': new_alert.id}
        return args

    @http.route('/data_accessed', auth="public")
    def get_all_record(self, **kw):
        tools_control = http.request.env['tools_control.tools_control'].search([])
        for record in tools_control:
            print(record['area'])
        return "<h1>Data Accessed</h1>"
