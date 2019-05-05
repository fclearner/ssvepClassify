import os
import math

import scipy.io as sio
import matplotlib.pyplot as plt
import numpy as np
import Preprocess
import Classify
import FeatureExtraction
import TestInterface

from sklearn.utils import shuffle


class SSVEP:
    def __init__(self, fList, samplingRate, samplingTime, timeWindow):
        self.fList = fList  # 频率列表
        self.fs = samplingRate  # 采样率
        self.samplingTime = samplingTime  # 采样总时间
        self.timeWindow = timeWindow  # 时间窗口

    def Filtering(self, dataList):  # 滤波
        result_list = []
        for i in range(len(dataList[0])):
            l1 = np.append(dataList.T[i][0:2000], dataList.T[i])
            f = Preprocess.Filtering()
            n = Preprocess.Normalize()
            result = f.ButterBandPass(True, lowcut=5, highcut=11, order=3,
                                      fs=self.fs, data=l1, axis=0)

            result_list.append(n.norm_mean_std(result[2000:]))

        # fft频谱图
        # c = Preprocess.Character()
        # c.fftPlot(np.array(result_list)[0, :], 256)

        return result_list

    def FeatureExtraction(self, dataList):  # 特征提取
        fe = FeatureExtraction.Feature()

        # PCA
        for i in range(np.array(dataList[0]).shape[0]):  # trainData PCA
            dataList[0][i] = fe.PCA(np.array(dataList[0][i]))

        for i in range(np.array(dataList[2]).shape[0]):  # testData PCA
            dataList[2][i] = fe.PCA(np.array(dataList[2][i]))

        dataList[0] = np.reshape(dataList[0], (np.array(dataList[0]).shape[0], np.array(dataList[0]).shape[1] * np.array(dataList[0]).shape[2]))
        dataList[2] = np.reshape(dataList[2], (np.array(dataList[2]).shape[0], np.array(dataList[2]).shape[1] * np.array(dataList[2]).shape[2]))

        return dataList

    def Classify(self, dataList):  # 分类
        c = Classify.Classify()
        name, accuracy, prediction = c.KNN(dataList)
        # name, accuracy, prediction = c.SVM(dataList)
        # name, accuracy, prediction = c.RandomForest(dataList)
        # #################################### 分类打字效果展示
        ti = TestInterface.SImage(prediction)
        ti.run()
        # #################################### 分类打字效果展示
        print(name, accuracy, prediction)

    def dataRead(self, mainDir):  # 读取数据
        allDataList = []
        trainDataList = []
        trainLabelList = []
        testDataList = []
        testLabelList = []
        for i in range(len(self.fList)):
            dataDir = mainDir + self.fList[i] + '/'
            allFile = os.listdir(dataDir)
            for j in range(len(allFile)):
                rawF = sio.loadmat(dataDir + allFile[j])['data_received']
                cutRawF = np.array(rawF)[self.fs*10:self.fs*(self.samplingTime+10), :]
                # c = Preprocess.Character()
                # c.fftPlot(np.array(cutRawF).T[0], self.fs)
                filteredData = self.Filtering(cutRawF)

                cutData = []
                cutDataLabel = []

                # 按照时间窗口切割数据
                for k in range(0, self.fs*self.samplingTime, self.fs*self.timeWindow):
                    cutData.append(np.array(filteredData)[:, k:k+self.fs*self.timeWindow])
                    cutDataLabel.append(i)

                # cutData, cutDataLabel = shuffle(cutData, cutDataLabel)

                # 将数据集分割成训练集和测试集(包含不同时序的数据)
                cutDataArray = np.array(cutData)
                cutDataLabelArray = np.array(cutDataLabel)
                trainDataList = trainDataList + list(cutDataArray[0:int(0.7*cutDataArray.shape[0]), :, :])
                trainLabelList = trainLabelList + list(cutDataLabelArray[0:int(0.7*cutDataLabelArray.shape[0])])
                testDataList = testDataList + list(cutDataArray[int(0.7*cutDataArray.shape[0]):, :, :])
                testLabelList = testLabelList + list(cutDataLabelArray[int(0.7*cutDataLabelArray.shape[0]):])

        # 将数据集随机排列,保证训练充分
        trainDataList, trainLabelList = shuffle(trainDataList, trainLabelList)
        testDataList, testLabelList = shuffle(testDataList, testLabelList)
        allDataList.append(trainDataList)
        allDataList.append(trainLabelList)
        allDataList.append(testDataList)
        allDataList.append(testLabelList)

        return allDataList


if __name__ == '__main__':
    # ############################### 文件目录,若更换文件夹则修改以下两个变量
    mainDir = "S01/"
    fList = ['6', '7.5', '10']
    # ###############################
    samplingRate = 256
    samplingTime = 20
    timeWindow = 2

    s = SSVEP(fList, samplingRate, samplingTime, timeWindow)

    allDataList = s.dataRead(mainDir)

    featuredDataList = s.FeatureExtraction(allDataList)

    s.Classify(featuredDataList)
