from django.contrib import admin

from apps.main.models import \
    Listing, Address, Agent, ListingClosingAgent

class ListingAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'created_date', 'address', 'sale_price', 'closing_date'
    )
    list_filter = ('listing_date', 'closing_date')
    ordering = ('created_date', )
    search_fields = ('address', )


class AddressAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'street1', 'street2', 'city', 'postal_code'
    )
    list_display_links = ['id', ]
    list_editable = ('street1', 'street2', 'city', 'postal_code')
    ordering = ('city', )
    search_fields = ('street1', 'street2', 'city', 'postal_code')


class AgentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'broker')
    list_filter = ('broker', )
    search_fields = ('first_name', 'last_name')
    

class ListingClosingAgentAdmin(admin.ModelAdmin):
    list_display = (
        'listing', 'agent', 'agent_commission', 'gross_commission'
    )
    list_filter = ('agent__broker', )
    search_fields = (
        'listing__address__street1', 'listing__address__street2',
        'listing__address__city', 'listing__address__postal_code',
        'agent__first_name', 'agent__last_name'
    )
    

admin.site.register(Listing, ListingAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(Agent, AgentAdmin)
admin.site.register(ListingClosingAgent, ListingClosingAgentAdmin)
