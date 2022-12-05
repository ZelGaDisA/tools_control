# -*- coding: utf-8 -*-
import json

from odoo import http
from odoo.http import request


class ToolsControl(http.Controller):

    @http.route('/api', auth='user', website=False, crf=True, cors='*', type='json', methods=['GET'])
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

    @http.route('/api_create', auth='public', website=False, crf=False, cors='*', type='json', methods=['GET', 'POST'])
    def create_alert(self, **kw):
        # http.request.env['tools_control.tools_control'].sudo().create({
        #         'action': kw['action'],
        #         'date': kw['date'],
        #         'area': kw['area'],
        #         'photo': kw['photo'],
        # alerts = http.request.env['tools_control.tools_control'].sudo().search([('id', '=', kw['id'])])
        alerts = http.request.env['tools_control.tools_control'].sudo().search([()])
        alerts.write({'action': kw['action'],
                      'date': kw['date'],
                      'area': kw['area'],
                      'photo': kw['photo'], })
        return kw

    @http.route('/get_tools_control', type="json", auth='public', cors='*', methods=['GET', 'POST'], crf=False)
    def get_all_alert(self):
        alert_rec = request.env['tools_control.tools_control'].sudo.search([])
        alerts = []
        for rec in alert_rec:
            print('rec.photo', type(rec.photo))
            vals = {
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

    @http.route('/tools_control/tools_control/objects/<model("tools_control.tools_control"):obj>', auth='public',
                crf=False)
    def object(self, obj, **kw):
        return http.request.render('tools_control.object', {
            'object': obj
        })

    @http.route('/api_alert', type='json', auth='user', methods=['POST'], cors='*', csrf=False)
    def create_employee(self, **kwargs):
        data = json.loads(request.httprequest.data)
        employee = request.env['tools_control.tools_control'].sudo().search([('action', '=', data.get('action'))])
        if employee:
            return {'message': 'already exists'}
        else:
            # Create
            home_action = request.env['tools_control.tools_control'].sudo().create({
                'action': 'action',
                'date': 'date',
                'area': 'area',
                'photo': 'photo',

            })
            if home_action:
                home_action = home_action.id
                employee = request.env['tools_control.tools_control'].sudo().create({
                    'date': data.get('date'),
                    'area': data.get('area'),
                    'photo': data.get('photo'),
                    'home_action.id': home_action
                })
                if employee:
                    employee = employee.id
            return {'message': 'Employee {} created'.format(employee)}

    @http.route('/create_alert', type="json", auth='public', crf=False)
    def create_patient(self, **rec):
        if request.jsonrequest:
            if rec['action']:
                vals = {
                    'action': rec['action'],
                    'date': rec['date'],
                    'area': rec['area'],
                    'photo': rec['photo'],
                }
                new_alert = request.env['tools_control.tools_control'].sudo().create(vals)
                args = {
                    'meaasge': 'success',
                    'success': 'True',
                    'data':
                        {
                            'id': new_alert.id,
                            'action': new_alert.action
                        },
                }
        return args
