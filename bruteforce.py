import itertools
import csv
import time

NULL_NUMBER = "0.0"

MAX_BUDGET = "500.00"

   # O(N^2)
def sort_shares(shares):
    total_cost = 0.0
    best_shares = []
    total_profit = 0.0
    for shares_number in range(0,len(shares)-1):
        for combinaison in itertools.combinations(shares,shares_number):
                if sum(float(items[1]) for items in combinaison) <= float(MAX_BUDGET):
                    best_shares.append(combinaison)

    best_combinaison = max(best_shares, key=lambda x: sum(items[2] for items in x))

    total_cost = sum(float(x[1]) for x in best_combinaison)
    total_profit = sum(float(x[2]) for x in best_combinaison)

    print("coût total :",total_cost)
    print("profit total :",total_profit)
        
    for i, best in enumerate(best_combinaison,1):
        print(f"{i} - {best}") 

def loading_data(data):
    tab_data = []
    with open(data, newline="") as file:
        data_set = csv.reader(file, delimiter=',')
        for lignes in data_set:
            if lignes[0] == "name" or lignes[1] <= NULL_NUMBER or lignes[2] <= NULL_NUMBER:
                pass
            else:
                lignes[2] = (float(lignes[1])*float(lignes[2])/100)
                tab_data.append(lignes)
        sort_shares(tab_data) 

star = time.time()

if __name__== '__main__':
    # loading_data("./data/dataset.csv")  
    loading_data("./data/dataset2_Python+P7.csv")          

            

end = time.time()
elapsed = (end - star)
print(f"Temps d'exécution : {elapsed:.3} s")
