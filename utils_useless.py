"""
@Author : Hishallyi
@Date   : 2024/7/24
@Code   : 暂时用不上的工具函数
"""
import jieba

from utils import *
from sklearn.feature_extraction.text import TfidfVectorizer
from gensim.models import Word2Vec

import numpy as np


def chinese_tokenizer(text):
    """
    custom tokenizers for Chinese text
    @param text:
    @return:
    """
    return jieba.lcut(text)


def compute_tfidf_vector(texts):
    """
    Compute the TF-IDF vector representation of the text
    @param texts:
    @return:
    """
    print_prompt('Compute the TF-IDF vector representation of the text')

    vectorizer = TfidfVectorizer(
        tokenizer=chinese_tokenizer,
        stop_words=None,
        lowercase=False,  # keep the original case
        ngram_range=(1, 2)
    )

    tfidf_matrix = vectorizer.fit_transform(texts)
    tfidf_matrix_array = tfidf_matrix.toarray()

    print('the shape of the tf idf matrix：', tfidf_matrix_array.shape)
    # print feature names words and phrases
    print('prints the feature name：', vectorizer.get_feature_names_out())

    return tfidf_matrix_array, vectorizer


def compute_word2vec_vector(texts):
    """
    Calculate the Word2vec vector representation of the text
    @param texts:
    @return:
    """
    print_prompt('Calculate the Word2vec vector representation of the text')
    tokenized_texts = [text.split() for text in texts]
    # print('Tokenized Texts Length:', len(tokenized_texts))

    model = Word2Vec(tokenized_texts, vector_size=100, window=5, min_count=1, workers=4)
    vectors = [np.mean([model.wv[word] for word in text if word in model.wv] or [np.zeros(100)], axis=0) for text in
               tokenized_texts]
    # print('Word2Vec Vectors Shape:', np.array(vectors).shape)
    return vectors


def get_news_data(root_dir):
    """
    读取新闻类型文件夹中的Word文档内容
    @param root_dir:
    @return:
    """
    # Dictionary to store news types and their corresponding Word file contents
    news_dict = {}

    # Dictionary to store Word file names and their relative paths
    path_dict = {}

    # Traverse the root directory
    for news_type in os.listdir(root_dir):
        news_type_path = os.path.join(root_dir, news_type)
        if os.path.isdir(news_type_path):
            # Initialize the dictionary for the current news type
            news_dict[news_type] = {}

            # Traverse the Word files in the current news type folder
            for file_name in os.listdir(news_type_path):
                if file_name.endswith('.docx'):
                    file_path = os.path.join(news_type_path, file_name)

                    # Read and store the content of the Word file
                    news_dict[news_type][file_name] = read_word_doc(file_path)

                    # Store the relative path of the Word file
                    path_dict[file_name] = file_path

    # print(news_dict)
    print(path_dict)

    return news_dict, path_dict
