import streamlit as st
from bs4 import BeautifulSoup
import requests
import nltk
from nltk.tokenize import word_tokenize
import matplotlib.pyplot as plt

# 获取静态网页的文本内容
def get_webpage_text(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    text = soup.get_text()
    return text

# 去除HTML标签
def remove_html_tags(text):
    soup = BeautifulSoup(text, "html.parser")
    return soup.get_text()

# 统计关键词
def count_keywords(text, keyword):
    tokens = word_tokenize(text)
    freq = nltk.FreqDist(tokens)
    return freq[keyword]

# 绘制折线图
def plot_line_chart(data, xlabel, ylabel):
    plt.plot(data)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    st.pyplot()

# Streamlit应用程序
def main():
    st.title('Webpage Analysis App')
    url = st.text_input('Enter the URL of the webpage:')
    if st.button('Get webpage content'):
        webpage_text = get_webpage_text(url)
        clean_text = remove_html_tags(webpage_text)
        st.text_area('Webpage content:', clean_text)

    keyword = st.text_input('Enter the keyword to count:')
    if st.button('Count keyword'):
        count = count_keywords(clean_text, keyword)
        st.write(f'The keyword "{keyword}" appears {count} times.')

    data = [1, 2, 3, 4, 5]  # Replace with your data
    plot_line_chart(data, 'X-axis', 'Y-axis')

if __name__ == '__main__':
    main()