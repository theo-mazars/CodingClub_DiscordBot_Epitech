import discord
import random

TOKEN = 'Votre Token'
prefix = '!'

class MyClient(discord.Client):
    async def on_ready(self):
        activity = discord.Game(name="Coding Club")
        await client.change_presence(status=discord.Status.online, activity=activity)
        print('Logged on as', self.user)

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content == 'ping':
            await message.channel.send('pong')
            return
        
        message_split = message.content.split("di")
        if len(message_split) == 2:
            if (len(message_split[1]) > 0):
                await message.channel.send(message_split[1])
            return

        message_split = message.content.split("cri")
        if len(message_split) == 2:
            if (len(message_split[1]) > 0):
                await message.channel.send("**" + message_split[1].upper() + "**")

        if message.content == '@someone':
            select_user = random.randint(0, len(message.guild.members))
            random_user = message.guild.members[select_user].id
            await message.channel.send("Laisse moi choisir quelqu'un au hasard");
            await message.channel.send("Salut <@" + str(random_user) + ">")
            return

        if message.content[0] == prefix:
            args = message.content.split(' ');

            if args[0] == prefix + "help":
                await message.author.send("Voici les commandes disponibles :")
                await message.channel.send("<@" + str(message.author.id) + ">, je viens de t'envoyer la liste des commandes en mp !")

            if args[0] == prefix + "repeat":
                await message.channel.send(args[1])

    async def on_message_delete(self, message):
        if message.author == self.user:
            return
        await message.channel.send("Alors **" + str(message.author) + "** on n'assume pas de dire `" + str(message.content) + "`")

client = MyClient()
client.run(TOKEN)
