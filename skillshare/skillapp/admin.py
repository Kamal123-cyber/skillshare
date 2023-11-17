from django.contrib import admin
from .models import UserProfile, Skill, Education

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio', 'location')  # Add fields you want to display in the admin list view

class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')  # Add fields you want to display in the admin list view

class EducationAdmin(admin.ModelAdmin):
    list_display = ('user_profile', 'institution_name', 'degree', 'field_of_study', 'graduation_year', 'achievements', 'created_at', 'updated_at')

admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Education, EducationAdmin)