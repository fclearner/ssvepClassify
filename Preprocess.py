import scipy.signal
import numpy as np
import matplotlib.pyplot as plt


class Filtering:

    def __init__(self):
        pass

    def ButterBandPass(self, Rt, lowcut, highcut, order, fs, data, axis=0):
        # Rt: whether its Real-time
        nyq = 0.5 * fs
        low = lowcut / nyq
        high = highcut / nyq
        b, a = scipy.signal.butter(order, [low, high], btype='bandpass')

        if Rt:
            return scipy.signal.filtfilt(b, a, data, axis)
        else:
            return scipy.signal.lfilter(b, a, data, axis)  # real-time filter

    def EllipordBandPass(self, lowcut, highcut, order, fs, data, axis=0):
        Wp = [lowcut/fs*2, highcut/fs*2]
        Ws = [(lowcut-0.5)/fs*2, (highcut+0.5)/fs*2]
        N, Wn = scipy.signal.ellipord(Wp, Ws, 3, 60, True)
        b, a = scipy.signal.ellip(N, 3, 60, Wn, 'bandpass', True)

        return scipy.signal.filtfilt(b, a, data, axis)


class Normalize:

    def __init__(self):
        pass

    def norm_min_max(self, data):  # 极差变换法
        return (data - np.min(data)) / (np.max(data)-np.min(data))

    def norm_mean_std(self, data):  # 0均值标准化
        mean = np.mean(data, axis=0)
        std_dev = np.std(data, axis=0)
        return (data - mean) / std_dev

    def norm_linear(self, data):  # 线性比例变换法
        return data / np.max(data)


class Character:

    def __init(self):
        pass

    def fftPlot(self, data, fs):
        plt.plot(np.arange(0, len(data)*fs/len(data), 1*fs/len(data)),
                 abs(np.fft.fft(data)*2/len(data)))
        plt.xlim(0, 20)
        plt.ylim(0, 10)
        plt.show()
