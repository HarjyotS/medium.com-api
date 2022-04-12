
# [MEDIUM.COM API](https://mediumapi.harjyotsahni.com/)

# Assigment
Create an API that can crawl medium.com for the purpose of web indexing or gathering data on a particular topic. The API  can show trending articles, authors, and topics from medium.com.

How I have accomplished this: I have created this api by using a headless browser that takes in a url, the need for a headless browser instead of the requests module is due to the system that medium.com uses to load articles, medium has a template for the search page and the popular page, this page includes javascript that queries a GraphQL database to fill in the template. A headless browser allows the computer to render the template and then it grabs the html. The html is then fed into a html parser called beautiful soup where all the data is extracted by css selectors and other identifying factors. 
Video showcase: https://www.youtube.com/watch?v=5rLN-SioRSY
Github Link: https://github.com/HarjyotS/slingshotbackend
# API Reference

#### Query a string for related 
```http
  GET /search/<query>
```
Query can be any string, **spaces are fine**.
##### [Search for databases on medium](https://mediumapi.harjyotsahni.com/search/database)

Example response:

```
{
   "content":[
      {
         "author":"Pavan Srinath",
         "author_link":"https://medium.com/@zeusisdead?source=search_post---------0-------------------------------",
         "description":"The Bangalore Water Supply and Sewerage Board (BWSSB) recently hiked its water tariff, a move that was long overdue. I am quoted in Citizen Matters on why this hike is a good move. The hike in BWSSB\u2019s water tariff is a welcome development that was long overdue. BWSBB has been\u2026",
         "link":"https://medium.com/indian-national-interest/a-long-overdue-hike-in-bangalores-water-prices-d2ca5801769c?source=search_post---------0-------------------------------",
         "title":"A Long Overdue Hike in Bangalore\u2019s Water Prices"
      },
      {
         "author":"Centre for Civil Society",
         "author_link":"https://medium.com/@ccsindia?source=search_post---------1-------------------------------",
         "description":"In this week\u2019s selection for #ThrowbackThursday, we have a piece by Minoo Masani, first published in Freedom First in 1976. In this piece, he talks about the dangers of inflation \u2014 tracing it fundamentally to the flawed economic policies of the government. \u2026",
         "link":"https://medium.com/spontaneous-order/throwbackthursday-m-r-masani-prices-are-like-water-1976-8860d73dd517?source=search_post---------1-------------------------------",
         "title":"#ThrowbackThursday: M R Masani \u2014 Prices are like Water (1976)"
      },
      {
         "author":"Hussain Maikah",
         "author_link":"https://medium.com/@hussainmaikah2020?source=search_post---------2-------------------------------",
         "description":"Reverse osmosis system in Pakistan A water purification process in which undesirable substances are removed from water by flowing water molecules under pressure through a semipermeable membrane. \u2026",
         "link":"https://medium.com/@hussainmaikah2020/water-logic-offers-best-ro-plants-in-pakistan-at-reasonable-prices-de8d04949ab1?source=search_post---------2-------------------------------",
         "title":"Water Logic Offers Best RO Plants In Pakistan At Reasonable Prices"
      }
   ]
}
```
Inside content you will always be given the keys, `title, description, link, author, author_link`.


#### Get popular articles.

```http
  GET /popular
```
##### [Get Popular](https://mediumapi.harjyotsahni.com/popular)
Example response:
```
{
   "content":[
      {
         "author":"Jolie A. Doggett",
         "author_link":"https://medium.com/@joliedoggett?source=topic_page---------0------------------1-------------",
         "description":"Struggling with writer\u2019s block? We may have the solution\u2026",
         "link":"https://medium.com/creators-hub/how-have-you-changed-write-here-7-4d7227b5e377?source=topic_page---------0------------------1-------------",
         "title":"How Have You Changed? | Write Here 7"
      },
      {
         "author":"Danielle Moodie",
         "author_link":"https://medium.com/@daniellemoodie?source=topic_page---------1------------------1-------------",
         "description":"Testimony from the Jan. 6 Capitol riot shows us exactly who we are",
         "link":"https://zora.medium.com/actually-this-is-america-143efa23994d?source=topic_page---------1------------------1-------------",
         "title":"Actually, This IS America"
      },
      {
         "author":"Garfield Hylton",
         "author_link":"https://garfield-hylton.medium.com/?source=topic_page---------2------------------1-------------",
         "description":"A Florida officer getting 12 years in prison for planting drugs on suspects triggered me and probably you too.",
         "link":"https://momentum.medium.com/cops-framing-suspects-my-take-on-why-every-traffic-stop-is-terrifying-443d03c58a5d?source=topic_page---------2------------------1-------------",
         "title":"Cops Framing Suspects: My Take on Why Every Traffic Stop Is Terrifying"
      }
   ]
}
```
Inside content you will always be given the keys, `title, description, link, author, author_link`.


## Installation and Setup
### **WINDOWS ONLY**

### Installation
Install with git

```bash
  git clone https://github.com/HarjyotS/slingshotbackend.git
```
Or download zip from github.

### Setup
Open command line and install requirements.
`pip install -r requirements.`


## Deployment
`python server.py`

Your api will now run locally on port 80!
You can access it by going to `https://localhost:80` or `https://localhost`
