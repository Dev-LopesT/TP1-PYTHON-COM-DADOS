# Elaborore aqui a sua solução do TP
perfis_validos = []
perfis = []

#Etapa 01 - 

usuarios_infwenet = [
  ["Thiago Lopes", 28,"São Paulo", "SP"],
  ["Maria Silva", 23, "Belo Horizonte", "MG"],
  ["José Santos", 35, "Rio de Janeiro", "RJ"],
  ["Paulo Roberto", 45, "Curitiba", "PR"],
  ["Ana Maria", 30, "São Paulo", "SP"]
]

## Etapa 02 - 

def criar_perfis(usuarios_infwenet, perfis):

    for usuario in usuarios_infwenet:
        perfil = {
            "nome": usuario[0],
            "idade": usuario[1],
            "endereco": (usuario[2], usuario[3])
        }
        perfis.append(perfil)
    return perfis

perfis = criar_perfis(usuarios_infwenet, perfis)

print(perfis)

# Etapa 03 - Explicação no arquivo .ipynb

#Exemplo de Lista - 
users = [
  ["Thiago Lopes", 28,"São Paulo", "SP"],
  ["Maria Silva", 23, "Belo Horizonte", "MG"],
  ["José Santos", 35, "Rio de Janeiro", "RJ"],
  ["Paulo Roberto", 45, "Curitiba", "PR"],
  ["Ana Maria", 30, "São Paulo", "SP"]
]

##Exemplo de Dicionário - 

user = {
    "nome": "Ana Silva",
    "idade": 28,
    "localização": ("São Paulo", "SP")
}

##Exempçlo de Tupla - 

data_nascimento = (21, 10, 1980)

print(data_nascimento)
print(user)
print(users)


# Etapa 04 - 

def filtrar_perfis_validos(perfis, perfis_validos):
  
    for perfil in perfis:
        if perfil.get("nome") and perfil.get("endereco")[0]: 
            perfis_validos.append(perfil)
    return perfis_validos

perfis_validos = filtrar_perfis_validos(perfis, perfis_validos)
  
print(perfis_validos)

# Etapa 05 - 

def carregar_dados(arquivo, perfis):
    
    with open(arquivo, 'r', encoding='utf-8') as f:
        for linha in f:
            dados = linha.strip().split('?')
            
            # Extraindo os dados do arquivo, considerando posições básicas
            perfil = {
                "nome": dados[0],
                "idade": int(dados[1]) if dados[1].isdigit() else None,
                "endereco": (dados[2], dados[3]),
            }
            perfis.append(perfil)
    
    return perfis

def filtrar_perfis_validos(perfis):

    perfis_validos = []
    for perfil in perfis:
        if perfil.get("nome") and perfil.get("endereco")[0]: 
            perfis_validos.append(perfil)
    return perfis_validos

arquivo = "C:/Users/thiag/OneDrive/Área de Trabalho/PYTHON_INFNET_TPS/TP1/TP1-PYTHON-COM-DADOS/base_inicial.txt"
perfis = carregar_dados(arquivo, perfis)
perfis_validos = filtrar_perfis_validos(perfis)

print(perfis_validos)

#Etapa 06 -


def carregar_dados(arquivo, perfis):
    with open(arquivo, 'r', encoding='utf-8') as f:
        for linha in f:
            dados = linha.strip().split('?')
            
            perfil = {
                "nome": dados[0] if dados[0] else "N/A",
                "idade": int(dados[1]) if dados[1].isdigit() else "N/A",
                "endereco": (dados[2] if dados[2] else "N/A", dados[3] if len(dados) > 3 else "N/A"),
            }
            perfis.append(perfil)
    
    return perfis

def salvar_rede_INFNET(perfis, arquivo_saida="rede_INFNET.txt"):
    with open(arquivo_saida, 'w', encoding='utf-8') as f:
        for perfil in perfis:
            nome = perfil["nome"] if perfil["nome"] != "N/A" else "N/A"
            idade = perfil["idade"] if perfil["idade"] != "N/A" else "N/A"
            cidade, estado = perfil["endereco"]
            cidade = cidade if cidade != "N/A" else "N/A"
            estado = estado if estado != "N/A" else "N/A"
            
            linha = f"{nome}?{idade}?{cidade}?{estado}\n"
            f.write(linha)

arquivo = "C:/Users/thiag/OneDrive/Área de Trabalho/PYTHON_INFNET_TPS/TP1/TP1-PYTHON-COM-DADOS/base_inicial.txt"

perfis = carregar_dados(arquivo, perfis)

novos_usuarios = [
  {"nome": "Thiago Lopes", "idade": 28, "endereco": ("São Paulo", "SP")},
  {"nome": "Maria Silva", "idade": 23, "endereco": ("Belo Horizonte", "MG")},
  {"nome": "José Santos", "idade": 35, "endereco": ("Rio de Janeiro", "RJ")},
  {"nome": "Paulo Roberto", "idade": 45, "endereco": ("Curitiba", "PR")},
  {"nome": "Ana Maria", "idade": 30, "endereco": ("São Paulo", "SP")}
]

perfis.extend(novos_usuarios)

salvar_rede_INFNET(perfis)

print("Arquivo 'rede_INFNET.txt' criado com sucesso.")
print(perfis)