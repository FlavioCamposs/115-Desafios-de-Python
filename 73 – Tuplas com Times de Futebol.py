times = ('Palmeiras', 'Grêmio', 'Atlético-MG', 'Flamengo', 'Botafogo', 'Red Bull Bragantino', 'Fluminense', 'Athletico-PR', 'Internacional', 'Fortaleza', 'São Paulo', 'Cuiabá', 'Corinthians', 'Cruzeiro', 'Vasco', 'Bahia', 'Santos', 'Goiás', 'Coritiba', 'América-MG')

print(times[0:6]) #OS 5 PRIMEIROS COLOCADOS
print(times[-4:]) #OS 4 ULTIMOS COLOCADOS
print(sorted(times)) #Mostrar os elementos da tupla em ordem alfabetica
print(f'O time do Botafogo se encontra na {times.index('Botafogo')+1}° posição') #Em que posição está o time do Botafogo
