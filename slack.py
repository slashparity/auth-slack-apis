import requests

# Prompt the user to enter their Slack API token
SLACK_TOKEN = input("Enter your Slack API token: ")

# List of Slack API endpoints to test
ENDPOINTS = [
    "auth.test",
    "rtm.start",
    "users.list",
    "channels.list",
    "conversations.list",
    "chat.postMessage",
    "reactions.add",
    "files.upload",
    "views.open",
    "emoji.list",
    "users.info",
    "conversations.history",
    "im.list",
    "groups.list",
    "mpim.list",
    "team.info",
    "users.lookupByEmail",
    "pins.list",
    "reactions.get",
    "reactions.get",
    # Add more endpoints as needed
]

# Loop through endpoints and make requests
for ENDPOINT in ENDPOINTS:
    print(f"Testing authentication for endpoint: {ENDPOINT}")

    # Make the request using the requests library
    response = requests.post(
        f"https://slack.com/api/{ENDPOINT}",
        headers={"Authorization": f"Bearer {SLACK_TOKEN}"},
    )

    # Change the color of the word "false" to red in the response text
    colored_response = response.text.replace('false', '\033[1;31mfalse\033[0m')

    print(f"Response: {colored_response}")
    print("-------------------------------------------")
