import tensorflow
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np
import string

def preprocess_text(text):
    if isinstance(text, list):
        text = ' '.join(text)
    # Convert text to lowercase and remove punctuation
    text = text.lower().translate(str.maketrans('', '', string.punctuation))
    return text.split() if text else []

def vectorize_stories(data, word_idx, story_maxlen, query_maxlen):
    X, Xq, Y = [], [], []

    for story, query, answer in data:
        # Preprocess story and query
        story = preprocess_text(story)
        query = preprocess_text(query)

        # Vectorize them
        x = [word_idx.get(w, 0) for w in story]  
        xq = [word_idx.get(w, 0) for w in query]

        # Vectorize answer
        y = np.zeros(len(word_idx) + 1)
        y[word_idx.get(answer, 0)] = 1

        X.append(x)
        Xq.append(xq)
        Y.append(y)

    return (pad_sequences(X, maxlen=story_maxlen),
            pad_sequences(Xq, maxlen=query_maxlen), np.array(Y))