import discord
from discord.ext import commands, tasks
from itertools import cycle

# from keep_alive import keep_alive

description = '''An example bot to showcase the discord.ext.commands extension
module.
There are a number of utility commands being showcased here.'''

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='',
                   description=description,
                   intents=intents)
status = cycle(['테스트1', '퉤스트트틑트2'])


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

    global on_cam_channel
    global off_cam_channel
    global talk_channel

    on_cam_channel = bot.get_channel(822652677217058838)
    off_cam_channel = bot.get_channel(830089564268789760)
    talk_channel = bot.get_channel(822652676813619245)

    check_channel_camera.start()


@bot.event
async def on_voice_state_update(member, before, after):
    channel = before.channel or after.channel
    if channel == on_cam_channel:  # Insert voice channel ID
        if after.channel is on_cam_channel:  # Member joins the defined channel
            message = f'{member.display_name}님이 화상 독서실에 입장하셨습니다. 오늘도 화이팅~!'
            await talk_channel.send(message)
    if channel == off_cam_channel:
        if after.channel is off_cam_channel:
            message = f'{member.display_name}님이 일반 독서실에 입장하셨습니다. 마지막까지 화이팅!'
            await talk_channel.send(message)


@tasks.loop(seconds=30)
async def check_channel_camera():
    members = on_cam_channel.members
    for members in members:
        if members.voice.self_video is False:
            print(f'{members.display_name}의 카메라가 꺼져있으므로 방을 이동합니다.')
            await members.move_to(off_cam_channel)
            message = f'{members.display_name}의 카메라가 꺼져있으므로 방을 이동합니다.'
            await talk_channel.send(message)


# keep_alive()
bot.run('ODI4OTgyMTMxNjU2NzUzMjAy.YGxfxQ.E274maOfODYW7wcV490ovcIPXdk')
