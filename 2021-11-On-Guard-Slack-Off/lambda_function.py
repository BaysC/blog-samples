import boto3
import json
import os
import urllib.request

organizations_client = boto3.client('organizations')
slack_url = os.environ["SLACK_URL"]


def do_post(url: str, body: dict):
    # convert input to a JSON string, and then convert to bytes using UTF-8 encoding
    json_bytes = json.dumps(body).encode('utf-8')

    # create a new HTTP request to the URL, add relevant headers, and send with body
    req = urllib.request.Request(url)
    req.add_header('Content-Type', 'application/json')
    req.add_header('Content-Length', str(len(json_bytes)))
    return urllib.request.urlopen(req, json_bytes)


def lambda_handler2(event, context):
    account_id = event["account"]
    account_desc = organizations_client.describe_account(AccountId=account_id)['Account']
    account_name = account_desc['Name']

    severity = event["detail"]["severity"]
    title = event["detail"]["title"]

    do_post(slack_url, {
        "blocks": [
            {
                "type": "header",
                "text": {
                    "type": "plain_text",
                    "text": "GuardDuty Finding"
                }
            },
            {
                "type": "section",
                "fields": [
                    {
                        "type": "mrkdwn",
                        "text": f"*Account:* {account_name}"
                    },
                    {
                        "type": "mrkdwn",
                        "text": f"*Severity:* {severity}"
                    }
                ]
            },
            {
                "type": "section",
                "text": {
                    "type": "plain_text",
                    "text": title
                }
            }
        ]
    })
