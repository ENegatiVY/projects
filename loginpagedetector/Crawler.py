import urllib.request
import re
import sys
import jieba
from WordFrequency import WordFrequency


class Crawler:
    @staticmethod
    def fetch_raw_html(url):
        try:
            connection = urllib.request.urlopen(url)
            pattern = "charset=([a-zA-Z0-9\-]+)\n"
            reg = re.compile(pattern)
            print(connection.info())
            charset = reg.findall(str(connection.info()))[0]
            return connection.read().decode(charset)
        except UnicodeDecodeError:
            print("Error decoding HTML.")
            return ''
        except Exception as e:
            print("Error fetching HTML: ")
            print(e)
            return ''

    def fetch_images(self, url):
        html = self.fetch_raw_html(url)
        reg = r'<img .+? src="([^>]+?\.jpg)" pic_ext'
        img_reg = re.compile(reg)
        return re.findall(img_reg, html)

    def fetch_links(self, url):
        try:
            # Fetch all links with the page as a root
            html = self.fetch_raw_html(url)
            hostname = re.findall("//(.+?)/", url)[0]
            # Remove '#'s
            reg = '<a[^>]+?href="([^#>]+?)"'
            link_reg = re.compile(reg)
            link_list = re.findall(link_reg, html)
            # print(linkList)
            i = 0
            # For each link in the list
            while i < len(link_list):
                # Remove '/'s and 'javascript:....'s
                if re.match("^/$", link_list[i]):
                    link_list.remove(link_list[i])
                    continue
                if re.match("^javascript", link_list[i]):
                    link_list.remove(link_list[i])
                    continue
                # Add 'http://' to some urls
                if not re.match("^http", link_list[i]):
                    if re.match("^/", link_list[i]):
                        link_list[i] = "http://" + link_list[i]
                    else:
                        link_list[i] = "http://" + hostname + "/" + link_list[i]
                # Remove other hosts' pages
                if not re.match("^http://" + hostname, link_list[i]):
                    link_list.remove(link_list[i])
                    continue
                # Remove '../'s
                link_list[i] = re.sub("\.\./", "", link_list[i])
                # Replace '&amp;'s
                link_list[i] = re.sub("&amp;", "&", link_list[i])
                i = i + 1
            return link_list
        except Exception:
            print("HTTP Error at URL: '" + url + "'. Aborting.")
            return []

    def fetch_words(self, url, min_length, max_length):
        html = self.fetch_raw_html(url)
        print("Fetching words in URL:" + url)
        reg = u"([\u4e00-\u9fa5]{" + str(min_length) + "," + str(max_length) + "})"
        wordReg = re.compile(reg)
        originalWords = wordReg.findall(html)
        words = []
        for word in originalWords:
            words = self.collect_list(words, filter(lambda wd: len(wd) > 1, jieba.cut(word)))
        return words

    @property
    def fetch_url_tree(self):
        processed_links = []
        link_queue = ["http://cy.xjtu.edu.cn/"]
        while len(link_queue) > 0:
            current_link = link_queue[0]
            link_queue.remove(link_queue[0])
            if current_link not in processed_links:
                print("Fetching URLs from: " + current_link)
                list = self.fetch_links(current_link)
                if len(list) > 0:
                    for link in self.fetch_links(current_link):
                        # print(link)
                        if not processed_links.__contains__(link):
                            link_queue.append(link)
                processed_links.append(current_link)
        print("==============================")
        print("Found Links:")
        for link in processed_links:
            print(link)
        print("==============================")
        return processed_links

    @staticmethod
    def collect(array, item):
        if not array.__contains__(item):
            array.append(item)
        return array

    def collect_list(self, array: object, items) -> object:
        for item in items:
            array = self.collect(array, item)
        return array

    def frequent_word_statistics(self):
        try:
            word_collection = []
            word_frequency_collection = []
            page_types = ["index", "login", "register"]
            for pageType in page_types:
                file = open("categories/" + pageType + "/url.txt")
                urls = file.read().split("\n")
                for url in urls:
                    for word in self.fetch_words(url, 2, 6):
                        word_collection = self.collect(word_collection, word)
                        if word_frequency_collection.__contains__(WordFrequency(word)):
                            for word_frequency in word_frequency_collection:
                                if word_frequency.word == word:
                                    word_frequency.frequency += 1
                                    break
                        else:
                            word_frequency_collection.append(WordFrequency(word))
            word_file = open("categories/words.txt", 'w', encoding='utf-8')
            vector_file = open("categories/all/vector.txt", 'w', encoding='utf-8')
            word_frequency_collection.sort(key=lambda wf: wf.frequency)
            word_frequency_collection.reverse()
            for word_frequency in word_frequency_collection:
                print(word_frequency.word + " " + str(word_frequency.frequency))
                word_file.write(word_frequency.word + "\n")
                vector_file.write(str(word_frequency.frequency) + "\n")
        except FileNotFoundError as e:
            print(e)
            sys.exit(1)

    def word_frequency_statistics_by_page_type(self, page_type):
        try:
            word_file = open("categories/words.txt", encoding='utf-8')
            url_file = open("categories/" + str(page_type) + "/url.txt", encoding='utf-8')
            words = word_file.read().split("\n")
            urls = url_file.read().split()
            vector = []
            for i in range(0, len(words)):
                vector.append(0)
            for url in urls:
                temp_vector = self.word_frequency_statistics_by_url(url, words)
                for i in range(0, len(words)):
                    vector[i] += temp_vector[i]
            vector_file = open("categories/" + str(page_type) + "/vector.txt", mode='w+', encoding='utf-8')
            for i in range(0, len(words)):
                vector_file.write(str(float(vector[i] / len(urls))) + "\n")
        except Exception as e:
            print(e)

    def word_frequency_statistics_by_url(self, url, words):
        try:
            vector = []
            for i in range(0, len(words)):
                vector.append(0)
            print("Calculating word frequencies on " + url)
            html = self.fetch_raw_html(url)
            html_file = open("categories/html.txt", mode='w', encoding='utf-8')
            html_file.write(html)
            for i in range(0, len(words)):
                # pattern = words[i]
                # reg = re.compile(pattern)
                # wordCount = len(reg.findall(html))
                # Count all occurrences
                # vector[i] += wordCount
                # Count this page as one
                if html.find(words[i]) > -1:
                    vector[i] += 1
            return vector
        except Exception as e:
            print(e)
            return []


if __name__ == "__main__":
    crawler = Crawler()
