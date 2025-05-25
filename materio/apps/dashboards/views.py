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

        student = Student.objects.select_related('program').all()[:63]

        context['student_data1'] = {
            'firstname': student[0].firstname,
            'lastname': student[0].lastname,
            'student_id': student[0].student_id,
            'program': student[0].program,
            'college': student[0].program.college.college_name
        }

        context['student_data2'] = {
            'firstname': student[1].firstname,
            'lastname': student[1].lastname,
            'student_id': student[1].student_id,
            'program': student[1].program,
            'college': student[1].program.college.college_name
        }

        context['student_data3'] = {
            'firstname': student[2].firstname,
            'lastname': student[2].lastname,
            'student_id': student[2].student_id,
            'program': student[2].program,
            'college': student[2].program.college.college_name
        }

        context['student_data4'] = {
            'firstname': student[3].firstname,
            'lastname': student[3].lastname,
            'student_id': student[3].student_id,
            'program': student[3].program,
            'college': student[3].program.college.college_name
        }

        context['student_data5'] = {
            'firstname': student[4].firstname,
            'lastname': student[4].lastname,
            'student_id': student[4].student_id,
            'program': student[4].program,
            'college': student[4].program.college.college_name
        }

        context['student_data6'] = {
            'firstname': student[5].firstname,
            'lastname': student[5].lastname,
            'student_id': student[5].student_id,
            'program': student[5].program,
            'college': student[5].program.college.college_name
        }

        context['student_data7'] = {
            'firstname': student[6].firstname,
            'lastname': student[6].lastname,
            'student_id': student[6].student_id,
            'program': student[6].program,
            'college': student[6].program.college.college_name
        }

        context['student_data8'] = {
            'firstname': student[7].firstname,
            'lastname': student[7].lastname,
            'student_id': student[7].student_id,
            'program': student[7].program,
            'college': student[7].program.college.college_name
        }

        return context