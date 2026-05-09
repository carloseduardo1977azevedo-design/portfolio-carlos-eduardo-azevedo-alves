import time

# Estrutura da empresa (dicionário aninhado)
empresa = {
    "TI": {
        "Infraestrutura": 120_000,
        "Desenvolvimento": {
            "Backend": 95_000,
            "Frontend": 80_000
        },
        "Segurança": 60_000
    },
    "RH": {
        "Recrutamento": 30_000,
        "Treinamento": 22_000,
        "Benefícios": 50_000
    },
    "Marketing": {
        "Publicidade": 75_000,
        "Eventos": 40_000
    },
    "Financeiro": {
        "Contabilidade": 35_000,
        "Tesouraria": 200_000
    }
}

# Decorator de auditoria
def auditor(funcao):
    def wrapper(*args, **kwargs):
        print("=" * 50)
        print(f"  Auditoria --- '{funcao.__name__}'")
        print(f"  Ignorados: {args[1:] or 'nenhum'}")
        print(f"  Cambio: {kwargs or 'sem conversao'}")
        print("=" * 50)

        inicio = time.time()
        resultado = funcao(*args, **kwargs)
        tempo = (time.time() - inicio) * 1000

        print(f"  Tempo: {tempo:.4f} ms")
        print("=" * 50)
        return resultado
    return wrapper

# Função principal com recursão, *args e **kwargs
@auditor
def calcular_orcamento(estrutura, *ignorados, **cambio):
    def somar(no):
        total = 0
        for chave, valor in no.items():
            if chave in ignorados:
                print(f"  Ignorando: '{chave}'")
                continue
            total += somar(valor) if isinstance(valor, dict) else valor
        return total

    total = somar(estrutura) * cambio.get("taxa_cambio", 1.0)
    moeda = cambio.get("moeda_destino", "USD")
    print(f"\n  Total ({moeda}): {total:,.2f}\n")
    return total

# Exemplos de uso
calcular_orcamento(empresa)
calcular_orcamento(empresa, "Marketing")
calcular_orcamento(empresa, "Marketing", "RH", moeda_destino="BRL", taxa_cambio=5.75)
