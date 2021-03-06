"""
Django settings for API project.

Generated by 'django-admin startproject' using Django 3.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'kdu&t!ag+9g-^#^c!$17%ifk)_r$b)5$qfkibxj_o*^tfvqg8a'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

# AUTH_USER_MODEL = "client_api.User"


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'seller_login',
    'client_api',
    'accounts',
    # 'paytm_gateway',
    'orders',
    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',
    # 'django_email_verification',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
CORS_ORIGIN_ALLOW_ALL = True
# CSRF_TRUSTED_ORIGINS = [
#     "http://localhost:8081/ ",
#     "http://127.0.0.1:8081/"
# ]





ROOT_URLCONF = 'API.urls'

AUTH_USER_MODEL = 'accounts.CustomUser'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'API.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'food_desk',
        'USER': 'postgres',
        'PASSWORD': 'abhishek',
        'HOST': 'localhost',
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

# TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Calcutta'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': (
        # 'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
        # 'rest_framework.permissions.IsAuthenticated'
    ),
    # 'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    # 'PAGE_SIZE': 2,
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        # 'rest_framework.authentication.BasicAuthentication',
    )
}







# payment gateway
# Django related code
PAYTM_COMPANY_NAME = "Company Name"   # For representation purposes
PAYTM_INDUSTRY_TYPE_ID = "Retail"     # For staging environment
PAYTM_CHANNEL_ID = "WEB"
PAYTM_MERCHANT_KEY = "wY&ySwcGerc_slBs"
PAYTM_MERCHANT_ID = "zwfsDv38259108810773"
PAYTM_CALLBACK_URL = "http://localhost:8000/paytm_gateway/response/" # Hardcode
# PAYTM_CALLBACK_URL = "http://localhost:8080/cart/" # Hardcode
PAYTM_WEBSITE = "WEBSTAGING"
PAYTM_PAYMENT_GATEWAY_URL = "https://securegw-stage.paytm.in/order/process"
PAYTM_TRANSACTION_STATUS_URL = "https://securegw-stage.paytm.in/order/status"








EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# EMAIL_HOST_USER = '*********'
# EMAIL_HOST_PASSWORD = '*********'




# Email System

# for reset password
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'mukmrjup@gmail.com'
EMAIL_HOST_PASSWORD = 'qddadglyawtdhmwp'


DEFAULT_FROM_EMAIL = 'Food Desk Team'


#  for email verification (common lines are only written once)
EMAIL_ACTIVE_FIELD = 'is_active'
EMAIL_SERVER = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_ADDRESS = 'mukmrjup@gmail.com'
EMAIL_FROM_ADDRESS = 'Food Desk Team'
EMAIL_PASSWORD = 'qddadglyawtdhmwp' # os.environ['password_key'] suggested
EMAIL_MAIL_SUBJECT = 'This Is My Subject'
EMAIL_MAIL_HTML = 'EMAIL_MAIL_HTML.html'
# EMAIL_MAIL_PLAIN = 'Mail Body ......'
EMAIL_PAGE_TEMPLATE = 'EMAIL_PAGE_TEMPLATE.html'
EMAIL_PAGE_DOMAIN = 'http://127.0.0.1:8000/'
