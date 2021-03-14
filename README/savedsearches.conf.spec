# Discord alert settings

action.discord = [0|1]
* Enable discord notification

action.discord.param.room = <string>
* Name of the room to send the notification to
* (required)

action.discord.param.message = <string>
* The message to send to the discord room. 
* (required)

action.discord.param.message_format = [html|text]
* The format of the room notification (optional)
* Default is "html"
* (optional)

action.discord.param.color = [red|green|blue|yellow|grey]
* Background color of the room notification (optional)
* (optional)

action.discord.param.notify = [1|0]
* Notify users in the room
* Defaults to 0 (not notifying users in the room)
* (optional)

action.discord.param.auth_token = <string>
* Override Discord API auth token from global alert_actions config
* (optional)