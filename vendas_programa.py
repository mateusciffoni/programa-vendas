vendas = [[1245,1160,1334,513],[726,1409,953,838],[501,769,1328,1497],[799,1141,757,1242],[1253,809,1462,1263]]
nomes = ["Alencar","Meireles","Veríssimo","Machado","Lobato"]
vendedores=5
semanas=4

#a) Total de vendas
total_vendas=0
for i in range(vendedores):
    for j in range(semanas):
        total_vendas+=vendas[i][j]
print(f"Total de vendas: R$ {total_vendas:.2f}")


maior_total_semana=0 #e)semana mais lucrativa

#b) Total de vendas por semana
print("Total de vendas por semana")
for j in range(semanas):
    total_semana=0
    for i in range(vendedores):
        total_semana+=vendas[i][j]
    print(f"      semana {j+1}: R$ {total_semana:.2f}")
    if total_semana > maior_total_semana: #e)semana mais lucrativa
        maior_total_semana=total_semana  #e)semana mais lucrativa
        melhor_semana = j   #e)semana mais lucrativa
print("Semana mais lucrativa: ",melhor_semana+1)

#c) Total de vendas por vendedor
print("Total de vendas por vendedor")
salarios=[]  #lista para armazenar todos os salários
for i in range(vendedores):    
    total_vendedor=0
    for j in range(semanas):
        total_vendedor+=vendas[i][j]
    print(f"      {nomes[i]:10}: R$ {total_vendedor:.2f}")
    salarios.append(2000+total_vendedor*0.1) #lista com todos os salários
    
#d) Maior venda por semana
print("Maior total de vendas por um mesmo vendedor em cada semana")
for j in range(semanas):
    maior_venda=0
    for i in range(vendedores):
        if vendas[i][j]> maior_venda:
            maior_venda = vendas[i][j]
    print(f"      semana {j+1}: R$ {maior_venda:.2f}")

maior_salario=0 #f) Maior salário
soma_salarios=0 #g) Lucro da loja
for i in range(len(salarios)):
    soma_salarios+=salarios[i] #g) Lucro da loja
    if salarios[i]>maior_salario: #f) Maior salário
        maior_salario=salarios[i] #f) Maior salário      
        indice_maior_salario = i  #f) Maior salário
print(f"O maior salário foi do vendedor {nomes[i]}: R$ {maior_salario:.2f}")
print(f"Lucro Total: R$ {total_vendas - soma_salarios:.2f}")