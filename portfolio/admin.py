import traceback
from django.contrib import admin
from django.core.exceptions import ValidationError

from .models import ContactMessage, Experience, Profile, Project, Service, Skill


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "title",
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
            raise e


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "subject", "created_at")
    list_filter = ("created_at",)
    search_fields = ("name", "email", "subject", "message")
    readonly_fields = ("name", "email", "subject", "message", "created_at")


# Optional: Register your remaining portfolio models
@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ("role", "company", "start_date", "end_date")

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("title",)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title",)