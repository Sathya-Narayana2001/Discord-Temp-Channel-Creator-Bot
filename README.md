# Discord-Temp-Channel-Creator-Bot
This bot can be used to create and delete temporary voice and text channels in discord community server.<br>
## Note
* This is only a source code for bot !
* Before doing this you need to create a bot at [Discord Developer Portal](https://discord.com/login?redirect_to=%2Fdevelopers%2Fapplications) and add the bot to the server. There are many videos and guides as well.

## Required Permissions
To make this bot working you must meet the required permissions. This will be asked at the time of bot creation.
#### General Permissions
* `Manage Channels` - To create and delete channels.
* `Create Invite` - To create instant invites for the channel.
#### Text Permissions
* `Read Messages` - To read the message that are being sent.
* `Send Messages` - To send the message in the channel.
* `Mention @everyone, @here, and All Roles` - To mention the users.
* `Manage Messages` - To delete the unwanted messages.
#### Voice permissions
* `View Channel` - To view the existing voice channels.
* `Move Members` - To move the members automatically to the created voice channels

## Pre-Usage Guide
Download the zip file of the project or clone this project.
#### Downloading Zip file
Go to the downloads folder and enter the following commands.
```
unzip Discord-Temp-Channel-Creator-Bot.zip
cd Discord-Temp-Channel-Creator-Bot
```
#### Cloning the Project
```
git clone https://github.com/Sathya-Narayana2001/Discord-Temp-Channel-Creator-Bot.git
cd Discord-Temp-Channel-Creator-Bot
```
_**Compulsory**_ :
#### 1.Replacing Your Token
Replace your token at ` Line No.80 ` within the quotes. You will be getting this in the developer portal page of your bot.
#### 2.Create a New Category named `GUEST CHANNELS` and a separate text channel for bot commands
#### 3.Making this bot to recognize message from only certain text channels
This is Very important step or else you bot will mess up the other messages.<br>
1.Goto the server <br>.
2.Right click the text channel and select ` Edit channel `.<br>
3.Select ` Permissions ` and under ` Advanced permissions ` add the bot in ` Roles/Members `. <br>
4.Goto the bot's permission and under ` General Channel permissions `
  * Deny the ` View Channel ` permission if the bot should not see the message from that particular channel.
  * Accept the `View Channel `permission if the bot should see the message from that particular channel.<br>

_**Not compulsory**_ :
#### Configuring the Category
Replace your category at ` Line No.46 ` within the quotes at ` name ` attribute. Default category is ` GUEST CHANNELS `. If you change please create a new catgeory in the discord server in the exact catgeory name typed here.<br>
## Making the bot to come online
1.Goto the folder.<br>
2.Fire up the bot by `python bot.py ` or `python3 bot.py` (Temprory this will only work till your system is on).<br>
3.To make the bot permanently online host it in any server or see tutorials.<br>
## Usage Guide
* ` $create ` to create a new text and voice channels under the catgeory ` GUEST CHANNELS `. You can also limit the voice channel members by adding the number, Example `$create 10` for 10 members. Default maximum members is 4.
* ` $delete ` to delete the channels that have been created by you.
## Features
* This bot will automatically delete the user messages and unrecognized messages automatically.
* If you join the voice channel and give the command it will automatically move to the newly created voice channel.
* If you are not in the voice channel it will send you invite in the particular text channel for easy joining.
## Additional info
Feel free to raise issue if you find any problems. I am very new to coding and open to learn from others. Please correct me if I'm wrong or help me to use the variables or functions efficently without any hesitation. Happy to learn always :)
