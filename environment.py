import random

fact_list = ["Plastik jest obecny w naszym życiu niemal na każdym kroku. Trudno byłoby nam zrezygnować z niego całkowicie, ale dla własnego (i pokolenia naszych dzieci!) dobra musimy znacząco ograniczyć korzystanie z tego nieekologicznego tworzywa.",
             'Większość z nas nie wyobraża sobie dnia bez kawy. Aromatyczny napój pijamy już nie tylko w  domach czy kawiarniach, ale także w trakcie przemieszczania się z miejsca na miejsce. Dostępność kawy na wynos jest coraz większa - a wraz z nią zużycie jednorazowych kubków i  plastikowych pokrywek. Jeśli często zdarza Ci się kupować kawę to go, zainwestuj w termiczny kubek wielokrotnego użytku.',
             'Nie bierz słomek - napój bez nich smakuje tak samo dobrze. Słomek używamy zaledwie przez kilka minut, a żeby uległy rozkładowi, musi minąć aż 200 lat. To aż dwa wieki zagrożenia, na które skazujemy środowisko, zwierzęta i siebie samych.']

async def on_message(message):
    if message.content.startswith('$environment'):
        channel = message.channel
        choice = random.choice(fact_list)
        message.channel.send(choice)
