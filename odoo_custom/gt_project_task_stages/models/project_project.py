
from odoo import models, fields, api


class ProjectProject(models.Model):
    _inherit = 'project.project'

    task_stage_template_id = fields.Many2one("task.stage.template", string="Task Stage Template")
    task_stage_ids = fields.Many2many("project.task.type", string="Task Stage", domain="[('user_id', '=', False)]")

    @api.onchange('task_stage_template_id')
    def _onchange_task_stage(self):
        self.task_stage_ids = self.task_stage_template_id.stage.ids


    @api.model
    def create(self, vals):
        res = super(ProjectProject, self).create(vals)
        if vals.get('task_stage_ids'):
            stage_id = self.env['project.task.type'].browse(vals.get('task_stage_ids')[0][2])
            stage_id.project_ids = [(4, res.ids[0])]
        return res
