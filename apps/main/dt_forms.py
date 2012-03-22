from decimal import Decimal

from django.core.urlresolvers import reverse
from django.db.models import Count, Sum
from django.utils.datastructures import SortedDict

from data_tables.forms import JQueryDataTable, DTColumn, DTButton
from main.models import Agent

__all__ = [
    'AgentsDataTable',
    'ListingsDataTable',
]


class AgentsDataTable(JQueryDataTable):
    agent = DTColumn(
        label='Agent Name',
    )

    listing_count = DTColumn(
        label='Listings'
    )

    total_gci = DTColumn(
        label='Total GCI',
        default=Decimal('0.00')
    )

    total_commission = DTColumn(
        label='Total Commission',
        default=Decimal('0.00')
    )
  
    add_agent_button = DTButton(
        label='Add Agent',
        action_type='JUMP',
# TODO: Fix the bug preventing reverse from working
#        target_view=reverse('main:add_agent'),
        target_view='/manage/agent/new',
        use_selected='IGNORE'
    )
        
    def load_data(self):
        '''
        Gets a list of all the agents and some counts associated with them
        '''
        
        agents = Agent.objects.annotate(
            listing_count=Count('listings'),
            commission=Sum('listings__agent_commission'),
            broker_commission=Sum('listings__broker_commission'),
        )

        for agent in agents.iterator():
            row = self.add_data_row()
            row['Agent Name'].value = agent.__unicode__()
            row['Agent Name'].format.link_url = agent.get_absolute_url()


            row['Listings'].value = agent.listing_count

            if agent.commission:
                row['Total Commission'].value = agent.commission

            if agent.broker_commission:
                row['Total GCI'].value = \
                    agent.commission + agent.broker_commission




class ListingsDataTable(JQueryDataTable):
    pass
