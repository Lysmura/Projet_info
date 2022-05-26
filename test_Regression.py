from Statistiques.Statistiques import Statistiques 

X = [1,2,4,5,6,6,7,8,10]
Y = [4,6,7,8,8,9,9,1,11]
results = Statistiques(X, Y)
print (results.Results)
print(results.beta())
print(results.beta0())
print(results.Err())