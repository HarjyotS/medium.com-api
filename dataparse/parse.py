from bs4 import BeautifulSoup


async def gather_popular(data):
    soup = BeautifulSoup(data, "html.parser")
    # find all elements with class "bh fd fj bj aw em en at eo av ep fo aq"
    elem = soup.find_all("div", class_="gw gx gc n gy gz ha hb hc am")
    # go through all elements and extract the h3, the description and the link
    main = []
    for index, e in enumerate(elem):
        if index == 100:
            continue
        else:
            try:
                # extract the h3
                title = e.find_all("h3")
                desc = title[1].find("a").text
                # extract the link
                link = title[1].find("a").get("href")
                if "https://" not in link:
                    link = "https://medium.com" + link
                title = title[0].find("a").text
                author = e.find("div", class_="bh b ge bj aq").find("a").text
                author_link = (
                    e.find("div", class_="bh b ge bj aq").find("a").get("href")
                )
                if "https://" not in author_link:
                    author_link = "https://medium.com" + author_link
                # append results
                main.append(
                    {
                        "title": title,
                        "description": desc,
                        "link": link,
                        "author": author,
                        "author_link": author_link,
                    }
                )
            except:
                pass
    return main


async def search_topics(data):
    soup = BeautifulSoup(data, "html.parser")
    # find all elements with class "ec ag"
    elem = soup.find_all("div", class_="ec ag")
    # go through all elements and extract the h2, the description and the link
    main = []
    for e in elem:

        # extract the h2
        h2 = e.find("h2")
        # extract the description
        author = e.find("a", class_="au av aw ax ay az ba bb bc bd be bf bg bh bi").text
        desc = e.find("div", class_="h k aj ak by").find("p").text
        # extract the link
        authorl = e.find("div", class_="o ao lv").find("a").get("href")
        link = e.find("span", class_="bo b bp bq br").find("a").get("href")
        # print the results

        main.append(
            {
                "link": "https://medium.com" + str(link),
                "author": author,
                "author_link": "https://medium.com" + str(authorl),
                "description": desc,
                "title": h2.text,
            }
        )
    return main
