# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Address'
        db.create_table('main_address', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('building_name', self.gf('django.db.models.fields.CharField')(default='', max_length=512, blank=True)),
            ('street1', self.gf('django.db.models.fields.CharField')(max_length=512)),
            ('street2', self.gf('django.db.models.fields.CharField')(default='', max_length=512, blank=True)),
            ('street3', self.gf('django.db.models.fields.CharField')(default='', max_length=512, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('state', self.gf('django.db.models.fields.CharField')(default='NJ', max_length=2)),
            ('postal_code', self.gf('django.db.models.fields.CharField')(max_length=16)),
        ))
        db.send_create_signal('main', ['Address'])

        # Adding model 'Agent'
        db.create_table('main_agent', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=512)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=512)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=512)),
            ('phone_number', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('business_address', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Address'], null=True)),
            ('broker', self.gf('django.db.models.fields.CharField')(default='LVL', max_length=512, blank=True)),
        ))
        db.send_create_signal('main', ['Agent'])

        # Adding model 'Listing'
        db.create_table('main_listing', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('contact', self.gf('django.db.models.fields.CharField')(default='', max_length=512, blank=True)),
            ('address', self.gf('django.db.models.fields.related.ForeignKey')(related_name='properties', to=orm['main.Address'])),
            ('created_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified_date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('listing_date', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('closing_date', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('sale_price', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2)),
            ('gross_commission_income', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2)),
        ))
        db.send_create_signal('main', ['Listing'])

        # Adding model 'ListingClosingAgent'
        db.create_table('main_listingclosingagent', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('listing', self.gf('django.db.models.fields.related.ForeignKey')(related_name='agents', to=orm['main.Listing'])),
            ('agent', self.gf('django.db.models.fields.related.ForeignKey')(related_name='listings', to=orm['main.Agent'])),
            ('agent_position', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('agent_commission', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
            ('broker_commission', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
            ('referral', self.gf('django.db.models.fields.DecimalField')(default='0.0', max_digits=10, decimal_places=2)),
            ('broker_fee', self.gf('django.db.models.fields.DecimalField')(default='0.0', max_digits=10, decimal_places=2)),
        ))
        db.send_create_signal('main', ['ListingClosingAgent'])


    def backwards(self, orm):
        
        # Deleting model 'Address'
        db.delete_table('main_address')

        # Deleting model 'Agent'
        db.delete_table('main_agent')

        # Deleting model 'Listing'
        db.delete_table('main_listing')

        # Deleting model 'ListingClosingAgent'
        db.delete_table('main_listingclosingagent')


    models = {
        'main.address': {
            'Meta': {'object_name': 'Address'},
            'building_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '512', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'postal_code': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'state': ('django.db.models.fields.CharField', [], {'default': "'NJ'", 'max_length': '2'}),
            'street1': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'street2': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '512', 'blank': 'True'}),
            'street3': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '512', 'blank': 'True'})
        },
        'main.agent': {
            'Meta': {'object_name': 'Agent'},
            'broker': ('django.db.models.fields.CharField', [], {'default': "'LVL'", 'max_length': '512', 'blank': 'True'}),
            'business_address': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Address']", 'null': 'True'}),
            'closed_properties': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['main.Listing']", 'through': "orm['main.ListingClosingAgent']", 'symmetrical': 'False'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'phone_number': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        'main.listing': {
            'Meta': {'object_name': 'Listing'},
            'address': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'properties'", 'to': "orm['main.Address']"}),
            'closing_agents': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['main.Agent']", 'through': "orm['main.ListingClosingAgent']", 'symmetrical': 'False'}),
            'closing_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'contact': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '512', 'blank': 'True'}),
            'created_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'gross_commission_income': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'listing_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'modified_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'sale_price': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2'})
        },
        'main.listingclosingagent': {
            'Meta': {'object_name': 'ListingClosingAgent'},
            'agent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'listings'", 'to': "orm['main.Agent']"}),
            'agent_commission': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'agent_position': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'broker_commission': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'broker_fee': ('django.db.models.fields.DecimalField', [], {'default': "'0.0'", 'max_digits': '10', 'decimal_places': '2'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'listing': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'agents'", 'to': "orm['main.Listing']"}),
            'referral': ('django.db.models.fields.DecimalField', [], {'default': "'0.0'", 'max_digits': '10', 'decimal_places': '2'})
        }
    }

    complete_apps = ['main']
