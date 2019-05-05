import numpy as np
import sklearn
from sklearn.model_selection import GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier

from sklearn.externals import joblib


class Classify:

    def __init__(self):
        pass

    # def BP(self, data):
    #     pass

    def SVM(self, data):  # accuracy:0.867
        name = 'SVM'
        clf = sklearn.svm.SVC(C=24, gamma=0.05, kernel='rbf', decision_function_shape='ovo', probability=True)
        clf.fit(data[0], data[1])
        # 保存模型
        # joblib.dump(clf, "model/SVM_model.pkl")

        # 网格搜索找到最优模型参数
        # param_grid = {'C': np.arange(15, 25, 1), 'gamma': np.arange(0.04, 0.06, 0.01)}
        # grid_search = GridSearchCV(clf, param_grid, n_jobs = 8, verbose=1)
        # grid_search.fit(data[0], data[1])

        # best_parameters = grid_search.best_estimator_.get_params()
        # for para, val in list(best_parameters.items()):
        #     print(para, val)
        # clf = sklearn.svm.SVC(kernel='rbf', C=best_parameters['C'], gamma=best_parameters['gamma'], decision_function_shape='ovo')
        # clf.fit(data[0], data[1])

        return name, clf.score(data[2], data[3]), clf.predict(data[2])

    def KNN(self, data):  # accuracy:0.6222
        name = 'KNN'
        clf = KNeighborsClassifier(n_neighbors=6, weights='uniform',
                                   algorithm='auto', leaf_size=1)
        # ###################################网格搜索
        # k_range = list(range(1, 10))
        # leaf_range = list(range(1, 10))
        # weight_options = ['uniform', 'distance']
        # algorithm_options = ['auto', 'ball_tree', 'kd_tree', 'brute']
        # param_grid = dict(n_neighbors=k_range, weights=weight_options, algorithm=algorithm_options, leaf_size=leaf_range)

        # grid_search = GridSearchCV(clf, param_grid, n_jobs=8, cv=10, scoring='accuracy', verbose=1)
        # grid_search.fit(data[0], data[1])

        # best_parameters = grid_search.best_estimator_.get_params()
        # for para, val in list(best_parameters.items()):
        #     print(para, val)
        # clf = KNeighborsClassifier(n_neighbors=best_parameters['n_neighbors'], weights=best_parameters['weights'],
        #                            algorithm=best_parameters['algorithm'], leaf_size=best_parameters['leaf_size'])
        clf.fit(data[0], data[1])
        # joblib.dump(clf, "model/KNN_model.pkl")

        return name, clf.score(data[2], data[3]), clf.predict(data[2])

    def RandomForest(self, data):
        name = 'RandomForest'

        # param_grid1 = {'n_estimators':np.arange(55,80,1)}
        # param_grid2 = {'max_depth':np.arange(16,18,1), 'min_samples_split':np.arange(40,42,1)}
        # param_grid4 = {'max_features':np.arange(15,25,1)}
        # # param_grid3 = {'min_samples_split':np.arange(39,45,1), 'min_samples_leaf':np.arange(1,10,1)}
        # clf = RandomForestClassifier(n_estimators = 55, min_samples_split=40, 
        # min_samples_leaf=3, max_depth=20, max_features='sqrt', random_state=10)
        # grid_search = GridSearchCV(clf, param_grid4, n_jobs = 8, scoring='accuracy', cv=5)
        # grid_search.fit(data[0], data[1])

        # best_parameters = grid_search.best_estimator_.get_params()
        # for para, val in list(best_parameters.items()):
        #     print(para, val)
        clf = RandomForestClassifier(n_estimators=55, min_samples_split=40,
                                     min_samples_leaf=3, max_depth=20,
                                     max_features=16, random_state=10)
        clf.fit(data[0], data[1])
        # joblib.dump(clf, "model/RF_model.pkl")

        return name, clf.score(data[2], data[3]), clf.predict(data[2])

    def CCA(self, data):
        name = 'CCA'
