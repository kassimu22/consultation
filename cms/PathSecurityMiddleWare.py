from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin




class PathSecurityMiddleWare(MiddlewareMixin):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        modulename = view_func.__module__
        print(modulename)
        user = request.user
        if user.is_authenticated:
            if user.user_type == "1":
                if modulename == "cms.adminView" or modulename == "django.views.static":
                    pass
                elif modulename == "cms.views":
                    pass
                else:
                    return HttpResponseRedirect(reverse("admin_dashboard"))
            elif user.user_type == "2":
                if modulename == "cms.staffView" or modulename == "django.views.static":
                    pass
                elif modulename == "cms.views" or modulename == "django.views.static":
                    pass
                else:
                    return HttpResponseRedirect(reverse("staff_panel"))
            elif user.user_type == "3":
                if modulename == "cms.studentView" or modulename == "django.views.static":
                    pass
                elif modulename == "cms.views" or modulename == "django.views.static":
                    pass
                else:
                    return HttpResponseRedirect(reverse("student_panel"))
            else:
                return HttpResponseRedirect(reverse("login"))

        else:
            if request.path == reverse("login") or request.path == reverse(
                    "dblogin") or modulename == "django.contrib.auth.views":
                pass
            else:
                return HttpResponseRedirect(reverse("login"))