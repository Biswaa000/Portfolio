# projects/models.py
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.core.validators import MinLengthValidator
from django.utils.crypto import get_random_string


class Project(models.Model):
    """Model for portfolio projects"""
    title = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(3)],
        help_text="Title of the project"
    )
    slug = models.SlugField(
        max_length=100,
        unique=True,
        blank=True,
        help_text="URL-friendly version of the title (auto-generated)"
    )
    short_description = models.CharField(
        max_length=200,
        help_text="Brief description (max 200 chars)"
    )

  
    github_url = models.URLField(
        blank=True,
        null=True,
        help_text="URL to GitHub repository"
    )
    live_url = models.URLField(
        blank=True,
        null=True,
        help_text="URL to live demo"
    )
  
    is_featured = models.BooleanField(
        default=False,
        help_text="Feature this project prominently"
    )
    display_order = models.PositiveIntegerField(
        default=0,
        help_text="Higher numbers appear first"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-display_order', '-created_at']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1
            while Project.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('project_detail', kwargs={'slug': self.slug})

   