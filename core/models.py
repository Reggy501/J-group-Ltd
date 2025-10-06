
from django.db import models
from django.utils.text import slugify


class Division(models.Model):
    name = models.CharField(max_length=100)
    sector = models.CharField(max_length=100)  # e.g., Packaging, Bakery
    description = models.TextField()
    image = models.ImageField(upload_to='divisions/', blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class DivisionImage(models.Model):
    division = models.ForeignKey(Division, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='divisions/gallery/')
    caption = models.CharField(max_length=200, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image for {self.division.name}" if self.division else "Division Image"

class Leadership(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)  # e.g., CEO, Director
    bio = models.TextField()
    photo = models.ImageField(upload_to='leadership/', blank=True, null=True)

    def __str__(self):
        return self.name

class Award(models.Model):
    title = models.CharField(max_length=200)
    year = models.PositiveIntegerField()
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.title} ({self.year})"

class Event(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    location = models.CharField(max_length=200, blank=True)
    details = models.TextField()
    image = models.ImageField(upload_to='events/', blank=True, null=True)

    def __str__(self):
        return self.title



class AboutPage(models.Model):
    about_us = models.TextField(blank=True, help_text="Main About Us/Intro text for the About page.")
    history_text = models.TextField()
    vision_text = models.TextField()
    mission_text = models.TextField(blank=True, help_text="Mission statement for the About page.")
    values_text = models.TextField(blank=True, help_text="Values statement for the About page.")
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "About Page Content"

class ContactInquiry(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)
    is_handled = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} - {self.email}"