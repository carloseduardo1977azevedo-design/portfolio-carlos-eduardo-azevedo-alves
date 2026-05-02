# Engenharia de Contexto e Logica Fisica

> Projeto desenvolvido por **Carlos Eduardo Azevedo Alves**  
> Curso: Análise e Desenvolvimento de Sistemas — UNICID

---

## Descrição

Análise de microclima urbano (Mooca, Tatuapé, Guaianases) e simulador de rota de evacuação com listas, loops e match-case.

---

## O que usei

- Listas aninhadas e loops duplos
- match-case (Python 3.10+)
- Fórmulas matemáticas aplicadas
- Inventário dinâmico com listas

---

## o que eu aprendi

- Aprender a programar ensina que dá pra resolver problemas grandes aos poucos.
- Estruturas como if e else refletem decisões lógicas do mundo real.

---

## Codigo

<details>
<summary>Parte 1 — Analise de Microclima Urbano</summary>

```python
def analisar_microclima():
    print("--- ANÁLISE DE MICROCLIMA: MOOCA | TATUAPÉ | GUAIANASES ---")
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
<summary>Parte 2 — Simulador de Evacuacao</summary>

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
        print("\nO agente cansou e não conseguiu sair a tempo.")

simulador_evacuacao()
```

</details>

---

## Como Executar
1. Clone o repositório.
2. Instale as dependências: `pip install -r requirements.txt`.
3. Execute o arquivo principal: `python main.py`.

---
[Voltar ao início](https://github.com/carlos-eduardo-azevedo/portfolio-carlos-eduardo-azevedo-alves)

## Tecnologia

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
