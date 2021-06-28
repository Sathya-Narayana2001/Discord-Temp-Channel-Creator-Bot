import discord

created = []
details = {}


# Returns User Name
def name_edited(message):
    name = str(message.author)
    alpha = ""
    for character in name:
        if character.isalpha():
            alpha += character
    return alpha


class MyClient(discord.Client):
    # Prints User
    async def on_ready(self):
        print('Logged on as', self.user)

    # Avoids Replying to self
    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return
        # Creates a Channel
        command = message.content
        if not "$create" in command and not "$delete" == command:
            await message.delete()
        if message.content.startswith('$create'):
            name = name_edited(message)
            mention = ("<@{}>".format(message.author.id))
            if name in created:
                await message.delete()
                await message.channel.send("{} your channel already exists!!".format(mention))
                return
            else:
                content = message.content.split()
                try:
                    content[1]
                    userlimit = content[1]
                except:
                    userlimit = 4
                created.append(name)
                user_category = discord.utils.get(message.guild.categories, name="GUEST CHANNELS")#Change the name if you want to change the category name
                tchannel = await message.guild.create_text_channel(name=str(name) + " text channel",category=user_category)
                vchannel = await message.guild.create_voice_channel(name=str(name) + "'s Voice channel",category=user_category, user_limit=userlimit)
                invite = await discord.VoiceChannel.create_invite(self.get_channel(vchannel.id))
                await message.channel.send("{} Separate Channels have been created on category named {} enjoy your game !!".format(mention, user_category))
                try:
                    await message.author.move_to(self.get_channel(vchannel.id))
                    details[name] = [message.author.id, tchannel.id, vchannel.id]
                except:
                    sent = await message.channel.send("{}".format(invite))
                    details[name] = [message.author.id, tchannel.id, vchannel.id, sent]
                await message.delete()
        # Delete The Channel
        if message.content.startswith("$delete"):
            name = name_edited(message)
            mention = ("<@{}>".format(message.author.id))
            if name in created:
                created.remove(name)
                await discord.guild.TextChannel.delete(self.get_channel(details[name][1]))
                await discord.guild.TextChannel.delete(self.get_channel(details[name][2]))
                await message.channel.send("{} your channel has been deleted !!".format(mention))
                try:
                    sent = details[name][3]
                    await sent.delete()
                    await message.delete()
                except:
                    await message.delete()
            else:
                await message.channel.send("{} No channel exists to delete".format(mention))
                await message.delete()


client = MyClient()
# bot Token Here
client.run('Edit your Token Here')
