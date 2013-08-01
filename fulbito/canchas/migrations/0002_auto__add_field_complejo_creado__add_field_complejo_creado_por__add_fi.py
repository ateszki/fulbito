# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Complejo.creado'
        db.add_column('canchas_complejo', 'creado',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Complejo.creado_por'
        db.add_column('canchas_complejo', 'creado_por',
                      self.gf('django.db.models.fields.related.ForeignKey')(related_name='complejo_creado_por', null=True, to=orm['auth.User']),
                      keep_default=False)

        # Adding field 'Complejo.modificado'
        db.add_column('canchas_complejo', 'modificado',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Complejo.modificado_por'
        db.add_column('canchas_complejo', 'modificado_por',
                      self.gf('django.db.models.fields.related.ForeignKey')(related_name='complejo_modificado_por', null=True, to=orm['auth.User']),
                      keep_default=False)

        # Adding M2M table for field users on 'Complejo'
        db.create_table('canchas_complejo_users', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('complejo', models.ForeignKey(orm['canchas.complejo'], null=False)),
            ('user', models.ForeignKey(orm['auth.user'], null=False))
        ))
        db.create_unique('canchas_complejo_users', ['complejo_id', 'user_id'])

        # Adding field 'Cliente.creado'
        db.add_column('canchas_cliente', 'creado',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Cliente.creado_por'
        db.add_column('canchas_cliente', 'creado_por',
                      self.gf('django.db.models.fields.related.ForeignKey')(related_name='cliente_creado_por', null=True, to=orm['auth.User']),
                      keep_default=False)

        # Adding field 'Cliente.modificado'
        db.add_column('canchas_cliente', 'modificado',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Cliente.modificado_por'
        db.add_column('canchas_cliente', 'modificado_por',
                      self.gf('django.db.models.fields.related.ForeignKey')(related_name='cliente_modificado_por', null=True, to=orm['auth.User']),
                      keep_default=False)

        # Adding field 'Abono.creado'
        db.add_column('canchas_abono', 'creado',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Abono.creado_por'
        db.add_column('canchas_abono', 'creado_por',
                      self.gf('django.db.models.fields.related.ForeignKey')(related_name='abono_creado_por', null=True, to=orm['auth.User']),
                      keep_default=False)

        # Adding field 'Abono.modificado'
        db.add_column('canchas_abono', 'modificado',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Abono.modificado_por'
        db.add_column('canchas_abono', 'modificado_por',
                      self.gf('django.db.models.fields.related.ForeignKey')(related_name='abono_modificado_por', null=True, to=orm['auth.User']),
                      keep_default=False)

        # Adding field 'Turno.fecha'
        db.add_column('canchas_turno', 'fecha',
                      self.gf('django.db.models.fields.DateField')(null=True),
                      keep_default=False)

        # Adding field 'Turno.creado'
        db.add_column('canchas_turno', 'creado',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Turno.creado_por'
        db.add_column('canchas_turno', 'creado_por',
                      self.gf('django.db.models.fields.related.ForeignKey')(related_name='turno_creado_por', null=True, to=orm['auth.User']),
                      keep_default=False)

        # Adding field 'Turno.modificado'
        db.add_column('canchas_turno', 'modificado',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Turno.modificado_por'
        db.add_column('canchas_turno', 'modificado_por',
                      self.gf('django.db.models.fields.related.ForeignKey')(related_name='turno_modificado_por', null=True, to=orm['auth.User']),
                      keep_default=False)

        # Adding field 'Cancha.creado'
        db.add_column('canchas_cancha', 'creado',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Cancha.creado_por'
        db.add_column('canchas_cancha', 'creado_por',
                      self.gf('django.db.models.fields.related.ForeignKey')(related_name='cancha_creado_por', null=True, to=orm['auth.User']),
                      keep_default=False)

        # Adding field 'Cancha.modificado'
        db.add_column('canchas_cancha', 'modificado',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Cancha.modificado_por'
        db.add_column('canchas_cancha', 'modificado_por',
                      self.gf('django.db.models.fields.related.ForeignKey')(related_name='cancha_modificado_por', null=True, to=orm['auth.User']),
                      keep_default=False)

        # Adding field 'CanchaCompuesta.creado'
        db.add_column('canchas_canchacompuesta', 'creado',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CanchaCompuesta.creado_por'
        db.add_column('canchas_canchacompuesta', 'creado_por',
                      self.gf('django.db.models.fields.related.ForeignKey')(related_name='cancha_compuesta_creado_por', null=True, to=orm['auth.User']),
                      keep_default=False)

        # Adding field 'CanchaCompuesta.modificado'
        db.add_column('canchas_canchacompuesta', 'modificado',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CanchaCompuesta.modificado_por'
        db.add_column('canchas_canchacompuesta', 'modificado_por',
                      self.gf('django.db.models.fields.related.ForeignKey')(related_name='cancha_compuesta_modificado_por', null=True, to=orm['auth.User']),
                      keep_default=False)

        # Adding field 'Precio.creado'
        db.add_column('canchas_precio', 'creado',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Precio.creado_por'
        db.add_column('canchas_precio', 'creado_por',
                      self.gf('django.db.models.fields.related.ForeignKey')(related_name='precio_creado_por', null=True, to=orm['auth.User']),
                      keep_default=False)

        # Adding field 'Precio.modificado'
        db.add_column('canchas_precio', 'modificado',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Precio.modificado_por'
        db.add_column('canchas_precio', 'modificado_por',
                      self.gf('django.db.models.fields.related.ForeignKey')(related_name='precio_modificado_por', null=True, to=orm['auth.User']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Complejo.creado'
        db.delete_column('canchas_complejo', 'creado')

        # Deleting field 'Complejo.creado_por'
        db.delete_column('canchas_complejo', 'creado_por_id')

        # Deleting field 'Complejo.modificado'
        db.delete_column('canchas_complejo', 'modificado')

        # Deleting field 'Complejo.modificado_por'
        db.delete_column('canchas_complejo', 'modificado_por_id')

        # Removing M2M table for field users on 'Complejo'
        db.delete_table('canchas_complejo_users')

        # Deleting field 'Cliente.creado'
        db.delete_column('canchas_cliente', 'creado')

        # Deleting field 'Cliente.creado_por'
        db.delete_column('canchas_cliente', 'creado_por_id')

        # Deleting field 'Cliente.modificado'
        db.delete_column('canchas_cliente', 'modificado')

        # Deleting field 'Cliente.modificado_por'
        db.delete_column('canchas_cliente', 'modificado_por_id')

        # Deleting field 'Abono.creado'
        db.delete_column('canchas_abono', 'creado')

        # Deleting field 'Abono.creado_por'
        db.delete_column('canchas_abono', 'creado_por_id')

        # Deleting field 'Abono.modificado'
        db.delete_column('canchas_abono', 'modificado')

        # Deleting field 'Abono.modificado_por'
        db.delete_column('canchas_abono', 'modificado_por_id')

        # Deleting field 'Turno.fecha'
        db.delete_column('canchas_turno', 'fecha')

        # Deleting field 'Turno.creado'
        db.delete_column('canchas_turno', 'creado')

        # Deleting field 'Turno.creado_por'
        db.delete_column('canchas_turno', 'creado_por_id')

        # Deleting field 'Turno.modificado'
        db.delete_column('canchas_turno', 'modificado')

        # Deleting field 'Turno.modificado_por'
        db.delete_column('canchas_turno', 'modificado_por_id')

        # Deleting field 'Cancha.creado'
        db.delete_column('canchas_cancha', 'creado')

        # Deleting field 'Cancha.creado_por'
        db.delete_column('canchas_cancha', 'creado_por_id')

        # Deleting field 'Cancha.modificado'
        db.delete_column('canchas_cancha', 'modificado')

        # Deleting field 'Cancha.modificado_por'
        db.delete_column('canchas_cancha', 'modificado_por_id')

        # Deleting field 'CanchaCompuesta.creado'
        db.delete_column('canchas_canchacompuesta', 'creado')

        # Deleting field 'CanchaCompuesta.creado_por'
        db.delete_column('canchas_canchacompuesta', 'creado_por_id')

        # Deleting field 'CanchaCompuesta.modificado'
        db.delete_column('canchas_canchacompuesta', 'modificado')

        # Deleting field 'CanchaCompuesta.modificado_por'
        db.delete_column('canchas_canchacompuesta', 'modificado_por_id')

        # Deleting field 'Precio.creado'
        db.delete_column('canchas_precio', 'creado')

        # Deleting field 'Precio.creado_por'
        db.delete_column('canchas_precio', 'creado_por_id')

        # Deleting field 'Precio.modificado'
        db.delete_column('canchas_precio', 'modificado')

        # Deleting field 'Precio.modificado_por'
        db.delete_column('canchas_precio', 'modificado_por_id')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'canchas.abono': {
            'Meta': {'object_name': 'Abono'},
            'cancha': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['canchas.Cancha']"}),
            'cancha_compuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['canchas.CanchaCompuesta']"}),
            'cliente': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['canchas.Cliente']"}),
            'creado': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'creado_por': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'abono_creado_por'", 'null': 'True', 'to': "orm['auth.User']"}),
            'desde': ('django.db.models.fields.DateTimeField', [], {}),
            'dia': ('django.db.models.fields.IntegerField', [], {}),
            'hasta': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modificado': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'modificado_por': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'abono_modificado_por'", 'null': 'True', 'to': "orm['auth.User']"}),
            'vigencia': ('django.db.models.fields.DateField', [], {})
        },
        'canchas.cancha': {
            'Meta': {'object_name': 'Cancha'},
            'complejo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['canchas.Complejo']"}),
            'creado': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'creado_por': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'cancha_creado_por'", 'null': 'True', 'to': "orm['auth.User']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jugadores': ('django.db.models.fields.IntegerField', [], {}),
            'modificado': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'modificado_por': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'cancha_modificado_por'", 'null': 'True', 'to': "orm['auth.User']"}),
            'numero': ('django.db.models.fields.IntegerField', [], {})
        },
        'canchas.canchacompuesta': {
            'Meta': {'object_name': 'CanchaCompuesta'},
            'canchas': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['canchas.Cancha']", 'symmetrical': 'False'}),
            'complejo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['canchas.Complejo']"}),
            'creado': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'creado_por': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'cancha_compuesta_creado_por'", 'null': 'True', 'to': "orm['auth.User']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jugadores': ('django.db.models.fields.IntegerField', [], {}),
            'modificado': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'modificado_por': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'cancha_compuesta_modificado_por'", 'null': 'True', 'to': "orm['auth.User']"}),
            'numero': ('django.db.models.fields.IntegerField', [], {})
        },
        'canchas.cliente': {
            'Meta': {'object_name': 'Cliente'},
            'celular': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'creado': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'creado_por': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'cliente_creado_por'", 'null': 'True', 'to': "orm['auth.User']"}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '254'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modificado': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'modificado_por': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'cliente_modificado_por'", 'null': 'True', 'to': "orm['auth.User']"}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'observaciones': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'canchas.complejo': {
            'Meta': {'object_name': 'Complejo'},
            'ciudad': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'coord': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'creado': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'creado_por': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'complejo_creado_por'", 'null': 'True', 'to': "orm['auth.User']"}),
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'domicilio': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modificado': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'modificado_por': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'complejo_modificado_por'", 'null': 'True', 'to': "orm['auth.User']"}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'pais': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'provincia': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['canchas.ComplejoTag']", 'symmetrical': 'False'}),
            'users': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.User']", 'symmetrical': 'False'})
        },
        'canchas.complejotag': {
            'Meta': {'object_name': 'ComplejoTag'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tag': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'users': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.User']", 'symmetrical': 'False'})
        },
        'canchas.precio': {
            'Meta': {'object_name': 'Precio'},
            'canchas': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['canchas.Cancha']", 'symmetrical': 'False'}),
            'creado': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'creado_por': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'precio_creado_por'", 'null': 'True', 'to': "orm['auth.User']"}),
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'desde': ('django.db.models.fields.DateTimeField', [], {}),
            'dias': ('django.db.models.fields.CharField', [], {'max_length': '13'}),
            'hasta': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modificado': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'modificado_por': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'precio_modificado_por'", 'null': 'True', 'to': "orm['auth.User']"})
        },
        'canchas.turno': {
            'Meta': {'object_name': 'Turno'},
            'anio': ('django.db.models.fields.IntegerField', [], {}),
            'cancha': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['canchas.Cancha']"}),
            'cancha_compuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['canchas.CanchaCompuesta']"}),
            'cliente': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['canchas.Cliente']"}),
            'creado': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'creado_por': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'turno_creado_por'", 'null': 'True', 'to': "orm['auth.User']"}),
            'desde': ('django.db.models.fields.DateTimeField', [], {}),
            'dia': ('django.db.models.fields.IntegerField', [], {}),
            'es_abono': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'estado': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'fecha': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'hasta': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modificado': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'modificado_por': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'turno_modificado_por'", 'null': 'True', 'to': "orm['auth.User']"}),
            'precio': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2'}),
            'semana': ('django.db.models.fields.IntegerField', [], {})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['canchas']