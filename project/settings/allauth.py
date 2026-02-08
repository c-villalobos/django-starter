AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by email
    'allauth.account.auth_backends.AuthenticationBackend',
]

# Override for customization

# ACCOUNT_FORMS = {
#     'add_email': 'allauth.account.forms.AddEmailForm',
#     'change_password': 'allauth.account.forms.ChangePasswordForm',
#     'confirm_login_code': 'allauth.account.forms.ConfirmLoginCodeForm',
#     'login': 'allauth.account.forms.LoginForm',
#     'request_login_code': 'allauth.account.forms.RequestLoginCodeForm',
#     'reset_password': 'allauth.account.forms.ResetPasswordForm',
#     'reset_password_from_key': 'allauth.account.forms.ResetPasswordKeyForm',
#     'set_password': 'allauth.account.forms.SetPasswordForm',
#     'signup': 'allauth.account.forms.SignupForm',
#     'user_token': 'allauth.account.forms.UserTokenForm',
# }

# ACCOUNT_SIGNUP_FIELDS = ['username*', 'email', 'password1*', 'password2*']

