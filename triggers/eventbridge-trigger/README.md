# aws-eventbridge-trigger-eventbridge

This is a basic webhook to accept eventbridge events as a webhook. Eventbridge does not currently implement a webhook target so events will need to be passed from a lambda function.

## Data Emitted

| Name             | Data type | Description                                |
|------------------|-----------|--------------------------------------------|
| webhook_contents | JSON      | The entire contents of the webhook payload |

## Usage

For a complete usage guide, see the [Using triggers in workflows](https://relay.sh/docs/using-workflows/using-triggers/) documentation.

```yaml
triggers:
- name: default-trigger
  image: relaysh/foobar-trigger-template
  binding:
    parameters:
      webhook: !Data webhook_contents
```
