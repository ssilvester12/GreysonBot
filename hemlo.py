# Made By Hunter
# Scammer Devil

from telethon import events, Button, custom
import re, os, random, asyncio
 
from telethon imporTelegramClient

# Start Text 
LSTART = f'''Hello, nice to meet you!

I'm Seona, an advanced group management bot built to help you manage your group easily.

I can do a lot of cool stuffs, here's a short list:
• I can restrict users.
• I can greet users with customizable welcome messages and even set a group's rules.
• I have an advanced anti-flood system.
• I can warn users until they reach max warns, with each predefined actions such as ban, mute, kick, etc.
• I have a note keeping system, blacklists, and even predetermined replies on certain keywords.
• I check for admins' permissions before executing any command.
…and much more stuffs, check out /help!

All of the possible commands can be used properly if I am an administrator in your group otherwise, I will not able to restrict users, send certain predefined actions etc.

Join my news channel to get information on all the latest updates.'''

@bot.on(events.callbackquery.CallbackQuery(data=re.compile(b"suru"))) 
async def _(event):
     await event.edit(LSTART, buttons=start) 

ohk = [[custom.Button.inline("Back", data="suru")]]

start = [[custom.Button.inline("Configuration Tutorial", data="contut"), custom.Button.inline("Commands", data="command")]]
start += [[custom.Button.url("Add me to your group", "t.me/Seona_RoBot?=start")]]



@bot.on(events.NewMessage(pattern="^/start$"))
async def _(event):
      START = f'''Hello {event.sender.first_name}, nice to meet you!

I'm Seona, an advanced group management bot built to help you manage your group easily.

I can do a lot of cool stuffs, here's a short list:
• I can restrict users.
• I can greet users with customizable welcome messages and even set a group's rules.
• I have an advanced anti-flood system.
• I can warn users until they reach max warns, with each predefined actions such as ban, mute, kick, etc.
• I have a note keeping system, blacklists, and even predetermined replies on certain keywords.
• I check for admins' permissions before executing any command.
…and much more stuffs, check out /help!

All of the possible commands can be used properly if I am an administrator in your group otherwise, I will not able to restrict users, send certain predefined actions etc.

Join my news channel to get information on all the latest updates.'''
      await bot.send_message(event.chat.id,START, buttons=start)

HLP = '''Here is the list of all possible commands:
- /start: Starts me! You've probably already used this.
- /help: Sends this message; I'll tell you more about myself!

If you have any bugs or questions on how to use me head to @DevsChatRoom.
 All commands can be used with the following: / ? !'''


@bot.on(events.callbackquery.CallbackQuery(data=re.compile(b"command"))) 
async def _(event):
     await event.edit(HLP, buttons=kk) 
  
@bot.on(events.NewMessage(pattern="/help"))
async def _(event):
   if not event.is_group:
    await bot.send_message(event.chat.id,HLP, buttons=kk)
   else:
    await event.reply("**Click me for help!**", buttons=[[Button.url("Click me for help","t.me/Seona_Robot?start=help")]])
    
@bot.on(events.NewMessage(pattern="^/start help"))
async def _(event):
     await event.reply(HLP, buttons=kk)

@bot.on(events.callbackquery.CallbackQuery(data="help"))
async def _(event):
     await event.reply(HLP, button=kk)

@bot.on(events.callbackquery.CallbackQuery(data=re.compile(b"contut"))) 
async def _(event):
    await event.edit('''**Welcome to the Seona configuration tutorial.**

The first thing to do is to add Seona to your group! For doing that, press the under button and select your group, then press "Done" to continue the tutorial..''', buttons=kk) 

done = [[custom.Button.inline("✅ Done", data="done")]]

@bot.on(events.callbackquery.CallbackQuery(data=re.compile(b"done"))) 
async def _(event):
    await event.edit('''Ok, well done!

Now for let me work correctly, you need to make me Admin of your Group!

To do that, follow this easy steps:
▫️ Go to your group
▫️ Press the Group's name
▫️ Press Modify
▫️ Press on Administrator
▫️ Press Add Administrator
▫️ Press the Magnifying Glass
▫️ Search @Seona_Robot
▫️ Confirm''', buttons=kk) 

@bot.on(events.callbackquery.CallbackQuery(data=re.compile(b"sed")))
async def _(event):
    await event.edit('''
Excellent!
Now the Bot is ready to use!

All commands can be used with /

Note: I recognise only the admins cached in my /admincache so as to avoid sending too many requests to the Telegram's servers. The admin cache will be updated every 10 minutes or upon executing /admincache command.''', buttons=kk) 

contut = [[custom.Button.inline("✅ Done", data="sed")]]
sed = [[custom.Button.inline("Main Menu", data="suru")]]

fuk = [[custom.Button.inline("Back", data="command")]]

kk = [[custom.Button.inline("AFK", data="afk"),custom.Button.inline("Admin",data="gheiadmin"),custom.Button.inline("Anti-Flood",data="flood")]]
kk += [[custom.Button.inline("Approval", data="approve"), custom.Button.inline("Backups", data="backup"), custom.Button.inline("Bans", data="bans")]]
kk += [[custom.Button.inline("Bios and Abouts", data="bios"), custom.Button.inline("Blacklists", data="black"), custom.Button.inline("Connections", data="connect")]]
kk += [[custom.Button.inline("Disabling", data="disable"), custom.Button.inline("Federations", data="feds"), custom.Button.inline("Filters", data="filters")]]
kk += [[custom.Button.inline("Greetings", data="welcome"), custom.Button.inline("Locks", data="locks"), custom.Button.inline("Logger", data="logger")]]
kk += [[custom.Button.inline("MarkDown", data="markdown"), custom.Button.inline("Misc", data="misc"), custom.Button.inline("Notes", data="notes")]]
kk += [[custom.Button.inline("Pin", data="pin"), custom.Button.inline("Purges", data="purges"), custom.Button.inline("Reporting", data="report")]]
kk += [[custom.Button.inline("Back", data="suru")]]




@bot.on(events.callbackquery.CallbackQuery(data=re.compile(b"bios"))) 
async def _(event):
    await event.edit('''Help others know yourself or what others think of yourself in a new way.

That's why here we have a way to describe yourself to the world around.

 • /setbio <text>: Set user's bio
 • /bio: Get user's bio
 • /resetbio: Reset your bio to default 
 • /setme <text>: Set your about
 • /resetabout: Reset your about to default 
 • /me: Get user's about''', buttons=kk) 

@bot.on(events.callbackquery.CallbackQuery(data=re.compile(b"black"))) 
async def _(event):
    await event.edit('''Blacklists are used to stop certain triggers from being said in a group. Any time the trigger is mentioned, the message will immediately be deleted. A good combo is sometimes to pair this up with warn filters!

NOTE: Blacklists do not affect group admins.

 • /blacklist: View the current blacklisted words.

Admin only:
 • /addblacklist <triggers>: Add a trigger to the blacklist. Each line is considered one trigger, so using different lines will allow you to add multiple triggers.
 • /unblacklist <triggers>: Remove triggers from the blacklist. Same newline logic applies here, so you can remove multiple triggers at once.
 • /rmblacklist <triggers>: Same as above.
 • /blacklistmode <off/del/warn/ban/kick/mute/tban/tmute>: Action to perform when someone sends blacklisted words.
 • /unblacklistall: Remove all blacklist triggers - chat creator only.''', buttons=kk) 

@bot.on(events.callbackquery.CallbackQuery(data=re.compile(b"connect"))) 
async def _(event):
    await event.edit('''Sometimes, you just want to add some notes and filters to a group chat, but you don't want everyone to see; This is where connections come in...

This allows you to connect to a chat's database, and add things to it without the commands appearing in chat! For obvious reasons, you need to be an admin to add things; but any member in the group can view your data.

 • /connect <chatid/username>: Connect to the specified chat, allowing you to view/edit contents.
 • /connection: List connected chats
 • /disconnect: Disconnect from the current chat
 • /helpconnect: List available commands that can be used remotely

Admin only:
 • /allowconnect <yes/no/on/off>: Allow a user to connect to a chat
 
 You can retrieve the chat id by using the /id command in your chat. Don't be surprised if the id is negative; all super groups have negative ids.''', buttons=kk) 

@bot.on(events.callbackquery.CallbackQuery(data=re.compile(b"bans"))) 
async def _(event):
    await event.edit('''Some people need to be publicly banned; spammers, annoyances, or just trolls.

This module allows you to do that easily, by exposing some common actions, so everyone will see!

User commands:
 • /kickme: kick out yourself.

Admins commands:
 • /ban: Ban a user.
 • /dban: Ban a user by reply, and delete their message. 
 • /sban: Silently ban a user, and delete your message.
 • /tban: Temporarily ban a user.
 • /unban: Unban a user.
 • /mute: Mute a user.
 • /dmute: Mute a user by reply, and delete their message. 
 • /smute: Silently mute a user, and delete your message.
 • /tmute: Temporarily mute a user.
 • /unmute: Unmute a user.
 • /kick: Kick a user.
 • /dkick: Kick a user by reply, and delete their message.  
 • /skick: Silently kick a user, and delete your message
 • /restrict: Restricts a user from sending media, gif, polls, etc.
 • /trestrict: Temporarily restricts a user.
 • /unrestrict: Unrestricts the user back to its default permissions.

 Example:
- Ban a user for two hours.
-> /tban @username 2h''', buttons=kk) 



@bot.on(events.callbackquery.CallbackQuery(data=re.compile(b"approve"))) 
async def _(event):
    await event.edit('''Sometimes, you might trust a user not to send unwanted content.
Maybe not enough to make them admin, but you might be ok with locks, blacklists, and antiflood not applying to them.

That's what approvals are for - approve of trustworthy users to allow them to send 

Admin commands:
 • /approval: Check a user's approval status in this chat.
 • /approve: Approve of a user. Locks, blacklists, and antiflood won't apply to them anymore.
 • /unapprove: Unapprove of a user. They will now be subject to locks, blacklists, and antiflood again.
 • /approved: List all approved users.
 • /unapproveall: Unapprove ALL users in a chat. This cannot be undone.''', buttons=kk) 

@bot.on(events.callbackquery.CallbackQuery(data=re.compile(b"backup"))) 
async def _(event):
    await event.edit('''Some people just want to see the world burn. Others, just want to have a way of grouping their chat data in one place so they can export their configuration to other chats!

Emilia import/export settings feature allows you to quickly set up a chat using a preexisting template. Instead of setting the same settings over and over again in different chats, you can use this feature to copy the general configuration across groups.
The generated file is in standard JSON format, so if there are any settings you dont want to import to your other chats, just open the file and edit it before importing.
Exporting settings can be done by any administrator, but for security reasons, importing can only be done by the group creator.

The following modules will have their data exported:
- admin
- antiflood
- blacklists
- disabled
- filters
- greetings
- locks
- notes
- pins
- reports
- rules
- warns

Chat owner commands:
- /export: Generate a file containing all your chat data.
- /import: Import the settings in the replied to data file.

Examples:
- To export chat data:
-> /export
- Or, to import a config file from emilia/rose, use:
-> /import <as a reply>

Note: To avoid abuse, this command is heavily rate limited; this is to make sure that people importing/exporting data don't slow down the bot.''', buttons=kk) 

@bot.on(events.callbackquery.CallbackQuery(data=re.compile(b"flood"))) 
async def _(event):
    await event.edit('''You know how sometimes, people join, send 100 messages, and ruin your chat? With antiflood, that happens no more!

Antiflood allows you to take action on users that send more than x messages in a row. Actions are: ban/kick/mute/tban/tmute

User commands:
 • /flood: Get the current flood control setting

Admin commands:
 • /setflood <number/off/no>:  Set the number of messages after which to take action on a user. Set to '0', 'off', or 'no' to disable.
 • /setfloodmode <action type>: Choose which action to take on a user who has been flooding. Options: ban/kick/mute/tban/tmute

Note:
- Value must be filled for tban and tmute!
-> It can be: 5m = 5 minutes, 6h = 6 hours, 3d = 3 days, 1w = 1 week

Examples:
- To set flood number:
-> /setflood 10
- Mute the user who tries to flood for 2 hours:
-> /setfloodmode tmute 2h''', buttons=kk) 

@bot.on(events.callbackquery.CallbackQuery(data=re.compile(b"admin"))) 
async def _(event):
    await event.edit('''Make it easy to promote and demote users with the admin module!

User commands:
 • /adminlist: List of admins in the chat.

Admins commands:
 • /promote <reply/username/mention/userid>: Promotes a user 
 • /demote <reply/username/mention/userid>: Demote a user
 • /admincache: Force update admin status in your group 
 • /send: Echo some message in the exact same state in a group  
 • /invitelink: gets invitelink of chat
 • /setgpic: As a reply to file or photo to set group profile pic
 • /delgpic: Same as above but to remove group profile pic
 • /setgsticker: As a reply to some sticker to set it as group sticker set
 
Sometimes, you promote or demote an admin manually, and Emilia doesn't realise it immediately. This is because to avoid spamming telegram servers, admin status is cached locally.
This means that you sometimes have to wait a few minutes for admin rights to update. If you want to update them immediately, you can use the /admincache command; that'll force Emilia to check who the admins are again.''', buttons=kk) 

@bot.on(events.callbackquery.CallbackQuery(data=re.compile(b"afk"))) 
async def _(event):
    await event.edit('''Help others know you are away from telegram with the help of AFK module!

 • /afk <reason>: mark yourself as AFK(away from keyboard).
 • brb <reason>: same as the afk command - but not a command.
When marked as AFK, any mentions will be replied to with a message to say you're not available!''', buttons=kk) 


@bot.on(events.callbackquery.CallbackQuery(data=re.compile(b"muta")))
async def _(event):
    await event.edit('''** Mutes **
- /mute: mute a user
- /unmute: unmutes a user
- /tmute [entity] : temporarily mutes a user for the time interval.''',buttons=sedlyf)

@bot.on(events.callbackquery.CallbackQuery(data=re.compile(b"gheiadmin")))
async def _(event):
     await event.edit('''Make it easy to admins for manage users and groups with the admin module!
**Available commands:**
** Admin List **
- /adminlist: Shows all admins of the chat.
- /admincache: Update the admin cache, to take into account new admins/admin permissions.''',buttons=cheator)

@bot.on(events.callbackquery.CallbackQuery(data=re.compile(b"promote"))) 
async def _(event):
    await event.edit('''** Promotes & Demotes**
- /promote (user) (?admin's title): Promotes the user to admin.
- /demote (user): Demotes the user from admin.
- /lowpromote: Promote a member with low rights
- /midpromote: Promote a member with mid rights
- /highpromote: Promote a member with max rights
- /lowdemote: Demote an admin to low permissions
- /middemote: Demote an admin to mid permissions''',buttons=sedlyf) 

@bot.on(events.callbackquery.CallbackQuery(data=re.compile(b"ban_kk")))
async def _(event):
    await event.edit('''** Bans & Kicks **
- /ban: bans a user
- /tban [entity] : temporarily bans a user for the time interval.
- /unban: unbans a user
- /unbanall: Unban all banned members
- /banme: Bans you
- /kick: kicks a user
- /kickme: Kicks you''',buttons=warn)

warn = [[custom.Button.inline("Admin Commands", data="ban_kk"), custom.Button.inline("User Commands", data="ucmds")]]
warn += [[custom.Button.inline("Warn Actions", data="actwar"),custom.Button.inline("Warn Limits", data="litwar")]]
warn += [[custom.Button.inline("Back", data="BCK")]]
@bot.on(events.callbackquery.CallbackQuery(data=re.compile(b"muta")))
async def _(event):
    await event.edit('''** Mutes **
- /mute: mute a user
- /unmute: unmutes a user
- /tmute [entity] : temporarily mutes a user for the time interval.''',buttons=warn)

@bot.on(events.callbackquery.CallbackQuery(data=re.compile(b"gheiadmin")))
async def _(event):
     await event.edit('''Make it easy to admins for manage users and groups with the admin module!
**Available commands:**
** Admin List **
- /adminlist: Shows all admins of the chat.
- /admincache: Update the admin cache, to take into account new admins/admin permissions.''',buttons=warn)

@bot.on(events.callbackquery.CallbackQuery(data=re.compile(b"promote"))) 
async def _(event):
    await event.edit('''** Promotes & Demotes**
- /promote (user) (?admin's title): Promotes the user to admin.
- /demote (user): Demotes the user from admin.
- /lowpromote: Promote a member with low rights
- /midpromote: Promote a member with mid rights
- /highpromote: Promote a member with max rights
- /lowdemote: Demote an admin to low permissions
- /middemote: Demote an admin to mid permissions''',buttons=warn) 

@bot.on(events.callbackquery.CallbackQuery(data=re.compile(b"ban_kk")))
async def _(event):
    await event.edit('''** Bans & Kicks **
- /ban: bans a user
- /tban [entity] : temporarily bans a user for the time interval.
- /unban: unbans a user
- /unbanall: Unban all banned members
- /banme: Bans you
- /kick: kicks a user
- /kickme: Kicks you''',buttons=warn)


@bot.on(events.callbackquery.CallbackQuery(data=re.compile(b"muta")))
async def _(event):
    await event.edit('''** Mutes **
- /mute: mute a user
- /unmute: unmutes a user
- /tmute [entity] : temporarily mutes a user for the time interval.''',buttons=warn)

@bot.on(events.callbackquery.CallbackQuery(data=re.compile(b"gheiadmin")))
async def _(event):
     await event.edit('''Make it easy to admins for manage users and groups with the admin module!
**Available commands:**
** Admin List **
- /adminlist: Shows all admins of the chat.
- /admincache: Update the admin cache, to take into account new admins/admin permissions.''',buttons=warn)

@bot.on(events.callbackquery.CallbackQuery(data=re.compile(b"promote"))) 
async def _(event):
    await event.edit('''** Promotes & Demotes**
- /promote (user) (?admin's title): Promotes the user to admin.
- /demote (user): Demotes the user from admin.
- /lowpromote: Promote a member with low rights
- /midpromote: Promote a member with mid rights
- /highpromote: Promote a member with max rights
- /lowdemote: Demote an admin to low permissions
- /middemote: Demote an admin to mid permissions''',buttons=warn) 

@bot.on(events.callbackquery.CallbackQuery(data=re.compile(b"ban_kk")))
async def _(event):
    await event.edit('''** Bans & Kicks **
- /ban: bans a user
- /tban [entity] : temporarily bans a user for the time interval.
- /unban: unbans a user
- /unbanall: Unban all banned members
- /banme: Bans you
- /kick: kicks a user
- /kickme: Kicks you''',buttons=warn)

warn = [[custom.Button.inline("Admin Commands", data="wac"), custom.Button.inline("User Commands", data="ucmds")]]
warn += [[custom.Button.inline("Warn Actions", data="actwar"),custom.Button.inline("Warn Limits", data="litwar")]]
warn += [[custom.Button.inline("Back", data="BCK")]]




















warn = [[custom.Button.inline("Admin Commands", data="wac"), custom.Button.inline("User Commands", data="ucmds")]]
warn += [[custom.Button.inline("Warn Actions", data="actwar"),custom.Button.inline("Warn Limits", data="litwar")]]
warn += [[custom.Button.inline("Back", data="BCK")]]


   
