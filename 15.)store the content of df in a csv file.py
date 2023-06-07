import pandas as pd
nme = ["Alekha", "Ritu", "Piu", "Diya"] 
deg = ["MBA", "BCA", "M.Tech", "MBA"] 
scr = [90, 40, 80, 98] 
employee={'name': nme, 'degree': deg, 'score': scr}  
df = pd.DataFrame(employee) 
    
df.to_csv('15.csv') 