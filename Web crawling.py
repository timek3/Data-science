from urllib import request
from bs4 import BeautifulSoup
import csv

with open('output.csv', mode='w+', newline='', encoding='utf-8') as f:
    fieldnames = ['Nick', 'Data', 'Komentarz']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for i in range(20):
        start_website = "https://www.pudelek.pl/artykul/144515/taniec_z_gwiazdami_justyna_zyla_odpadla_z_programu/"+str(i)+"/#comments"
        site = BeautifulSoup(request.urlopen(start_website).read(), "html.parser")
        div = site.findAll("div", class_='comment', limit=None)
        for data in div:
            nick = data.find(class_='comment-author')
            date = data.find(class_='comment-date')
            comment = data.find(class_='comment-text')
            writer.writerow({'Nick': nick.text, 'Data': date.text, 'Komentarz': comment.text.strip()})

#backup
#     start_website = "https://www.pudelek.pl/artykul/144515/taniec_z_gwiazdami_justyna_zyla_odpadla_z_programu/1/#comments"
#     site = BeautifulSoup(request.urlopen(start_website).read(), "html.parser")
#     div = site.findAll("div", class_='comment', limit=None)
#     #details = site.findAll(class_='comment-details')
#     #comments = site.findAll(class_='comment-text')
#     with open('output.csv', 'w', newline='') as f:
#         fieldnames = ['Nick', 'Data', 'Komentarz']
#         writer = csv.DictWriter(f, fieldnames = fieldnames)
#         writer.writeheader()
#         for data in div:
#             nick = data.find(class_='comment-author')
#             date = data.find(class_='comment-date')
#             comment = data.find(class_='comment-text')
#             writer.writerow({'Nick': nick.text, 'Data': date.text, 'Komentarz': comment.text.lstrip()})


#Wczeniejsze proby
#dataset = [(x.text, y.text) for x,y in zip(details, comments)]
#print(dataset)
# with open("output.csv", "w", newline='') as csvfile:
#     writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
#     for data in site.findAll(class_=['comment-details', 'comment-text']):
#         details = data.findAll(class_='comment-details')
#         comments = data.findAll(class_='comment-text')
#         writer.writerow(details.text, comments.text)

# with open('output.csv', 'wb') as f:
#     csv.writer(f).writerow("Nazwa,Data,Komentarz")
# for komentarze in site.findAll(class_=['comment-details','comment-text']):
#     with open('output.csv', 'wb') as f:
#         csv.writer(f).writerow(komentarze.text)


