# from django.contrib import admin
# from django.urls import path, include
from django.views.generic import TemplateView


# urlpatterns = [
# 	path('store/', TemplateView.as_view(template_name = 'store.html')),
# 	path('chetan_bhagat/', TemplateView.as_view(template_name = 'chetan_bhagat.html')),
#     path('', admin.site.urls),
# ]

from django.urls import path

from . import views

urlpatterns = [
    #path('', views.index, name='template.html'),
    path('store/', TemplateView.as_view(template_name = 'store.html')),
    path('chetan_bhagat/', TemplateView.as_view(template_name = 'chetan_bhagat.html')),

]