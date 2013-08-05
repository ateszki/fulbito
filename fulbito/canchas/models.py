# encoding: utf-8
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
class ComplejoTag(models.Model):
    tag = models.CharField(max_length=200)

    def __unicode__(self):
        return self.tag

class Complejo(models.Model):
    nombre = models.CharField(max_length=300)
    descripcion = models.CharField(max_length=300)
    domicilio = models.CharField(max_length=300)
    ciudad = models.CharField(max_length=300)
    provincia = models.CharField(max_length=300)
    pais = models.CharField(max_length=300)
    coord = models.CharField(max_length=300)
    tags = models.ManyToManyField(ComplejoTag,blank=True, null=True)
    creado = models.DateTimeField(auto_now_add=True, null=True, editable=False)
    creado_por = models.ForeignKey(User, null=True, editable=False, related_name='complejo_creado_por')
    modificado = models.DateTimeField(auto_now=True, null=True, editable=False)
    modificado_por = models.ForeignKey(User, null=True, editable=False, related_name='complejo_modificado_por')
    slug = models.SlugField(null=True)

    def __unicode__(self):
        return self.nombre
    
class ComplejoUsuario(models.Model):
    complejo = models.ForeignKey(Complejo, null=True)
    user = models.OneToOneField(User,blank=True, null=True)
    es_admin = models.BooleanField(default=False)
    def __unicode__(self):
        return self.user.username

    def create_complejo_usuario(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)
    
    post_save.connect(create_complejo_usuario, sender=User)
    
class Cancha(models.Model):
    complejo = models.ForeignKey(Complejo)
    numero = models.IntegerField()
    jugadores = models.IntegerField()
    es_compuesta = models.BooleanField(default=False)
    canchas_relacionadas = models.ManyToManyField('self', blank=True, null=True)
    creado = models.DateTimeField(auto_now_add=True, null=True)
    creado_por = models.ForeignKey(User, null=True, editable=False, related_name='cancha_creado_por')
    modificado = models.DateTimeField(auto_now=True, null=True)
    modificado_por = models.ForeignKey(User, null=True, editable=False, related_name='cancha_modificado_por')

    def __unicode__(self):
        return '%s - Cancha %s' % (self.complejo, self.numero)

class Cliente(models.Model):
    nombre = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    celular = models.CharField(max_length=200)
    telefono = models.CharField(max_length=200)
    observaciones = models.CharField(max_length=500)
    creado = models.DateTimeField(auto_now_add=True, null=True)
    creado_por = models.ForeignKey(User, null=True, editable=False, related_name='cliente_creado_por')
    modificado = models.DateTimeField(auto_now=True, null=True)
    modificado_por = models.ForeignKey(User, null=True, editable=False, related_name='cliente_modificado_por')

    def __unicode__(self):
        return self.nombre

class Turno(models.Model):
    anio = models.IntegerField()
    semana = models.IntegerField()
    fecha = models.DateField(null=True)
    DIAS_SEMANA = ((1, 'Lunes'), (2, 'Martes'), (3, 'Miércoles'), (4, 'Jueves'), (5, 'Viernes'), (6, 'Sabado'), (7, 'Domingo'))
    dia = models.IntegerField(choices=DIAS_SEMANA)
    desde = models.DateTimeField()
    hasta = models.DateTimeField()
    cliente = models.ForeignKey(Cliente)
    cancha = models.ForeignKey(Cancha)
    es_abono = models.BooleanField()
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    ESTADOS_TURNOS = (
    ('SE', 'Señado'),
    ('CA', 'Cancelado'),
    ('LI', 'Libre'),
    ('JU', 'Jugado'),
    ('RE', 'Reservado'),
    )
    estado = models.CharField(max_length=2, choices=ESTADOS_TURNOS)
    creado = models.DateTimeField(auto_now_add=True, null=True)
    creado_por = models.ForeignKey(User, null=True, editable=False, related_name='turno_creado_por')
    modificado = models.DateTimeField(auto_now=True, null=True)
    modificado_por = models.ForeignKey(User, null=True, editable=False, related_name='turno_modificado_por')
    
    
    def __unicode__(self):
        dias_dic = dict(self.DIAS_SEMANA)
        return u'%s %s %s %s ' % ('Turno', self.cliente, dias_dic[self.dia],self.desde)

    
class Abono(models.Model):
    vigencia = models.DateField()
    cliente = models.ForeignKey(Cliente)
    cancha = models.ForeignKey(Cancha)
    dia = models.IntegerField()
    desde = models.DateTimeField()
    hasta = models.DateTimeField()
    creado = models.DateTimeField(auto_now_add=True, null=True)
    creado_por = models.ForeignKey(User, null=True, editable=False, related_name='abono_creado_por')
    modificado = models.DateTimeField(auto_now=True, null=True)
    modificado_por = models.ForeignKey(User, null=True, editable=False, related_name='abono_modificado_por')

    def __unicode__(self):
        return u'%s %s' % ('Abono', self.cliente)

class Precio(models.Model):
    descripcion = models.CharField(max_length=200)
    dias = models.CharField(max_length=13)
    desde = models.DateTimeField()
    hasta = models.DateTimeField()
    canchas = models.ManyToManyField(Cancha)
    creado = models.DateTimeField(auto_now_add=True, null=True)
    creado_por = models.ForeignKey(User, null=True, editable=False, related_name='precio_creado_por')
    modificado = models.DateTimeField(auto_now=True, null=True)
    modificado_por = models.ForeignKey(User, null=True, editable=False, related_name='precio_modificado_por')

    def __unicode__(self):
        return self.descripcion
    
    

