# your_app_name/dashboard.py
from admin_tools.dashboard import modules, Dashboard
from django.utils.translation import ugettext_lazy as _

class CustomIndexDashboard(Dashboard):
    def init_with_context(self, context):
        self.children.append(modules.ModelList(
            _('My Models'),
            models=('intro.models.Order',),
        ))
