
from odoo import models, fields


class TaskStageTemplate(models.Model):
    _name = 'task.stage.template'
    _description = "Task Stage Template"

    name = fields.Char(string="Name")
    stage = fields.Many2many("project.task.type", string="Stage", domain="[('user_id', '=', False)]")
