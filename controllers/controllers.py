# -*- coding: utf-8 -*-
from odoo import http


class ToolsControl(http.Controller):
    @http.route('/tools_control/tools_control', auth='public', crf=False)
    def index(self, **kw):
        return "Hello, world"

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
