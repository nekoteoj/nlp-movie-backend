from pythainlp.tokenize import word_tokenize
import tensorflow as tf
import tensorflow
import pickle
from tensorflow.keras.models import load_model
import numpy as np


class MovieRecomender():
    def __init__(self, model_path="core/resource/model.h5", metadata_path="core/resource/meta.pkl", UNK_thresh=0.8, allow_TFIDF_matching=True):
        super(MovieRecomender, self).__init__()
        self.model = load_model(model_path)
        meta = pickle.load(open(metadata_path, "rb"))
        self.word_to_idx = meta["word_to_idx"]
        self.idx_to_class = meta["idx_to_class"]
        self.pad_length = 40
        self.TF = meta["TF"]
        self.IDF = meta["IDF"]
        self.word_to_idx_summary = meta["word_to_idx_summary"]
        self.UNK_thresh = UNK_thresh
        self.allow_TFIDF_matching = allow_TFIDF_matching

    def preprocess_X(self, data):
        processed_data = []
        for words in data:
            x_new = []
            for word in words:
                if(word not in self.word_to_idx):
                    word = "UNK"
                x_new.append(self.word_to_idx[word])
            processed_data.append(x_new)
        processed_data = tensorflow.keras.preprocessing.sequence.pad_sequences(
            processed_data, maxlen=self.pad_length, dtype="int32", padding="post", truncating="pre", value=0.)
        return processed_data

    def recommend(self, text):
        t = [word_tokenize(text.strip(), engine="ulmfit",
                           keep_whitespace=False)]
        sentence = t.copy()[0]
        t = self.preprocess_X(t)
        UNK_ratio_wrong = (t == self.word_to_idx["UNK"]).sum(
            axis=1) / np.count_nonzero(t, axis=1)
        res = None
        # perform tf-idf
        if(UNK_ratio_wrong[0] > self.UNK_thresh and self.allow_TFIDF_matching):
            logit = []
            for i in range(len(self.TF)):
                tdidf_score = 0
                for word in sentence:
                    if(word in self.word_to_idx_summary and word != 0):
                        tdidf_score += self.TF[i, self.word_to_idx_summary[word]
                                               ] * self.IDF[self.word_to_idx_summary[word]]
                tdidf_score = 0
                logit.append(tdidf_score)
            logit = np.array(logit)
            x = np.sum(logit)
            res = logit / (x if x != 0 else 1)
        if(res is None or np.sum(res) == 0):
            res = self.model.predict(t)[0]
        movie_list = [self.idx_to_class[i] for i in range(res.shape[0])]
        a = sorted(zip(res, movie_list), key=lambda x: x[0], reverse=True)
        return a[:5]
