"""
A automation tool used for sending certain Zoom webinar registration stats to certain Slack channel.
Requires a file named "config.json" to store Zoom key (to specify which Zoom to get info from), Slack API (specify which Slack channel to send to), and the webinar list.

JSON file structure: 
{"zoom_key": ########, "slack_api": ########, 
"webinar_list" : {
        webinar id: webinar info
        }
}
"""

import requests
import json

# read Zoom key and Slack API dir
config = json.loads(open("registrator_reporter_config.json", mode="r").read())

# get webniar registration stats
def get_webinar(webinar_number):
    url = 'https://api.zoom.us/v2/webinars/' + str(webinar_number) + '/tracking_sources'
    headers = {
        'authorization': "Bearer " + config['zoom_key'],
        'content-type': "application/json"
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    content = data['tracking_sources']
    print(content)
    return content

# format text to "channel: registor #, visitor #"
def formating(webinar_number):
    content = get_webinar(webinar_number)
    message = str()
    for i in content:
        channel = i['source_name']
        visitor = i['visitor_count']
        try:
            reg = i['registrationr_count']
        except:
            reg = 0
        text = ("%s: registor %d, visitor %d" % (channel, reg, visitor))
        if i is content[0]:
            message = message + text
        else: 
            message = message + "\n" + text
    print(message)
    return message

# encode and post to Slack
def post(webinar_number, webinar_info):
    # add webinar info to formated text
    data = str(webinar_info) + ":\n" + formating(webinar_number)
    json = {"text": data}
    text = str(json).encode("utf-8").decode("latin1")
    headers = {'Content-type': 'application/json'}
    r = requests.post(config['slack_api'], data=text, headers=headers)
    print(r)

if __name__ == '__main__':
    for webinar in config['webinar_list']:
        post(webinar, config['webinar_list'][webinar])
