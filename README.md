# portfolio-Carlos-Eduardo-Azevedo-
<h1 align="center">Olá, eu sou o Carlos Eduardo! 👋</h1>

<h3 align="center">Análise e Desenvolvimento de Sistemas | Python Developer | IA Enthusiast</h3>

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=Portfolio-Carlos-Eduardo-Azevedo-Alves&show_icons=true&theme=radical&include_all_commits=true&count_private=true" alt="Estatísticas do GitHub" height="180">
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=Portfolio-Carlos-Eduardo-Azevedo-Alves&layout=compact&theme=radical" alt="Linguagens mais usadas" height="180">
</p>

---

## 👨‍💻 Sobre Mim

Estou graduando em **Análise e Desenvolvimento de Sistemas na Universidade Cidade de São Paulo (UNICID)**. Minha abordagem une lógica de programação com foco na resolução de problemas reais.

Acredito que a tecnologia só é eficiente quando é acessível, organizada e bem documentada.

- 🐍 **Desenvolvimento:** Construindo bases sólidas em Python com foco em lógica, estruturas de dados e algoritmos.
- 🤖 **IA:** Uso ferramentas como Claude, Gemini e ChatGPT para potencializar soluções e aprendizado.
- 🎨 **Design:** Criação visual com Figma, Adobe e Canva para comunicar ideias com clareza.

---

## 🛠️ Ferramentas Favoritas

### 🎨 Design
![Figma](https://img.shields.io/badge/figma-%23F24E1E.svg?style=for-the-badge&logo=figma&logoColor=white)
![Adobe](https://img.shields.io/badge/adobe-%23FF0000.svg?style=for-the-badge&logo=adobe&logoColor=white)
![Canva](https://img.shields.io/badge/Canva-%2300C4CC.svg?style=for-the-badge&logo=Canva&logoColor=white)

### 💻 Linguagens e Tecnologias
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![VS Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078D4?style=for-the-badge&logo=visual%20studio%20code&logoColor=white)
![Google Colab](https://img.shields.io/badge/Colab-F9AB00?style=for-the-badge&logo=googlecolab&logoColor=white)

### 🤖 Inteligência Artificial
![Claude](https://img.shields.io/badge/Claude-D97757?style=for-the-badge&logo=anthropic&logoColor=white)
![ChatGPT](https://img.shields.io/badge/ChatGPT-74aa9c?style=for-the-badge&logo=openai&logoColor=white)
![Gemini](https://img.shields.io/badge/Gemini-8E75B2?style=for-the-badge&logo=googlegemini&logoColor=white)

---

## 🚀 Projetos em Destaque

> Abaixo estão os projetos desenvolvidos ao longo da minha formação. Cada um representa um conceito diferente de programação aplicado a situações reais.

---

### 📊 EX1 — Algoritmo de Auditoria de Dados

**Conceitos:** Outliers, Normalização, Margem de Tolerância, Teste de Estresse

> Algoritmo que identifica discrepâncias em conjuntos de dados. Valores muito fora do padrão (como o 5000 em um conjunto com 100 e 200) são detectados automaticamente como candidatos à revisão — simulando uma auditoria real de dados financeiros.

**Aprendizados:**
- Variáveis globais podem ser perigosas: qualquer parte do sistema pode alterá-las, gerando erros ou fraudes.
- Erro de indentação foi corrigido após revisão cuidadosa — o Python interpreta o código de forma literal.

---

### 🧩 EX2 — Engenharia de Soluções Lógicas

**Conceitos:** Decomposição de problemas, raciocínio lógico estruturado

> Projeto focado em dividir problemas complexos em partes menores e resolvê-los de forma organizada, aplicando lógica passo a passo.

---

### 🔧 EX3 — Modularização

**Conceitos:** Funções, reutilização de código, organização modular

> Exercício prático de modularização — separar o código em funções independentes para facilitar manutenção, leitura e reutilização.

---

### 🐍 EX4 — Traduzindo Lógica para Python

**Conceitos:** Funções, loops, condicionais, tipagem, `range()`

Quatro programas completos:

<details>
<summary><b>1. Processador de Vendas com Desconto</b></summary>

```python
def processar_vendas():
    total_compra = 0.0
    itens_comprados = 0

    quantidade_tipos = int(input("Quantos produtos diferentes foram comprados? "))

    contador = 0
    while contador < quantidade_tipos:
        nome = input("Nome do produto: ")
        preco = float(input("Preço unitário: "))
        qtd = int(input(f"Quantidade de '{nome}': "))

        if preco <= 0 or qtd <= 0:
            print(f"Valores inválidos para '{nome}'. Item ignorado.")
        else:
            subtotal = preco * qtd
            total_compra += subtotal
            itens_comprados += qtd

        contador += 1

    if total_compra > 500:
        total_final = total_compra * 0.90
        print("Desconto de 10% aplicado!")
    elif total_compra > 200:
        total_final = total_compra * 0.95
        print("Desconto de 5% aplicado!")
    else:
        total_final = total_compra

    print(f"\nResumo: {itens_comprados} itens. Total a pagar: R$ {total_final:.2f}")

processar_vendas()
```
</details>

<details>
<summary><b>2. Analisador de Clima Semanal</b></summary>

```python
def analisar_clima():
    soma_temperaturas = 0.0
    dias_quentes = 0
    alerta_extremo = False

    for dia in [1, 2, 3, 4, 5, 6, 7]:
        temp = float(input(f"Digite a temperatura do dia {dia}: "))
        soma_temperaturas = soma_temperaturas + temp

        if temp > 35.0:
            dias_quentes = dias_quentes + 1

        if temp > 45.0 or temp < -5.0:
            alerta_extremo = True

    media = soma_temperaturas / 7
    print("Média semanal:", media)
    print("Dias acima de 35°C:", dias_quentes)

    if alerta_extremo == True:
        print("CUIDADO: Condições climáticas perigosas detectadas!")
    else:
        print("Clima dentro da normalidade operacional.")

analisar_clima()
```
</details>

<details>
<summary><b>3. Sistema de Notas da Turma</b></summary>

```python
def sistema_notas_turma():
    total_alunos = int(input("Quantos alunos existem na turma? "))

    for j in range(total_alunos):
        aluno_nome = input("Nome do aluno: ")
        n1 = float(input("Nota 1: "))
        n2 = float(input("Nota 2: "))

        media_aluno = (n1 + n2) / 2

        if media_aluno >= 7.0:
            print(aluno_nome, ": Aprovado com média", media_aluno)
        elif media_aluno >= 5.0:
            print(aluno_nome, ": Recuperação (Média:", media_aluno, ")")
        else:
            print(aluno_nome, ": Reprovado")

sistema_notas_turma()
```
</details>

<details>
<summary><b>4. Simulador de Poupança</b></summary>

```python
def simulador_poupanca():
    saldo = float(input("Valor inicial do investimento: "))
    taxa = float(input("Taxa de juros mensal (em %): "))
    meses = int(input("Número de meses da simulação: "))

    m = 1
    while m <= meses:
        aporte = float(input(f"Quanto deseja depositar no mês {m}? (0 para nenhum) "))

        saldo = saldo + aporte
        juros = saldo * (taxa / 100)
        saldo = saldo + juros

        print("Mês", m, ": Saldo atualizado = R$", saldo)

        if saldo > 10000.0:
            print("Parabéns! Você atingiu a meta de 10k no mês", m)

        m = m + 1

    print("Resultado final após", meses, "meses: R$", saldo)

simulador_poupanca()
```
</details>

**Notas técnicas:**
- `input()` sempre retorna `string` — use `int()` ou `float()` para converter antes de operar matematicamente.
- `range()` não inclui o valor final: para ir de 1 até N, use `range(1, N + 1)`.

---

### 🏙️ EX5 — Engenharia de Contexto e Lógica Física

**Conceitos:** Listas aninhadas, loops duplos, `match-case`, fórmulas matemáticas, inventário com listas

<details>
<summary><b>Parte 1 — Análise de Microclima Urbano (Mooca | Tatuapé | Guaianases)</b></summary>

```python
def analisar_microclima():
    print("--- ANÁLISE DE MICROCLIMA: MOOCA | TATUAPÉ | GUAIANASES ---")

    # Lista de Listas: [Local, Horário, Temperatura, Umidade, IQA]
    dados_locais = [
        ["Mooca", "Manhã", 19, 78, 42],
        ["Mooca", "Tarde", 31, 35, 72],
        ["Tatuapé (Unicid)", "Manhã", 19, 76, 38],
        ["Tatuapé (Unicid)", "Tarde", 30, 36, 68],
        ["Guaianases", "Manhã", 18, 82, 35],
        ["Guaianases", "Tarde", 29, 38, 58]
    ]

    for local in dados_locais:
        nome_cidade = local[0]
        periodo = local[1]

        metricas = local[2:]
        for valor in metricas:
            temp = local[2]
            umid = local[3]
            iqa = local[4]

        match iqa:
            case i if 0 <= i <= 40:
                status_ar = "Boa"
            case i if 41 <= i <= 80:
                status_ar = "Moderada"
            case i if 81 <= i <= 120:
                status_ar = "Ruim"
            case _:
                status_ar = "Péssima"

        penalidade_temp = abs(temp - 22) * 0.3
        penalidade_iqa = iqa * 0.05
        nota_ncu = 10 - (penalidade_temp + penalidade_iqa)

        if nota_ncu < 0:
            nota_ncu = 0

        print(f"\nLocal: {nome_cidade} ({periodo})")
        print(f" > IQA: {iqa} - Classificação: {status_ar}")
        print(f" > Nota de Conforto Urbano: {nota_ncu:.1f}/10")

analisar_microclima()
```
</details>

<details>
<summary><b>Parte 2 — Simulador de Evacuação (Unicid)</b></summary>

```python
def simulador_evacuacao():
    print("--- SIMULADOR DE ROTA DE FUGA: SAINDO DA UNICID ---")

    locais = ["Sala de Aula", "Corredor 1", "Escada", "Recepção", "Rua"]
    estados = ["Livre", "Fumaça", "Obstrução", "Porta Trancada", "Final"]

    posicao = 0
    energia = 10
    mochila = []
    concluido = False

    while energia > 0 and concluido == False:
        onde_estou = locais[posicao]
        o_que_tem = estados[posicao]

        print(f"\nEstou no(a): {onde_estou} | Situação: {o_que_tem}")

        if o_que_tem == "Final":
            print(">>> SUCESSO! Cheguei na rua em segurança.")
            concluido = True

        elif o_que_tem == "Livre":
            posicao = posicao + 1
            energia = energia - 1

        elif o_que_tem == "Fumaça":
            print("Agente rastejou para passar pela fumaça.")
            posicao = posicao + 1
            energia = energia - 3

        elif o_que_tem == "Porta Trancada":
            if "Chave" in mochila:
                print("Agente usou a chave e abriu a porta!")
                posicao = posicao + 1
            else:
                print("Porta trancada! Voltando um cômodo para buscar a chave...")
                mochila.append("Chave")
                posicao = posicao - 1
            energia = energia - 2

        elif o_que_tem == "Obstrução":
            print("Móveis no caminho! Agente pulou os obstáculos.")
            posicao = posicao + 1
            energia = energia - 2

    if energia <= 0 and concluido == False:
        print("\n O agente cansou e não conseguiu sair a tempo.")

simulador_evacuacao()
```
</details>

**Reflexão:**
> Aprender a programar me ensinou que dá pra resolver problemas grandes aos poucos. As estruturas como `if` e `else` me ajudaram a enxergar que muitas decisões seguem uma lógica básica — e isso mudou minha forma de pensar fora do computador também.

---

### 🎨 EX6 — Desenhando Emojis com Dados

**Conceitos:** Matrizes, dicionários, listas aninhadas, `matplotlib`, transposição de matrizes

<details>
<summary><b>Emoji com Matplotlib</b></summary>

```python
import matplotlib.pyplot as plt

emoji_data = {
    "nome": "Smile",
    "grade": [
        [(255,255,0), (255,255,0), (255,255,0), (255,255,0), (255,255,0)],  # Linha 0
        [(255,255,0), (0,0,0),     (255,255,0), (0,0,0),     (255,255,0)],  # Linha 1 (Olhos)
        [(255,255,0), (255,255,0), (255,255,0), (255,255,0), (255,255,0)],  # Linha 2
        [(255,255,0), (0,0,0),     (0,0,0),     (0,0,0),     (255,255,0)],  # Linha 3 (Boca)
        [(255,255,0), (255,255,0), (255,255,0), (255,255,0), (255,255,0)]   # Linha 4
    ]
}

plt.imshow(emoji_data["grade"])
plt.show()
```
</details>

<details>
<summary><b>Biblioteca Musical com Transposição de Matriz</b></summary>

```python
biblioteca_musical = {
    "Toques": [
        {"Alegre": ([440, 480], [520, 560])},
        {"Triste": ([200, 150], [100, 50])}
    ]
}

for chave, lista_toques in biblioteca_musical.items():
    for musica in lista_toques:
        for nome, matriz in musica.items():
            print(f"Música: {nome}")
            print("Antes:", list(matriz))

            transposta = [
                [matriz[0][0], matriz[1][0]],
                [matriz[0][1], matriz[1][1]]
            ]

            for linha in transposta:
                print(" linha transposta:", linha)

            musica.update({nome: transposta})
            print("Depois:", musica[nome])
```
</details>

<details>
<summary><b>Playlist com Inserção e Remoção de Imagens</b></summary>

```python
playlist = {
    "nome": "Minha Playlist",
    "imagens": [
        {"titulo": "Sol",   "pixels": ((255,200,0),  (255,220,50), (200,150,0))},
        {"titulo": "Céu",   "pixels": ((100,150,255),(50,100,200), (30,80,180))},
        {"titulo": "Grama", "pixels": ((0,180,50),   (0,140,30),   (50,200,80))}
    ]
}

nova_imagem = {"titulo": "Fogo", "pixels": ((255,80,0), (255,40,0), (200,20,0))}
playlist["imagens"].insert(0, nova_imagem)

removida = playlist["imagens"].pop()
print(f"Imagem removida: {removida['titulo']}")

for chave in playlist.keys():
    if chave == "imagens":
        for imagem in playlist[chave]:
            print(f" Imagem: {imagem['titulo']}")
            for pixel in imagem["pixels"]:
                print(f"  pixel: {pixel}")
```
</details>

---

## 📫 Vamos nos conectar?

<p align="left">
  <a href="https://www.linkedin.com/in/carlos-eduardo-4968a92a8" target="_blank">
    <img src="https://img.shields.io/badge/-LinkedIn-%230077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn">
  </a>
  <a href="mailto:carloseduardo.1977azevedo@gmail.com">
    <img src="https://img.shields.io/badge/-Email-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="Email">
  </a>
</p>

---

> *"O código é poesia — cada linha conta uma história."*
