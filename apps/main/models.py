from django.contrib.localflavor.us.us_states import STATE_CHOICES
from django.db import models


class Address(models.Model):
    """
    A generic US address
    """
    building_name = models.CharField(max_length=512, blank=True, default='')
    street1 = models.CharField(max_length=512)
    street2 = models.CharField(max_length=512, blank=True, default='')
    street3 = models.CharField(max_length=512, blank=True, default='')
    city = models.CharField(max_length=256)
    state = models.CharField(
            max_length=2,
            choices=STATE_CHOICES,
            default='NJ'
    )
    postal_code = models.CharField(max_length=16)

    def __unicode__(self):
        if self.street2:
            addr2 = " " + self.street2
        else:
            addr2 = ''

        return (
            '{street1}{street2} {city}, {state} {zip}'
            .format(
                street1=self.street1,
                street2=addr2,
                city=self.city,
                state=self.state,
                zip=self.postal_code
            )
        )


class Agent(models.Model):
    """
    This is a list of all known agents
    """
    first_name = models.CharField(max_length=512)
    last_name = models.CharField(max_length=512)
    email = models.CharField(max_length=512, default='', blank=True)

    phone_number = models.CharField(max_length=15, default='', blank=True)
    business_address = models.ForeignKey(Address, null=True)

    # The agency the broker belongs to
    # TODO: Add in a new model for this. The charfield is just a place holder
    broker = models.CharField(max_length=512, blank=True, default='LVL')

    closed_properties = models.ManyToManyField(
        'Listing', through='ListingClosingAgent'
    )

    def __unicode__(self):
        return (
            '{first} {last}'
            .format(
                first=self.first_name,
                last=self.last_name,
            )
        )

    def get_absolute_url(self):
        return '/agent/{0}'.format(self.id)


class Listing(models.Model):
    """
    The base of all transactions is a listing. This is the item
    being sold. If the same house is sold multiple times, there
    should be one entry for each listing.
    """

    # For an internal listing this should be the home owner.
    # If a sale, it should be the sales agent.
    # TODO: Expand this field into other models if there is a need
    contact = models.CharField(max_length=512, blank=True, default='')

    # The physical location of the listing
    address = models.ForeignKey(Address, related_name='properties')

    # TODO: created/modified should be pulled out into a generic so it can
    #       be inherited. Users to be added later.
    created_date = models.DateTimeField(auto_now_add=True)
    # created_by = models.ForeignKey(User)

    modified_date = models.DateTimeField(auto_now=True)
    # modified_by =  models.ForeignKey(User)

    # The date the listing went on the market
    listing_date = models.DateTimeField(null=True)

    # The date the listing was closed on
    closing_date = models.DateTimeField(null=True)

    # TODO: There were several more milestone dates that I need to find
    #       out about and add

    # The amount that the listing actually closed for
    # TODO: for internally listed properties, we may want to
    #       add price changes
    sale_price = models.DecimalField(
        max_digits=10, decimal_places=2, null=True
    )

    # How much total commission for the company was
    # TODO: This may need to be a listing instead of a field
    gross_commission_income = models.DecimalField(
        max_digits=10, decimal_places=2, null=True
    )

    closing_agents = models.ManyToManyField(
        'Agent', through='ListingClosingAgent'
    )

    def __unicode__(self):
        return (
            'Listing {pk} at {addr}'
            .format(
                pk=self.pk,
                addr=self.address.__unicode__()
            )
        )


AGENT_CHOICES = (
    ('listing', 'listing'),
    ('selling', 'selling'),
    ('associate listing', 'assoc_listing'),
    ('associate seller', 'assoc_sell'),
)

class ListingClosingAgent(models.Model):
    """
    A list of all agents associated with the closing on a listing.
    Commission calculations/overrides go here.
    """

    listing = models.ForeignKey('Listing', related_name='agents')
    agent = models.ForeignKey('Agent', related_name='listings')

# TODO: This needs a better name.
    agent_position = models.CharField(
        max_length=20,
        choices=AGENT_CHOICES,
    ) 
        
    agent_commission = models.DecimalField(max_digits=10, decimal_places=2)
    broker_commission = models.DecimalField(max_digits=10, decimal_places=2)

    # this is the price that the agent had to pay out of their commission
    # as a price to get to closing
    # TODO: Figure out if this should be assigned to an agent, or moved
    #       a listing level
    # TODO: Could there be more than one or could there be multiples
    #       needing a separate model to document them
    referral =  models.DecimalField(
        max_digits=10, decimal_places=2, default='0.0'
        )
    
    # This is a fee taken off the top of the commission
    # TODO: Is this a one off or could there be multiple requiring a
    #       separate model to document them
    broker_fee =  models.DecimalField(
        max_digits=10, decimal_places=2, default='0.0'
    )
       
    @property
    def gross_commission(self):
        """
        The total commission generated by this closing. Usually used
        to calculate the following year's commission structure.

        TODO: This calculation most likely needs to be updated
        """

        return self.agent_commission + self.broker_commission
