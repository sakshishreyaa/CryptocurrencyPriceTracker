from datetime import datetime
from django.http import JsonResponse
import pytz
from .models import CryptoTracker
from .config import DOMAIN


def get(request, *args, **kwargs):
    data = request.GET
    date = data.get("date")
    limit = int(data.get("limit", 100))
    offset = int(data.get("offset", 0))
    current_url = f"{DOMAIN}/api/prices/btc?date={date}&offset={offset}&limit={limit}"
    next_url = (
        f"{DOMAIN}/api/prices/btc?date={date}&offset={offset+limit}&limit={limit}"
    )

    date = datetime.strptime(date, "%d-%m-%Y").astimezone(pytz.utc)
    resp = CryptoTracker.objects.all()[offset : offset + limit]
    count = CryptoTracker.objects.count()

    data = []
    for i in resp:
        data.append({"name": i.name, "price": int(i.price), "date": i.created_at})
    final_resp = {
        "url": current_url,
        # current url
        "next": next_url,
        # next url in pagination
        "count": count,
        # total no of records for the given query
        "data": data,
        # array of price objects
    }
    return JsonResponse(final_resp, safe=False)
