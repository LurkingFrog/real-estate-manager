from django.shortcuts import render_to_response
from django.template import RequestContext


def landing_page(request):
    """
    A landing page where a welcome message, recent additions
    and the like can be displayed
    """
    template = 'main/landing.html'
    context = dict()

    return render_to_response(
        template,
        context,
        context_instance=RequestContext(request)
    )
