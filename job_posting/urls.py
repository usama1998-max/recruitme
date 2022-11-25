from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import home, candidate_profile, hr_profile, hr_register, candidate_register, login_user, logout_user

urlpatterns = [
    path('', home, name='home'),
    # path('hr/', hr_profile, name='hr'),
    path('hr/register/', hr_register, name='hr_register'),
    path('hr/profile/', hr_profile, name='hr_profile'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('candidate/profile/', candidate_profile, name='candidate_profile'),
    path('candidate/register/', candidate_register, name='candidate_register'),
]

urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

