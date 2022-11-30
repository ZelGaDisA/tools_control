# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo import modules
import requests
import logging
import base64


def create_string():
    self = str.split(',')
    print(self)
    return self[-1]


class ToolsControl(models.Model):
    _name = 'tools_control.tools_control'
    _description = 'tools_control.tools_control'

    action = fields.Char()
    date = fields.Char()
    area = fields.Char()
    photo = fields.Binary(string="Image")

    def create(self, action, date, area, photo):
        self.action = action
        self.date = date
        self.area = area
        self.photo = (photo.split(','))[-1]


