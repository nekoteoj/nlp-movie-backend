from pythainlp.tokenize import word_tokenize
import tensorflow as tf
import tensorflow
import pickle
from tensorflow.keras.models import load_model


class MovieRecomender():
    def __init__(self,
                 model_path="core/resource/model.h5",
                 metadata_path="core/resource/meta.pkl"):
        super(MovieRecomender, self).__init__()
        self.model = load_model(model_path)
        meta = pickle.load(open(metadata_path, "rb"))
        self.word_to_idx = meta["word_to_idx"]
        self.idx_to_class = meta["idx_to_class"]
        self.pad_length = 40

    def preprocess_X(self, data):
        processed_data = []
        for words in data:
            x_new = []
            for word in words:
                if (word not in self.word_to_idx): word = 'UNK'
                x_new.append(self.word_to_idx[word])
            processed_data.append(x_new)
        processed_data = tensorflow.keras.preprocessing.sequence.pad_sequences(
            processed_data,
            maxlen=self.pad_length,
            dtype='int32',
            padding='post',
            truncating='pre',
            value=0.)
        return processed_data

    def recommend(self, text):
        t = [word_tokenize(text, engine="ulmfit")]
        t = self.preprocess_X(t)
        t = tensorflow.keras.preprocessing.sequence.pad_sequences(
            t,
            maxlen=self.pad_length,
            dtype='int32',
            padding='post',
            truncating='pre',
            value=0.)
        res = self.model.predict(t)[0]
        movie_list = [self.idx_to_class[i] for i in range(res.shape[0])]
        a = sorted(zip(res, movie_list), key=lambda x: x[0], reverse=True)
        return a[:5]
