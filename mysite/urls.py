from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from core import views
from django.urls import re_path
from .decorators import allowed_users



urlpatterns = [
    path('register/', views.registerPage, name="register"),
	path('login', views.loginPage, name="login"),  
	path('logout/', views.logoutUser, name="logout"),
    path('adminpdflist', views.PdfListView.as_view(), name='class_pdf_list'),
    path('', views.pdf_list, name='pdf_list'),
    path('adminpdfupload/', views.UploadPdfView.as_view(), name='class_upload_pdf'),
    path('pdfs/<int:pk>/', views.delete_pdf, name='delete_pdf'),
    path('admin/', admin.site.urls),
    re_path(r'^1/$', views.pdf_view, name = "pdf_view"),   
    re_path(r'^2/$', views.pdf_view1, name = "pdf_view"),
    re_path(r'^3/$', views.pdf_view2, name = "pdf_view"),   
    re_path(r'^4/$', views.pdf_view3, name = "pdf_view"),
    re_path(r'^5/$', views.pdf_view4, name = "pdf_view"),   
    re_path(r'^6/$', views.pdf_view5, name = "pdf_view"),
    re_path(r'^7/$', views.pdf_view6, name = "pdf_view"),   
    re_path(r'^8/$', views.pdf_view7, name = "pdf_view"),
    re_path(r'^9/$', views.pdf_view8, name = "pdf_view"),   
    re_path(r'^10/$', views.pdf_view9, name = "pdf_view"),
    re_path(r'^11/$', views.pdf_view10, name = "pdf_view"),   
    re_path(r'^12/$', views.pdf_view11, name = "pdf_view"),  
    
]

handler404="core.views.handle_not_found"

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

