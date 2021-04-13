package main

import (
    "fmt"

    "github.com/cch123/elasticsql"
)


var sql = `
select * from wwwwww
where text like 'text'
and dt>="2017-01-01" and dt<="2017-12-31"
`

/*
var sql = `
select stock_index,count(1) from wwwwww
where aa in content
and dt>="2017-01-01" and dt<="2017-12-31"
group by stock_index
*/

func main() {
    dsl, esType, _ := elasticsql.Convert(sql)
    fmt.Println(dsl)
    fmt.Println(esType)        
    fmt.Println("aaa")        
}
