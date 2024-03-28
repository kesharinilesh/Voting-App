from django.contrib import admin
from votingProject.models import UserProfile,Choice,Vote,Poll


# Register your models here.

admin.site.register(UserProfile)
admin.site.register(Choice)
admin.site.register(Vote)
admin.site.register(Poll)