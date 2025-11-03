import pandas as pd
# import numpy as np
import matplotlib.pyplot as plt
from os import path
from collections import defaultdict
from typing import List, Dict, Set

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
    s: Dict[str, Dict[int, List[float]]] = defaultdict(lambda: defaultdict(list))
    for item, values in data.items():
        for thread in sorted_threads:
            for n in sorted_N:
                mean = values[values["threads"] == thread][values["N"] == n]["time_s"].mean()
                s[item][thread].append(mean)
    for item, values in s.items():
        for thread in sorted_threads:
            plt.plot(sorted_N, values[thread], label=f"{thread}") # type: ignore
        plt.xlabel("N") # type: ignore
        plt.ylabel("Time (s)") # type: ignore
        plt.title(f"{item} threads") # type: ignore
        plt.legend() # type: ignore
        plt.grid(True) # type: ignore
        plt.show() # type: ignore
    for thread in sorted_threads:
        for item, values in s.items():
            values[thread]
            plt.plot(sorted_N, values[thread], label=f"{item}") # type: ignore
        plt.xlabel("N") # type: ignore
        plt.ylabel("Time (s)") # type: ignore
        plt.title(f"Execution Time vs N thread {thread}") # type: ignore
        plt.legend() # type: ignore
        plt.grid(True) # type: ignore
        plt.show() # type: ignore
        
                
        
        
            
results = path.join(path.dirname(path.abspath(__file__)), "data", "resultados_master.csv")
data = loadFromCsv(results)
plotThreads(data)