import copy, json, datetime
from django.utils import timezone
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from .models import WebhookTransaction


@csrf_exempt
# @require_POST #TODO: commented until understand why it doesn't work
def webhook(request):
    jsondata = request.body
    # jsondata = '{"key2": "value2", "key1": "value1", "timestamp": "10000"}'
    data = json.loads(jsondata)
    meta = copy.copy(request.META)
    for k, v in meta.items():
        if not isinstance(v, basestring):
            del meta[k]

    WebhookTransaction.objects.create(
        date_event_generated=datetime.datetime.fromtimestamp(
            float(data['timestamp']) / 1000.0,
            tz=timezone.get_current_timezone()
        ),
        body=data,
        request_meta=meta
    )

    return HttpResponse(status=200)