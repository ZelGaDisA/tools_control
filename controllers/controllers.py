from odoo import http
from odoo.http import request
import requests
import json


class ToolsControl(http.Controller):
    @http.route('/tools/get_all_alerts', auth='user', type='json')
    def all_alerts(self, **kw):
        # session_id = http.request.env['ir.http'].sudo().search([])
        # print(session_id)
        alert_rec = http.request.env['tools_control.tools_control'].sudo().search([])
        alerts = []
        for rec in alert_rec:
            alerts.append({
                'action': rec.action,
                'date': rec.date,
                'area': rec.area,
                'photo': rec.photo,
            })
        print()
        return alerts

    @http.route('/tools/create_alert', auth='user', type='json')
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

    @http.route('/tools/ping', type='json', auth='public')
    def ping(self):
        return {'success': True}

    @http.route('/tools/custom_auth', type='json', auth='public')
    def get_session_id(self, url, db, login, password):
        urls = f"{url}/web/session/authenticate"
        payload = json.dumps({
            "jsonpc": "2.0",
            "params": {
                "db": db,
                "login": login,
                "password": password
            }
        })
        headers = {'Content-Type': 'application/json'}
        try:
            response = requests.request("GET", urls, headers=headers, data=payload)
            if response.json().get('error'):
                return response.json()
            session_id = ((response.headers.get("Set-Cookie").split(';')[0]).split('session_id=')[1])
            data_response = (response.json())
            data = {
                'data': data_response,
                'session_id': session_id,
            }
            return data
        except ValueError:
            return ValueError

