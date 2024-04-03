
{
    "name": "Project Task Stages",
    "version": "17.0.1.0",
    "category": "Sale/Project",
    "summary": "Project Stages",
    "description": """Auto create project task stages""",
    "author": "Nguyen Dinh Tung",
    "maintainer": "Nguyen Dinh Tung.",
    "images": ["static/description/banner.jpg"],
    "depends": ['project', 'sale_management', 'sale_project'],
    "data": [
        "security/ir.model.access.csv",
        "views/task_stage_template_view.xml",
        "views/product_template_view.xml",
        "views/project_project_view.xml",
    ],
    "installable": True,
    "application": True,
    "auto_install": True,
    "license": "OPL-1",
}
