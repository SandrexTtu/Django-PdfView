from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from core import views
from django.urls import re_path
from django.views.static import serve
from django.conf.urls import handler404

urlpatterns = [
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
	path('login', views.loginPage, name="login"),  
    path('', views.pdf_list, name='pdf_list'), 
    path('register/', views.registerPage, name="register"),
    path('logout/', views.logoutUser, name="logout"),
    path('list', views.PdfListView.as_view(), name='class_pdf_list'),
    path('adminpdfupload/', views.UploadPdfView.as_view(), name='class_upload_pdf'),
    path('pdfs/<int:pk>/', views.delete_pdf, name='delete_pdf'),
    path('admin/', admin.site.urls),
    re_path(r'^Files/Pdf/ჭაბურღილი1.pdf/$', views.pdf_view, name = "pdf_view"),   
    re_path(r'^Files/Pdf/ჭაბურღილი2.pdf/$', views.pdf_view1, name = "pdf_view"),
    re_path(r'^Files/Pdf/ჭაბურღილი3.pdf/$', views.pdf_view2, name = "pdf_view"),   
    re_path(r'^Files/Pdf/ჭაბურღილი4.pdf/$', views.pdf_view3, name = "pdf_view"),
    re_path(r'^Files/Pdf/ჭაბურღილი5.pdf/$', views.pdf_view4, name = "pdf_view"),   
    re_path(r'^Files/Pdf/ჭაბურღილი6.pdf/$', views.pdf_view5, name = "pdf_view"),
    re_path(r'^Files/Pdf/ჭაბურღილი7.pdf/$', views.pdf_view6, name = "pdf_view"),   
    re_path(r'^Files/Pdf/ჭაბურღილი8.pdf/$', views.pdf_view7, name = "pdf_view"),
    re_path(r'^Files/Pdf/ჭაბურღილი9.pdf/$', views.pdf_view8, name = "pdf_view"),   
    re_path(r'^Files/Pdf/ჭაბურღილი10.pdf/$', views.pdf_view9, name = "pdf_view"),
    re_path(r'^Files/Pdf/ჭაბურღილი11.pdf/$', views.pdf_view10, name = "pdf_view"),   
    re_path(r'^Files/Pdf/ჭაბურღილი12.pdf/$', views.pdf_view11, name = "pdf_view"),  

    
]

handler404="core.views.handle_not_found"


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

