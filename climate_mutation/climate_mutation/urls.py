"""climate_mutation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from climate_app import views
from django.conf import settings
from django.contrib.staticfiles.urls import static
#from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("index/",views.index,name='index'),
    path("admin/", admin.site.urls),
    path('login',views.login,name='login'),
    path('register',views.register,name="register"),
    path('head_foot',views.head_foot,name='head_foot'),
    path('changepass',views.changepass,name="changepass"),
    path('forgetpass',views.forgetpass),
    path('faqs',views.faqs,name='faqs'),
    path('blogs',views.allblogs,name='blog'),
    path('sidebar',views.sidebar),
    path('review',views.myreview,name="review"),
    path('myprofiledetails',views.my_profile_details,name="myprofile" ),
    path('editprofile',views.edit_profile,name='editprofile'),
    path('logout',views.logout,name="logout"),
    path('help',views.h_support,name='help'),
    path('contactus',views.contactus,name='contactus'),
    path('blogdetail/<int:id>',views.blogdetail,name='blogdetail'),
    path('ozoneperdiction',views.oz_perdiction),
    path('causes',views.showcause ,name='causes'),
    path('evidence',views.showevidence,name='evidence' ),
    path('effects',views.showeffects,name='effects'),
    path('actions',views.showeactions,name='actions'),
    path('ngos',views.showngos,name='ngo'),
    path('ngodescription/<int:id>',views.ngodescription,name='ngodescription'),
    path('dataset/<int:id>',views.showdataset,name='dataset'),
    path('visuals/<int:id>',views.showvisuals,name='visuals'),
    path('visuals/<str:l>',views.all_visualization),
    path('dataset/download/<str:path>',views.download,name='download'),
    path('perdictions/<int:id>',views.showperdictions,name='perdictions'),
    path('perdictions/<str:l>',views.all_perdictions),
    path('dash-board',views.dashboard_welcome,name='dash')

  

    

]

#urlpatterns+=staticfiles_urlpatterns()
#urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )

