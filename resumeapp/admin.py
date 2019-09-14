from django.contrib import admin

from solo.admin import SingletonModelAdmin
from .models import SiteConfiguration,Experience,Education,Skill,Interest,Award

from django.contrib.auth.models import User, Group


admin.site.unregister(User)
admin.site.unregister(Group)




admin.site.register(SiteConfiguration, SingletonModelAdmin)
admin.site.register(Experience)
admin.site.register(Education)
admin.site.register(Skill)
admin.site.register(Interest)
admin.site.register(Award)

