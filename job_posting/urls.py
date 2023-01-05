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
    dashboard, \
    job_post_list \



urlpatterns = [
    path('', home, name='home'),
    path('hr/<slug:user>/', about_hr, name='hr'),
    path('register-hr/', hr_register, name='hr_register'),
    path('hr/<slug:user>/profile/', hr_profile, name='hr_profile'),
    path('hr/<slug:user>/create-job/', create_job, name='create_job'),
    path('hr/dashboard/<str:title>/', dashboard, name='dashboard'),
    path('company/<slug:user>/', about_company, name='about_company'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('candidate/<slug:user>/profile/', candidate_profile, name='candidate_profile'),
    path('candidate/<slug:user>/', about_candidate, name='candidate'),
    path('register-candidate/', candidate_register, name='candidate_register'),
    path('jobs/', jobs, name='jobs'),
    path('jobs/<int:job_id>/', view_job, name='view_job'),
    path('hr/<slug:user>/all/', job_post_list, name='job_dashboard'),
    path('info/<slug:user>/', job_post_list, name='candidate_info'),
]
