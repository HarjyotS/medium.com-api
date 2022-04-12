from pyppeteer import launch


async def getdata(url):
    browser = await launch(handleSIGINT=False, handleSIGTERM=False, handleSIGHUP=False)
    page = await browser.newPage()
    await page.goto(
        url,
        {"waitUntil": "networkidle2"},
    )
    await page.waitFor(3)
    await page.setViewport({"width": 1920, "height": 1280})
    c = await page.content()
    # screenshot page
    await page.screenshot({"path": "screenshot.png"})
    with open("medium.html", "w", encoding="utf-8") as f:
        f.write(c)
    await browser.close()
    return c


# import time

# a = time.time()
# c = asyncio.get_event_loop().run_until_complete(
#     getdata(
#         "https://medium.com/search?source=home----------------------------------------&q=fortnite"
#     )
# )
# d = asyncio.get_event_loop().run_until_complete(search_topics(c))
# print(time.time() - a, "seconds")
# # print(d)
# # print all the values out pretty
# for i in d:
#     print(i["title"])
#     print(i["description"])
#     print(i["link"])
#     print(i["author"], "author")
#     print(i["author_link"], "author_link")
#     print("\n\n")
# print(time.time() - a, "seconds")
