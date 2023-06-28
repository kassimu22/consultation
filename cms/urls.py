from django.urls import path
from . import views, adminView, staffView, studentView

#
urlpatterns = [
    path('', views.homepage),
    path('login', views.showLoginPage, name='login'),
    path('dblogin', views.dblogin, name='dblogin'),
    path('user_details', views.getUserDetails),
    path('logout', views.logout_user, name='logout'),
    path('admin_dashboard', adminView.admin_home, name='admin_dashboard'),

    # add blocks urls
    path('add_block',adminView.add_block,name = 'add_block'),
    path('add_block_save',adminView.add_block_save, name = 'add_block_save'),
    path('view_blocks',adminView.view_blocks, name = 'view_blocks'),
    path('edit_block/<str:block_id>',adminView.edit_block, name = 'edit_block'),
    path('edit_block_save',adminView.edit_block_save, name = 'edit_block_save'),

# paths for departments
    path('add_department', adminView.add_department, name='add_department'),
    path('add_department_save', adminView.add_department_save, name='add_department_save'),
    path('view_departments', adminView.view_department, name='view_departments'),
    path('edit_department/<str:department_id>', adminView.edit_department, name='edit_department'),
    path('edit_department_save', adminView.edit_department_save, name='edit_department_save'),

# paths for students
    path('add_student', adminView.add_student, name='add_student'),
    path('add_student_save', adminView.add_student_save, name='add_student_save'),
    # path('student_panel', studentView.student_panel, name='student_panel'),
    path('view_student', adminView.view_student, name='view_student'),
    path('edit_student/<str:stud_id>', adminView.edit_student, name='edit_student'),
    path('edit_student_save', adminView.edit_student_save, name='edit_student_save'),
#paths for offices
    path('add_office', adminView.add_office, name='add_office'),
    path('view_offices', adminView.view_offices, name='view_offices'),
    path('add_office_save', adminView.add_office_save, name='add_office_save'),
    path('edit_office/<str:office_id>', adminView.edit_office, name = 'edit_office'),
    path('edit_office_save', adminView.edit_office_save, name = 'edit_office_save'),

#paths for staffs
    path('add_staff', adminView.add_staff, name = 'add_staff'),
    path('view_staff', adminView.view_staff, name = 'view_staff'),
    path('add_staff_save', adminView.add_staff_save, name = 'add_staff_save'),
    path('edit_staff/<str:staff_id>', adminView.edit_staff, name = 'edit_staff'),
    path('edit_staff_save', adminView.edit_staff_save, name = 'edit_staff_save'),

#paths for courses
    path('add_course', adminView.add_course, name='add_course'),
    path('add_course_save', adminView.add_course_save, name='add_course_save'),
    path('view_course', adminView.view_course, name='view_course'),
    path('edit_course/<str:course_id>', adminView.edit_course, name='edit_course'),
    path('edit_course_save', adminView.edit_course_save, name='edit_course_save'),

    # staffs roles
    path('create_schedule', staffView.create_schedule, name='create_schedule'),
    path('add_slots_save', staffView.add_slots_save, name='add_slots_save'),
    path('appointments', staffView.view_appointments, name='appointments'),
    path('approve_appointment/<str:appointment_id>', staffView.approve_appointment, name="approve_appointment"),
    path('reject_appointment/<str:appointment_id>', staffView.reject_appointment, name="reject_appointment"),
    path('staff_profile', staffView.staff_profile, name='staff_profile'),
    path('staff_profile_save', staffView.staff_profile_save, name='staff_profile_save'),

    # paths for students roles
    path('student_panel', studentView.student_panel, name='student_panel'),
    path('view_lectures', studentView.view_lectures, name='view_lectures'),
    path('add_appointment/<str:staff_id>', studentView.add_appointment, name='add_appointment'),
    path('get_time_slots', studentView.get_time_slots, name='get_time_slots'),
    path('add_booking_save', studentView.add_booking_save, name='add_booking_save'),
    path('student_profile', studentView.student_profile, name='student_profile'),
    path('student_profile_save', studentView.student_profile_save, name='student_profile_save'),


    # paths for staff roles
    path('staff_panel', staffView.staff_panel, name='staff_panel'),
    path('new_appointments', staffView.newAppointments, name='new_appointments'),
    path('view_shedule', staffView.view_shedule, name="view_shedule"),


# paths for profiles
    path('admin_profile', adminView.admin_profile, name="admin_profile"),
    path('admin_profile_save', adminView.admin_profile_save, name="admin_profile_save"),
]