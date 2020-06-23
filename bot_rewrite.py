import discord
from discord.ext import commands
from discord.ext.commands import bot
from discord.utils import get
from discord import role
from discord import TextChannel
from discord import VoiceChannel
from discord import channel
import datetime
import asyncio
import os
import json
import requests
import random

bot = commands.Bot(command_prefix='/')
bot.remove_command('help')
global role_price
#role_price[{'id': '714223774584799283', 'price': 1000, 'name': 'Business Woman'}]
role_price={'714223774584799283' : 10000, '713326514376278106' : 2000, '719923309780664362' : 50000 , '720327708143255564': 5000,
           '722218339652337744' : 30000, '722217773954236427': 40000, '722218157603029022' : 150000, '722217974001303665':75000,
           '722218370476539986': 10000}
@bot.command(pass_context=True)
async def гугл(ctx):
    try:
                quest=ctx.message.content
                h=quest.split(" ")
                man= ctx.message.mentions
                man1=str(man[0])
                man2=man1[:-5]
                g='+'.join(h[2:])
                k=' '.join(h[2:])
                await ctx.send('Так как '+ str(h[1])+ ' не умеет гуглить, то мы его научим')
                embed_obj=discord.Embed(description='['+k+'](https://google.gik-team.com/?q='+g+')', colour=0xe67e22)
                await ctx.send(embed=embed_obj)
    except:
        emb= discord.Embed(title=0, description=':x:'+' КОМАНДА ВВЕДЕНА НЕКОРРЕКТНО '+':x:', colour=0xff0000)
        await ctx.send(embed=emb)
#####################################################################
@bot.command(pass_context=True)
async def help(ctx):
    emb= discord.Embed(title='Доступные команды:',description="Возможно получить полную справку о команде , написав знак Q, например: !переводчикQ",colour = 0xe67e22)#0x12FF11)
    emb.set_thumbnail( url= "https://cdn.discordapp.com/attachments/715633213212721192/718150133329428540/image0.jpg")
    emb.add_field(name='Полезные команды'.format(), value='/время - сколько сейчас время\n'+
                  '/дата - какая сегодня дата',
     inline=False)
    emb.add_field(name ='Развлекательные', value="/гугл @Имя что_гуглим\n/переводчик язык язык фраза",
        inline=False)
    emb.add_field(name = 'Серверные', value="/баланс - Ваш баланс\n/ставка Х - поставить ставку в канале казино, вместо Х - сама ставка")
    emb.add_field(name='Для Владельца Жигули', value = "/небухти @Имя\n/незаводись @Имя\n/сплошняк @Имя - не переходи границы")
    await ctx.send(embed=emb)
################################################################
@bot.command(pass_context=True)
async def время(ctx):
    f=str(datetime.datetime.now())
    v=f[:-10]
    b=v[-5:]
    emb= discord.Embed(title='Время по гринвичу:',description=b, colour=0x12eb19)#салатовый
    await ctx.send(embed=emb)
###################################################################
@bot.command(pass_context=True)
async def дата(ctx):
    f=str(datetime.datetime.now())
    v=f[:-15]
    emb= discord.Embed(title='Сегоднящняя дата:',description=v, colour=0xff006c)
    await ctx.send(embed=emb)
####################################################################
##@bot.command(pass_context=True)
##async def play(ctx):
##    #await bot.get_channel(713762909834051594).connect()
##  song_there= os.path.isfile("music.mp3")
##  await ctx.author.voice.channel.connect()
##  await ctx.message.delete()
##  await os.play(song_there)
##  voice = get(bot.voice_clients, guild = ctx.guild)
##  ydl_opts = {
##      'format': 'bestaudio/best'
##      'postprocessors'
##  }
###################################################################
@bot.command(pass_context=True)
async def переводчик(ctx):
    try:
        quest=ctx.message.content
        h=quest.split(" ")
        #g='+'.join(h[1:])
        print(h[0])
        #f='+'.join(h[2:])
        print(h[1])
        #k='+'.join(h[3:])
        print(h[2])
        print(h[3])
        g='+'.join(h[3:])
        print(g)
        k=' '.join(h[3:])
        if h[1]=='rus' or h[1]=='eng' or h[1]=='fra' or h[1]=='deu' or h[1]=='english' or h[1]=='русский' or h[2]=='рус':
          embed_obj=discord.Embed(description=':x:'+' ЯЗЫК ВВЕДЁН\nНЕКОРРЕКТНО '+':x:'+'\nВы можете посмотреть справку по команде: !переводчикQ',colour=0xff0000)
          await ctx.send(embed=embed_obj)
          return
        if h[2]=='rus' or h[2]=='eng' or h[2]=='fra' or h[2]=='deu' or h[2]=='english':
          embed_obj=discord.Embed(description=':x:'+' ЯЗЫК ВВЕДЁН\nНЕКОРРЕКТНО '+':x:'+'\nВы можете посмотреть справку по команде: !переводчикQ',colour=0xff0000)
          await ctx.send(embed=embed_obj)
          return
        embed_obj=discord.Embed(description='[перевод с ' +h[1]+' на '+h[2]+': '+k+'](https://translate.google.com/?hl=ru#view=home&op=translate&sl='+h[1]+'&tl='+h[2]+'&text='+g+')', colour=0x00FFFF)
        await ctx.send(embed=embed_obj)
        
    except:
        embed_obj=discord.Embed(description=':x:'+' КОМАНДА ВВЕДЕНА НЕКОРРЕКТНО '+':x:'+'\nВы можете посмотреть справку по команде: !переводчикQ',colour=0xff0000)
        await ctx.send(embed=embed_obj)
@bot.command(pass_context=True)
async def переводчикQ(ctx):
    emb= discord.Embed(title='Переводчик',description="Чтообы посмотреть описание:\n/Переводчик1\n"+
                       'Чтобы посмотреть написание языков:\n/Переводчик2'
                       ,colour = 0x1BFF00)#0x12FF11)
    await ctx.send(embed=emb)
@bot.command(pass_context=True)
async def переводчик2(ctx):
    emb= discord.Embed(title='Написания языков',colour=0xFFF700,description="en - английский\nfr - французский\nru - русский\nde - немецкий"+
                       "\nes - испанский")
    await ctx.send(embed=emb)
@bot.event
async def on_raw_reaction_add(payload):
    print(payload)
    emoji = payload.emoji
    this_member = payload.member
    this_guild = this_member.guild
    this_channel = payload.channel_id
    if this_channel != 719124796847292457:
        return
    if emoji.name=='🐍':
        this_role = get(this_guild.roles, id=int(719153280655032322))
        await this_member.add_roles(this_role)
    elif emoji.name=='🦅':
        this_role = get(this_guild.roles, id=int(719153448595226654))
        await this_member.add_roles(this_role)
    elif emoji.name=='🍁':
        this_role = get(this_guild.roles, id=int(719153481977430116))
        await this_member.add_roles(this_role)
    elif emoji.name=='📜':
        this_role = get(this_guild.roles, id=int(719153580875055204))
        await this_member.add_roles(this_role)
    elif emoji.name == '🐸':
        this_role = get(this_guild.roles, id=int(719153533047406592))
        await this_member.add_roles(this_role)
    elif emoji.name=='🔮':
        this_role = get(this_guild.roles, id=int(719153691159953409))
        await this_member.add_roles(this_role)
    elif emoji.name=='🍍':
        this_role = get(this_guild.roles, id=int(719153723657682954))
        await this_member.add_roles(this_role)
    elif emoji.name=='🏀':
        this_role = get(this_guild.roles, id=int(719153854163451944))
        await this_member.add_roles(this_role)
    elif emoji.name=='🎨':
        this_role = get(this_guild.roles, id=int(719153795304521729))
        await this_member.add_roles(this_role)
    elif emoji.name=='⌨️':
        this_role = get(this_guild.roles, id=int(719153759900401665))
        await this_member.add_roles(this_role)
    elif emoji.name=='💡':
        this_role = get(this_guild.roles, id=int(719153999315599432))
        await this_member.add_roles(this_role)
    elif emoji.name=='🎓':
        this_role = get(this_guild.roles, id=int(719154042521255957))
        await this_member.add_roles(this_role)
    elif emoji.name=='🎩':
        this_role = get(this_guild.roles, id=int(719154036858814494))
        await this_member.add_roles(this_role)
    elif emoji.name=='🦢':
        this_role = get(this_guild.roles, id=int(719154046140809256))
        await this_member.add_roles(this_role)
    elif emoji.name=='⚔️':
        this_role = get(this_guild.roles, id=int(719154154941186058))
        await this_member.add_roles(this_role)
    elif emoji.name=='🌋':
        this_role = get(this_guild.roles, id=int(719154223714926623))
        await this_member.add_roles(this_role)
    elif emoji.name=='🚀':
        this_role = get(this_guild.roles, id=int(719154322209898556))
        await this_member.add_roles(this_role)
    elif emoji.name=='🧬':
        this_role = get(this_guild.roles, id=int(719154330070155265))
        await this_member.add_roles(this_role)

@bot.command(pass_context=True)
async def roles(ctx):
    emb= discord.Embed(title='Получение Ролей', description='Для Получения/удаления роли нажмите на реакцию к этому сообщению, обозначающую Вашу роль.\n\n'+
                       '🐍  ---  **Python**\n\n 🦅 --- **Swift**\n\n 📜 --- **Вёрстка**\n\n🍁 --- **JavaScript**\n\n'+
                       '🔮 --- **C++**\n\n🍍 --- **C#**\n\n🐸 -- **JAVA**\n\n🏀 --- **3D**\n\n🎨 --- **Веб Дизайн**\n\n'+
                       '⌨️ --- **Game Dev**\n\n💡 --- **WEB**\n\n🎓 --- **Backend**\n\n🎩 --- **Frontend**\n\n🦢️ --- **Хакер**\n\n'+
                       '⚔️ --- **CS:GO**\n\n🌋 --- **Minecraft**\n\n🚀 --- **Инженер**\n\n🧬 --- **Био-Хим**', colour=0x00FF04)
    await ctx.send(embed=emb)
@bot.command()
async def delete(ctx):
    this_member = ctx.message.author
    this_guild = this_member.guild
    h=ctx.message.content.split(" ")
    if ctx.channel.id!=719226842586021889:
        return
    if len(h)==2:
        this_role = get(this_guild.roles, name=h[1])#int(s))
        await this_member.remove_roles(this_role)
    elif len(h)==3:
        this_role = get(this_guild.roles, name=str(h[1]+' '+h[2])) # int(s))
        await this_member.remove_roles(this_role)
        await ctx.send("Роль успешно удалена")
@bot.command()
async def ful(ctx):

    emb= discord.Embed(title='Удаление роли', description='Удаление роли происходит в одноимённом канале.\nДля этого напишите сообщение по шаблону: !delete Python \nНазвание роли, должно'+
                       ' быть точно такое, как в списке выше.', color=0xFFFB00)
    await ctx.send(embed=emb)
@bot.event
async def on_raw_reaction_remove(payload):
    emoji = payload.emoji
    print(payload)
    this_member1 = payload.user_id
    this_guild = bot.get_guild(payload.guild_id)
    this_member = this_guild.get_member(payload.user_id)
    print(this_member)
    print(this_guild)
    #this_guild = this_member.guild
    this_channel = payload.channel_id
    if this_channel != 719124796847292457:
        return
    print('событие было')    #это удали
    print(emoji.name)     #это удали
    if emoji.name=='🐍':
        this_role = get(this_guild.roles, id=int(719153280655032322))
        await this_member.remove_roles(this_role)
    elif emoji.name=='🦅':
        this_role = get(this_guild.roles, id=int(719153448595226654))
        await this_member.remove_roles(this_role)
    elif emoji.name=='🍁':
        this_role = get(this_guild.roles, id=int(719153481977430116))
        await this_member.remove_roles(this_role)
    elif emoji.name=='📜':
        this_role = get(this_guild.roles, id=int(719153580875055204))
        await this_member.remove_roles(this_role)
    elif emoji.name == '🐸':
        this_role = get(this_guild.roles, id=int(719153533047406592))
        await this_member.remove_roles(this_role)
    elif emoji.name=='🔮':
        this_role = get(this_guild.roles, id=int(719153691159953409))
        await this_member.remove_roles(this_role)
    elif emoji.name=='🍍':
        this_role = get(this_guild.roles, id=int(719153723657682954))
        await this_member.remove_roles(this_role)
    elif emoji.name=='🏀':
        this_role = get(this_guild.roles, id=int(719153854163451944))
        await this_member.remove_roles(this_role)
    elif emoji.name=='🎨':
        this_role = get(this_guild.roles, id=int(719153795304521729))
        await this_member.remove_roles(this_role)
    elif emoji.name=='⌨️':
        this_role = get(this_guild.roles, id=int(719153759900401665))
        await this_member.remove_roles(this_role)
    elif emoji.name=='💡':
        this_role = get(this_guild.roles, id=int(719153999315599432))
        await this_member.remove_roles(this_role)
    elif emoji.name=='🎓':
        this_role = get(this_guild.roles, id=int(719154042521255957))
        await this_member.remove_roles(this_role)
    elif emoji.name=='🎩':
        this_role = get(this_guild.roles, id=int(719154036858814494))
        await this_member.remove_roles(this_role)
    elif emoji.name=='🦢':
        this_role = get(this_guild.roles, id=int(719154046140809256))
        await this_member.remove_roles(this_role)
    elif emoji.name=='⚔️':
        this_role = get(this_guild.roles, id=int(719154154941186058))
        await this_member.remove_roles(this_role)
    elif emoji.name=='🌋':
        this_role = get(this_guild.roles, id=int(719154223714926623))
        await this_member.remove_roles(this_role)
    elif emoji.name=='🚀':
        this_role = get(this_guild.roles, id=int(719154322209898556))
        await this_member.remove_roles(this_role)
    elif emoji.name=='🧬':
        this_role = get(this_guild.roles, id=int(719154330070155265))
        await this_member.remove_roles(this_role)
@commands.has_permissions(manage_roles=True)
@bot.command()
async def мут(ctx, member: discord.Member):
    info=ctx.message.content
    info= info.split(' ')
    prison=info[1]
    mention=info[1]
    prison=prison[2:]
    prison_id=prison[:-1]
    print(prison_id)
    time=info[2]
    this_guild = ctx.message.author.guild
    print(this_guild)
    user=bot.get_user(prison_id)
    member=float(prison_id)
    print(member)
    this_member = get(this_guild.members, id=int(prison_id))
    print(this_member)
    his_roles= this_member.roles
    a=0
    for role in this_member.roles:
        his_roles[a]=(f'{role.name}')
        a=a+1
    print(his_roles)
    for i in range(1,len(his_roles)):
        this_role = get(this_guild.roles, name=his_roles[i])
        await this_member.remove_roles(this_role)
    mute_role = get(this_guild.roles, id=int(720565692981837965))
    await this_member.add_roles(mute_role)
    reason = info[4:]
    reason = ' '.join(reason)
    await ctx.send(
        mention + ' успешно отправлен в мут :no_entry_sign::no_entry_sign::no_entry_sign: \nПричина: ' + reason)
    time=info[2]
    print(time)
    how=info[3]
    print(how)
    if how=='h':
        mute_time= int(time)*3600
        await asyncio.sleep(mute_time)
    elif how=='m':
        mute_time= int(time)*60
        await asyncio.sleep(mute_time)
    elif how=='s':
        mute_time= int(time)
        await asyncio.sleep(mute_time)
    await ctx.send(mention+' снова может писать')
    for i in range(1, len(his_roles)):
        this_role = get(this_guild.roles, name=his_roles[i])
        await this_member.add_roles(this_role)
        await this_member.remove_roles(mute_role)
    reason = info[4:]
    reason = ' '.join(reason)
@bot.command()
async def баланс(ctx):
    name= ctx.message.author
    users = (requests.get('https://api.npoint.io/f48dd72c49b6cc84d2f4')).json()
    user_index = -1 
    for i in range (len(users)):
        if users[i]['username'] == str(name):
            user_index=i
            break
    if user_index == -1:
        users.append({"username": str(name),"money":0,"factor":1})
        data = json.dumps(users)
        requests.post('https://api.npoint.io/f48dd72c49b6cc84d2f4', data=data)
    user = users[user_index]
    emb = discord.Embed(title = 0, description = 'Dark Gibbons', colour = 0xFEFCFD)
    emb.add_field(name = 'Ваш баланс', value = user['money'])
    emb.set_footer (text = ctx.author.name,icon_url= ctx.author.avatar_url)
    await ctx.send(embed = emb)
    #await ctx.send(f"Ваш баланс: {user['money']}")
token = os.environ.get('BOT_TOKEN')

@bot.command()
async def купить(ctx):
    global role_price
    this_guild = ctx.message.author.guild
    info = ctx.message.content
    avtor= ctx.message.author.id
    this_member = get(this_guild.members, id=int(avtor))
    info = info.split(' ')
    role_ment = info[1]
    role_id= role_ment[3:]
    role_id = role_id[:-1]
    this_role = get(this_guild.roles, id=int(role_id))
    users = (requests.get('https://api.npoint.io/f48dd72c49b6cc84d2f4')).json()
    user_index = -1
    name= ctx.message.author
    for i in range (len(users)):
        if users[i]['username'] == str(name):
            user_index=i
            break
    if user_index == -1:
        users.append({"username": str(name),"money":0,"factor":1})
        data = json.dumps(users)
        requests.post('https://api.npoint.io/f48dd72c49b6cc84d2f4', data=data)
    user = users[user_index]
    if user['money'] >= role_price[role_id]:
        user['money'] -= role_price[role_id]
        await this_member.add_roles(this_role)
        data = json.dumps(users)
        requests.post('https://api.npoint.io/f48dd72c49b6cc84d2f4', data=data)
        await ctx.send('Вы успешно приобрели роль')
    else:
        await ctx.send(":x::x::x:Вы не достойны такой роскоши, так как у Вас недостаточно средств:x::x::x:")
@bot.command()
@commands.has_role('Владелец Жигули')
async def небухти(ctx):
        info = ctx.message.content
        msg = info.split(' ')
        emb= discord.Embed(title = 'Не бухти', description =msg[1]+', разве ты старый автомобиль, чтоб так бухтеть?\n'+ctx.message.author.mention +' просит тебя не бухтеть!')
        emb.set_image(url = 'https://cdn.discordapp.com/attachments/713748958916247592/724645466024706108/buhta.gif')
        emb.set_footer(text = 'Команда доступна только для Владельца Жигули')
        await ctx.send(embed = emb)
@bot.command()
@commands.has_role('Владелец Жигули')
async def незаводись(ctx):
        info = ctx.message.content
        msg = info.split(' ')
        emb= discord.Embed(title = 'Не заводись', description =msg[1]+', что-то ты не похож на Audi, чтоб заводиться\n'+
                           ctx.message.author.mention +' просит тебя не начинать злиться')
        emb.set_image(url = 'https://cdn.discordapp.com/attachments/701789648841736283/724654650963394630/fari.gif')
        emb.set_footer(text = 'Команда доступна только для Владельца Жигули')
        await ctx.send(embed = emb)
@bot.command()
@commands.has_role('Владелец Жигули')
async def сплошняк(ctx):
        info = ctx.message.content
        msg = info.split(' ')
        emb= discord.Embed(title = 'Ты сплошняк не пересекай', description =msg[1]+', не пересекай сплошную линию\n'+
                           ctx.message.author.mention +' просит тебя не переходить границы')
        emb.set_image(url = 'https://cdn.discordapp.com/attachments/701789648841736283/724657032933671052/splosh.gif')
        emb.set_footer(text = 'Команда доступна только для Владельца Жигули')
        await ctx.send(embed = emb)
@bot.command()
async def ставка(ctx):
    this_guild = ctx.message.author.guild
    
    this_channel = discord.utils.get(this_guild.channels, id = 724722525371629598)
    if ctx.channel !=this_channel:
        await ctx.send('Эту команду можно использовать только в канале казино')
        return
    info = ctx.message.content
    msg = info.split(' ')
    stavka = msg[1]
    stavka = int(stavka)
    if stavka < 10:
        await ctx.send(':x:Нельзя делать ставку меньше 10:x:')
        return
    kof = random.randint(0,100)
    kof = kof/50
    kof = round(kof,1)
    prize = kof*stavka
    prize = int(prize)
    users = (requests.get('https://api.npoint.io/f48dd72c49b6cc84d2f4')).json()
    user_index = -1
    name= ctx.message.author
    for i in range (len(users)):
        if users[i]['username'] == str(name):
            user_index=i
            break
    if user_index == -1:
        await ctx.send('Вы не зарегистрированы в базе данных, для регистрации пропишите /баланс')
    user = users[user_index]
    if user['money'] >=stavka:
            user['money'] -= stavka
            user['money'] += prize
            data = json.dumps(users)
            requests.post('https://api.npoint.io/f48dd72c49b6cc84d2f4', data=data)
    else:
        await ctx.send(':x:Недостаточно средств:x:')
        return
    if prize < stavka:
        emb = discord.Embed(title = 'Ваш выигрыш:', description = str(prize)+'\n\n:red_circle::white_circle::red_circle:\n\nВы проиграли'+
                            '\n\n:red_circle::white_circle::red_circle:', colour = 0xFF1F00)
        
        await ctx.send(embed = emb)
    if prize >=stavka:
        emb = discord.Embed(title = 'Ваш выигрыш:', description = str(prize)+'\n\n:green_circle::white_circle::green_circle:\n\nВы выиграли'+
                            '\n\n:green_circle::white_circle::green_circle:', colour = 0x00FF2A)
    
        await ctx.send(embed = emb)
                  
bot.run(token)
