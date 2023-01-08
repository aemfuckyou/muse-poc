
from Utility.transform_data import compute_feature_matrix, epoch
from dbconnection import dbmodel, dbcon
import numpy as np


class PlotTestModel:

    def __init__(self, test):
        self._observers = []
        self.test = test
        self.user = test.user_id
        self.test_type = test.test_type_id
        self.transformed_vectors = None
        self.transformed_vectors_mean = None
        dbcon.pg_db.connect(reuse_if_open=True)
        self.raw_data = list(dbmodel.RawDataEntry.select(dbmodel.RawDataEntry, dbmodel.Test)
                                .join(dbmodel.Test)
                                .where(dbmodel.RawDataEntry.test_id==test)
                                .order_by(dbmodel.RawDataEntry.test_id)
                                .execute())
        dbcon.pg_db.close()
        self._transform_data()

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def _notify_observers(self):
        for x in self._observers:
            x.model_is_changed()

    def _transform_data(self):
        arr = np.zeros((len(self.raw_data), 4))
        for idx, raw in enumerate(self.raw_data):
            arr[idx] = [raw.tp9, raw.af7, raw.af8, raw.tp10]
        epochs = epoch(arr, 256)
        self.transformed_vectors = compute_feature_matrix(epochs, 256)
        self.transformed_vectors_mean = np.zeros([self.transformed_vectors.shape[0],4])
        for idx, vec in enumerate(self.transformed_vectors):
            delta_vector, theta_vector, alpha_vector, beta_vector = np.split(vec, 4)
            self.transformed_vectors_mean[idx] = np.array(
                                                        [np.mean(delta_vector),
                                                        np.mean(theta_vector), 
                                                        np.mean(alpha_vector), 
                                                        np.mean(beta_vector)])

        print(self.transformed_vectors_mean)

    '''
    def _divide_chunks(self, l, n):
        for i in range(0, len(l), n):
            yield l[i:i + n]
    '''
