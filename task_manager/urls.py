from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h2>Welcome to the Task Manager API ✅</h2><p>Go to <a href='/api/tasks/'>/api/tasks/</a> to view tasks.</p>")

urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    path('api/', include('tasks.urls')),
]
