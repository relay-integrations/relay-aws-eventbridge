# aws-eventbridge-trigger-eventbridge

This is a basic webhook to accept EventBridge events as a webhook.

### Note
EventBridge does not currently implement a webhook target so events will need to be proxied from EventBridge to Relay by a Lambda function. An example Lamda function is provided in the `lambda/` folder. To produce a `function.zip` to be uploaded, edit `./lambda/lambda_function.py` and enter the webhook URL, then run `build.sh`. If successful, the resulting `function.zip` maybe uploaded to Lambda and used as an EventBridge target to pass the payload to Relay.

## Data Emitted

| Name             | Data type | Description                                |
|------------------|-----------|--------------------------------------------|
| webhook_contents | JSON      | The entire contents of the webhook payload |

## Usage

For a complete usage guide, see the [Using triggers in workflows](https://relay.sh/docs/using-workflows/using-triggers/) documentation.

```yaml
parameters:
  data:
    description: In ur data eatin ur cookies

triggers:
- name: generic-webhook
  source:
    type: webhook
    image: relaysh/aws-eventbridge-trigger-eventbridge
  binding:
    parameters:
      data: !Data webhook_contents

steps:
- name: we-get-signal
  image: relaysh/core
  spec:
    data: !Parameter data
  input:
    - "ni get -p {.data} > /data.txt"
    - "cat /data.txt"
```
