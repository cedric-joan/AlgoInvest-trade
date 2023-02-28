import csv



def sortData_1(data):
    # boucle sur chaque i du tableau
    for i in range(1, len(data)):
        print(data[1][2])
        # boucle sur
        for shares in data:

            if shares[1] == "price" or shares[1] <= "0.0":
                pass
            else:
                shares[2] = format(float(shares[2])/float(shares[1])*100, ".2f")
    
    # print(shares)

        # min_index = 0
        # number_min = 


            # if list_pourcent[i] < index:
            #     print(list_pourcent)

            #     min_number = data[i] 
            #     min_index = i
        # data[min_index] = data[i]
        # data[i] = min_number





tab_data = []
with open("./data/dataset1_Python+P7.csv", newline="") as file:
    data_set = csv.reader(file, delimiter=',')
    for lignes in data_set:
        tab_data.append(lignes)
    sortData_1(tab_data)   
        

