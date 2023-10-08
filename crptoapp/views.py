from django.shortcuts import render
import requests
# Create your views here.
def Crpto(request):
    apidata = requests.get('https://api.coingecko.com/api/v3/coins/markets?vs_currency=inr&order=market_cap_desc&per_page=100&page=1&sparkline=false').json()
    
    return render(request,'Crptoprice.html',{'apidata':apidata})