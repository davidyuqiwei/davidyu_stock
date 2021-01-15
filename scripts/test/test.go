package main

import (
    "fmt"

    "github.com/cch123/elasticsql"
)

var sql = `
select * from aaa
where a=1 and x = '三个男人'
and create_time between '2015-01-01T00:00:00+0800' and '2016-01-01T00:00:00+0800'
and process_id > 1 order by id desc limit 100,10
`

func main() {
    dsl, esType, _ := elasticsql.Convert(sql)
    fmt.Println(dsl)
    fmt.Println(esType)
}




