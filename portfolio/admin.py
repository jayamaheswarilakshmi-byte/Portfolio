from django.contrib import admin
from django.core.exceptions import ValidationError
import traceback

from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "designation",
        "email",
        "phone",
    )

    def save_model(self, request, obj, form, change):
        try:
            super().save_model(request, obj, form, change)
        except Exception as e:
            print("===== CLOUDINARY UPLOAD ERROR =====")
            print(type(e).__name__)
            print(str(e))
            traceback.print_exc()
            print("===== END CLOUDINARY UPLOAD ERROR =====")
            raise