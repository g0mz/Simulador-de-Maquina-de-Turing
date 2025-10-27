import json
import time
import sys

def simular(json_path, input_path):

    try:
        with open(json_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        with open(input_path, "r", encoding="utf-8") as f:
            conteudo = f.read().strip()
    except FileNotFoundError as e:
        print(f"ERRO: Arquivo não encontrado: {e.filename}", file=sys.stderr)
        return
    except (json.JSONDecodeError, KeyError) as e:
        print(f"ERRO: O arquivo JSON ('{json_path}') está mal formatado. Detalhe: {e}", file=sys.stderr)
        return

    trans = {(t["from"], t["read"]): (t["to"], t["write"], t["dir"]) for t in data["transitions"]}
    estado = data["initial"]
    finais = set(data["final"])
    branco = data["white"]

    fita_pos = list(conteudo)
    fita_neg = []
    fita_pos_len = len(fita_pos)
    fita_neg_len = 0

    cabeca = 0
    passos = 0
    limite_passos = 7000000

    start = time.time() 

    while True:
        passos += 1
        if passos > limite_passos:
            print(0) 
            print(f"Tempo: {time.time() - start:.6f}s")
            return

        if cabeca >= 0:
            simbolo = fita_pos[cabeca] if cabeca < fita_pos_len else branco
        else:
            idx_neg = -cabeca - 1
            simbolo = fita_neg[idx_neg] if idx_neg < fita_neg_len else branco

        chave = (estado, simbolo)

        if chave not in trans:
            print(1 if estado in finais else 0)
            print(f"Tempo: {time.time() - start:.6f}s")
            return
        
        novo_estado, novo_simbolo, direcao = trans[chave]

        if cabeca >= 0:
            if cabeca < fita_pos_len:
                fita_pos[cabeca] = novo_simbolo
            else: 
                fita_pos.append(novo_simbolo)
                fita_pos_len += 1
        else:
            idx_neg = -cabeca - 1
            if idx_neg < fita_neg_len:
                fita_neg[idx_neg] = novo_simbolo
            else:
                fita_neg.append(novo_simbolo)
                fita_neg_len += 1

        estado = novo_estado
        cabeca += 1 if direcao == "R" else -1

if __name__ == "__main__":
    
    if len(sys.argv) != 3:
        print(f"Uso: python simulador_mt.py maquina.json entrada.in", file=sys.stderr)
        sys.exit(1)
    
    NOME_ARQUIVO_MAQUINA = sys.argv[1]
    NOME_ARQUIVO_ENTRADA = sys.argv[2]
    
    simular(NOME_ARQUIVO_MAQUINA, NOME_ARQUIVO_ENTRADA)