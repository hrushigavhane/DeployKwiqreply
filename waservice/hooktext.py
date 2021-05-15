import hashlib
import hmac
import httplib
import json

from django.conf import settings
from django.http import HttpResponse, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt


def handle_webhook(event, payload):
    """Simple webhook handler that prints the event and payload to the console"""
    print('Received the {} event'.format(event))
    print(json.dumps(payload, indent=4))


@csrf_exempt
def handle_github_hook(request):
    # Check the X-Hub-Signature header to make sure this is a valid request.
    github_signature = request.META['HTTP_X_HUB_SIGNATURE']
    signature = hmac.new(settings.GITHUB_WEBHOOK_SECRET, request.body, hashlib.sha1)
    expected_signature = 'sha1=' + signature.hexdigest()
    if not hmac.compare_digest(github_signature, expected_signature):
        return HttpResponseForbidden('Invalid signature header')

    # Sometimes the payload comes in as the request body, sometimes it comes in
    # as a POST parameter. This will handle either case.
    if 'payload' in request.POST:
        payload = json.loads(request.POST['payload'])
    else:
        payload = json.loads(request.body)

    event = request.META['HTTP_X_GITHUB_EVENT']

    # This is where you'll do something with the webhook
    handle_webhook(event, payload)

    return HttpResponse('Webhook received', status=httplib.ACCEPTED)