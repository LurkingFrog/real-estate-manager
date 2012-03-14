from django.utils.datastructures import SortedDict

from django.db.models import Count, Sum

from data_tables.forms import JQueryDataTable, DTColumn, DTButton
from main.models import Agent

__all__ = [
    'AgentsDataTable',
    'ListingsDataTable',
]


class AgentsDataTable(JQueryDataTable):
    agent = DTColumn(
        label='Agent Name'
    )

    listing_count = DTColumn(
        label='Listings'
    )

    total_gci = DTColumn(
        label='Total GCI'
    )

    total_commission = DTColumn(
        label='Total Commission'
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
            row = self.add_data()
            row['Agent Name'] = agent.__unicode__()
            row['Listings'] = agent.listing_count
            row['Total GCI'] = agent.commission + agent.broker_commission
            row['Total Commission'] = agent.commission

class ListingsDataTable(JQueryDataTable):
    pass
