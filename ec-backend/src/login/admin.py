from django.contrib import admin

from .models import Profile, ThirdLoginInfo


# class ThirdPartyInfoAdmin(admin.ModelAdmin):
#     list_display = ["__unicode__", 'slug']
#
#     class Meta:
#         model = ThirdPartyInfo
#
#
# admin.site.register(ThirdPartyInfo, ThirdPartyInfoAdmin)
admin.site.register(ThirdLoginInfo)

admin.site.register(Profile)
