import pandas as pd
# import numpy as np
import matplotlib.pyplot as plt
from os import path
from typing import List

hilosFold = "hilos"
linealFold = "lineal"
procesosFold = "procesos"
dirName = path.dirname(__file__)

def plotVsDataframes(datas1: List[pd.DataFrame], datas2: List[pd.DataFrame], name: List[str]):
    i = 0
    while i < len(datas1):
        meanData1 = datas1[i].mean()
        meanData2 = datas2[i].mean()
        plt.plot(meanData1, label=name[1]) # type: ignore
        plt.plot(meanData2, label=name[2]) # type: ignore
        plt.title(f"{name[0]} {(i+1)*4}") # type: ignore
        plt.xlabel("n") # type: ignore
        plt.ylabel("t promedio") # type: ignore
        plt.legend() # type: ignore
        plt.grid(True) # type: ignore
        plt.show() # type: ignore
        i += 1

def plotAll(datas1: List[pd.DataFrame], data2: pd.DataFrame, name: List[str]):
    meanData2 = data2.mean()
    plt.plot(meanData2, label="secuencial") # type: ignore
    i = 0
    while i < len(datas1):
        meanData1 = datas1[i].mean()
        plt.plot(meanData1, label=f"{name[1]} {(i+1)*4}") # type: ignore
        i += 1
    plt.title(f"{name[0]}") # type: ignore
    plt.xlabel("n") # type: ignore
    plt.ylabel("t promedio") # type: ignore
    plt.legend() # type: ignore
    plt.grid(True) # type: ignore
    plt.show() # type: ignore
    i = 0
    while i < len(datas1):
        meanData1 = datas1[i].mean()
        series = pd.Series({
            "1000": meanData2["1000"] / meanData1["1000"],
            "1500": meanData2["1500"] / meanData1["1500"],
            "2000": meanData2["2000"] / meanData1["2000"],
            "2500": meanData2["2500"] / meanData1["2500"],
            "3000": meanData2["3000"] / meanData1["3000"],
            "3500": meanData2["3500"] / meanData1["3500"],
            "4000": meanData2["4000"] / meanData1["4000"],
        })
        print(series)
        plt.plot(series, label=f"{(i+1)*4}") # type: ignore
        i += 1
    plt.title(f"{name[0]}") # type: ignore
    plt.xlabel("n") # type: ignore
    plt.ylabel("speedup") # type: ignore
    plt.legend() # type: ignore
    plt.grid(True) # type: ignore
    plt.show() # type: ignore
    

tradicionalSecuencial:pd.DataFrame = pd.read_csv(path.join(dirName, linealFold, "tradicional.csv")) # type: ignore
libroSecuencial:pd.DataFrame = pd.read_csv(path.join(dirName, linealFold, "libro.csv")) # type: ignore

meanTradicional = tradicionalSecuencial.mean()
meanLibro = libroSecuencial.mean()

tradicionalHilos:pd.DataFrame = pd.read_csv(path.join(dirName, hilosFold, "tradicional.csv")) # type: ignore
libroHilos:pd.DataFrame = pd.read_csv(path.join(dirName, hilosFold, "libro.csv")) # type: ignore

dataframesHilos = [
    pd.DataFrame({"1000": [], "1500": [], "2000": [], "2500": [], "3000": [], "3500": [], "4000": []}),
    pd.DataFrame({"1000": [], "1500": [], "2000": [], "2500": [], "3000": [], "3500": [], "4000": []}),
    pd.DataFrame({"1000": [], "1500": [], "2000": [], "2500": [], "3000": [], "3500": [], "4000": []}),
    pd.DataFrame({"1000": [], "1500": [], "2000": [], "2500": [], "3000": [], "3500": [], "4000": []}),
]

dataframesLibroHilos = [
    pd.DataFrame({"1000": [], "1500": [], "2000": [], "2500": [], "3000": [], "3500": [], "4000": []}),
    pd.DataFrame({"1000": [], "1500": [], "2000": [], "2500": [], "3000": [], "3500": [], "4000": []}),
    pd.DataFrame({"1000": [], "1500": [], "2000": [], "2500": [], "3000": [], "3500": [], "4000": []}),
    pd.DataFrame({"1000": [], "1500": [], "2000": [], "2500": [], "3000": [], "3500": [], "4000": []}),
]

for index, i in enumerate(tradicionalHilos['0']):
    data: pd.DataFrame | None = None
    match i:
        case 4:
            data = dataframesHilos[0]
            data.loc[len(data)] =(
                [
                    tradicionalHilos["1000"][index], 
                    tradicionalHilos["1500"][index],
                    tradicionalHilos["2000"][index],
                    tradicionalHilos["2500"][index],
                    tradicionalHilos["3000"][index],
                    tradicionalHilos["3500"][index],
                    tradicionalHilos["4000"][index],
                ]
            )
        case 8:
            data = dataframesHilos[1]
            data.loc[len(data)] =(
                [
                    tradicionalHilos["1000"][index], 
                    tradicionalHilos["1500"][index],
                    tradicionalHilos["2000"][index],
                    tradicionalHilos["2500"][index],
                    tradicionalHilos["3000"][index],
                    tradicionalHilos["3500"][index],
                    tradicionalHilos["4000"][index],
                ]
            )
        case 12:
            data = dataframesHilos[2]
            data.loc[len(data)] =(
                [
                    tradicionalHilos["1000"][index], 
                    tradicionalHilos["1500"][index],
                    tradicionalHilos["2000"][index],
                    tradicionalHilos["2500"][index],
                    tradicionalHilos["3000"][index],
                    tradicionalHilos["3500"][index],
                    tradicionalHilos["4000"][index],
                ]
            )
        case 16:
            data = dataframesHilos[3]
            data.loc[len(data)] =(
                [
                    tradicionalHilos["1000"][index], 
                    tradicionalHilos["1500"][index],
                    tradicionalHilos["2000"][index],
                    tradicionalHilos["2500"][index],
                    tradicionalHilos["3000"][index],
                    tradicionalHilos["3500"][index],
                    tradicionalHilos["4000"][index],
                ]
            )
        case _:pass
        
for index, i in enumerate(libroHilos['0']):
    match i:
        case 4:
            data = dataframesLibroHilos[0]
            data.loc[len(data)] =(
                [
                    libroHilos["1000"][index], 
                    libroHilos["1500"][index],
                    libroHilos["2000"][index],
                    libroHilos["2500"][index],
                    libroHilos["3000"][index],
                    libroHilos["3500"][index],
                    libroHilos["4000"][index],
                ]
            )
        case 8:
            data = dataframesLibroHilos[1]
            data.loc[len(data)] =(
                [
                    libroHilos["1000"][index], 
                    libroHilos["1500"][index],
                    libroHilos["2000"][index],
                    libroHilos["2500"][index],
                    libroHilos["3000"][index],
                    libroHilos["3500"][index],
                    libroHilos["4000"][index],
                ]
            )
        case 12:
            data = dataframesLibroHilos[2]
            data.loc[len(data)] =(
                [
                    libroHilos["1000"][index], 
                    libroHilos["1500"][index],
                    libroHilos["2000"][index],
                    libroHilos["2500"][index],
                    libroHilos["3000"][index],
                    libroHilos["3500"][index],
                    libroHilos["4000"][index],
                ]
            )
        case 16:
            data = dataframesLibroHilos[3]
            data.loc[len(data)] =(
                [
                    libroHilos["1000"][index], 
                    libroHilos["1500"][index],
                    libroHilos["2000"][index],
                    libroHilos["2500"][index],
                    libroHilos["3000"][index],
                    libroHilos["3500"][index],
                    libroHilos["4000"][index],
                ]
            )
        case _:pass
i = 0

tradicionalProcesos:pd.DataFrame = pd.read_csv(path.join(dirName, procesosFold, "tradicional.csv")) # type: ignore
libroProcesos:pd.DataFrame = pd.read_csv(path.join(dirName, procesosFold, "libro.csv")) # type: ignore

dataframes = [
    pd.DataFrame({"1000": [], "1500": [], "2000": [], "2500": [], "3000": [], "3500": [], "4000": []}),
    pd.DataFrame({"1000": [], "1500": [], "2000": [], "2500": [], "3000": [], "3500": [], "4000": []}),
    pd.DataFrame({"1000": [], "1500": [], "2000": [], "2500": [], "3000": [], "3500": [], "4000": []}),
    pd.DataFrame({"1000": [], "1500": [], "2000": [], "2500": [], "3000": [], "3500": [], "4000": []}),
]

dataframesLibro = [
    pd.DataFrame({"1000": [], "1500": [], "2000": [], "2500": [], "3000": [], "3500": [], "4000": []}),
    pd.DataFrame({"1000": [], "1500": [], "2000": [], "2500": [], "3000": [], "3500": [], "4000": []}),
    pd.DataFrame({"1000": [], "1500": [], "2000": [], "2500": [], "3000": [], "3500": [], "4000": []}),
    pd.DataFrame({"1000": [], "1500": [], "2000": [], "2500": [], "3000": [], "3500": [], "4000": []}),
]

for index, i in enumerate(tradicionalProcesos['0']):
    data: pd.DataFrame | None = None
    match i:
        case 4:
            data = dataframes[0]
            data.loc[len(data)] =(
                [
                    tradicionalProcesos["1000"][index], 
                    tradicionalProcesos["1500"][index],
                    tradicionalProcesos["2000"][index],
                    tradicionalProcesos["2500"][index],
                    tradicionalProcesos["3000"][index],
                    tradicionalProcesos["3500"][index],
                    tradicionalProcesos["4000"][index],
                ]
            )
        case 8:
            data = dataframes[1]
            data.loc[len(data)] =(
                [
                    tradicionalProcesos["1000"][index], 
                    tradicionalProcesos["1500"][index],
                    tradicionalProcesos["2000"][index],
                    tradicionalProcesos["2500"][index],
                    tradicionalProcesos["3000"][index],
                    tradicionalProcesos["3500"][index],
                    tradicionalProcesos["4000"][index],
                ]
            )
        case 12:
            data = dataframes[2]
            data.loc[len(data)] =(
                [
                    tradicionalProcesos["1000"][index], 
                    tradicionalProcesos["1500"][index],
                    tradicionalProcesos["2000"][index],
                    tradicionalProcesos["2500"][index],
                    tradicionalProcesos["3000"][index],
                    tradicionalProcesos["3500"][index],
                    tradicionalProcesos["4000"][index],
                ]
            )
        case 16:
            data = dataframes[3]
            data.loc[len(data)] =(
                [
                    tradicionalProcesos["1000"][index], 
                    tradicionalProcesos["1500"][index],
                    tradicionalProcesos["2000"][index],
                    tradicionalProcesos["2500"][index],
                    tradicionalProcesos["3000"][index],
                    tradicionalProcesos["3500"][index],
                    tradicionalProcesos["4000"][index],
                ]
            )
        case _:pass
        
for index, i in enumerate(libroProcesos['0']):
    match i:
        case 4:
            data = dataframesLibro[0]
            data.loc[len(data)] =(
                [
                    libroProcesos["1000"][index], 
                    libroProcesos["1500"][index],
                    libroProcesos["2000"][index],
                    libroProcesos["2500"][index],
                    libroProcesos["3000"][index],
                    libroProcesos["3500"][index],
                    libroProcesos["4000"][index],
                ]
            )
        case 8:
            data = dataframesLibro[1]
            data.loc[len(data)] =(
                [
                    libroProcesos["1000"][index], 
                    libroProcesos["1500"][index],
                    libroProcesos["2000"][index],
                    libroProcesos["2500"][index],
                    libroProcesos["3000"][index],
                    libroProcesos["3500"][index],
                    libroProcesos["4000"][index],
                ]
            )
        case 12:
            data = dataframesLibro[2]
            data.loc[len(data)] =(
                [
                    libroProcesos["1000"][index], 
                    libroProcesos["1500"][index],
                    libroProcesos["2000"][index],
                    libroProcesos["2500"][index],
                    libroProcesos["3000"][index],
                    libroProcesos["3500"][index],
                    libroProcesos["4000"][index],
                ]
            )
        case 16:
            data = dataframesLibro[3]
            data.loc[len(data)] =(
                [
                    libroProcesos["1000"][index], 
                    libroProcesos["1500"][index],
                    libroProcesos["2000"][index],
                    libroProcesos["2500"][index],
                    libroProcesos["3000"][index],
                    libroProcesos["3500"][index],
                    libroProcesos["4000"][index],
                ]
            )
        case _:pass
plt.plot(meanLibro, label="subdivisión") # type: ignore
plt.plot(meanTradicional, label="tradicional") # type: ignore
plt.title(f"secuencial") # type: ignore
plt.xlabel("n") # type: ignore
plt.ylabel("t promedio") # type: ignore
plt.legend() # type: ignore
plt.grid(True) # type: ignore
plt.show() # type: ignore
plotAll(dataframes, tradicionalSecuencial, ["Proceso", "Proceso "])
plotAll(dataframesHilos, tradicionalSecuencial, ["Hilo", "Hilo "])
plotVsDataframes(dataframes, dataframesLibro, ["Tradicional vs Subdivisión hilos:", "tradicional", "subdivisión"])
plotVsDataframes(dataframesHilos, dataframesLibroHilos, ["Tradicional vs Subdivisión hilos:", "tradicional", "subdivisión"])