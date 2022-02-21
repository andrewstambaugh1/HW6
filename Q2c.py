import requests
import os
import json
import sys

# To set your environment variables in your terminal run the following line:
# export 'BEARER_TOKEN'='<your_bearer_token>'
bearer_token = 'AAAAAAAAAAAAAAAAAAAAAN7WZQEAAAAAbjoqdaNlUTpOhCmNOb%2B9uy%2F5BeU%3D8WkUX2VfwQlihRUWu9quV9HtUTjNQX8eq2q1gapujCrzVuOXvZ'
username=sys.argv[1]

def connect_to_endpoint_for_userID(url):
    response = requests.request("GET", url, auth=bearer_oauth,)
    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                response.status_code, response.text
            )
        )
    return response.json()

def userID():
    url = "https://api.twitter.com/2/users/by?{}&{}".format(f"usernames={username}", "user.fields=id")
    json_response = connect_to_endpoint_for_userID(url)
    return(json_response['data'][0]['id'])

def create_url():
    # Replace with user ID below
    user_id = userID()
    return "https://api.twitter.com/2/users/{}/tweets".format(user_id)


def get_params():
    # Tweet fields are adjustable.
    # Options include:
    # attachments, author_id, context_annotations,
    # conversation_id, created_at, entities, geo, id,
    # in_reply_to_user_id, lang, non_public_metrics, organic_metrics,
    # possibly_sensitive, promoted_metrics, public_metrics, referenced_tweets,
    # source, text, and withheld
    return {"tweet.fields": "created_at"}


def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2UserTweetsPython"
    return r


def connect_to_endpoint(url, params):
    response = requests.request("GET", url, auth=bearer_oauth, params=params)
    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                response.status_code, response.text
            )
        )
    return response.json()


def main():
    url = create_url()
    params = get_params()
    json_response = connect_to_endpoint(url, params)
    return(json_response['data'][0])
output=main()
date=output['created_at'].split('T')[0]
time=output['created_at'].split('T')[1].split('Z')[0].split('.')[0]
tweet=output['text'].replace('\n',' ')
print(f'{date} {time} @{username}: {tweet}')
