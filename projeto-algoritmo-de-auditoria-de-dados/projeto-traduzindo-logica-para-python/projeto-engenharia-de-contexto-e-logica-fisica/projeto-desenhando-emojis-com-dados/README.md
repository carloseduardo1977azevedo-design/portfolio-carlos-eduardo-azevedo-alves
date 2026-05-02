# Desenhando Emojis com Dados

> Projeto desenvolvido por **Carlos Eduardo Azevedo Alves**  
> Curso: Análise e Desenvolvimento de Sistemas — UNICID

---

## Descrição

Manipulação de matrizes, dicionários e tuplas com loops aninhados para criar arte visual em pixel com matplotlib.

---

## Conceitos Aplicados

- Matrizes e listas aninhadas
- Dicionários e tuplas
- Loops aninhados
- Transposição de matrizes
- Visualização com matplotlib

---

## Aprendizados

- Matrizes são estruturas poderosas para representar dados visuais.
- A transposição inverte linhas e colunas — conceito fundamental em álgebra linear.

---

## Codigo

<details>
<summary>Emoji com Matplotlib</summary>

```python
import matplotlib.pyplot as plt

emoji_data = {
    "nome": "Smile",
    "grade": [
        [(255,255,0), (255,255,0), (255,255,0), (255,255,0), (255,255,0)],
        [(255,255,0), (0,0,0),     (255,255,0), (0,0,0),     (255,255,0)],
        [(255,255,0), (255,255,0), (255,255,0), (255,255,0), (255,255,0)],
        [(255,255,0), (0,0,0),     (0,0,0),     (0,0,0),     (255,255,0)],
        [(255,255,0), (255,255,0), (255,255,0), (255,255,0), (255,255,0)]
    ]
}

plt.imshow(emoji_data["grade"])
plt.show()
```

</details>

<details>
<summary>Biblioteca Musical com Transposicao de Matriz</summary>

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
<summary>Playlist com Insercao e Remocao de Imagens</summary>

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

## Como Executar
1. Clone o repositório.
2. Instale as dependências: `pip install -r requirements.txt`.
3. Execute o arquivo principal: `python main.py`.

---
[Voltar ao início](https://github.com/carlos-eduardo-azevedo/portfolio-carlos-eduardo-azevedo-alves)

## Tecnologia

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
