"""
Django settings for yaoling project.

Generated by 'django-admin startproject' using Django 2.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
import sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'qk&dh+)s1ngnq72vmav()&ls+qan)iqnur0_sp@toei8d4tqnc'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*', ]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'xadmin',
    'crispy_forms',
    'reversion',
    'ckeditor',
    'ckeditor_uploader',
    'accounts.apps.AccountsConfig',
    'tieba.apps.TiebaConfig',
    'dmhy.apps.DmhyConfig',
    'gateway.apps.GatewayConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'yaoling.urls'

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
                'accounts.views.global_setting',
                'django.template.context_processors.request',
            ],
            'builtins':['django.templatetags.static'],
        },
    },
]

WSGI_APPLICATION = 'yaoling.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'yaoling',
        'USER': 'root',
        'PASSWORD': '19920124Zhy@.',
        'HOST': '',
        'PORT': '',
        # 'OPTIONS': {'init_command': "SET sql_mode='STRICT_TRANS_TABLES'", },
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

# 语言设置
LANGUAGE_CODE = 'zh-Hans'
# 时区设置
TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/


# 自定义项
# 自定义用户model
AUTH_USER_MODEL = 'accounts.MyUser'
# apps目录
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))
# 静态文件目录
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, '/static/')
]
# 文本编辑器设置
MEDIA_URL = '/media/'   # 图片上传路径
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')    # 图片储存路径
CKEDITOR_UPLOAD_PATH = "upload/"
CKEDITOR_JQUERY_URL = 'https://apps.bdimg.com/libs/jquery/2.1.4/jquery.min.js'
CKEDITOR_IMAGE_BACKEND = 'pillow'
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
    }
}
'''
# 自定义日志输出信息
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(threadName)s:%(thread)d] [%(name)s:%(lineno)d] [%(module)s:%(funcName)s] [%('
                      'levelname)s]- %(message)s'}  # 日志格式
    },
    'filters': {
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'include_html': True,
            },
        'default': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'log/all.log',     # 日志输出文件
            'maxBytes': 1024*1024*5,                  # 文件大小
            'backupCount': 5,                         # 备份份数
            'formatter': 'standard',                   # 使用哪种formatters日志格式
        },
        'error': {
            'level':'ERROR',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': 'log/error.log',
            'maxBytes':1024*1024*5,
            'backupCount': 5,
            'formatter': 'standard',
            },
        'console':{
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
        },
        'request_handler': {
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': 'log/script.log',
            'maxBytes': 1024*1024*5,
            'backupCount': 5,
            'formatter':'standard',
            },
        'scprits_handler': {
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': 'log/script.log',
            'maxBytes': 1024*1024*5,
            'backupCount': 5,
            'formatter': 'standard',
            }
    },
    'loggers': {
        'django': {
            'handlers': ['default', 'console'],
            'level': 'DEBUG',
            'propagate': False
        },
        'django.request': {
            'handlers': ['request_handler'],
            'level': 'DEBUG',
            'propagate': False,
            },
        'scripts': {
            'handlers': ['scprits_handler'],
            'level': 'INFO',
            'propagate': False
        },
        'blog.views': {
            'handlers': ['default', 'error'],
            'level': 'DEBUG',
            'propagate': True
        },
    }
}
'''
# 网站基本信息配置
SITE_NAME = '瑶玲之家'      # 页面标题
SITE_DESC = '您的学习、休闲港湾'     # 网站描述
SITE_KEY = ''      # 关键词
WEIBO_SINA = 'https://weibo.com/zhouyao92124'
BLOG_EMAIL = '498330580@qq.com'
BLOG_RSS = 'http://www.yaoling.ltd'
