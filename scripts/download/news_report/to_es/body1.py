body1={
    "query": {
        "bool": {
            "must": [
                {
                    "match_phrase": {
                        "text": {
                            "query": "text"
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
    "size": 0,
    "aggregations": {
        "stock_index": {
            "aggregations": {
                "COUNT(1)": {
                    "value_count": {
                        "field": "1"
                    }
                }
            },
            "terms": {
                "field": "stock_index",
                "size": 200
            }
        }
    }
}
