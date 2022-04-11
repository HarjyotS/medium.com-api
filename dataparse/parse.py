from bs4 import BeautifulSoup


async def search_topics(data):
    soup = BeautifulSoup(data, "html.parser")
    # find all elements with class "l dt ki"
    elem = soup.find_all("div", class_="l dt ki")
    # go through all elements and extract the h2, the description and the link
    main = []
    for e in elem:
        # extract the h2
        h2 = e.find("h2")
        # extract the description
        desc = e.find("p")
        # extract the link
        link = e.find("a")
        # print the results
        print("\n")
        main.append(
            {
                "title": h2.text,
                "description": desc.text,
                "link": "https://medium.com" + str(link.get("href")),
            }
        )
    return main
