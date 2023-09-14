# import re
#
# from bs4 import BeautifulSoup
#
#
# with open('blank/index.html') as file:
#     src = file.read()
# # print(src)
#
# soup = BeautifulSoup(src, "lxml")


# title = soup.title
# print(title)
# print(title.string)
# print(title.text)

# .find(), .find_all()
# page_h1 = soup.find("h1")
# print(page_h1)
#
# page_h1_all = soup.find_all("h1")
# print(page_h1_all)
#
# for item in page_h1_all:
#     print(item.text)

# user_name = soup.find("div", class_="user__name")
# print(user_name.text.strip())

# user_name = soup.find("div", class_="user__name").find("span")
# print(user_name.text)


# user_name = soup.find("div", {"class": "user__name"}).find("span")
# print(user_name.text)


# find_all_spans_in_user_info = soup.find(class_="user__info").find_all("span")
# print(find_all_spans_in_user_info[0].text)

# for item in find_all_spans_in_user_info:
#     print(item.text)

# social_list = soup.find(class_="social__networks").find("ul").find_all("a")
# print(social_list)
#
# for link in social_list:
#     print(link.text)

# social_list = soup.find_all("a")
# # print(social_list)
#
# for item in social_list:
#     item_text = item.text
#     item_url = item.get('href')
#     item_url1 = item['href']
#     print(f"{item_text}: {item_url}")

# .find_parent(), .find_parents()

# post_div = soup.find(class_="post__text").find_parent()
# print(post_div)


# post_div = soup.find(class_="post__text").find_parents()
# print(post_div)

# .next_element, .previous_element

# next_el = soup.find(class_="post__title").next_element.next_element.text
# print(next_el)
#
# next_el = soup.find(class_="post__title").find_next().text
# print(next_el)


# soup.find_next_sibling(), soup.find_previous_sibling()

# next_sib = soup.find(class_="post__title").find_next_sibling()
# print(next_sib.text)

# find_a_by_text = soup.find("a", text=re.compile("Instagram"))
# print(find_a_by_text)

# find_all_instagram = soup.find_all(text=re.compile("[Ii]nstagram"))
# print(find_all_instagram)

import csv
with open('eggs.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
    spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])