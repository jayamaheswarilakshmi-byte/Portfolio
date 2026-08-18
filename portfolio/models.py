from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=150)
    about = models.TextField()

    email = models.EmailField()
    phone = models.CharField(max_length=20)

    address = models.CharField(max_length=200, blank=True)

    github = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)

    profile_image = models.ImageField(
        upload_to="profile/",
        blank=True,
        null=True
    )

    resume = models.FileField(
        upload_to="resume/",
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name