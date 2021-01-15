body={
    "query": {
        "bool": {
            "must": [
                {
                    "match": {
                        "text": {
                            "query": "地热"
                        }
                    }
                }, 
                {
                    "range": {
                        "dt": {
                            "from": "2017-01-01"
                        }
                    }
                }, 
                {
                    "range": {
                        "dt": {
                            "to": "2017-12-31"
                        }
                    }
                }
            ]
        }
    }, 
    "from": 0, 
    "size": 100
}
