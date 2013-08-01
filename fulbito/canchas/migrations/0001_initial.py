# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ComplejoTag'
        db.create_table('canchas_complejotag', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tag', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('canchas', ['ComplejoTag'])

        # Adding M2M table for field users on 'ComplejoTag'
        db.create_table('canchas_complejotag_users', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('complejotag', models.ForeignKey(orm['canchas.complejotag'], null=False)),
            ('user', models.ForeignKey(orm['auth.user'], null=False))
        ))
        db.create_unique('canchas_complejotag_users', ['complejotag_id', 'user_id'])

        # Adding model 'Complejo'
        db.create_table('canchas_complejo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('descripcion', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('domicilio', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('ciudad', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('provincia', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('pais', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('coord', self.gf('django.db.models.fields.CharField')(max_length=300)),
        ))
        db.send_create_signal('canchas', ['Complejo'])

        # Adding M2M table for field tags on 'Complejo'
        db.create_table('canchas_complejo_tags', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('complejo', models.ForeignKey(orm['canchas.complejo'], null=False)),
            ('complejotag', models.ForeignKey(orm['canchas.complejotag'], null=False))
        ))
        db.create_unique('canchas_complejo_tags', ['complejo_id', 'complejotag_id'])

        # Adding model 'Cancha'
        db.create_table('canchas_cancha', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('complejo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['canchas.Complejo'])),
            ('numero', self.gf('django.db.models.fields.IntegerField')()),
            ('jugadores', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('canchas', ['Cancha'])

        # Adding model 'CanchaCompuesta'
        db.create_table('canchas_canchacompuesta', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('complejo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['canchas.Complejo'])),
            ('numero', self.gf('django.db.models.fields.IntegerField')()),
            ('jugadores', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('canchas', ['CanchaCompuesta'])

        # Adding M2M table for field canchas on 'CanchaCompuesta'
        db.create_table('canchas_canchacompuesta_canchas', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('canchacompuesta', models.ForeignKey(orm['canchas.canchacompuesta'], null=False)),
            ('cancha', models.ForeignKey(orm['canchas.cancha'], null=False))
        ))
        db.create_unique('canchas_canchacompuesta_canchas', ['canchacompuesta_id', 'cancha_id'])

        # Adding model 'Cliente'
        db.create_table('canchas_cliente', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=254)),
            ('celular', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('telefono', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('observaciones', self.gf('django.db.models.fields.CharField')(max_length=500)),
        ))
        db.send_create_signal('canchas', ['Cliente'])

        # Adding model 'Turno'
        db.create_table('canchas_turno', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('anio', self.gf('django.db.models.fields.IntegerField')()),
            ('semana', self.gf('django.db.models.fields.IntegerField')()),
            ('dia', self.gf('django.db.models.fields.IntegerField')()),
            ('desde', self.gf('django.db.models.fields.DateTimeField')()),
            ('hasta', self.gf('django.db.models.fields.DateTimeField')()),
            ('cliente', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['canchas.Cliente'])),
            ('cancha', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['canchas.Cancha'])),
            ('cancha_compuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['canchas.CanchaCompuesta'])),
            ('es_abono', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('precio', self.gf('django.db.models.fields.DecimalField')(max_digits=8, decimal_places=2)),
            ('estado', self.gf('django.db.models.fields.CharField')(max_length=2)),
        ))
        db.send_create_signal('canchas', ['Turno'])

        # Adding model 'Abono'
        db.create_table('canchas_abono', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('vigencia', self.gf('django.db.models.fields.DateField')()),
            ('cliente', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['canchas.Cliente'])),
            ('cancha', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['canchas.Cancha'])),
            ('cancha_compuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['canchas.CanchaCompuesta'])),
            ('dia', self.gf('django.db.models.fields.IntegerField')()),
            ('desde', self.gf('django.db.models.fields.DateTimeField')()),
            ('hasta', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('canchas', ['Abono'])

        # Adding model 'Precio'
        db.create_table('canchas_precio', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('descripcion', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('dias', self.gf('django.db.models.fields.CharField')(max_length=13)),
            ('desde', self.gf('django.db.models.fields.DateTimeField')()),
            ('hasta', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('canchas', ['Precio'])

        # Adding M2M table for field canchas on 'Precio'
        db.create_table('canchas_precio_canchas', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('precio', models.ForeignKey(orm['canchas.precio'], null=False)),
            ('cancha', models.ForeignKey(orm['canchas.cancha'], null=False))
        ))
        db.create_unique('canchas_precio_canchas', ['precio_id', 'cancha_id'])


    def backwards(self, orm):
        # Deleting model 'ComplejoTag'
        db.delete_table('canchas_complejotag')

        # Removing M2M table for field users on 'ComplejoTag'
        db.delete_table('canchas_complejotag_users')

        # Deleting model 'Complejo'
        db.delete_table('canchas_complejo')

        # Removing M2M table for field tags on 'Complejo'
        db.delete_table('canchas_complejo_tags')

        # Deleting model 'Cancha'
        db.delete_table('canchas_cancha')

        # Deleting model 'CanchaCompuesta'
        db.delete_table('canchas_canchacompuesta')

        # Removing M2M table for field canchas on 'CanchaCompuesta'
        db.delete_table('canchas_canchacompuesta_canchas')

        # Deleting model 'Cliente'
        db.delete_table('canchas_cliente')

        # Deleting model 'Turno'
        db.delete_table('canchas_turno')

        # Deleting model 'Abono'
        db.delete_table('canchas_abono')

        # Deleting model 'Precio'
        db.delete_table('canchas_precio')

        # Removing M2M table for field canchas on 'Precio'
        db.delete_table('canchas_precio_canchas')


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
            'desde': ('django.db.models.fields.DateTimeField', [], {}),
            'dia': ('django.db.models.fields.IntegerField', [], {}),
            'hasta': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'vigencia': ('django.db.models.fields.DateField', [], {})
        },
        'canchas.cancha': {
            'Meta': {'object_name': 'Cancha'},
            'complejo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['canchas.Complejo']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jugadores': ('django.db.models.fields.IntegerField', [], {}),
            'numero': ('django.db.models.fields.IntegerField', [], {})
        },
        'canchas.canchacompuesta': {
            'Meta': {'object_name': 'CanchaCompuesta'},
            'canchas': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['canchas.Cancha']", 'symmetrical': 'False'}),
            'complejo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['canchas.Complejo']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jugadores': ('django.db.models.fields.IntegerField', [], {}),
            'numero': ('django.db.models.fields.IntegerField', [], {})
        },
        'canchas.cliente': {
            'Meta': {'object_name': 'Cliente'},
            'celular': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '254'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'observaciones': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'canchas.complejo': {
            'Meta': {'object_name': 'Complejo'},
            'ciudad': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'coord': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'domicilio': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'pais': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'provincia': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['canchas.ComplejoTag']", 'symmetrical': 'False'})
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
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'desde': ('django.db.models.fields.DateTimeField', [], {}),
            'dias': ('django.db.models.fields.CharField', [], {'max_length': '13'}),
            'hasta': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'canchas.turno': {
            'Meta': {'object_name': 'Turno'},
            'anio': ('django.db.models.fields.IntegerField', [], {}),
            'cancha': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['canchas.Cancha']"}),
            'cancha_compuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['canchas.CanchaCompuesta']"}),
            'cliente': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['canchas.Cliente']"}),
            'desde': ('django.db.models.fields.DateTimeField', [], {}),
            'dia': ('django.db.models.fields.IntegerField', [], {}),
            'es_abono': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'estado': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'hasta': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
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