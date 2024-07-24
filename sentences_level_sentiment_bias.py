"""
@Author : Hishallyi
@Date   : 2024/7/24
@Code   : 句子层面的情感偏见计算
"""

from utils import *


def sentiment_bias_on_pair_texts(document_path1, document_path2):
    """
    计算一对新闻的情感偏见
    @param document_path1:
    @param document_path2:
    @return:
    """
    print()
    male_sentences_score_1, female_sentences_score_1 = population_group_average_sentiment_scores(document_path1)
    print(
        f'The male and female sentences in Document 1 are scored respectively：{male_sentences_score_1, female_sentences_score_1}')
    male_sentences_score_2, female_sentences_score_2 = population_group_average_sentiment_scores(document_path2)
    print(
        f'The male and female sentences in Document 2 are scored respectively：{male_sentences_score_2, female_sentences_score_2}\n')
    sentences_level_bias = max(abs(male_sentences_score_1 - female_sentences_score_1),
                               abs(male_sentences_score_2 - female_sentences_score_2))
    return sentences_level_bias


if __name__ == '__main__':
    # 示例 Word 文档路径
    # file_path1 = '大规模宕机为全球信息技术安全敲响警钟.docx'

    file_path1 = 'news_AI/财经/科技金融探索服务新路径.docx'
    file_path2 = 'news/财经/科技金融探索服务新路径.docx'

    sentences_level_bias = sentiment_bias_on_pair_texts(file_path1, file_path2)
    print(sentences_level_bias)
