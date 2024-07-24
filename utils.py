"""
@Author : Hishallyi
@Date   : 2024/7/22
@Code   : tools functions
"""
from collections import Counter
import docx
import re
import os
from snownlp import SnowNLP


def print_prompt(prompt):
    """
    print the prompt message to beautify the output
    @param prompt:
    @return:
    """
    print('\n-----------------' + prompt + '-----------------')


def read_word_doc(file_path):
    """
    read the contents of Word document
    @param file_path:
    @return:
    """
    doc = docx.Document(file_path)
    full_text = []
    for paragraph in doc.paragraphs:
        full_text.append(paragraph.text)

    text = ' '.join(full_text)

    return text


def remove_punctuation_spaces(text):
    """
    Remove spaces and punctuation from the text
    @param text:
    @return:
    """
    print('The length of the text before removing spaces and punctuation：', len(text))
    text = re.sub(r'\s+', '', text)  # 去除所有空格
    text = re.sub(r'[^\w]', '', text)  # 去除所有标点符号
    print('The length of the text after removing spaces and punctuation：', len(text))
    return text


def count_gender_words(words, gender_words):
    """
    Statistics on the distribution of gender vocabulary
    @param words: list，词汇列表
    @param gender_words: list，性别词汇列表
    @return: words中性别词汇的数量
    """
    word_counts = Counter(words)
    # 获取性别词汇的词频，字典的键是性别词汇，值是词频
    words_frequency = {word: word_counts.get(word, 0) for word in gender_words}
    words_num = sum(words_frequency.values())
    return words_num


def calculate_words_distribution(document):
    """
    Calculate words distribution
    @param document: list，包含文档中的所有词汇
    @return:
    """
    # 定义性别相关词汇列表
    male_related_words = ["他", "男", "男人", "男性", "男孩", "先生", "爸爸", "儿子", "男士", "哥哥", "爷爷", "孙子",
                          "外公",
                          "外孙", "公公", "老公", "丈夫", "弟弟", "兄弟", "舅舅", "侄子"]
    female_related_words = ["她", "女", "女人", "女性", "女孩", "女士", "妈妈", "女儿", "姐姐", "太太", "外婆",
                            "外孙女",
                            "婆婆",
                            "老婆", "妻子", "姐妹", "妹妹", "舅妈", "姑姑", "侄女"]

    # 获取每个文档的性别词汇分布
    male_n = count_gender_words(document, male_related_words)
    female_n = count_gender_words(document, female_related_words)

    total_related_words_num = male_n + female_n
    if total_related_words_num == 0:
        print('文档中没有性别词汇')
        words_distribution = [0.5, 0.5]
    else:
        words_distribution = [male_n / total_related_words_num, female_n / total_related_words_num]
    print(f'性别词汇分布: {words_distribution}')

    return words_distribution


def average_sentiment_scores(sentences):
    """
    给定一组句子，计算平均情感分数
    @param sentences:
    @return:
    """
    scores = []
    for sentence in sentences:
        s = SnowNLP(sentence)
        score = s.sentiments
        scores.append(score)
    average_score = sum(scores) / len(scores)

    return average_score


def population_group_average_sentiment_scores(document_path):
    """
    划分文档中不同人群的句子，并计算平均情感分数
    @param document_path:
    @return:
    """

    text = read_word_doc(document_path)

    # 分句处理
    sentences = SnowNLP(text).sentences

    male_related_words = ["他", "男", "男人", "男性", "男孩", "先生", "爸爸", "儿子", "男士", "哥哥", "爷爷", "孙子",
                          "外公",
                          "外孙", "公公", "老公", "丈夫", "弟弟", "兄弟", "舅舅", "侄子"]
    female_related_words = ["她", "女", "女人", "女性", "女孩", "女士", "妈妈", "女儿", "姐姐", "太太", "外婆",
                            "外孙女",
                            "婆婆",
                            "老婆", "妻子", "姐妹", "妹妹", "舅妈", "姑姑", "侄女"]

    # 划分不同人群的句子
    male_sentences = []
    female_sentences = []
    for sentence in sentences:
        male_words_num = count_gender_words(sentence, male_related_words)
        female_words_num = count_gender_words(sentence, female_related_words)
        if male_words_num > female_words_num:
            male_sentences.append(sentence)
        elif male_words_num < female_words_num:
            female_sentences.append(sentence)
        else:
            continue
    # 打印输出
    print(f'文档中的男性句子：{male_sentences}')
    print(f'文档中的女性句子：{female_sentences}')

    # 对不同人群列表计算平均情感分数
    male_sentences_score = 0 if len(male_sentences) == 0 else average_sentiment_scores(male_sentences)
    female_sentences_score = 0 if len(female_sentences) == 0 else average_sentiment_scores(female_sentences)

    # 返回不同人群的平均情感分数
    return male_sentences_score, female_sentences_score
