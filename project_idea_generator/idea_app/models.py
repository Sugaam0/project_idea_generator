from django.db import models
from django.conf import settings

class ProjectIdea(models.Model):
    FIELD_CHOICES = [
        ('AI', 'Artificial Intelligence'),
        ('Web', 'Web Development'),
        ('Mobile', 'Mobile App Development'),
        ('Data', 'Data Science'),
    ]
    
    TYPE_CHOICES = [
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Advanced', 'Advanced'),
    ]
    
    GENRE_CHOICES = [
        ('Education', 'Education'),
        ('Entertainment', 'Entertainment'),
        ('Healthcare', 'Healthcare'),
        ('Finance', 'Finance'),
    ]
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    field = models.CharField(max_length=100, choices=FIELD_CHOICES)
    type = models.CharField(max_length=100, choices=TYPE_CHOICES)
    genre = models.CharField(max_length=100, choices=GENRE_CHOICES)
    additional_info = models.TextField(blank=True, null=True)
    generated_ideas = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.field} ({self.type})"
