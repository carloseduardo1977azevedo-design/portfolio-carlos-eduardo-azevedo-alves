# Auditoria de Orcamentos Corporativos (Python)

[![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/)
[![Status](https://img.shields.io/badge/status-concluido-brightgreen.svg)]()

## Sobre o Projeto
Este projeto foi desenvolvido como parte da disciplina de Programacao de Computadores do curso de Analise e Desenvolvimento de Sistemas.
O script processa e calcula o orcamento de uma estrutura organizacional complexa usando dicionarios aninhados,
aplicando regras de negocio dinamicas e auditoria de execucao.

## Funcionalidades
- Calculo hierarquico percorrendo a estrutura completa, independente do nivel de profundidade
- Filtros dinamicos para ignorar departamentos especificos e seus sub-setores
- Conversao de cambio com parametros opcionais em tempo de execucao
- Auditoria automatizada medindo o tempo de execucao e registrando os parametros utilizados

## Conceitos Aplicados
- **Recursao:** navegacao na arvore de dicionarios aninhados
- **Decorators:** `@auditor` injeta log e cronometragem sem alterar a logica principal
- **`*args` e `**kwargs`:** permitem passar departamentos ignorados e taxas de cambio dinamicamente

## Como Executar
1. Clone o repositorio:
```bash
   git clone https://github.com/carlos-eduardo-azevedo/portfolio-carlos-eduardo-azevedo-alves.git
```
2. Acesse a pasta:
```bash
   cd projeto-auditoria-orcamentos
```
3. Execute:
```bash
   python main.py
```

## Autor
- **Carlos Eduardo Azevedo Alves**
- LinkedIn: [seu link aqui]
- E-mail: [seu email aqui]

---
Projeto academico com foco na aplicacao pratica de conceitos avancados de Python.
