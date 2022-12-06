# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
import json


class ToolsControl(http.Controller):
    @http.route('/tools/get_all_alerts', auth='user', crf=True, cors='*', type='json', methods=['POST'])
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

    @http.route('/tools/create_alert', auth='user', website=False, crf=True, cors='*', type='json', methods=['POST'])
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

    @http.route('/tools/ping', type='json', auth='public', cors='*', crf=False, methods=['POST'])
    def ping(self):
        return {'success': True}
