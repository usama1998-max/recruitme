from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import home,\
    candidate_profile,\
    hr_profile, hr_register,\
    candidate_register,\
    login_user,\
    logout_user,\
    about_company, \
    about_hr, \
    about_candidate, \
    jobs, \
    create_job, \
    view_job, \
    dashboard


urlpatterns = [
    path('', home, name='home'),
    path('hr/<slug:user>', about_hr, name='hr'),
    path('hr/register/', hr_register, name='hr_register'),
    path('hr/profile/', hr_profile, name='hr_profile'),
    path('hr/create-job/', create_job, name='create_job'),
    path('hr/dashboard/', dashboard, name='dashboard'),
    path('company/<slug:user>', about_company, name='about_company'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('candidate/profile/', candidate_profile, name='candidate_profile'),
    path('candidate/', about_candidate, name='candidate'),
    path('candidate/register/', candidate_register, name='candidate_register'),
    path('jobs/', jobs, name='jobs'),
    path('jobs/<int:pk>', view_job, name='view_job'),
]
