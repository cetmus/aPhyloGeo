import subprocess
import pandas as pd
import os
from pipeline import getDissimilaritiesMatrix

def print_menu():
    print('====================================================================================================================')
    print("Before running this script, please make sure there is a .csv file containing all the data to analyze in this repo")
    print('====================================================================================================================')

def get_csv_file_name(correct = False):
    while not correct:
        file_name = input("Please enter the name of the csv file: ")
        # valide que le nom existe vraiment
        try:
            pd.read_csv(file_name)
        except Exception:
            print("Could not find the csv file with this name or the file is empty.")
        else:
            correct = True
    return file_name

def get_columns_names(file_name):
    columns = pd.read_csv(file_name).columns
    names = [] # liste qui va contenir les noms des colonnes a traiter
    while True:
        number = input("Number of trees to create: \n")
        number = int(number)
        if number < 1:
            print("Error, the number of trees cannot be below 1.")
            continue
        else:
            specimen = input("Please enter the name of the colum containing the specimens names: ")
            valide = specimen in columns
            while not valide:
                print("Error, this column name does not exist.")
                name = input("Please enter the name of the colum containing the specimens names: ")
                valide = name in columns
            names.append(specimen)
            for i in range(number):
                name = input("Please enter the name of the column to analyze in your csv file (" + str(i+1) + "): ")
                valide = name in columns
                while not valide:
                    print("Error, this column name does not exist.")
                    name = input("Please enter the name of the column to analyze in your csv file (" + str(i+1) + "): ")
                    valide = name in columns
                names.append(name)
            return names

def create_tree(file_name, names):
    for i in range(1, len(names)):
        getDissimilaritiesMatrix(file_name, names[0], names[i], "infile") # liste a la position 0 contient les noms des specimens
        os.system("./exec/neighbor < input_matrix.txt")
        os.system("mv outtree intree; rm infile outfile")
        os.system("./exec/consense < input_matrix.txt" )
        newick_file = names[i] + "_newick"
        tree_file = names[i] + "_consensus_tree"
        subprocess.call(["mv", "outfile", tree_file])
        subprocess.call(["mv", "outtree", newick_file])




if __name__ == '__main__':
    try:
        print_menu()
        file_name = get_csv_file_name()
        names = get_columns_names(file_name)
        create_tree(file_name, names)
    except:
        print("An error has occured.")
    else:
        subprocess.call(["rm", "intree"])



            
      
