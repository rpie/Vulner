import os, discord

bot = discord.Client()

channel_id = 839911728644096010
token = 'ODQxNzgwODQxNDg2MzUyNDg0.YJrvlA.cojiC_q1sUowYrIqt65btLX_e_M'

async def on_ready(self):
    print(f"Discord version: {discord.__version__}")

async def on_voice_state_update(self, member, before, after):
    try:
        if after.channel:
            if after.channel.id == self.channel_id:
                await member.move_to(None)
    except:
        print('packer recived but failed')

bot.run(token, bot=False)