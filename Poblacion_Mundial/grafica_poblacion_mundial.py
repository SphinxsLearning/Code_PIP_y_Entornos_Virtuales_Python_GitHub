""" Realiza un programa que grafique el World Population percentage """

import csv
import matplotlib.pyplot as plt

def run():
    list_continents = ["south america", "north america", "central america", "europe", "asia", "africa", "oceania"]
    while True:
        continent = input("Type continent: ").lower()
        if continent in list_continents:
            break
    continent = continent.title()
    list_countries_dict = get_list_countries_dict("./data.csv")
    list_labels = get_labels(continent, list_countries_dict)
    list_values = get_values(continent, list_countries_dict)
    Generar_Grafica_Pie(continent, list_labels, list_values)

def get_list_countries_dict(path):
    with open(path, "r") as countries_data:
        reader = csv.reader(countries_data, delimiter=",")
        header = next(reader)
        data_countries_list = []
        for row in reader:
            country_data_dict = {key:value for (key, value) in zip(header, row)}
            data_countries_list.append(country_data_dict)
    return data_countries_list

def get_labels(name_continent, list_countries_dict):
    list_labels = []
    for country_dict in list_countries_dict:
        if country_dict["Continent"] == name_continent:
            list_labels.append(country_dict["Country/Territory"])
    return list_labels

def get_values(name_continent, list_countries_dict):
    list_values = []
    for country_dict in list_countries_dict:
        if country_dict["Continent"] == name_continent:
            list_values.append(float(country_dict["World Population Percentage"]))
    return list_values

def Generar_Grafica_Pie(name_continent, labels, values):
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    ax.axis("equal")
    plt.savefig(f"./Graficas_continentes/{name_continent}.png")
    plt.close()

if __name__ == "__main__":
    run()