import numpy as np
import faiss
import pickle
import os

class VectorDB:
    def __init__(self, dim, db_path="closet_db.pkl"):
        self.dim = dim
        self.db_path = db_path
        self.index = faiss.IndexFlatL2(dim)
        self.vectors = []
        self.metadata = []
        self.load_db()
    
    def load_db(self):
        if os.path.exists(self.db_path):
            try:
                with open(self.db_path, 'rb') as f:
                    data = pickle.load(f)
                    self.vectors = data['vectors']
                    self.metadata = data['metadata']
                    if self.vectors:
                        self.index.add(np.array(self.vectors).astype('float32'))
            except Exception as e:
                print(f"Error loading database: {e}")
    
    def save_db(self):
        try:
            with open(self.db_path, 'wb') as f:
                pickle.dump({
                    'vectors': self.vectors,
                    'metadata': self.metadata
                }, f)
        except Exception as e:
            print(f"Error saving database: {e}")

    def add_item(self, vector, meta):
        self.index.add(np.array([vector]).astype('float32'))
        self.vectors.append(vector)
        self.metadata.append(meta)
        self.save_db()

    def search(self, query_vector, k=3):
        if len(self.vectors) == 0:
            return []
        D, I = self.index.search(np.array([query_vector]).astype('float32'), k)
        return [self.metadata[i] for i in I[0]]
    
    def get_all_items(self):
        return self.metadata
