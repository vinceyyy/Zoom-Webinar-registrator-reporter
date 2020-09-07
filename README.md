# Zoom-Webinar-registrator-reporter

A automation tool used for sending certain Zoom webinar registration stats to certain Slack channel. Useful for reporting webinar registration stats to your marketing team channel every weekday morning.

## Before using

Requires a JSON file named "config.json" to store Zoom key (to specify which Zoom to get info from), Slack API (specify which Slack channel to send to), and the webinar list.

JSON file structure:

```
{
        "zoom_key": ########, 
        
        "slack_api": ########,

        "webinar list" : {
                webinar id: extra webinar info
        }
}
```

## How to use
1. Go to https://marketplace.zoom.us and sign in.
2. Build an App, choose JWT as App type.
3. Get JWT Token and put it into zoom_key in JSON file.
4. Go to https://api.slack.com/apps and sign in.
5. Create an App and install into desired Slack Workspace and Channel.
6. Get the Slack API (starts with https://hooks.slack.com/services) and put it into slack_api in in JSON file.
7. Put the desired webinar id and the extra words (such as the description of the webinar) you want to send along with the stats into webinar list.
8. Run it or schedule it runs everyday.