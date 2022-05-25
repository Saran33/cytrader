from cytrader import Analyzer
from river import metrics

class ROCAUC(Analyzer):
    '''Receiving Operating Characteristic Area Under the Curve.
       For classification strategies.
       https://riverml.xyz/latest/api/metrics/ROCAUC/
    '''
    params = (('n_thresholds', None),)

    def __init__(self):
        super(ROCAUC, self).__init__()
        self.metric = dict()

    def start(self):
        pass

    def next(self):
        pass

    def stop(self):
        for i, d in enumerate(self.datas):
            tkr = self.datas[i]._name
            y_true = self.strategy.y[tkr]
            y_pred = self.strategy.y_pred[tkr]
            if self.p.n_thresholds:
                self.metric[tkr] = metrics.ROCAUC(n_thresholds=self.p.n_thresholds)
            else:
                self.metric[tkr] = metrics.ROCAUC(n_thresholds=len(y_pred))
            for yt, yp in zip(y_true, y_pred):
                self.metric[tkr] = self.metric[tkr].update(yt, yp)

    def get_analysis(self):
        return self.metric
