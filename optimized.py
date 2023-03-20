import csv
import time

NULL_NUMBER = "0.0"

MAX_BUDGET = "500.0"

   # O(N^2)
def sort_shares(stocks):
    shares_max_cost = [items for items in stocks if items[1] <= MAX_BUDGET]
    best_list_shares = []
    shares = sorted(shares_max_cost, key=lambda profit:float(profit[2]),reverse=True)
    best_list_shares.append(shares[0])
    for i in range(1,len(shares)):
        if (float(best_list_shares[0][1]) + float(shares[i][1])) > float(MAX_BUDGET):
            pass
        else :
            best_list_shares.append(shares[i])

        while sum(float(items[1]) for items in best_list_shares) > float(MAX_BUDGET):
            best_list_shares.pop()

    for i, best in enumerate(best_list_shares,1):
        print(f"{i} - {best}") 
    total_cost = sum(float(x[1]) for x in best_list_shares)
    total_profit = sum(float(x[2]) for x in best_list_shares)

    print("coût total :",total_cost)
    print("profit total :",total_profit)
        

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
    # loading_data("./data/datashares.csv")          
    loading_data("./data/dataset1_Python+P7.csv")
    # loading_data("./data/dataset2_Python+P7.csv")          

end = time.time()
elapsed = (end - star)
print(f"Temps d'exécution : {elapsed:.3} s")
