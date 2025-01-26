import requests
import discord
import os
import random
import numpy as np
from discord.ext import commands
import webserver
import os
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def poke(ctx,arg):
    try:
        pokemon = arg.split(" ",1)[0].lower()
        result = requests.get("https://pokeapi.co/api/v2/pokemon/"+pokemon)
        if result.text == "Not Found":
            await ctx.send("Pokemon no encontrado")
        else:
            image_url = result.json()["sprites"]["front_default"]
            print(image_url)
            await ctx.send(image_url)
    except Exception as e:
        print("Error:", e)
@poke.error
async def error_type(ctx,error):
    if isinstance(error,commands.errors.MissingRequiredArgument):
        await ctx.send("Tienes que darme un pokemon")

@bot.command()
async def limpiar(ctx):
    await ctx.channel.purge()
    await ctx.send("Mensajes eliminados", delete_after = 3)

@bot.command()
async def divide(ctx, left: int, right: int):
    """divide two numbers together."""
    if right == 0:
        await ctx.send("Error: Division por cero no esta definida!")
    else:
        await ctx.send(left / right)

@bot.command()
async def raiz(ctx,n1:int):
    """Esta función saca la raíz cuadrada de los números."""
    resultado2 = np.sqrt(n1)
    await ctx.send(f"La raiz cuadrada de {n1} {resultado2}")

@bot.command()
async def exp(ctx,n1:int, n2: int):
    resultado_exp = n1**n2
    await ctx.send(f"el numero {n1} elevado a la {n2} es {resultado_exp}")

@bot.command()
async def guide(ctx):
    await ctx.send(f"""Hola soy el bot de este servidor y mi nombre es Hero276 Bot y estas son mis funciones:
                    1. Saludo a un nuevo integrante del servidor
                    2. Puedo aparecer imágenes de Pokemones
                    3. Puedo limpiar y borrar los mensajes del servidor
                    4. Puedo dividir numeros (menos el 0)
                    5. Puedo sacar la raiz cuadrada de los números
                    6. Puedo elevar al cuadrado los números""")           

@bot.command()
async def gif(ctx):
    gif = random.choice(os.listdir("gifs de Discord"))
    await ctx.send(file=discord.File(f'gifs de Discord/{gif}'))

webserver.keep_alive()
bot.run("DISCORD_TOKEN")
