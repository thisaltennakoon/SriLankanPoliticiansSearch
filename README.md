# Sri Lankan Politicians Search
Information Retrieval Project
This repository contain source code for Sri Lankan Politicians Search engine created using Python and Elasticsearch

## Directory Structure

The important files and directories of the repository is shown below

    ├── scrape.py : Contains functions used to scrape data and store the scraped data in scraped.txt  
    ├── scraped.txt : data scraped from the [website](http://www.manthri.lk/)                      
    ├── preprocess.py : Contains the functions used to preprocess the scraped data and store the preprocessed data in preprocessed.json
    ├── preprocessed.json : Contains the cleaned data used to build the index
    ├── data_upload.py : Contains functions used to upload data to elasticsearch cluster
    ├── search.py : Contains functions used to map user search phrases and elasticsearch queries        


## Starting the search app

### Starting the elasticsearch cluster

Source codes provided in this repository can be used to interact with the elasticsearch cluster installed locally. 
For more details visit [website](https://www.elastic.co/guide/en/elasticsearch/reference/current/getting-started-install.html)
But you can use their cloud deployments to do the same things. For more details regarding cloud deployments, visit [youtube](https://www.youtube.com/watch?v=CCTgroOcyfM)

Once elasticsearch is install, start elasticsearch cluster on port 9200

## Data fields 

Each Politician instance contains following data fields

1. name: තලතා අතුකෝරල
2 .position: පාර්ලිමේන්තු මන්ත්‍රී
3 .party: සමගි ජන බලවේගය
4 .district: රත්නපුර දිස්ත්‍රික්කය
5 .contact_information: ['452274287', 'atukorale_t@parliament.lk']
6. overall_rank: 24
7. participated_in_parliament: 13
8. related_subjects: ['අයිතිවාසිකම් හා නියෝජනය', 'යුක්තිය, ආරක්ෂාව හා මහජන සාමය', 'අධ්\u200dයාපන', 'ආණ්ඩුකරණ, පරිපාලන හා පාර්ලිමේන්තු කටයුතු', 'ආර්ථික හා මුල්\u200dය']
9. date_of_birth: 1963-05-30
10. gender: ස්ත්‍රී
11. school: ['R/Ferguson උසස් පාසල, රත්නපුර', 'ශාන්ත බිෂොප් විද්\u200dයාලය', 'මියුසියස් විද්\u200dයාලය']
12. first_degree: ශ්‍රී ලංකා නීති විද්‍යාලය, කොළඹ
13. post_grads:
14. terms_in_parliament: 2020-08-20 සිට අද දක්වා
15. biography: තලතා අතුකෝරල මහත්මිය 1963-05-30 දින උපත ලබා ඇත.මෙතුමිය R/Ferguson උසස් පාසල, රත්නපුර ශාන්ත බිෂොප් විද්‍යාලය මියුසියස් විද්‍යාලය යන පාසල්වල අධ්යාපනය ලබා ඇත.තම ප්‍රථම උපාධිය ශ්‍රී ලංකා නීති විද්‍යාලය, කොළඹ ලබාගෙන ඇත.2020-08-20 සිට අද දක්වා සමගි ජන බලවේගය නියෝජනය කරමින් පාර්ලිමේන්තුවේ අසුන් ගෙන සිටී.

## Data Scraping process

The process with scraping data from the site, the HTML/XML parsing library BeautifulSoup was used for scraping the web pages. Then the text extracted was passed through the text processing unit. Both simple techniques like replacing complex methods like regex are used for this process. This text processing unit generates cleaned text data which is then passed to the translator to translate to Sinhala, here both translation and transliteration takes place. Then the translated data is sent for post processing and the final data set with an aggregated dataset containing information about fields is generated

![Scraping process](scraper.png)

## Search Process

### Indexing and quering

For indexing the data and querying the Elasticsearch is used and I have used the standard indexing methods,mapping and the analyzer provided in the Elasticsearch. When a user enters a query the related intent is identified and the search query is related to the intent is executed. The searching can be done related to any field in the index and predefined size is used which the user can override using his search query. Also filtered queries are provided where users can filter the search result. 

## Advance Features                  
* Text mining and text preprocessing
    * Search queries are processed before intent classification, here spelling errors are corrected and the query is cleaned. Also data extracted is also cleaned and processed before displaying on the web application.
* Intent Classification
    * Once the query is added, intent behind the query is found by intent classification. The intent could be simple text search or a select top type, etc. The intent classifier used word tokenization and text vectorization and cosine distance to classify intentens
* Faceted Search
    * The search engine supported faceted search related to Genre, Artist, Composer and Lyricist. 
* Bilingual support
    * The search engine supports queries in both Sinhala and English. User can type queries like top 10 songs or හොඳම ගීත 10 and expect to yield the same result.
* Synonyms support
    * The search engine also support synonyms and that can be either in Sinhala or in English, user can type best, popular, good instead of top or හොඳ, ජනප්රිය, ප්‍රසිද්ධ instead of හොඳම. 
* Resistant to simple spelling errors
    * Due to the use of vectorization and distance calculation the search engine is resistant to small spelling errors and these are automatically corrected and related search results are generated.


![search process](search.png)


