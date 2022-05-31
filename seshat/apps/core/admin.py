from django.contrib import admin
from .models import Polity, Country, Section, Subsection, Citation, Reference, VariableHierarchy


admin.site.register(Section)
admin.site.register(Subsection)
admin.site.register(VariableHierarchy)
admin.site.register(Polity)
admin.site.register(Country)
admin.site.register(Citation)
admin.site.register(Reference)


# class CustomUserAdmin(UserAdmin):
#     inlines = (ProfileInline, )

#     list_display = ('username', 'email', 'first_name',
#                     'last_name', 'is_staff', 'get_location')
#     list_select_related = ('profile', )

#     def get_location(self, instance):
#         return instance.profile.location
#     get_location.short_description = 'Location'

#     def get_inline_instances(self, request, obj=None):
#         if not obj:
#             return list()
#         return super(CustomUserAdmin, self).get_inline_instances(request, obj)


# admin.site.unregister(User)
# admin.site.register(User, CustomUserAdmin)
