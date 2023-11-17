from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    HIGH = "HIGH"
    MEDIUM = "MEDIUM"
    LOW = "LOW"
    proficency_level = [
        (HIGH, "High"),
        (MEDIUM, "Medium"),
        (LOW, "Low"),
    ]
    CHRISTIAN = "CHRISTIAN"
    HINDU = "HINDU"
    ISLAM = "ISLAM"
    OTHERS = "OTHERS"
    Religions = [
        (CHRISTIAN, "Christian"),
        (HINDU, "Hindu"),
        (ISLAM, "Islam"),
        (OTHERS, "Others")
    ]
    MALE = "MALE"
    FEMALE = "FEMALE"
    TRANS = "TRANS"
    Gender =[(MALE,'Male'),(FEMALE,'Female'), (TRANS, 'Trans')]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=100, blank=True)
    skills_offered = models.ManyToManyField('Skill', related_name='offered_by', blank=True)
    skills_wanted = models.ManyToManyField('Skill', related_name='wanted_by', blank=True)
    age = models.IntegerField(null=True, blank=True)
    religion = models.CharField(choices=Religions, max_length=10, default=None, null=True, blank=True)
    religion_others = models.CharField(max_length=10, null=True, blank=True)
    gender = models.CharField(choices=Gender, max_length=10, null=True, blank=True)
    expertiese_level = models.CharField(
        max_length=8,
        choices=proficency_level,
        default=LOW,
        null=True,
        blank=True
    )
    profile_picture = models.ImageField(default='default1.png',upload_to='profile_pictures', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    # Other fields for user profile information (e.g., contact details, interests, etc.)

    def __str__(self):
        return self.user.username

class Skill(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(max_length=500, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.name

class Education(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True, blank=True)
    institution_name = models.CharField(max_length=100, null=True, blank=True)
    degree = models.CharField(max_length=100, null=True, blank=True)
    field_of_study = models.CharField(max_length=100, null=True, blank=True)
    graduation_year = models.IntegerField(null=True, blank=True)
    achievements = models.TextField(max_length=500, blank=True)
    teaching_experience = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user_profile.user.username} - {self.degree} in {self.field_of_study}"

class Contacts(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True, blank=True)
    contact_no = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.contact_no