"""
@Author : Hishallyi
@Date   : 2024/7/22
@Code   : tools functions
"""
from collections import Counter
import docx
import jieba
import re
import os


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
    print('The length of the text before removing spaces and punctuation：', len(text))

    text = re.sub(r'\s+', '', text)  # 去除所有空格
    text = re.sub(r'[^\w]', '', text)  # 去除所有标点符号
    print('The length of the text after removing spaces and punctuation：', len(text))
    # 分词
    words = jieba.lcut(text)

    return words


def count_gender_words(words, gender_words):
    """
    Statistics on the distribution of gender vocabulary
    @param words:
    @param gender_words:
    @return:
    """
    word_counts = Counter(words)
    # 获取性别词汇的词频，字典的键是性别词汇，值是词频
    gender_word_counts = {word: word_counts.get(word, 0) for word in gender_words}
    return gender_word_counts


def calculate_words_distribution(document):
    """
    Calculate words distribution
    @param document:
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
    male_frequency = count_gender_words(document, male_related_words)
    female_frequency = count_gender_words(document, female_related_words)

    # 存储各个词的词频的列表
    male_n = sum(male_frequency.values())
    female_n = sum(female_frequency.values())
    total_related_words_num = male_n + female_n
    if total_related_words_num == 0:
        print('文档中没有性别词汇')
        words_distribution = [0.5, 0.5]
    else:
        words_distribution = [male_n / total_related_words_num, female_n / total_related_words_num]
    print(f'性别词汇分布: {words_distribution}')

    return words_distribution


def get_news_data(folder_path):
    """
    read news data
    @param folder_path:
    @return:
    """
    news_data = {}

    # Traverse each subfolder in the folder (news type folder)
    for news_type_folder in os.listdir(folder_path):
        news_type_path = os.path.join(folder_path, news_type_folder)
        if os.path.isdir(news_type_path):
            # Initialize the news dictionary corresponding to the news type
            news_data[news_type_folder] = {}

            for doc_file in os.listdir(news_type_path):
                doc_file_path = os.path.join(news_type_path, doc_file)
                if doc_file_path.endswith('.docx'):
                    try:
                        content = read_word_doc(doc_file_path)
                        # add news content to the news dictionary
                        news_data[news_type_folder][doc_file] = content
                    except Exception as e:
                        print(f"Error reading {doc_file_path}: {e}")

    return news_data
