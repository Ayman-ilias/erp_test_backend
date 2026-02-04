# from django.apps import AppConfig


# class BuyerConfig(AppConfig):
#     default_auto_field = 'django.db.models.BigAutoField'
#     name = 'buyer'
from django.apps import AppConfig

class BuyerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'client_information.buyer'  # Full path with dot notation