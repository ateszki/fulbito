# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing M2M table for field users on 'ComplejoTag'
        db.delete_table('canchas_complejotag_users')


    def backwards(self, orm):
        # Adding M2M table for field users on 'ComplejoTag'
        db.create_table('canchas_complejotag_users', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('complejotag', models.ForeignKey(orm['canchas.complejotag'], null=False)),
            ('user', models.ForeignKey(orm['auth.user'], null=False))
        ))
        db.create_unique('canchas_complejotag_users', ['complejotag_id', 'user_id'])


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
            'tag': ('django.db.models.fields.CharField', [], {'max_length': '200'})
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