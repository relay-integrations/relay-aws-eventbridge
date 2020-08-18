import json
import requests

webhook_url = 'https://<relay-webhook-here>.webhook-proxy.stage.relay-infra.net'

def lambda_handler(event, context):
    print(event)
    response = requests.post(
        webhook_url, data=json.dumps(event),
        headers={'Content-Type': 'application/json'}
    )
    if response.status_code != 200:
        return {
            'statusCode': response.status_code,
            'body': json.dumps(
                'Request to webhook returned an error %s, the response is:\n%s'
                % (response.status_code, response.text)
            ),
        }

    return {
        'statusCode': 200,
        'body': response.json(),
    }
