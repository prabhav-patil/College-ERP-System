from django.contrib import admin

# Register your models here.
from .models import course
from .models import student
from .models import faculty
from .models import enrollment
from .models import prereq

admin.site.register(course)
admin.site.register(student)
admin.site.register(faculty)
admin.site.register(enrollment)
admin.site.register(prereq)
