import discord 
from discord.ext import commands
import random
import colorama
from colorama import Fore
import os
import token
os.system(f'cls & mode 150,13 & title Fake Image Logger Bot - Version 1.0')

bot= discord.Client()
bot = commands.Bot(command_prefix="!" ,help_command=None)
bot.remove_command('help')

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.idle, activity=discord.Game(' Joses Fake Image Logger Builder'))
    print(Fore.CYAN + Fore.BLUE +  """
 
  ▄▀▀█▀▄    ▄▀▀▄ ▄▀▄  ▄▀▀█▄   ▄▀▀▀▀▄   ▄▀▀█▄▄▄▄      ▄▀▀▀▀▄    ▄▀▀▀▀▄   ▄▀▀▀▀▄    ▄▀▀▀▀▄   ▄▀▀█▄▄▄▄  ▄▀▀▄▀▀▀▄      ▄▀▀█▄▄   ▄▀▀▀▀▄   ▄▀▀▀█▀▀▄ 
█   █  █  █  █ ▀  █ ▐ ▄▀ ▀▄ █        ▐  ▄▀   ▐     █    █    █      █ █         █        ▐  ▄▀   ▐ █   █   █     ▐ ▄▀   █ █      █ █    █  ▐ 
▐   █  ▐  ▐  █    █   █▄▄▄█ █    ▀▄▄   █▄▄▄▄▄      ▐    █    █      █ █    ▀▄▄  █    ▀▄▄   █▄▄▄▄▄  ▐  █▀▀█▀        █▄▄▄▀  █      █ ▐   █     
    █       █    █   ▄▀   █ █     █ █  █    ▌          █     ▀▄    ▄▀ █     █ █ █     █ █  █    ▌   ▄▀    █        █   █  ▀▄    ▄▀    █      
 ▄▀▀▀▀▀▄  ▄▀   ▄▀   █   ▄▀  ▐▀▄▄▄▄▀ ▐ ▄▀▄▄▄▄         ▄▀▄▄▄▄▄▄▀ ▀▀▀▀   ▐▀▄▄▄▄▀ ▐ ▐▀▄▄▄▄▀ ▐ ▄▀▄▄▄▄   █     █        ▄▀▄▄▄▀    ▀▀▀▀    ▄▀       
█       █ █    █    ▐   ▐   ▐         █    ▐         █                ▐         ▐         █    ▐   ▐     ▐       █    ▐            █         
▐       ▐ ▐    ▐                      ▐              ▐                                    ▐                      ▐                 ▐         
 """)
    print( Fore.CYAN + 'We Have Awaked {0.user}'.format(bot))



@bot.command(name="Ping")
async def Ping(ctx: commands.Context):
    await ctx.send(f"The Bots Ping: {round(bot.latency * 1000)}ms")




@bot.command(name='Help')
async def Help(ctx):
  embed = discord.Embed(
    title = 'Help Commands:',
    description = 'This Will Tell You All The Features The Bot Has And How To Use The Bot Features',
    color = discord.Color.blue()

  )
  embed.set_footer(text=f'Requested By - {ctx.author}',icon_url=ctx.author.avatar_url)
  embed.add_field(name='Credits',value='Made By Joseyt#0001')
  embed.add_field(name='Moderation',value='Ban,Kick,UnBan',inline=False)
  embed.add_field(name='How To Use Moderation Commands',value='!Ban [Username] !Kick [Username] !Unban [User]',inline=False)
  embed.add_field(name='Utilities',value='Purge Chat, Ping',inline=False)
  embed.add_field(name='How To Use Utilities Commands',value='!Purge [Amount Of Messages], !Ping',inline=False)
  embed.add_field(name='How To Build Your Image Logger',value='!Build @[your username] Webhook:[your webhook] Image:[your image_url]',inline=False)
  await ctx.send(embed=embed)




@bot.command()
@commands.has_any_role('Mod', 'Founder', 'Support', 'Helper', 'Owner','Staff','Admin', 'Moderator', 'MOD', 'FOUNDER', 'SUPPORT', 'HELPER', 'OWNER','STAFF','ADMIN', 'MODERATOR')
async def Purge(ctx, amount=300):
    await ctx.channel.purge(limit=amount+1)
    




@bot.command()
@commands.has_any_role('Mod', 'Founder', 'Support', 'Helper', 'Owner','Staff','Admin', 'Moderator', 'MOD', 'FOUNDER', 'SUPPORT', 'HELPER', 'OWNER','STAFF','ADMIN', 'MODERATOR')
async def Kick(ctx, user: discord.Member, *, reason=None):
    await user.kick(reason=reason)
    await ctx.send(f'{user} Has Been Kicked From The Server!')





@bot.command()
@commands.has_any_role('Mod', 'Founder', 'Support', 'Helper', 'Owner','Staff','Admin', 'Moderator', 'MOD', 'FOUNDER', 'SUPPORT', 'HELPER', 'OWNER','STAFF','ADMIN', 'MODERATOR')
async def Ban(ctx, user: discord.Member, *, reason=None):
    await user.ban(reason=reason)
    await ctx.send(f'{user} Has Been Banned From The Server!')






@bot.command()
@commands.has_any_role('Mod', 'Founder', 'Support', 'Helper', 'Owner','Staff','Admin', 'Moderator', 'MOD', 'FOUNDER', 'SUPPORT', 'HELPER', 'OWNER','STAFF','ADMIN', 'MODERATOR')
async def Unban(ctx, *, member):
    bannedUsers = await ctx.guild.bans()
    name, discriminator = member.split("#")

    for ban in bannedUsers:
        user = ban.user

        if(user.name, user.discriminator) == (name, discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f"{user.mention} was unbanned.")
            return




@bot.command()
@commands.has_any_role('Mod', 'Buyer', 'Customer', 'CUSTOMER', 'BUYER' 'Founder', 'Support', 'Helper', 'Owner','Staff','Admin', 'Moderator', 'MOD', 'FOUNDER', 'SUPPORT', 'HELPER', 'OWNER','STAFF','ADMIN', 'MODERATOR')
async def Build(ctx, user: discord.User, *, message=None):
    message = message or "Test"
    await user.send(message)
    await ctx.send(f'{user} Your Image Logger Was Built Sucessfully Checks Your Discord Dms')
    





bot.run('Your Token')
