from django.conf import settings
from .views import *
from django.urls import path
from django.conf.urls.static import static

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('news/', NewsListView.as_view(), name='news'),
    path('news/<int:pk>/', NewsDetailView.as_view(), name='detail_news'),
    path('application/list', AdminApplicationListView.as_view(), name='application'),
    path('application/<int:pk>', AdminApplicationDetailView.as_view(), name='application_detail'),
    path('about/', Home.as_view(), name='about'),
    path('about/platform/', Home.as_view(), name='about_platform'),
    path('security/', Home.as_view(), name='security'),
    path('send_application', SendApplicationView.as_view(), name='send_application'),
    path('success/', ApplicationSendSuccessView.as_view(), name='success'),
    path('login/', login, name='login'),
    path('aboutus/', aboutus, name='aboutus'),
    path('aboutplatform/', aboutplatform, name='AboutPlatform'),
    path('security/', security, name='security'),
    path('success/', ApplicationSendSuccessView.as_view(), name='success'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
