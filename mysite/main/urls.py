from django.urls import path
from . import views
from django.conf import settings # for images handling
from django.conf.urls.static import static 

app_name = "main"


urlpatterns = [
	path('', views.index, name="index"),
	path('about/', views.about, name="about"),
    path('home', views.homepage, name="homepage"),
	path('home/category<int:quessubject_id>/', views.series, name='series'),
    path('home/category<int:quessubject_id>/<int:subseries_id>/', views.papers, name='papers'),
	path('home/category<int:quessubject_id>/<int:subseries_id>/<str:horse_slug>', views.horse, name='horse'),
	path('logout', views.logout_request, name="logout"),
	path('login', views.login_request, name="login"),
	path('register', views.register, name="register"),

	path('community', views.community, name="community"),
	path('feedback', views.feedback, name="feedback"),
	path('<single_slug>', views.single_slug, name="single_slug"),
]

# if settings.DEBUG:
#         urlpatterns += static(settings.MEDIA_URL,
#                               document_root=settings.MEDIA_ROOT)
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
