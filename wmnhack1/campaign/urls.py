from django.urls import path
from . import views
from django.conf import settings
#from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
#from django.views.generic.base import TemplateView

urlpatterns = [
    path('', views.issue_list, name='issue_list'),
    path('watercampaign/<int:pk>/', views.water_campaign_detail, name='campaign_detail'),
    path('watercampaign/new/', views.water_campaign_new, name='water_campaign_new'),
    path('watercampaigns/', views.water_campaign_list, name='water_campaign_list'),
    path('water/', views.issue_water, name='issue_water'),
    #path('watercampaign/<int:pk>/delete/', views.CampaignDelete.as_view(), name='water_campaign_delete'),

]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
