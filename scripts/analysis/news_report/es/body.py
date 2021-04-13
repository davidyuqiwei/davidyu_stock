body={
    "query": {
        "bool": {
            "must": [
                {
                    "match": {
                        "text": {
                            "query": "独特"
                        }
                    }
                }, 
                {
                    "range": {
                        "dt": {
                            "from": "2018-01-01"
                        }
                    }
                }, 
                {
                    "range": {
                        "dt": {
                            "to": "2020-12-31"
                        }
                    }
                }
            ]
        }
    }, 
    "from": 0, 
    "size": 10000
}
