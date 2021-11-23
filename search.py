from elasticsearch import Elasticsearch
from datetime import timedelta, date


class Politician:
    def __init__(self, name, position, party, district, contact_information, overall_rank, participated_in_parliament,
                 related_subjects, date_of_birth, gender, school, first_degree, post_grads, terms_in_parliament,
                 biography):
        self.name = name
        self.position = position
        self.party = party
        self.district = district
        self.contact_information = contact_information
        self.overall_rank = overall_rank
        self.participated_in_parliament = participated_in_parliament
        self.related_subjects = related_subjects
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.school = school
        self.first_degree = first_degree
        self.post_grads = post_grads
        self.terms_in_parliament = terms_in_parliament
        self.biography = biography

    def print_me(self):
        print("name: " + self.name)
        print("position: " + self.position)
        print("party: " + self.party)
        print("district: " + self.district)
        print("contact_information: " + str(self.contact_information))
        print("overall_rank: " + self.overall_rank)
        print("participated_in_parliament: " + self.participated_in_parliament)
        print("related_subjects: " + str(self.related_subjects))
        print("date_of_birth: " + str(self.date_of_birth))
        print("gender: " + self.gender)
        print("school: " + str(self.school))
        print("first_degree: " + self.first_degree)
        print("post_grads: " + self.post_grads)
        print("terms_in_parliament: " + self.terms_in_parliament)
        print("biography: " + self.biography)
        print("=======================================================================\n")


es = Elasticsearch([{'host': 'localhost', 'port': 9200}])


def search_text(search_term):
    results = es.search(index='politicians2', body={
        "size": 500,
        "query": {
            "multi_match": {
                "query": search_term,
                "type": "best_fields",
                "fields": ["name", "position", "party", "district", "contact_information", "overall_rank",
                           "related_subjects", "gender", "school", "first_degree", "post_grads", "terms_in_parliament",
                           "biography"]
            }
        }
    })

    results = (results["hits"]["hits"])
    print("Number of search results: ", len(results))
    for result in results:
        a = result["_source"]
        Politician(a['name'], a['position'], a['party'], a['district'], a['contact_information'], a['overall_rank'],
                   a['participated_in_parliament'],
                   a['related_subjects'], a['date_of_birth'], a['gender'], a['school'], a['first_degree'],
                   a['post_grads'], a['terms_in_parliament'],
                   a['biography']).print_me()


def phrase_queries(search_term, attribute):
    results = es.search(index='politicians2', body={
        "size": 500,
        "query": {
            "match_phrase": {
                attribute: {
                    "query": search_term
                }
            }
        }
    })

    results = (results["hits"]["hits"])
    print("Number of search results: ", len(results))
    for result in results:
        a = result["_source"]
        Politician(a['name'], a['position'], a['party'], a['district'], a['contact_information'], a['overall_rank'],
                   a['participated_in_parliament'],
                   a['related_subjects'], a['date_of_birth'], a['gender'], a['school'], a['first_degree'],
                   a['post_grads'], a['terms_in_parliament'],
                   a['biography']).print_me()


def faceted_search(search_term, attributes):
    final_attributes = {"name": 1,
                        "position": 1,
                        "party": 1,
                        "contact_information": 1,
                        "overall_rank": 1,
                        "related_subjects": 1,
                        "gender": 1,
                        "school": 1,
                        "first_degree": 1,
                        "post_grads": 1,
                        "terms_in_parliament": 1,
                        "biography": 1
                        }
    for attribute in attributes:
        final_attributes[attribute] = 5
    fields = []
    for final_attribute in final_attributes:
        fields.append(final_attribute + "^" + str(final_attributes[final_attribute]))
    results = es.search(index='politicians2', body={
        "size": 500,
        "query": {
            "multi_match": {
                "query": search_term,
                "type": "best_fields",
                "fields": fields
            }
        }
    })

    results = (results["hits"]["hits"])
    print("Number of search results: ", len(results))
    for result in results:
        a = result["_source"]
        Politician(a['name'], a['position'], a['party'], a['district'], a['contact_information'], a['overall_rank'],
                   a['participated_in_parliament'],
                   a['related_subjects'], a['date_of_birth'], a['gender'], a['school'], a['first_degree'],
                   a['post_grads'], a['terms_in_parliament'],
                   a['biography']).print_me()


def find_politicians_older_than(age):
    start_date = str(date.today() - timedelta(days=age * 365))
    results = es.search(index='politicians2', body={
        "size": 500,
        "query": {
            "range": {
                "date_of_birth": {
                    "gt": "1800-12-31",
                    "lte": start_date
                }
            }
        }
    }
                        )

    results = (results["hits"]["hits"])
    print("Number of search results: ", len(results))
    for result in results:
        a = result["_source"]
        Politician(a['name'], a['position'], a['party'], a['district'], a['contact_information'], a['overall_rank'],
                   a['participated_in_parliament'],
                   a['related_subjects'], a['date_of_birth'], a['gender'], a['school'], a['first_degree'],
                   a['post_grads'], a['terms_in_parliament'],
                   a['biography']).print_me()


def count_by_category(category):
    results = es.search(index='politicians2', body={
        "aggs": {
            "by_category": {
                "terms": {
                    "field": category,
                    "size": 100
                }
            }
        }
    }
                        )
    for i in results['aggregations']['by_category']['buckets']:
        print(i['key'], i['doc_count'])


def top_n_politicians(n, field, search_term):
    results = es.search(index='politicians2', body={
        "size": n,
        "query": {
            "match_phrase": {
                field: {
                    "query": search_term
                }
            }
        },
        "sort": [{"participated_in_parliament": "desc"}]

    })

    results = (results["hits"]["hits"])
    print("Number of search results: ", len(results))
    for result in results:
        a = result["_source"]
        Politician(a['name'], a['position'], a['party'], a['district'], a['contact_information'], a['overall_rank'],
                   a['participated_in_parliament'],
                   a['related_subjects'], a['date_of_birth'], a['gender'], a['school'], a['first_degree'],
                   a['post_grads'], a['terms_in_parliament'],
                   a['biography']).print_me()

# search_text("කැලණිය ධර්මාලෝක විද්‍යාලය")
# phrase_queries("කැලණිය ධර්මාලෝක විද්‍යාලය", "school")
# faceted_search("නාලන්දා විද්‍යාලය", ["school", "first_degree", "post_grads", "terms_in_parliament", "biography"])
# find_politicians_older_than(85)
# count_by_category("district")
# count_by_category("gender")
# top_n_politicians(20, "gender", "ස්ත්‍රී")
# top_n_politicians(10, "district", "රත්නපුර දිස්ත්‍රික්කය")
