import numpy as np 
from numpy import log,dot,exp,shape
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification

X,y = make_classification(n_features=4)
from sklearn.model_selection import train_test_split 



class LogidticRegression:
    
    def __standardize(self, X_tr):
        """
            Standardize the train dataset input 
        Args:
            X_tr (_type_): _description_

        Returns:
            _type_: _description_
        """
        for i in range(shape(X_tr)[1]):
            X_tr[:,i] = (X_tr[:,i] - np.mean(X_tr[:,i]))/np.std(X_tr[:,i])
        return X_tr

    def __sigmoid(self,z):
        sig = 1/(1+exp(-z))
        return sig

    def __initialize(self,X):
        weights = np.zeros((shape(X)[1]+1,1))
        X = np.c_[np.ones((shape(X)[0],1)),X]
        return weights,X

    def fit(self,X,y,alpha=0.001,iter=400):
        """fit the model

        Args:
            X (np.Array): train data
            y (np.Array): target data
            alpha (float, optional): learning rate. Defaults to 0.001.
            iter (int, optional): iteration. Defaults to 400.

        Returns:
            _type_: _description_
        """
        
        X = self.__standardize(X)
        weights,X = self.__initialize(X)
        def cost(theta):
            z = dot(X,theta)
            cost0 = y.T.dot(log(self.__sigmoid(z)))
            cost1 = (1-y).T.dot(log(1-self.__sigmoid(z)))
            cost = -((cost1 + cost0))/len(y)
            return cost
        cost_list = np.zeros(iter,)
        for i in range(iter):
            weights = weights - alpha*dot(X.T,self.__sigmoid(dot(X,weights))-np.reshape(y,(len(y),1)))
            cost_list[i] = cost(weights)
        self.weights = weights
        return cost_list

    def predict(self,X):
        X = self.__standardize(X)
        z = dot(self.__initialize(X)[1],self.weights)
        lis = []
        for i in self.__sigmoid(z):
            if i>0.5:
                lis.append(1)
            else:
                lis.append(0)
        return lis

# f1_score function 
def F1_score(y,y_hat):
        tp,tn,fp,fn = 0,0,0,0
        for i in range(len(y)):
            if y[i] == 1 and y_hat[i] == 1:
                tp += 1
            elif y[i] == 1 and y_hat[i] == 0:
                fn += 1
            elif y[i] == 0 and y_hat[i] == 1:
                fp += 1
            elif y[i] == 0 and y_hat[i] == 0:
                tn += 1
        precision = tp/(tp+fp)
        recall = tp/(tp+fn)
        f1_score = 2*precision*recall/(precision+recall)
        return f1_score


    
    