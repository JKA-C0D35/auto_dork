import os
import time
import random
import  webbrowser as wb


dork_list = [
    # Philippines (.ph)
    'inurl: php?id=1 site:.ph',
    'inurl:php?id= site:edu.ph',
    'inurl:?page_id= site:.ph',
    'inurl:newsdetail.php?id= site:.edu.ph',
    'inurl:product.php?id= site:.ph',
    'inurl:blog.php?id= site:.ph',
    'inurl:article.php?id= site:.ph',
    'inurl:page.php?id= site:.ph',
    'inurl:view.php?id= site:.ph',
    'inurl:item.php?id= site:.ph',
    'inurl:profile.php?id= site:.ph',
    'inurl:shop.php?id= site:.ph',
    'inurl:details.php?id= site:.ph',
    'inurl:event.php?id= site:.ph',
    'inurl:gallery.php?id= site:.ph',
    'inurl:forum.php?id= site:.ph',
    'inurl:php?id=1 site:.ph',
    'inurl:php?id= site:.ph',
    'inurl:?page_id= site:.ph',
    'inurl:news.php?id= site:.ph',
    'inurl:content.php?id= site:.ph',
    'inurl:about.php?id= site:.ph',
    'inurl:service.php?id= site:.ph',
    'inurl:team.php?id= site:.ph',
    'inurl:profile.php?id= site:.ph',
    'inurl:blog-detail.php?id= site:.ph',
    'inurl:article-detail.php?id= site:.ph',
    'inurl:gallery-detail.php?id= site:.ph',
    'inurl:category.php?id= site:.ph',
    'inurl:product-detail.php?id= site:.ph',
    'inurl:case-study.php?id= site:.ph',
    'inurl:faq.php?id= site:.ph',
    'inurl:portfolio.php?id= site:.ph',
    'inurl:projects.php?id= site:.ph',
    'inurl:testimonials.php?id= site:.ph',
    'inurl:partners.php?id= site:.ph',
    'inurl:services.php?id= site:.ph',
    'inurl:contact.php?id= site:.ph',
    'inurl:careers.php?id= site:.ph',
    'inurl:newsdetail.php?id= site:.edu',
    'inurl:product.php?id= site:.gov',
    'inurl:blog.php?id= site:.in',
    'inurl:article.php?id= site:.com',
    'inurl:page.php?id= site:.org',
    'inurl:view.php?id= site:.net',
    'inurl:item.php?id= site:.info',
    'inurl:profile.php?id= site:.edu',
    'inurl:shop.php?id= site:.gov',
    'inurl:details.php?id= site:.co.uk',
    'inurl:event.php?id= site:.au',
    'inurl:gallery.php?id= site:.ca',
    'inurl:forum.php?id= site:.za',
    'inurl: php?id=1 site:.ph',
    'inurl:php?id= site:edu.ph',
    'inurl:?page_id= site:.ph',
    'inurl:news.php?id= site:.ph',
    'inurl:newsdetail.php?id= site:.edu.ph',
    'inurl:product.php?id= site:.ph',
    'inurl:blog.php?id= site:.ph',
    'inurl:article.php?id= site:.ph',
    'inurl:page.php?id= site:.ph',
    'inurl:view.php?id= site:.ph',
    'inurl:item.php?id= site:.ph',
    'inurl:profile.php?id= site:.ph',
    'inurl:shop.php?id= site:.ph',
    'inurl:details.php?id= site:.ph',
    'inurl:event.php?id= site:.ph',
    'inurl:gallery.php?id= site:.ph',
    'inurl:forum.php?id= site:.ph',
    'inurl:php?id=1 site:.ph',
    'inurl:php?id= site:.ph',
    'inurl:?page_id= site:.ph',
    'inurl:news.php?id= site:.ph',
    # United States (.us)
    'inurl:newsdetail.php?id= site:.us',
    'inurl:product.php?id= site:.us',
    'inurl:blog.php?id= site:.us',
    'inurl:article.php?id= site:.us',
    'inurl:page.php?id= site:.us',
    'inurl:view.php?id= site:.us',
    'inurl:item.php?id= site:.us',
    'inurl:profile.php?id= site:.us',
    'inurl:shop.php?id= site:.us',
    'inurl:details.php?id= site:.us',
    'inurl:event.php?id= site:.us',
    'inurl:gallery.php?id= site:.us',
    'inurl:forum.php?id= site:.us',
    'inurl:php?id=1 site:.us',
    'inurl:php?id= site:.us',
    'inurl:?page_id= site:.us',
    'inurl:news.php?id= site:.us',
    # United Kingdom (.uk)
    'inurl:newsdetail.php?id= site:.uk',
    'inurl:product.php?id= site:.uk',
    'inurl:blog.php?id= site:.uk',
    'inurl:article.php?id= site:.uk',
    'inurl:page.php?id= site:.uk',
    'inurl:view.php?id= site:.uk',
    'inurl:item.php?id= site:.uk',
    'inurl:profile.php?id= site:.uk',
    'inurl:shop.php?id= site:.uk',
    'inurl:details.php?id= site:.uk',
    'inurl:event.php?id= site:.uk',
    'inurl:gallery.php?id= site:.uk',
    'inurl:forum.php?id= site:.uk',
    'inurl:php?id=1 site:.uk',
    'inurl:php?id= site:.uk',
    'inurl:?page_id= site:.uk',
    'inurl:news.php?id= site:.uk',
    # Canada (.ca)
    'inurl:newsdetail.php?id= site:.ca',
    'inurl:product.php?id= site:.ca',
    'inurl:blog.php?id= site:.ca',
    'inurl:article.php?id= site:.ca',
    'inurl:page.php?id= site:.ca',
    'inurl:view.php?id= site:.ca',
    'inurl:item.php?id= site:.ca',
    'inurl:profile.php?id= site:.ca',
    'inurl:shop.php?id= site:.ca',
    'inurl:details.php?id= site:.ca',
    'inurl:event.php?id= site:.ca',
    'inurl:gallery.php?id= site:.ca',
    'inurl:forum.php?id= site:.ca',
    'inurl:php?id=1 site:.ca',
    'inurl:php?id= site:.ca',
    'inurl:?page_id= site:.ca',
    'inurl:news.php?id= site:.ca',
    # Australia (.au)
    'inurl:newsdetail.php?id= site:.au',
    'inurl:product.php?id= site:.au',
    'inurl:blog.php?id= site:.au',
    'inurl:article.php?id= site:.au',
    'inurl:page.php?id= site:.au',
    'inurl:view.php?id= site:.au',
    'inurl:item.php?id= site:.au',
    'inurl:profile.php?id= site:.au',
    'inurl:shop.php?id= site:.au',
    'inurl:details.php?id= site:.au',
    'inurl:event.php?id= site:.au',
    'inurl:gallery.php?id= site:.au',
    'inurl:forum.php?id= site:.au',
    'inurl:php?id=1 site:.au',
    'inurl:php?id= site:.au',
    'inurl:?page_id= site:.au',
    'inurl:news.php?id= site:.au',
    # India (.in)
    'inurl:newsdetail.php?id= site:.in',
    'inurl:product.php?id= site:.in',
    'inurl:blog.php?id= site:.in',
    'inurl:article.php?id= site:.in',
    'inurl:page.php?id= site:.in',
    'inurl:view.php?id= site:.in',
    'inurl:item.php?id= site:.in',
    'inurl:profile.php?id= site:.in',
    'inurl:shop.php?id= site:.in',
    'inurl:details.php?id= site:.in',
    'inurl:event.php?id= site:.in',
    'inurl:gallery.php?id= site:.in',
    'inurl:forum.php?id= site:.in',
    'inurl:php?id=1 site:.in',
    'inurl:php?id= site:.in',
    'inurl:?page_id= site:.in',
    'inurl:news.php?id= site:.in',
    # South Africa (.za)
    'inurl:newsdetail.php?id= site:.za',
    'inurl:product.php?id= site:.za',
    'inurl:blog.php?id= site:.za',
    'inurl:article.php?id= site:.za',
    'inurl:page.php?id= site:.za',
    'inurl:view.php?id= site:.za',
    'inurl:item.php?id= site:.za',
    'inurl:profile.php?id= site:.za',
    'inurl:shop.php?id= site:.za',
    'inurl:details.php?id= site:.za',
    'inurl:event.php?id= site:.za',
    'inurl:gallery.php?id= site:.za',
    'inurl:forum.php?id= site:.za',
    'inurl:php?id=1 site:.za',
    'inurl:php?id= site:.za',
    'inurl:?page_id= site:.za',
    'inurl:news.php?id= site:.za'
]

def dork():
    print("\033[32m \n[+] Dork List:\n \033[0m")
    for i, d in enumerate(dork_list, start=1):
        time.sleep(0.1)
        print(f"\033[32m[{i}] {d}\033[0m")

    choice = input("\033[32m \nroot@dorker:~# \033[0m")

    try:
        choice_dork = dork_list[int(choice) -1]
        
        if "inurl:" not in choice_dork:
          print("[-] Invalid Choice!")

        else:
            print(f"\033[32m \n[+] Selected: {choice_dork}\033[0m\n")
            print("\033[32m Searching...... \033[0m")
            perform_dork_search([choice_dork])


    except (IndexError, ValueError):
        print("[-] Invalid input!")

def perform_dork_search(dork_queries):
    for query in dork_queries:
        url = "https://www.google.com/search?q=" + query.replace(" ", "%20")
        wb.open(url)

dork()