from django.views.generic import TemplateView
from .models import College, Organization, OrgMember, Program, Student
from web_project import TemplateLayout
from django.db.models import Count

class DashboardsView(TemplateView):
    template_name = 'dashboard_analytics.html'
    
    def get_context_data(self, **kwargs):
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))

        context['colleges_count'] = College.objects.count()
        context['organizations_count'] = Organization.objects.count()
        context['orgmember_count'] = OrgMember.objects.count()
        context['programs_count'] = Program.objects.count()
        context['students_count'] = Student.objects.count()

        context['college_cah'] = College.objects.get(college_name='College of Arts and Humanitiess')
        context['college_cba'] = College.objects.get(college_name='College of Business and Accountancy')
        context['college_cs'] = College.objects.get(college_name='College of Sciences')
        context['college_ec'] = College.objects.get(college_name='External Campuses')
        context['college_cc'] = College.objects.get(college_name='College of Criminal')

        context['program_social_work'] = Program.objects.get(prog_name='Bachelor of Science in Social Work')
        context['program_psychology'] = Program.objects.get(prog_name='Bachelor of Science in Psychology')
        context['program_accountancy'] = Program.objects.get(prog_name='Bachelor of Science in Accountancy')
        context['program_comm'] = Program.objects.get(prog_name='Bachelor of Arts in Communication')
        context['program_track2'] = Program.objects.get(prog_name='Track 2-Agri-business')


        students = Student.objects.select_related('program__college').all()[:60]
        org_memberships = OrgMember.objects.select_related('organization', 'student')


        student_org_map = {}
        for membership in org_memberships:
            sid = membership.student.id
            if sid not in student_org_map:
                student_org_map[sid] = membership.organization.name

        context['student_data1'] = {
            'firstname': students[0].firstname,
            'lastname': students[0].lastname,
            'student_id': students[0].student_id,
            'program': students[0].program.prog_name,
            'college': students[0].program.college.college_name,
            'organization': student_org_map.get(students[0].id, 'N/A')
        }

        context['student_data2'] = {
            'firstname': students[1].firstname,
            'lastname': students[1].lastname,
            'student_id': students[1].student_id,
            'program': students[1].program.prog_name,
            'college': students[1].program.college.college_name,
            'organization': student_org_map.get(students[1].id, 'N/A')
        }

        context['student_data3'] = {
            'firstname': students[2].firstname,
            'lastname': students[2].lastname,
            'student_id': students[2].student_id,
            'program': students[2].program.prog_name,
            'college': students[2].program.college.college_name,
            'organization': student_org_map.get(students[2].id, 'N/A')
        }

        context['student_data4'] = {
            'firstname': students[3].firstname,
            'lastname': students[3].lastname,
            'student_id': students[3].student_id,
            'program': students[3].program.prog_name,
            'college': students[3].program.college.college_name,
            'organization': student_org_map.get(students[3].id, 'N/A')
        }

        context['student_data5'] = {
            'firstname': students[4].firstname,
            'lastname': students[4].lastname,
            'student_id': students[4].student_id,
            'program': students[4].program.prog_name,
            'college': students[4].program.college.college_name,
            'organization': student_org_map.get(students[4].id, 'N/A')
        }

        context['student_data6'] = {
            'firstname': students[5].firstname,
            'lastname': students[5].lastname,
            'student_id': students[5].student_id,
            'program': students[5].program.prog_name,
            'college': students[5].program.college.college_name,
            'organization': student_org_map.get(students[5].id, 'N/A')
        }

        context['student_data7'] = {
            'firstname': students[6].firstname,
            'lastname': students[6].lastname,
            'student_id': students[6].student_id,
            'program': students[6].program.prog_name,
            'college': students[6].program.college.college_name,
            'organization': student_org_map.get(students[6].id, 'N/A')
        }

        context['student_data8'] = {
            'firstname': students[7].firstname,
            'lastname': students[7].lastname,
            'student_id': students[7].student_id,
            'program': students[7].program.prog_name,
            'college': students[7].program.college.college_name,
            'organization': student_org_map.get(students[7].id, 'N/A')
        }

        context['student_data15'] = {
            'firstname': students[15].firstname,
            'lastname': students[15].lastname,
            'student_id': students[15].student_id,
            'program': students[15].program.prog_name,
            'college': students[15].program.college.college_name,
            'organization': student_org_map.get(students[15].id, 'N/A')
        }

        context['student_data12'] = {
            'firstname': students[11].firstname,
            'lastname': students[11].lastname,
            'student_id': students[11].student_id,
            'program': students[11].program.prog_name,
            'college': students[11].program.college.college_name,
            'organization': student_org_map.get(students[11].id, 'N/A')
        }

        college_qs = College.objects.annotate(
            student_count=Count('program__student')
        ).order_by('-student_count')

        # Manually assign acronyms
        college_acronyms = {
            "College of Computer Studies": "CCS",
            "College of Arts and Humanitiess": "CAH",
            "College of Business and Accountancy": "CBA",
            "College of Sciences": "CS",
            "College of Engineering Architecture and Technology": "CEAT",
            "College of Criminal": "CC",
            "College of Hospitality Management and Tourism": "CHTM",

        }

        # Build context list
        top_colleges = []
        for college in college_qs[:5]:  # top 5
            top_colleges.append({
                'name': college.college_name,
                'acronym': college_acronyms.get(college.college_name, '---'),
                'student_count': college.student_count
            })

        context['top_colleges'] = top_colleges

        college_labels = [college['acronym'] for college in top_colleges]
        college_data = [college['student_count'] for college in top_colleges]

        context['college_labels'] = college_labels
        context['college_data'] = college_data

        return context
