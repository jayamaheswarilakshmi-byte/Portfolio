from django.db import models
from cloudinary_storage.storage import RawMediaCloudinaryStorage

class Profile(models.Model):
    name = models.CharField(max_length=100, default="Jayalakshmi Subramanian")
    title = models.CharField(max_length=100, default="Web Developer")
    about_text = models.TextField()
    
    # Optional image fields using clean relative path
    profile_image = models.ImageField(upload_to='profile/', blank=True, null=True)
    hero_image = models.ImageField(upload_to='profile/', blank=True, null=True)
    about_image = models.ImageField(upload_to='profile/', blank=True, null=True)
    
    # Non-image raw files (PDF/Doc) MUST use RawMediaCloudinaryStorage
    resume_file = models.FileField(upload_to='resume/', storage=RawMediaCloudinaryStorage(), blank=True, null=True)
    
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=50) # e.g., Design, Development
    percentage = models.IntegerField(default=80)

    def __str__(self):
        return f"{self.name} - {self.percentage}%"


class Experience(models.Model):
    company = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    start_date = models.CharField(max_length=50) # e.g., 01-Jan-2020
    end_date = models.CharField(max_length=50)   # e.g., Present
    description = models.TextField()

    def __str__(self):
        return f"{self.role} at {self.company}"


class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon_class = models.CharField(max_length=50, help_text="FontAwesome icon class e.g., fa-desktop")

    def __str__(self):
        return self.title


class Project(models.Model):
    CATEGORY_CHOICES = [
        ('design', 'Design'),
        ('development', 'Development'),
        ('marketing', 'Marketing'),
    ]
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    project_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name}"