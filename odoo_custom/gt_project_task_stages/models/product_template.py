
from odoo import models, fields, api
class ProductTempalte(models.Model):
    _inherit = 'product.template'

    task_stage_template_id = fields.Many2one("task.stage.template", string="Task Stage Template")
    task_stage_ids = fields.Many2many("project.task.type", string="Task Stage", domain="[('user_id', '=', False)]")

    @api.onchange('task_stage_template_id')
    def _onchange_task_stage(self):
        self.task_stage_ids = self.task_stage_template_id.stage.ids
