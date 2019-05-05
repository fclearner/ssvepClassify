import numpy as np
from sklearn.decomposition import pca


class Feature:

    def __init__(self):
        pass

    def PCA(self, data):
        model = pca.PCA(n_components=1).fit(data)   # 拟合数据，n_components定义要降的维度
        featuredData = model.transform(data)

        return featuredData
