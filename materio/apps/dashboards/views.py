from django.views.generic import TemplateView
from .models import College, Organization, OrgMember, Program, Student
from web_project import TemplateLayout


class DashboardsView(TemplateView):
    def get_context_data(self, **kwargs):
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        context['colleges_count'] = College.objects.count()
        context['organizations_count'] = Organization.objects.count()
        context['programs_count'] = Program.objects.count()
        context['students_count'] = Student.objects.count()

        return context