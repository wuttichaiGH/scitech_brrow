from django.apps import AppConfig


class BrAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'br_app'

    def ready(self):
        # นำเข้า signals เมื่อแอปนี้พร้อม
        import br_app.signals