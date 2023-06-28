from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from setuptools.config._validate_pyproject import ValidationError

from .models import Staffs, CustomUser, Students, Department, Courses, Blocks, Office


#
def admin_home(request):
    staffCount = Staffs.objects.count()
    studentCount = Students.objects.count()
    countDepartment = Department.objects.count()
    context = {
        "staffCount": staffCount,
        "studentCount":studentCount,
        "countDepartment" : countDepartment
    }
    return render(request, 'cms/admin/admin_dashboard.html', context)


def add_block(request):
    return render(request, 'cms/admin/add_block.html')

def add_block_save(request):
    if request.method != 'POST':
        return HttpResponse('Method not allowed')
    else:
        block_name = request.POST.get('block_name').upper() # get value of name attribute

        check_block = Blocks.objects.filter(block_name=block_name).exists()
        if not check_block:
            try:
                block = Blocks.objects.create(block_name = block_name)
                block.save()
                messages.success(request, 'Block added successfully')
                return HttpResponseRedirect(reverse('add_block'))
            except:
                messages.error(request, 'Failed to add block')
                return HttpResponseRedirect(reverse('add_block'))
        else:
            messages.error(request, 'This block is already added, create new one')
            return HttpResponseRedirect(reverse('add_block'))

def view_blocks(request):
    blocks = Blocks.objects.all()
    context = {'blocks': blocks}
    return render(request, 'cms/admin/view_blocks.html', context)

def edit_block(request, block_id):
    blocks = Blocks.objects.get(id=block_id)
    context = {'blocks':blocks, 'id':block_id}
    return render(request, 'cms/admin/edit_block.html', context)

def edit_block_save(request):
    if request.method != 'POST':
        return HttpResponse('Method not allowed')
    else:
        block_id = request.POST.get('block_id') # get value of id attribute
        block_name = request.POST.get('block_name') # get value of name attribute
        block_upper = block_name.upper()

        try:
            block = Blocks.objects.get(id = block_id)
            block.block_name = block_upper
            block.save()
            messages.success(request, 'Block updated successfully')
            return HttpResponseRedirect(reverse('edit_block',kwargs={'block_id':block_id}))
        except:
            messages.error(request, 'Failed to update block')
            return HttpResponseRedirect(reverse('edit_block',kwargs={'block_id':block_id}))

#departments
def add_department(request):
    return render(request, 'cms/admin/add_department.html')


def add_department_save(request):
    if request.method != 'POST':
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        department_name = request.POST.get('department_name').upper()

        check_depart = Department.objects.filter(department_name=department_name).exists()
        if not check_depart:
            try:
                department = Department.objects.create(department_name=department_name)
                department.save()
                messages.success(request, 'Department added successfully')
                return HttpResponseRedirect(reverse('add_department'))
            except:
                messages.error(request, 'Problem in department creation')
                return HttpResponseRedirect(reverse('add_department'))
        else:
            messages.error(request, 'Department exitst, create new one')
            return HttpResponseRedirect(reverse('add_department'))

def view_department(request):
    departments = Department.objects.all()
    context = {'departments':departments}
    return render(request, 'cms/admin/view_departments.html', context)


def edit_department(request, department_id):
    department = Department.objects.get(id=department_id)
    context = {'department': department, 'id': department_id}
    return render(request, 'cms/admin/edit_department.html', context)


def edit_department_save(request):
    if request.method != 'POST':
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        department_id = request.POST.get('department_id')
        department_name = request.POST.get('department_name').upper()

        try:
            department = Department.objects.get(id=department_id)
            department.department_name = department_name
            department.save()
            messages.success(request, 'Department updated successfully')
            return HttpResponseRedirect(reverse('edit_department', kwargs={'department_id': department_id}))
        except:
            messages.error(request, 'Failed to update department')
            return HttpResponseRedirect(reverse('edit_department', kwargs={'department_id': department_id}))


def add_student(request):
    return render(request, 'cms/admin/add_student.html')


def add_student_save(request):
    if request.method != 'POST':
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:  # process the form
        student_id = request.POST.get('student_id')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('student_id')
        email = request.POST.get('email')
        password = request.POST.get('password')
        program = request.POST.get('program')
        gender = request.POST.get('gender')
        level = request.POST.get('level')

        # create custom user object
        try:
            user = CustomUser.objects.create_user(
                username=username, email=email, password=password, first_name=first_name, last_name=last_name,
                user_type=3)
            user.students.student_id = student_id
            user.students.level = level
            user.students.program = program
            user.students.gender = gender
            user.save()
            messages.success(request, "Student added successfully...")
            return HttpResponseRedirect(reverse("add_student"))

        except:
            messages.error(request, 'Failed to add student')
            return HttpResponseRedirect(reverse("add_student"))

def view_student(request):
    students = Students.objects.all()
    start_index = 1
    context = {'students':students, "start_index":start_index}
    return render(request, 'cms/admin/view_students.html', context)


def edit_student(request, stud_id):
    student=Students.objects.get(admin=stud_id)
    context = {'student':student}
    return render(request,'cms/admin/edit_student.html', context)

def edit_student_save(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        studs_id=request.POST.get("stud_id")
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        email=request.POST.get("email")
        program=request.POST.get("program")
        gender=request.POST.get("gender")
        level = request.POST.get("level")



        try:
            user=CustomUser.objects.get(id=studs_id)
            user.first_name=first_name
            user.last_name=last_name
            user.email=email
            # user.username=username
            user.save()

            student_model=Students.objects.get(admin=studs_id)
            student_model.program=program
            student_model.gender=gender
            student_model.level = level
            student_model.save()
            messages.success(request,"Student updated successfully")
            return HttpResponseRedirect(reverse("edit_student",kwargs={"stud_id":studs_id}))
        except:
            messages.error(request,"Failed to Edit Student")
            return HttpResponseRedirect(reverse("edit_student",kwargs={"stud_id":studs_id}))


def add_office(request):
    blocks = Blocks.objects.all()
    return render(request, 'cms/admin/add_office.html', {"blocks":blocks})

def add_office_save(request):
    if request.method != "POST":
        return HttpResponse('Method not allowed')
    else:
        block_name = request.POST.get("block_name")
        office_no = request.POST.get("office_number")

        block_id = Blocks.objects.get(id=block_name)

        check_office = Office.objects.filter(block=block_id, office_number=office_no).exists()

        if not check_office:
            try:
                block_id = Blocks.objects.get(id=block_name)
                office = Office.objects.create(office_number = office_no, block = block_id)
                office.save()
                messages.success(request, "Office Added Successfully")
                return HttpResponseRedirect(reverse('add_office'))

            except:
                messages.error(request, "Something Went Wrong")
                return HttpResponseRedirect(reverse('add_office'))
        else:
            messages.error(request, "Office No exists, create new one")
            return HttpResponseRedirect(reverse('add_office'))

def view_offices(request):
    offices = Office.objects.all()
    return render(request, 'cms/admin/view_offices.html',{"offices":offices})

def edit_office(request, office_id):
    office = Office.objects.get(id=office_id)
    blocks = Blocks.objects.all()
    office_dict = {
        "office":office,
        "office_id":office_id,
        "blocks":blocks
    }
    return render(request, 'cms/admin/edit_office.html', context=office_dict)

def edit_office_save(request):
    if request.method != "POST":
        return HttpResponse('Method not allowed')
    else:
        office_id = request.POST.get("office_id")
        block_name = request.POST.get("block_name")
        office_no = request.POST.get("office_number")

        try:
            block_id = Blocks.objects.get(id=block_name)
            office = Office.objects.get(id=office_id)
            office.office_number = office_no
            office.block = block_id
            office.save()
            messages.success(request, "Office Updated Successfully")
            return HttpResponseRedirect(reverse('edit_office', kwargs={"office_id":office_id}))

        except:
            messages.error(request, "Something Went Wrong")
            return HttpResponseRedirect(reverse('edit_office', kwargs={"office_id":office_id}))


def add_staff(request):
    departments = Department.objects.all()
    offices = Office.objects.all()
    context = {'departments': departments, 'offices': offices}
    return render(request, 'cms/admin/add_staff.html', context)


def add_staff_save(request):
    if request.method != 'POST':
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:  # process the form
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        address = request.POST.get('address')
        department_id = request.POST.get('department')
        office_id = request.POST.get('office_number')

        # create custom user object
        try:
            user = CustomUser.objects.create_user(
                username=username, email=email, password=password, first_name=first_name, last_name=last_name,
                user_type=2)
            user.staffs.address = address
            depart_obj = Department.objects.get(id=department_id)
            office_obj = Office.objects.get(id=office_id)
            user.staffs.department = depart_obj
            user.staffs.office = office_obj
            user.save()
            messages.success(request, "Staff added successfully...")
            return HttpResponseRedirect(reverse("add_staff"))

        except:
            messages.error(request, 'Problem in adding staffs')
            return HttpResponseRedirect(reverse("add_staff"))

def view_staff(request):
    staffs = Staffs.objects.all()
    context = {'staffs':staffs}
    return render(request, 'cms/admin/view_staffs.html', context)

def edit_staff(request, staff_id):
    staff=Staffs.objects.get(admin=staff_id)
    departments = Department.objects.all()
    offices = Office.objects.all()
    context = {'staff':staff,'departments':departments,"offices":offices}
    return render(request,'cms/admin/edit_staff.html', context)

def edit_staff_save(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        staff_id=request.POST.get("staff_id")
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        email=request.POST.get("email")
        address=request.POST.get("address")
        office=request.POST.get("office_number")

        office_obj = Office.objects.get(id=office)

        try:
            user=CustomUser.objects.get(id=staff_id)
            user.first_name=first_name
            user.last_name=last_name
            user.email=email
            user.save()

            staff_model=Staffs.objects.get(admin=staff_id)
            staff_model.address=address
            staff_model.office=office_obj
            staff_model.save()
            messages.success(request,"Staff updated successfully")
            return HttpResponseRedirect(reverse("edit_staff",kwargs={"staff_id":staff_id}))
        except:
            messages.error(request,"Failed to Edit Staff")
            return HttpResponseRedirect(reverse("edit_staff",kwargs={"staff_id":staff_id}))


def add_course(request):
    departments = Department.objects.all()
    return render(request, 'cms/admin/add_course.html', {'departments': departments})


def add_course_save(request):
    if request.method != 'POST':
        return HttpResponse("<h2>Method not allowed</h2>")
    else:
        course_name = request.POST.get('course_name')
        course_code = request.POST.get('course_code')
        department_id = request.POST.get('department')
        department_obj = Department.objects.get(id=department_id)

        try:
            course = Courses.objects.create(course_name=course_name, course_code=course_code, department=department_obj)
            course.save()
            messages.success(request, 'Course added successfully')
            return HttpResponseRedirect(reverse('add_course'))

        except:
            messages.error(request, 'Problem in course creation')
            return HttpResponseRedirect(reverse('add_course'))

def view_course(request):
    courses = Courses.objects.all()
    context = {'courses':courses}
    return render(request, 'cms/admin/view_courses.html', context)


def edit_course(request, course_id):
    course = Courses.objects.get(id=course_id)
    departments = Department.objects.all()
    context = {'course': course, 'departments': departments, 'id': course_id}
    return render(request, 'cms/admin/edit_course.html', context)


def edit_course_save(request):
    if request.method != 'POST':
        return HttpResponse("<h2>Method not allowed</h2>")
    else:
        course_name = request.POST.get('course_name')
        course_code = request.POST.get('course_code')
        course_id = request.POST.get('course_id')
        department_id = request.POST.get('department')

        try:
            course = Courses.objects.get(id=course_id)
            department_obj = Department.objects.get(id=department_id)
            course.course_name = course_name
            course.course_code = course_code
            course.department = department_obj
            course.save()
            messages.success(request, 'Course updated successfully')
            return HttpResponseRedirect(reverse('edit_course', kwargs={'course_id': course_id}))

        except:
            messages.error(request, 'Failed to update course')
            return HttpResponseRedirect(reverse('edit_course', kwargs={'course_id': course_id}))

def admin_profile(request):
    user = CustomUser.objects.get(id=request.user.id)
    context = {'user': user}
    return render(request, 'cms/admin/admin_profile.html', context)

def admin_profile_save(request):
    if request.method != 'POST':
        return HttpResponseRedirect(reverse('admin_profile'))
    else:
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get("password")
        try:
            customuser = CustomUser.objects.get(id=request.user.id)
            customuser.first_name = first_name
            customuser.last_name = last_name
            if password != None and password != '':
                customuser.set_password(password)
            customuser.save()
            messages.success(request, "Successfully Updated Profile")
            return HttpResponseRedirect(reverse("admin_profile"))
        except:
            messages.error(request, "Failed to Update Profile")
            return HttpResponseRedirect(reverse("admin_profile"))
