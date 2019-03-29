from flask import render_template, g
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder.models.sqla.filters import FilterEqualFunction
from flask_appbuilder import ModelView
from app import appbuilder, db
from app.models import Project, ProjectFiles

def get_user_id():
    return g.user.id

"""
    Create your Views::


    class MyModelView(ModelView):
        datamodel = SQLAInterface(MyModel)


    Next, register your Views::


    appbuilder.add_view(MyModelView, "My View", icon="fa-folder-open-o", category="My Category", category_icon='fa-envelope')
"""

class ProjectFilesModelView(ModelView):
    datamodel = SQLAInterface(ProjectFiles)

    label_columns = {'file_name': 'File Name', 'download': 'Download'}
    add_columns = ['file', 'description','project']
    edit_columns = ['file', 'description','project']
    list_columns = ['file_name', 'download']
    show_columns = ['file_name', 'download']


class ProjectModelView(ModelView):
    datamodel = SQLAInterface(Project)
    base_filters = [['created_by_fk', FilterEqualFunction, get_user_id]]
    related_views = [ProjectFilesModelView]

    show_template = 'appbuilder/general/model/show_cascade.html'
    edit_template = 'appbuilder/general/model/edit_cascade.html'

    add_columns = ['name']
    edit_columns = ['name']
    list_columns = ['name', 'created_by', 'created_on', 'changed_by', 'changed_on']
    show_fieldsets = [
        ('Info', {'fields': ['name']}),
        ('Audit', {'fields': ['created_by', 'created_on', 'changed_by', 'changed_on'], 'expanded': False})
    ]

"""
    Application wide 404 error handler
"""
@appbuilder.app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', base_template=appbuilder.base_template, appbuilder=appbuilder), 404

db.create_all()

appbuilder.add_view(ProjectModelView, "List Projects", icon="fa-table", category="Projects")
appbuilder.add_view_no_menu(ProjectFilesModelView)
