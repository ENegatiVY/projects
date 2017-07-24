import math
from Crawler import Crawler


def page_check(html):
    print("Checking")


def cos(vector1, vector2):
    dimension = min(len(vector1), len(vector2))
    if dimension == 0:
        return 0
    inner_product = 0.0
    length1 = 0.0
    length2 = 0.0
    for i in range(0, dimension):
        inner_product += int(vector1[i]) * int(vector2[i])
        length1 += int(vector1[i]) * int(vector1[i])
        length2 += int(vector2[i]) * int(vector2[i])
    length1 = math.sqrt(length1)
    length2 = math.sqrt(length2)
    return inner_product / (length1 * length2)


def check_with_cosine():
    url_file = open("categories/index/url.txt", encoding="utf-8")
    urls = url_file.read().split()
    login_vector_file = open("categories/login/vector.txt", encoding="utf-8")
    index_vector_file = open("categories/index/vector.txt", encoding="utf-8")
    register_vector_file = open("categories/register/vector.txt", encoding="utf-8")
    login_vector = login_vector_file.read().split()
    for i in range(0, len(login_vector)):
        login_vector[i] = int(login_vector[i])
    indexVector = index_vector_file.read().split()
    registerVector = register_vector_file.read().split()
    crawler = Crawler()
    for url in urls:
        # url = "https://mail.sjtu.edu.cn/"
        try:
            words = open("categories/words.txt", encoding='utf-8').read().split("\n")
            vector = crawler.word_frequency_statistics_by_url(url, words)
            print(login_vector)
            print(vector)
            print("Possibility of " + url + " being a login page is " + str(cos(login_vector, vector)))
        except Exception:
            continue


def check_with_naive_bayes(url):
    url_file = open("categories/index/url.txt", encoding="utf-8")
    urls = url_file.read().split()
    types = ['login', 'register', 'index']
    possibility_of_types = [0.3518987, 0.2987342, 0.3493671]
    words = open("categories/words.txt", encoding='utf-8').read().split("\n")
    crawler = Crawler()
    vector = crawler.word_frequency_statistics_by_url(url, words)
    for i in range(0, len(types)):
        possibility_of_existence = open("categories/" + types[i] + "/vector.txt", encoding="utf-8").read().split("\n")
        print(possibility_of_existence)
        print(vector)
        possibility = possibility_of_types[i]
        for value in vector:
            if value == 1:
                possibility = possibility * float(possibility_of_existence[i])
            else:
                possibility = possibility * (1 - float(possibility_of_existence[i]))
        print(possibility)


if __name__ == "__main__":
    print("213")
