from django.shortcuts import render
from django.template import RequestContext

from dt_forms import AgentsDataTable, ListingsDataTable


def landing_page(request):
    """
    A landing page where a welcome message, recent additions
    and the like can be displayed
    """
    template = 'main/landing.html'
    context = dict()

    return render(
        request,
        template,
        context,
    )

def agents(request):
    template = 'main/agents.html'
    context = {
        'table_type': 'AgentsDataTable'
    }

    return render(
        request,
        template,
        context,
    )
