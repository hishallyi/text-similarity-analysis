"""
@Author : Hishallyi
@Date   : 2024/7/22
@Code   : Calculate the gender lexical similarity of two texts
"""

from utils import *
from scipy.stats import wasserstein_distance


def similarity_calculation_of_two_texts(file_path1, file_path2):
    """
    Calculate the similarity of gender words in two texts
    @param file_path1:
    @param file_path2:
    @return:
    """
    print('\nread the contents of Word document 1')
    document1 = read_word_doc(file_path1)
    words_distribution_1 = calculate_words_distribution(document1)

    print('read the contents of Word document 2')
    document2 = read_word_doc(file_path2)
    words_distribution_2 = calculate_words_distribution(document2)

    distance = wasserstein_distance(words_distribution_1, words_distribution_2)

    print('#####################################################################')
    print(f'The Wasserstein distance based between the two texts is: {distance}')
    print('#####################################################################\n')


# main
if __name__ == '__main__':
    # 示例 Word 文档路径
    file_path1 = 'news_AI/财经/科技金融探索服务新路径.docx'
    file_path2 = 'news/财经/科技金融探索服务新路径.docx'

    similarity_calculation_of_two_texts(file_path1, file_path2)
