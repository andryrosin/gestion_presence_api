from mtcnn import MTCNN
from keras_facenet import FaceNet
import cv2
import numpy as np
import faiss


class FaceModel:
    def __init__(self):
        self.detector = MTCNN()
        self.facenet = FaceNet()
        
    def get_embedding(self, face_pixels):
        samples = np.expand_dims(face_pixels.astype('float32'), axis=0)
        yhat = self.facenet.embeddings(samples)
        return yhat[0]
    
    def detect_face(self, image_path):
        image = cv2.imread(image_path)
        if image is None:
            print(f"Impossible de charger l'image : {image_path}")
            return None, None        
        rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        faces = self.detector.detect_faces(rgb)
        
        if len(faces) == 0:
            print(f"Aucun visage détecté dans : {image_path}")
            return None, None
        
        x, y, w, h = faces[0]['box']
        x, y = abs(x), abs(y)

        padding = int(w * 0.1)
        x = max(0, x - padding)
        y = max(0, y - padding)
        w = w + padding * 2
        h = h + padding * 2
        
        face = rgb[y:y + h, x:x + w]
        face = cv2.resize(face, (160, 160))
        
        embedding = self.get_embedding(face)
        face_box = {"x": x, "y": y, "w": w, "h": h}
        return embedding, face_box
    
    def compare_embeddings(self, emb1, emb2, threshold=1.1):
        dist = np.linalg.norm(emb1 - emb2)
        print(f"Distance calculée : {dist}")
        return dist < threshold
    def find_closest_embeddings(self, emb, objects, embedding_attr="embedding", threshold=1.1, top_k=1):
        emb_array = []
        valid_objects = []
        for obj in objects:
            obj_emb = getattr(obj, embedding_attr, None)
            if obj_emb is not None:
                emb_array.append(obj_emb)
                valid_objects.append(obj)
        
        if len(emb_array) == 0:
            return []
        emb_matrix = np.stack(emb_array)
        diffs = emb_matrix - emb 
        dists = np.linalg.norm(diffs, axis=1)
        mask = dists <= threshold
        filtered_objs = [valid_objects[i] for i in range(len(valid_objects)) if mask[i]]
        filtered_dists = dists[mask]

        sorted_idx = np.argsort(filtered_dists)
        results = [(filtered_objs[i], filtered_dists[i]) for i in sorted_idx[:top_k]]
        return results
    def find_closest_embeddings_faiss(self, emb, objects, embedding_attr="embedding", threshold=1.1, top_k=1):
        """
        Recherche les embeddings les plus proches avec FAISS.
        """
        emb_array = []
        valid_objects = []
        for obj in objects:
            obj_emb = getattr(obj, embedding_attr, None)
            if obj_emb is not None:
                emb_array.append(obj_emb)
                valid_objects.append(obj)
        
        if len(emb_array) == 0:
            return []
    
        emb_matrix = np.stack(emb_array).astype('float32')
        emb_query = np.expand_dims(emb.astype('float32'), axis=0)
    
        d = emb_matrix.shape[1]  
        index = faiss.IndexFlatL2(d)
        index.add(emb_matrix)
        D, I = index.search(emb_query, top_k)
        results = []
        for dist, idx in zip(D[0], I[0]):
            if dist <= threshold:
                results.append((valid_objects[idx], dist))
        return results