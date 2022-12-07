# -- coding: utf-8 --

from odoo import api, models
from odoo.http import request


class Http(models.AbstractModel):
    _inherit = 'ir.http'

    def session_info(self):
        res = super(Http, self).session_info()
        if not res.get('session_id'):
            # Add Session id
            res['session_id'] = request.session.sid
        return res