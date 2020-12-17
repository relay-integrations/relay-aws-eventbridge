# simple webhook responder that just puts the entire
# content of the webhook into a parameter for use by a 
# workflow.

from relay_sdk import Interface, WebhookServer
from quart import Quart, request, jsonify, make_response
import json
import logging

relay = Interface()
app = Quart('my-app')

logging.getLogger().setLevel(logging.INFO)

@app.route('/', methods=['POST'])
async def handler():
    payload = await request.get_json()
    logging.info("Received the following webhook payload: \n%s", json.dumps(payload, indent=4))

    if payload is None:
        return {'message': 'not a valid webhook'}, 400, {}

    relay.events.emit({
        'webhook_contents': json.dumps(payload)
    })

    return {'message': 'success'}, 200, {}

if __name__ == '__main__':
    WebhookServer(app).serve_forever()
