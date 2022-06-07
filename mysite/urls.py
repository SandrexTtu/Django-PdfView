from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from core import views
from django.urls import re_path
from django.views.static import serve

urlpatterns = [
    path('register/', views.registerPage, name="register"),
	path('', views.loginPage, name="login"),  
	path('logout/', views.logoutUser, name="logout"),
    path('list', views.PdfListView.as_view(), name='class_pdf_list'),
    path('lists/', views.pdf_list, name='book_list'),
    path('upload/', views.UploadPdfView.as_view(), name='class_upload_pdf'),
    path('pdfs/<int:pk>/', views.delete_pdf, name='delete_pdf'),
    path('admin/', admin.site.urls),
    re_path(r'^1/$', views.pdf_view, name = "pdf_view"),   
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}), 
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)