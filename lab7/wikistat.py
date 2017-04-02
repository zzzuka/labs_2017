import os
import sys
import math

import array

import statistics

from matplotlib import rc
rc('font', family='Droid Sans', weight='normal', size=14)

import matplotlib.pyplot as plt


class WikiGraph:

    def load_from_file(self, filename):
        print('Загружаю граф из файла: ' + filename)

        with open(filename) as f:
            (n, _nlinks) = [int(x) for x in f.readline().split()]
            self._n = n

            # links - это edges
            self._titles = []   #
            self._sizes = array.array('L', [0]*n)
            self._links = array.array('L', [0]*_nlinks)
            self._redirect = array.array('B', [0]*n)
            self._offset = array.array('L', [0]*(n+1))

            for i in range(n):
                self._titles.append(f.readline())
                a, b, c = map(int, f.readline().split())
                self._sizes[i] = a
                self._redirect[i] = b
                for j in range(c):
                    self._links[self._offset[i] + j] = int(f.readline())
                    self._offset[i + 1] = c + self._offset[i]


        print('Граф загружен')

    def get_number_of_links_from(self, _id):
        return len(self.get_links_from(_id))

    def get_links_from(self, _id):
        return self._links[self._offset[_id]:self._offset[_id + 1]]

    def get_id(self, title):
        for i in range(len(self._titles)):
            if title == self._titles[i]:
                return int(i)

    def get_number_of_pages(self):
        return self._n

    def is_redirect(self, _id):
        if self._redirect[_id]:
            return True
        return False

    def get_title(self, _id):
        return self._titles[_id]

    def get_page_size(self, _id):
        return self._sizes[_id]


def hist(fname, data, bins, xlabel, ylabel, title, facecolor='green', alpha=0.5, transparent=True, **kwargs):
    plt.clf()
    # TODO: нарисовать гистограмму и сохранить в файл

"""
if __name__ == '__main__':

    if len(sys.argv) != 2:
        print('Использование: wiki_stats.py <файл с графом статей>')
        sys.exit(-1)

    if os.path.isfile(sys.argv[1]):
        wg = WikiGraph()
        wg.load_from_file(sys.argv[1])
        wg.is_redirect(4)
        print()
    else:
        print('Файл с графом не найден')
        sys.exit(-1)

    # TODO: статистика и гистограммы

"""
wg = WikiGraph()
wg.load_from_file('wiki_small.txt')

#1 path Python --> Spisok...
k = wg.get_number_of_pages()

x = wg.get_id('Python\n')
y = wg.get_id('Список_файловых_систем\n')

d = [10**9 for i in range(k)]
d[x] = 0
prev = [None] * k
used = [False] * k
min_d = 0
min_v = x
while min_d < 10**9:
    i = min_v
    used[i] = True
    for neighbour in wg.get_links_from(i):
        if d[i] + 1 < d[neighbour]:
            d[neighbour] = d[i] + 1
            prev[neighbour] = i
    min_d = 10**9
    for i in range(k):
        if not used[i] and d[i] < min_d:
            min_d = d[i]
            min_v = i
way = []
j = y
while j is not None:
    way.append(wg.get_title(j))
    j = prev[j]
way = way[::-1]
print('Найден путь: ', *way)


#2 number of redirecting articles
res2 = 0
for i in range(k):
    if wg.is_redirect(i):
        res2 += 1
print('Количество статей с перенаправлением: ', res2)

#3 minimal number of links from article
res3 = k
for i in range(k):
    u = wg.get_number_of_links_from(i)
    res3 = min(res3, u)
print('Минимальное количество ссылок из статьи: ', res3)

#4 number of articles with minimal number of links
res4 = 0
for i in range(k):
    if wg.get_number_of_links_from(i) == res3:
        res4 += 1
print('Количество статей с минимальным количеством ссылок: ', res4)

#5 maximal number of links from article
res5 = 0
for i in range(k):
    u = wg.get_number_of_links_from(i)
    res5 = max(res5, u)
print('Максимальное количество ссылок из статьи: ', res5)

#6 number of articles with maximal number of links
res6 = 0
for i in range(k):
    if wg.get_number_of_links_from(i) == res5:
        res6 += 1
print('Количество статей с максимальным количеством ссылок: ', res6)

#7 article with maximal number of links
l = 0
while wg.get_number_of_links_from(l) != res5:
    l += 1
print('Статья с наибольшим количеством ссылок: ', wg.get_title(l))

#8 the sample arithmetic mean of links
res8 = []
for i in range(k):
    res8.append(wg.get_number_of_links_from(i))
print('Среднее количество ссылок в статье: ', "%.2f" % (statistics.mean(res8)))

#9 minimal number of outdoor links
res9 = k
outdoor = [0 for i in range(k)]
for i in range(k):
    for j in wg.get_links_from(i):
        outdoor[j] += 1
for i in range(k):
    res9 = min(res9, outdoor[i])
print('Минимальное количество ссылок на статью: ', res9)

#10 number of articles with #9
res10 = 0
for i in range(k):
    if outdoor[i] == res9:
        res10 += 1
print('Количество статей с минимальным количеством внешних ссылок: ', res10)

#11 maximal number of outdoor links
res11 = 0
for i in range(k):
    res11 = max(res11, outdoor[i])
print('Максимальное количество ссылок на статью: ', res11)

#12 number of articles with #11
res12 = 0
res13 = []
for i in range(k):
    if outdoor[i] == res11:
        res12 += 1
        res13.append(wg.get_title(i))
print('Количество статей с максимальным количеством внешних ссылок: ', res12)

#13 article with maximal number of outdoor links
print('Статья с наибольшим количеством внешних ссылок: ', res13)

#14 mean number of outdoor links
print('Среднее количество внешних ссылок на статью: ', "%.2f" % (statistics.mean(outdoor)))

#15 minimal number of redirecting
res15 = [0 for i in range(k)]
for i in range(k):
    if wg.is_redirect(i):
        for j in wg.get_links_from(i):
            res15[j] += 1
print('Минимальное количество перенаправлений на статью: ', min(res15))

#16 number of articles with #15
res16 = 0
res18 = 0
res19 = []
for i in range(k):
    if res15[i] == min(res15):
        res16 += 1
    if res15[i] == max(res15):
        res18 += 1
        res19.append(wg.get_title(i))

print('Количество статей с минимальным количеством внешних перенаправлений: ', res16)

#17 maximal number of redirecting
print('Максимальное количество перенаправлений на статью: ', max(res15))

#18 number of #17
print('Количество статей с максимальным количеством внешних перенаправлений: ', res18)

#19 title of the article with maximal number of redirecting
print('Статья с наибольшим количеством внешних перенаправлений: ', *res19)

#20 mean number of redirecting
print('Среднее количество внешних перенаправлений на статью: ', "%.2f" % (statistics.mean(res15)))