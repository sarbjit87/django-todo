from django.conf.urls import url
from .views import RegisterUserView

from django.urls import reverse_lazy
from django.contrib.auth.views import(
    LoginView,
    LogoutView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordChangeView,
    PasswordChangeDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)

app_name = 'accounts'

urlpatterns = [
    url(r'^register/$', RegisterUserView.as_view(), name='register'),
    url(r'^login/$', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    url(r'^logout/$', LogoutView.as_view(next_page=reverse_lazy('accounts:login')), name='logout'),
    url(r'^password-change/$', PasswordChangeView.as_view(template_name='accounts/password-change.html'), name='password-change'),
    url(r'^password-change-done/$', PasswordChangeDoneView.as_view(template_name='accounts/password-change-done.html'), name='password_change_done'),
    url(r'^password-reset/$', PasswordResetView.as_view(template_name='accounts/password-reset.html'), name='password-reset'),
    url(r'^password-reset-done/$', PasswordResetDoneView.as_view(template_name='accounts/password-reset-done.html'), name='password_reset_done'),
    url(r'^password-reset-confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', PasswordResetConfirmView.as_view(template_name='accounts/password-reset-confirm.html'), name='password_reset_confirm'),
    url(r'^password-reset-complete/$', PasswordResetCompleteView.as_view(template_name='accounts/password-reset-complete.html'), name='password_reset_complete'),
]
