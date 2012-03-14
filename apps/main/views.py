from django.shortcuts import render, get_object_or_404, redirect
from django.template import RequestContext

from dt_forms import AgentsDataTable, ListingsDataTable
from forms import ManageAgentForm
from models import Agent
 

def landing_page(request):
    """
    A landing page where a welcome message, recent additions
    and the like can be displayed
    """
    template = 'main/landing.html'
    context = dict()

    return render(request, template, context)


def agents(request):
    template = 'main/agents.html'
    context = {
        'table_type': 'AgentsDataTable'
    }

    return render(request, template, context)


def agent_details(request, agent_id=None):
    template = 'main/agent_details.html'
    context = {
        'agent': get_object_or_404(Agent, pk=agent_id),
    }

    return render(request, template, context)    


def manage_agent(request, agent_id=None):
    template = 'main/forms/manage_agent.html'
    context = {
        'form': None,
        'agent': None
    } 

    if agent_id:
        context['agent'] = get_object_or_404(Agent, pk=agent_id)

    # I had to add the first name because I always come to this page via post 
    if request.method == 'POST' and 'first_name' in request.POST:
        context['form'] = ManageAgentForm(
            request.POST,
            instance=context['agent']
        )
        if context['form'].is_valid():
            agent = context['form'].save()
            return redirect(agent)
            
    else:
        context['form'] = ManageAgentForm(instance=context['agent'])

    return render(request, template, context)
