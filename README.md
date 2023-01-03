# Wikipedia Countries Scraper
A lightweight package that scrapes country data from wikipedia. Simply pass name of country, and the results are returned as an array of JSON objects. This is the assignment given by solar labs as a part of recruitment test 

# Problem Statement
Create an API using Django Rest Framework which has the following endpoint
localhost:8000/country_info/<country_name>

This API will scrape the information from a wikipedia’s country page and will return data in JSON format. You can use any tool for scraping, BeautifulSoup is the most popular.

For example

localhost:8000/country_info/india localhost:8000/country_info/united_states

Api with India as parameter will scrape the data from the infobar on the right side of
 https://en.wikipedia.org/wiki/India and will return the following data
 
 
 
 
{


‘flag_link’ : ‘https://upload.wikimedia.org/wikipedia/en/4/41/Flag_of_India.svg’, 

‘capital’ : ‘New Delhi’,

‘largest_city’: [‘Mumbai’, ‘New Delhi’], ‘official_languages’: [‘Hindi’,’English’], ‘area_total’: 3287263,

‘Population’: ‘1,352,642,280’,

‘GDP_nominal’: ‘ $3.050 trillion’,



}


This should work for all the countries in the world.
Look out for special cases like https://en.wikipedia.org/wiki/South_Africa which has 3 capitals and only one largest city. In this case return a list with all three in front of ‘capital’ and only a string in front of the ‘largest_city’. Similarly if there is just one official language of a country it should return just a string.


## Results
### For India ![1](https://user-images.githubusercontent.com/89767461/210044956-9328af92-6f25-4360-844f-cb265f8e4e81.png)
### For South Africa ![2](https://user-images.githubusercontent.com/89767461/210044976-41d7e8d4-2e2c-446f-93fd-9c9ce67089bb.png)
### For Germany ![image](https://user-images.githubusercontent.com/89767461/210045104-c34ed2e8-f927-4b4f-a1e5-f808583996f1.png)
### For Japan ![image](https://user-images.githubusercontent.com/89767461/210045163-822bb2af-ee43-4261-a51b-d82439ffca7e.png)

