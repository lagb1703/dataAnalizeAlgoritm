import pandas as pd
# import numpy as np
import matplotlib.pyplot as plt
from os import path

hilosFold = "hilos"
linealFold = "lineal"
procesosFold = "procesos"
dirName = path.dirname(__file__)

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
            tradicionalHilos
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
            print("4")
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
            print("8")
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
            print("12")
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
            print("16")
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
i = 0
# while i < len(dataframes):
#     meanTradicional = dataframes[i].mean()
#     meanTradicionalHilos = dataframesHilos[i].mean()
#     plt.plot(meanTradicional, label="procesos") # type: ignore
#     plt.plot(meanLibro, label="hilos") # type: ignore
#     plt.plot(tradicionalSecuencial.mean(), label="secuencial") # type: ignore
#     plt.title(f"tradicional procesos {(i+1)*4} vs hilos {(i+1)*4} vs secuencial") # type: ignore
#     plt.xlabel("n") # type: ignore
#     plt.ylabel("t promedio") # type: ignore
#     plt.legend() # type: ignore
#     plt.grid(True) # type: ignore
#     plt.show() # type: ignore
#     i+=1
    
while i < len(dataframes):
    meanTradicional = dataframesLibro[i].mean()
    meanTradicionalHilos = dataframesLibroHilos[i].mean()
    plt.plot(meanTradicional, label="procesos") # type: ignore
    plt.plot(meanLibro, label="hilos") # type: ignore
    plt.plot(tradicionalSecuencial.mean(), label="secuencial") # type: ignore
    plt.title(f"subdivisión procesos {(i+1)*4} vs hilos {(i+1)*4} vs secuencial") # type: ignore
    plt.xlabel("n") # type: ignore
    plt.ylabel("t promedio") # type: ignore
    plt.legend() # type: ignore
    plt.grid(True) # type: ignore
    plt.show() # type: ignore
    i+=1