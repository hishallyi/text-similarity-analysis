"""
@Author : Hishallyi
@Date   : 2024/7/22
@Code   : Calculate the gender lexical similarity of two texts
"""
import jieba

from utils import *
from scipy.stats import wasserstein_distance
import os


def gender_bias_on_pair_texts(file_path1, file_path2):
    """
    Calculate the similarity of gender words in two texts
    @param file_path1:
    @param file_path2:
    @return:
    """
    print('\nread the contents of Word document 1')
    text1 = remove_punctuation_spaces(read_word_doc(file_path1))
    document1 = jieba.lcut(text1)  # 分词
    words_distribution_1 = calculate_words_distribution(document1)

    print('read the contents of Word document 2')
    text2 = remove_punctuation_spaces(read_word_doc(file_path2))
    document2 = jieba.lcut(text2)  #
    words_distribution_2 = calculate_words_distribution(document2)

    distance = wasserstein_distance(words_distribution_1, words_distribution_2)

    print('#####################################################################')
    print(f'The Wasserstein distance based between the two texts is: {distance}')
    print('#####################################################################\n')

    return distance


def gender_bias_on_all_news(real_news_root_dir, ai_news_root_dir):
    """
    计算真实新闻和AI新闻的综合性别偏见
    @param real_news_root_dir:
    @param ai_news_root_dir:
    @return:
    """
    real_news = get_filename_and_relative_paths(real_news_root_dir)
    ai_news = get_filename_and_relative_paths(ai_news_root_dir)
    distances = []
    for news_file_name, real_news_relative_path in real_news.items():
        ai_news_relative_path = ai_news.get(news_file_name)
        distance = gender_bias_on_pair_texts(real_news_relative_path, ai_news_relative_path)
        distances.append(distance)
    average_distance = sum(distances) / len(distances)
    return average_distance


# main
if __name__ == '__main__':
    #####################################
    #          遍历文件夹文档内容          #
    #####################################
    root_dir = 'PeopleDaily'
    path_dict = get_filename_and_relative_paths(root_dir)

    # 遍历新闻类型和文档名称
    for news_file_name, relative_path in path_dict.items():
        print(f"Document name: {news_file_name}, Relative path: {relative_path}")
