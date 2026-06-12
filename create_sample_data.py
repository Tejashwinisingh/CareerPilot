import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth import get_user_model
from jobs.models import Job, Application

User = get_user_model()

# Create Recruiter
recruiter, created = User.objects.get_or_create(
    username='recruiter1',
    defaults={
        'email': 'recruiter@infosys.com',
        'role': 'recruiter'
    }
)
if created:
    recruiter.set_password('recruiter123')
    recruiter.save()
    print(f"✓ Created recruiter: {recruiter.username}")
else:
    print(f"✓ Recruiter already exists: {recruiter.username}")

# Create Job Seeker
jobseeker, created = User.objects.get_or_create(
    username='jobseeker1',
    defaults={
        'email': 'jobseeker@gmail.com',
        'role': 'jobseeker'
    }
)
if created:
    jobseeker.set_password('jobseeker123')
    jobseeker.save()
    print(f"✓ Created job seeker: {jobseeker.username}")
else:
    print(f"✓ Job seeker already exists: {jobseeker.username}")

# Create Job
job, created = Job.objects.get_or_create(
    recruiter=recruiter,
    title='Python Developer',
    defaults={
        'company': 'Infosys',
        'description': 'Looking for an experienced Python developer to join our team.',
        'skills_required': 'Python, Django, MySQL',
        'location': 'Bangalore',
        'salary': '6 LPA'
    }
)
if created:
    print(f"✓ Created job: {job.title} at {job.company}")
else:
    print(f"✓ Job already exists: {job.title}")

# Create Application
application, created = Application.objects.get_or_create(
    applicant=jobseeker,
    job=job,
    defaults={'status': 'applied'}
)
if created:
    print(f"✓ Created application: {jobseeker.username} applied to {job.title}")
else:
    print(f"✓ Application already exists")

print("\n✅ All sample data ready!")
