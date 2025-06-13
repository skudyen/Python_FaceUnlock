from insightface.app import FaceAnalysis
import warnings
import os
import sys
import contextlib

class FaceEncoder:
    def __init__(self):
        warnings.filterwarnings("ignore")

        with open(os.devnull, 'w') as fnull:
            with contextlib.redirect_stdout(fnull), contextlib.redirect_stderr(fnull):
                self.app = FaceAnalysis(name='buffalo_l')
                self.app.prepare(ctx_id=0)  # ctx_id=0 สำหรับ GPU, -1 สำหรับ CPU

    def get_embedding(self, image):
        faces = self.app.get(image)
        if faces:
            return faces[0].embedding 
        return None
