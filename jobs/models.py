from django.db import models
from django.conf import settings

class Job(models.Model):
    recruiter = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    title = models.CharField(max_length=200)

    company = models.CharField(max_length=200)

    description = models.TextField()

    skills_required = models.TextField()

    location = models.CharField(max_length=100)

    salary = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Application(models.Model):
    STATUS_CHOICES = (
        ('applied', 'Applied'),
        ('reviewing', 'Reviewing'),
        ('shortlisted', 'Shortlisted'),
        ('rejected', 'Rejected'),
        ('accepted', 'Accepted'),
    )

    applicant = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    job = models.ForeignKey(
        Job,
        on_delete=models.CASCADE
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='applied'
    )

    applied_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.applicant.username} - {self.job.title}"