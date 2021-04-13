def make_search_body(keyword,start_date="2020-01-01",end_date="2020-12-31",size=500):
    body={
        "query": {
            "bool": {
                "must": [
                    {
                        "match_phrase": {
                            "text": {
                                "query": keyword
                            }
                        }
                    },
                    {
                        "range": {
                            "dt": {
                                "from": start_date
                            }
                        }
                    },
                    {
                        "range": {
                            "dt": {
                                "to": end_date
                            }
                        }
                    }
                ]
            }
        },
        "from": 0,
        "size": size
    }
    return body
