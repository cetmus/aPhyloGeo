import subprocess
import os
import re
import pandas as pd
from scripts import reference

def menuGetTrees():
    names = []
    while True:
        count = input("How many climatic data tree will be used?: ")
        if not count.isnumeric():
            print("This is not a number.")
        elif int(count) < 1:
            print("The number cannot be lower than 1.")
        else:
            # VALIDER LE FORMAT NEWICK??
            for i in range(int(count)):
                try:
                    name = input("Name of the tree file (" + str(i+1) + "): " )
                    f = open(name, "r")
                    names.append(name)
                except:
                    print("This file does not exist or is empty.")
            break
    return names


# def getBootstrapThreshold():



def menu(option=0):
    names = menuGetTrees()
    # print('===============================================')
    # print('Please select an option among the following: ')
    # print('===============================================')
    # print('1. Use the whole DNA sequences')
    # print('2. Study specific genes of SARS-CoV-2')
    
    # while option != '1' or option != '2':
    #     option = input("Please enter 1 or 2: ")
    #     if option == '1':
    #         # faire un loop ici au cas ou il rentre nimporte quoi
    #         option = input("Use a sliding window?[y/n]\n")
    #         while True:
    #             if option == 'Y' or option =='y': # ici l'utilisateur choisit la fenetre coulissante
    #                 size = input('Window size:\n')
    #                 if int(size) > 0:
    #                     print('Yes')
    #                     break
    #             elif option == 'n' or option == 'N': # ici, pas de fenetre coulissante on peut analyser toutes les sequences
    #                 reference.getReferenceTree()
    #                 break
    #     elif option == '2':
    #         print("ok2")
    #         break
    #     else: 
    #         print('This is not a valid option.')


def useWholeSequence(option=0):
    option = input("Use a sliding window?[y/n]\n")
    while True:
        if option == 'Y' or option == 'y':  # ici l'utilisateur choisit la fenetre coulissante
            size = input('Window size:\n')
            if int(size) > 0:
                print('Yes')
                break
        elif option == 'n' or option == 'N':  # ici, pas de fenetre coulissante on peut analyser toutes les sequences
            reference.get_reference_tree()
            break


def changeNameSequences():
    sequences_file = open("output/reference_gene/reference_gene.fasta", "r")
    list_of_lines = sequences_file.readlines()
    for index in range(len(list_of_lines)):
        if list_of_lines[index].startswith(">"):
            splitted_line = list_of_lines[index].split("/")
            name = ">" + splitted_line[2] + "\n"
            list_of_lines[index] = name

    sequences_file = open("output/reference_gene/reference_gene.fasta", "w")
    sequences_file.writelines(list_of_lines)
    sequences_file.close()


def getGene(gene, pattern): 
    sequences_file = open("output/reference_gene/reference_gene.fasta", "r").read()
    list_of_sequences = sequences_file.split(">")
    s = pattern
    directory_name = gene + "_gene"
    file_name = gene + "_gene.fasta"
    path = os.path.join("output", directory_name, file_name)
    new_file = open(path, "w")
    for index in range(len(list_of_sequences)):
        if list_of_sequences[index] == "":
            continue
        name = list_of_sequences[index].split("\n")[0]
        gene_sequence = list_of_sequences[index].replace("\n", "")
        gene_sequence = (re.search(s, gene_sequence).group())
        new_file.writelines(">" + name + "\n")
        new_file.writelines(gene_sequence + "\n")

    new_file.close()

def alignSequences(gene):
    sequences_file_name = gene + '_gene.fasta'
    directory_name = gene + '_gene'
    file_path = os.path.join('output', directory_name, sequences_file_name)
    subprocess.call(["./exec/muscle", "-in", file_path, "-physout", "infile", "-maxiters", "1", "-diags"])


def createBoostrap(gene):
    aligned_gene_file_name = 'aligned_' + gene + '_gene'
    directory_name = gene + '_gene'
    input_file_path = os.path.join('output', directory_name, aligned_gene_file_name)
    subprocess.call("./exec/seqboot")
    # subprocess.call(["mv", "infile", input_file_path])
    subprocess.call(["mv", "outfile", "infile"])


def getDissimilaritiesMatrix(nom_fichier_csv,column_with_specimen_name, column_to_search, outfile_name):
    df = pd.read_csv(nom_fichier_csv)
    # creation d'une liste contenant les noms des specimens et les temperatures min
    meteo_data = df[column_to_search].tolist()
    nom_var = df[column_with_specimen_name].tolist()
    nbr_seq = len(nom_var)
    # ces deux valeurs seront utiles pour la normalisation
    max_value = 0  
    min_value = 0

    # premiere boucle qui permet de calculer une matrice pour chaque sequence
    temp_tab = []
    for e in range(nbr_seq):
        # une liste qui va contenir toutes les distances avant normalisation
        temp_list = []
        for i in range(nbr_seq):        
            maximum = max(float(meteo_data[e]), float(meteo_data[i]))
            minimum = min(float(meteo_data[e]), float(meteo_data[i]))
            distance = maximum - minimum
            temp_list.append(float("{:.6f}".format(distance)))

        # permet de trouver la valeur maximale et minimale pour la donnee meteo et ensuite d'ajouter la liste temporaire a un tableau
        if max_value < max(temp_list):
            max_value = max(temp_list)
        if min_value > min(temp_list):
            min_value = min(temp_list)
        temp_tab.append(temp_list)
    
    # ecriture des matrices normalisees dans les fichiers respectifs
    with open(outfile_name, "w") as f:
        f.write("   " + str(len(nom_var)) + "\n")
        for j in range(nbr_seq):
            f.write(nom_var[j])
            # petite boucle pour imprimer le bon nbr d'espaces
            for espace in range(11-len(nom_var[j])):
                f.write(" ")
            for k in range(nbr_seq):
                # la normalisation se fait selon la formule suivante: (X - Xmin)/(Xmax - Xmin)
                f.write("{:.6f}".format((temp_tab[j][k] - min_value)/(max_value - min_value)) + " ")
            f.write("\n")
    subprocess.call(["rm", "outfile"]) # clean up


def createDistanceMatrix(gene):
    bootstrap_file_name = 'bootstrap_' + gene + '_gene'
    directory_name = gene + '_gene'
    input_file_path = os.path.join('output', directory_name, bootstrap_file_name)
    subprocess.call("./exec/dnadist")
    # subprocess.call(["cp", "infile", input_file_path])
    subprocess.call(["mv", "outfile", "infile"])

def createUnrootedTree(gene):
    distance_matrix_file_name = 'distance_matrix_' + gene + '_gene'
    directory_name = gene + '_gene'
    output_file_name = 'unrooted_tree_'+ gene + '_gene'
    input_file_path = os.path.join('output', directory_name, distance_matrix_file_name)
    output_file_path = os.path.join(
        'output', directory_name, output_file_name)
    subprocess.call("./exec/neighbor")
    # subprocess.call(["mv", "infile", input_file_path])
    subprocess.call(["mv", "outtree", "intree"])
    # subprocess.call(["mv", "outfile", output_file_path])


def createConsensusTree(gene):
    unrooted_tree_data_file_name = 'unrooted_tree_data_'+ gene + '_gene'
    outtree_file_name = 'consensus_tree_' + gene + '_gene'
    output_file_name = 'consensus_tree_data_' + gene + '_gene'
    directory_name = gene + '_gene'
    intree_file_path = os.path.join(
        'output', directory_name, unrooted_tree_data_file_name)
    outtree_file_path = os.path.join('output', directory_name, outtree_file_name)
    output_file_path = os.path.join('output', directory_name, output_file_name)
    subprocess.call("./exec/consense")
    # subprocess.call(["mv", "intree", intree_file_path])
    subprocess.call(["mv", "outtree", output_file_path])
    subprocess.call(["mv", "outfile", outtree_file_path])


if __name__ == '__main__':
    menu()
