from django.shortcuts import render
from portfolio.models import Portfolio

def portfolio_index(request):
    portfolios = Portfolio.objects.all()
    context = {
        'portfolios': portfolios
    }
    return render(request, 'portfolio_index.html', context)

def portfolio_detail(request, id):
    portfolio = Portfolio.objects.get(pk=id)
    context = {
        'portfolio': portfolio
    }
    return render(request, 'portfolio_detail.html', context)
