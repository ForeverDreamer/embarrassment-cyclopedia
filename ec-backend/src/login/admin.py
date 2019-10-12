from django.contrib import admin

from .models import Profile, ThirdPartyInfo


# class ThirdPartyInfoAdmin(admin.ModelAdmin):
#     list_display = ["__unicode__", 'slug']
#
#     class Meta:
#         model = ThirdPartyInfo
#
#
# admin.site.register(ThirdPartyInfo, ThirdPartyInfoAdmin)
admin.site.register(ThirdPartyInfo)

admin.site.register(Profile)
