import pickle
import os

class FaceDatabase:
    def __init__(self, path='data/encodings.pkl'):
        self.path = path
        self.data = self.load_database()

    def load_database(self):
        if os.path.exists(self.path):
            with open(self.path, 'rb') as f:
                return pickle.load(f)
        return {}

    def save_database(self):
        with open(self.path, 'wb') as f:
            pickle.dump(self.data, f)

    def add_embedding(self, name, embedding):
        if name not in self.data:
            self.data[name] = []
        self.data[name].append(embedding)
        self.save_database()

    def get_all(self):
        return self.data

