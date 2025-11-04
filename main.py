import pandas as pd
import matplotlib.pyplot as plt
from os import path
from collections import defaultdict
from typing import Dict, Set

def loadFromCsv(path: str)->Dict[str, pd.DataFrame]:
    result: Dict[str, pd.DataFrame] = {}
    csv: pd.DataFrame = pd.read_csv(path) # type: ignore
    programs:Set[str] = set(csv["programa"])
    for program in programs:
            subset = csv[csv["programa"] == program].copy()
            subset.drop(columns=["programa", "rep"], inplace=True, errors="ignore")
            result[program] = subset
    return result

def plotThreads(data: Dict[str, pd.DataFrame]):
    threads: Set[int] = set()
    N: Set[int] = set()
    for _, values in data.items():
        threads.update(values["threads"])
        N.update(values["N"])
    sorted_threads = sorted(list(threads))
    sorted_N = sorted(list(N))
    # Construir un diccionario por item->thread->N->mean para asegurar alineamiento por N
    s: Dict[str, Dict[int, Dict[int, float]]] = defaultdict(lambda: defaultdict(dict))
    for item, values in data.items():
        for thread in sorted_threads:
            for n in sorted_N:
                mean = values[(values["threads"] == thread) & (values["N"] == n)]["time_s"].mean()
                s[item][thread][n] = mean

    # Etiquetas formateadas para el eje X (evita notación poco legible)
    x_labels = [f"{int(n):,}" for n in sorted_N]

    # Graficar por item (cada línea = thread)
    for item, values in s.items():
        for thread in sorted_threads:
            y = [values[thread].get(n, float('nan')) for n in sorted_N]
            plt.plot(sorted_N, y, label=f"{thread}") # type: ignore
        plt.xlabel("N") # type: ignore
        plt.ylabel("Time (s)") # type: ignore
        plt.title(f"{item} threads") # type: ignore
        plt.xticks(sorted_N, x_labels, rotation=45) # type: ignore
        plt.legend() # type: ignore
        plt.grid(True) # type: ignore
        plt.tight_layout() # type: ignore
        plt.show() # type: ignore

    # Graficar por thread (cada línea = item)
    for thread in sorted_threads:
        for item, values in s.items():
            y = [values[thread].get(n, float('nan')) for n in sorted_N]
            plt.plot(sorted_N, y, label=f"{item}") # type: ignore
        plt.xlabel("N") # type: ignore
        plt.ylabel("Time (s)") # type: ignore
        plt.title(f"Execution Time vs N thread {thread}") # type: ignore
        plt.xticks(sorted_N, x_labels, rotation=45) # type: ignore
        plt.legend() # type: ignore
        plt.grid(True) # type: ignore
        plt.tight_layout() # type: ignore
        plt.show() # type: ignore

def plotSpeedUp(data: Dict[str, pd.DataFrame]):
    threads: Set[int] = set()
    N: Set[int] = set()
    for _, values in data.items():
        threads.update(values["threads"])
        N.update(values["N"])
    sorted_threads = sorted(list(threads))
    sorted_N = sorted(list(N))
    # Construir mapping item->thread->N->speedup (usar thread 1 como base)
    s: Dict[str, Dict[int, Dict[int, float]]] = defaultdict(lambda: defaultdict(dict))
    for item, values in data.items():
        # calcular tiempos base para thread 1 por cada N
        base: Dict[int, float] = {}
        for n in sorted_N:
            base[n] = values[(values["threads"] == 1) & (values["N"] == n)]["time_s"].mean()
        for thread in sorted_threads:
            for n in sorted_N:
                mean = values[(values["threads"] == thread) & (values["N"] == n)]["time_s"].mean()
                if thread == 1:
                    # por convención, speedup de la misma configuración = 1
                    s[item][thread][n] = 1.0
                else:
                    b = base.get(n, float('nan'))
                    s[item][thread][n] = (mean / b) if (b and not pd.isna(b)) else float('nan')

    x_labels = [f"{int(n):,}" for n in sorted_N]
    threads_no1 = [t for t in sorted_threads if t != 1]

    # Graficar speedup por item (cada línea = thread > 1)
    for item, values in s.items():
        for thread in threads_no1:
            y = [values[thread].get(n, float('nan')) for n in sorted_N]
            plt.plot(sorted_N, y, label=f"{thread}") # type: ignore
        plt.xlabel("N") # type: ignore
        plt.ylabel("Speedup") # type: ignore
        plt.title(f"Speed Up {item}") # type: ignore
        plt.xticks(sorted_N, x_labels, rotation=45) # type: ignore
        plt.legend() # type: ignore
        plt.grid(True) # type: ignore
        plt.tight_layout() # type: ignore
        plt.show() # type: ignore
    
    for item, value in s.items():
        print(item)
        print(value)
    
                
        
        
            
results = path.join(path.dirname(path.abspath(__file__)), "data", "resultados_master.csv")
resultSeq = path.join(path.dirname(path.abspath(__file__)), "data", "resultados_master_seq.csv")
data = loadFromCsv(results)
dataSeq = loadFromCsv(resultSeq)
for itemSeq, valueSeq in dataSeq.items():
    name = itemSeq.split("_")[0].lower()
    for item, value in data.items():
        if item.lower().find(name) != -1:
            data[item] = pd.concat([valueSeq, value], ignore_index=True)
plotThreads(data)
plotSpeedUp(data)