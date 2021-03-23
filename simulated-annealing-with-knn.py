import math
import pandas as pd
import numpy as np 
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score

df = pd.read_csv("divorce.csv",sep = ";")

y = df.Class.values
x_data = df.drop(["Class"], axis =1)

#%% normalization with min-max normalization
x_data = (x_data - np.min(x_data))/(np.max(x_data)-np.min(x_data))

#%% Changing column names of x dataframe with 0 and 1
Z = np.random.random(54) > 0.5
Z = Z.astype(int).astype(str)

x_data.columns = Z

# Taking only 1's of feature for knn
x = x_data.loc[:,["1"]]

#%% train test split
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size = 0.25)

#%% Appliying the KNN
knn = KNeighborsClassifier(n_neighbors=5)
# knn.fit(x_train,y_train.values.ravel())
# print("test accuracy: ",knn.score(x_test,y_test))
# knn_score = knn.score(x_test,y_test)

#%% K-fold CV K = 5
accuracies = cross_val_score(estimator=knn,X = x_train, y = y_train.ravel(), cv = 5)
acc = np.mean(accuracies)
print("average accuracy: ",np.mean(accuracies))
print("average std: ",np.std(accuracies))


#%% neigbor parameter has randomly selected 1's
def get_neighbors(a):
    Z = np.random.random(54) > 0.5
    Z = Z.astype(int).astype(str)

    a.columns = Z
    a = a.xs('1', axis=1)  
    return a    

def get_cost(x,y):
    x_train, x_test, y_train, y_test = train_test_split(x,y,test_size = 0.25)
    knn = KNeighborsClassifier(n_neighbors=3)
    accuracies = cross_val_score(estimator=knn,X = x_train, y = y_train.ravel(), cv = 5)
    return np.mean(accuracies)
#%% Simulated Annealing
# param = dataframe with 0's and 1's
def simulated_annealing(param, initial_state, y):
    """Peforms simulated annealing to find a solution"""
     
    initial_temp = 4
    final_temp = .1
    alpha = 0.01
    
    current_temp = initial_temp

    # Start by initializing the current state with the initial state
    #initial_state is knn score of df with only 1's selected
    current_state = initial_state    
    solution = current_state

    while current_temp >=  final_temp:
        neighbor = get_neighbors(param)
        # Check if neighbor is best so far
        cost_diff = get_cost(neighbor,y)

        if cost_diff < math.exp(cost_diff / current_temp):
            solution = cost_diff
        # decrement the temperature
        current_temp -= alpha
    return solution
#%% Print the score with simulated annealing
print("score", simulated_annealing(x_data, acc, y))
