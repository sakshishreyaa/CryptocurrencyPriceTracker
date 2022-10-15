from datetime import datetime
from django.http import JsonResponse

from .models import CryptoTracker


def get(request, *args, **kwargs):
    data=request.GET
    date=data.get('date')
    limit=int(data.get('limit',100))
    offset=int(data.get('offset',0))
    date =datetime.strptime(date,"%d-%m-%Y")
    resp = CryptoTracker.objects.filter().all()[offset:offset+limit]

    data=[]
    for i in resp:
        data.append({'name':i.name,'price':i.price,'date':i.created_at})
    return JsonResponse(data,safe=False)