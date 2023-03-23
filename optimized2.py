import csv
import time

NULL_NUMBER = "0.0"

MAX_BUDGET = "500.0"

   # O(Nlogn)
def sort_shares(stocks):
    best_shares = []
    shares = sorted(stocks, key=lambda profit:float(profit[2]),reverse=True)
    for i in range(0,len(shares)):
        if float(shares[i][1]) < float(shares[i][2]):
            shares[i][2] = (float(shares[i][1])*float(shares[i][2])/100)
            best_shares.append(shares[i])

        while sum(float(items[1]) for items in best_shares) > float(MAX_BUDGET):
            best_shares.pop()

    for i, best in enumerate(best_shares,1):
        print(f"{i} - {best}") 
    total_cost = sum(float(x[1]) for x in best_shares)
    total_profit = sum(float(x[2]) for x in best_shares)

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
                tab_data.append(lignes)
        sort_shares(tab_data) 

star = time.time()

if __name__== '__main__':
    # loading_data("./data/dataset1_Python+P7.csv")
    loading_data("./data/dataset2_Python+P7.csv")          

end = time.time()
elapsed = (end - star)
print(f"Temps d'exécution : {elapsed:.3} s")
