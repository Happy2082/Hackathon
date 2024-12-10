import discord
from discord.ext import commands
import asyncio
import random
import os

fact_list = ["Plastik jest obecny w naszym życiu niemal na każdym kroku. Trudno byłoby nam zrezygnować z niego całkowicie, ale dla własnego (i pokolenia naszych dzieci!) dobra musimy znacząco ograniczyć korzystanie z tego nieekologicznego tworzywa.",
             'Większość z nas nie wyobraża sobie dnia bez kawy. Aromatyczny napój pijamy już nie tylko w  domach czy kawiarniach, ale także w trakcie przemieszczania się z miejsca na miejsce. Dostępność kawy na wynos jest coraz większa - a wraz z nią zużycie jednorazowych kubków i  plastikowych pokrywek. Jeśli często zdarza Ci się kupować kawę to go, zainwestuj w termiczny kubek wielokrotnego użytku.',
             'Nie bierz słomek - napój bez nich smakuje tak samo dobrze. Słomek używamy zaledwie przez kilka minut, a żeby uległy rozkładowi, musi minąć aż 200 lat. To aż dwa wieki zagrożenia, na które skazujemy środowisko, zwierzęta i siebie samych.']


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Zalogowaliśmy się jako {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Cześć, jestem bot{bot.user}!')

@bot.command()
async def samochód(ctx):
    await ctx.send("Samochody spalinowe – Emitują dwutlenek węgla i inne zanieczyszczenia, które przyczyniają się do globalnego ocieplenia i smogu w miastach. Samochody są bardzo szkodliwe gdy są korki.")

@bot.command()
async def opakowania(ctx):
    await ctx.send("Plastikowe torby i opakowania – Plastik rozkłada się przez setki lat, zanieczyszcza gleby i wody, a jego produkcja wiąże się z emisją gazów cieplarnianych.")

@bot.command()
async def ogrzewanie(ctx):
    await ctx.send("Nieekologiczne ogrzewanie domów – Spalanie węgla czy śmieci powoduje emisję pyłów i dwutlenku węgla, co zanieczyszcza powietrze i przyspiesza zmiany klimatyczne.")

@bot.command()
async def jedzenie(ctx):
    await ctx.send("Marnowanie jedzenia – Produkcja żywności pochłania ogromne zasoby (woda, energia), a wyrzucanie jej prowadzi do powstawania metanu na wysypiskach.")

@bot.command()
async def energia(ctx):
    await ctx.send("Nadmierne użycie energii elektrycznej – Niepotrzebne zużycie energii, zwłaszcza tej z nieodnawialnych źródeł, zwiększa emisję gazów cieplarnianych.")

@bot.command()
async def wylesienie(ctx):
    await ctx.send("Wylesianie – Wycinanie drzew ogranicza zdolność Ziemi do pochłaniania dwutlenku węgla, co nasila efekt cieplarniany.")

@bot.command()
async def hodowle(ctx):
    await ctx.send("Hodowle zwierząt - Hodowla zwierząt generuje duże ilości metanu i pochłania ogromne zasoby, jak woda czy ziemia uprawna.")
    
@bot.command()
async def pal_śmieci(ctx):
    await ctx.send("Palenie śmieci – Wytwarza toksyczne substancje, które zanieczyszczają powietrze i przyczyniają się do chorób oraz ocieplenia klimatu.")
    
@bot.command()
async def klima(ctx):
    await ctx.send("Klimatyzatory – Pobierają duże ilości energii, a często używane czynniki chłodnicze są gazami cieplarnianymi.")

@bot.command()
async def wysypiska(ctx):
    await ctx.send("Brak recyklingu – Odpady trafiają na wysypiska, gdzie rozkładają się przez dziesięciolecia, uwalniając szkodliwe substancje do atmosfery i wód gruntowych.")

@bot.command()
async def nawóz(ctx):
    await ctx.send("Sztuczne nawozy – Używane w nadmiarze zanieczyszczają gleby i wody, a ich produkcja wiąże się z emisją gazów cieplarnianych.")

@bot.command()
async def brudna_woda(ctx):
    await ctx.send("Zanieczyszczanie wód – Śmieci i chemikalia w rzekach i jeziorach niszczą ekosystemy wodne i pogarszają jakość wody pitnej.")

@bot.command()
async def papier(ctx):
    await ctx.send("Nadmierne zużycie papieru – Wycinka drzew pod produkcję papieru zmniejsza obszary lasów pochłaniających dwutlenek węgla.")

@bot.command()
async def samoloty(ctx):
    await ctx.send("Transport lotniczy – Krótkie loty są wyjątkowo energochłonne i emitują ogromne ilości dwutlenku węgla w krótkim czasie.")

@bot.command()
async def woda(ctx):
    await ctx.send("Nieodpowiedzialne zużycie wody – Nadmierne korzystanie z wody zwiększa zapotrzebowanie na jej oczyszczanie i transport, co zużywa energię.")

@bot.command()
async def odpady_elek(ctx):
    await ctx.send("Odpady elektroniczne – Nieodpowiednia utylizacja starej elektroniki prowadzi do zanieczyszczenia środowiska metalami ciężkimi.")

@bot.command()
async def olej_palmowy(ctx):
    await ctx.send("Produkty z olejem palmowym – Plantacje palm olejowych przyczyniają się do wycinania lasów deszczowych i niszczenia siedlisk wielu gatunków.")

@bot.command()
async def papierosy(ctx):
    await ctx.send("Palarnie papierosów – Niedopałki papierosów to jeden z najczęstszych odpadów, który zatruwa glebę i wodę.")

        
#Odczytywanie zdjęć
@bot.command()
async def meme (ctx):
    with open('zdjęcia/kod_mem1.jpg','rb')as f:
        mem = discord.File(f)
    await ctx.send('hello', file=mem)

@bot.command()
async def environment(ctx):
    choice = random.choice(fact_list)
    await ctx.send(choice)
#reakcję 
@bot.event
async def on_message(message):
    await bot.process_commands(message)
    if message.content.startswith('$done'):
        channel = message.channel
        await channel.send('Czy to wszystko?')

        def check(reaction, user):
            return user == message.author and str(reaction.emoji) == '👍'

        try:
            reaction, user = await bot.wait_for('reaction_add', timeout=60.0, check=check)
        except asyncio.TimeoutError:
            await channel.send('👎')
        else:
            await channel.send('👍')
    if message.content.startswith('$meme'):
        plik = random.choice(os.listdir('zdjęcia'))
        with open(f'zdjęcia/{plik}','rb')as f:
            mem = discord.File(f)
        await message.channel.send('hello', file=mem)
    if message.content.startswith('$meme/bazinga'):
        plik = random.choice(os.listdir('bazinga.mem'))
        with open('bazinga.mem/{plik}','rb')as f:
            mem = discord.File(f)
        await message.channel.send('hello', file=mem)
        
bot.run("")
