from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'so!r6w(h)a%vdd#dk_9eb2k0%p@$^20@&ec2u254+b#1d)euyv'

DEBUG = env.bool('DJANGO_DEBUG', default=True)
