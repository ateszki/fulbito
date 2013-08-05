from canchas.models import Complejo, ComplejoTag, ComplejoUsuario, Cancha
from django.contrib import admin
from django import forms
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

#complejos

class ComplejoAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('nombre',)}
    list_display = ('nombre', 'descripcion', 'modificado')


admin.site.register(Complejo, ComplejoAdmin)
admin.site.register(ComplejoTag)


#usuarios

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

#canchas
class CanchaForm(forms.ModelForm):
    
    class meta:
        model = Cancha
    
    def __init__(self, *args, **kwargs):
        super(CanchaForm, self).__init__(*args, **kwargs)
        if self.instance.pk:
            self.fields['canchas_relacionadas'].queryset = Cancha.objects.filter(complejo=self.instance.complejo)
            #self.fields['complejo'].widget.attrs['readonly'] = True

class CanchaAdmin(admin.ModelAdmin):
    form = CanchaForm

    def get_form(self, request, obj=None, **kwargs):
        form = super(CanchaAdmin, self).get_form(request, obj, **kwargs)
        if obj == None:
           del form.base_fields['canchas_relacionadas']
        return form
    def get_readonly_fields(self, request, obj=None):
        if obj: # editing an existing object
            return self.readonly_fields + ('complejo',)
        return self.readonly_fields

admin.site.register(Cancha, CanchaAdmin)


    