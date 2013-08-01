from canchas.models import Complejo, ComplejoTag, ComplejoUsuario
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User



class ComplejoAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('nombre',)}
    list_display = ('nombre', 'descripcion', 'modificado')


admin.site.register(Complejo, ComplejoAdmin)
admin.site.register(ComplejoTag)


# Define an inline admin descriptor for UserProfile model
# which acts a bit like a singleton
class ComplejoUsuarioInline(admin.StackedInline):
    model = ComplejoUsuario
    can_delete = False
    verbose_name_plural = 'Complejo'

# Define a new User admin
class UserAdmin(UserAdmin):
    inlines = (ComplejoUsuarioInline, )
    list_filter = ('complejousuario__complejo','complejousuario__es_admin')

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

    