# Define server logic required to draw a histogram ----
library("plotly")
library(dplyr)
#import_owner = read.csv("/home/davidyu/stock/data/daily_report/2021-02-02/important_owner_today_report_2021-02-02.csv")
#names(import_owner)=c("stock_index","stock_name","owner_name","type","date","volume")


bankuai = read.csv("/home/davidyu/stock/scripts/davidyu_stock/scripts/analysis/bankuai/bankuai_zde.csv")
server <- function(input, output,session) {
  IP <- reactive({ input$getIP })

  observe({
    cat(capture.output(str(IP()), split=TRUE))
    #cat(print(Sys.Time()))
  })

  # 1. It is "reactive" and therefore should be automatically
  #    re-executed when inputs (input$bins) change
  # 2. Its output type is a plot
    
    #############################
    #-------重要股东变化--------#
    #############################
    output$table_import_owner <- DT::renderDataTable({
        source("task_important_owner.r")
        print(paste0("login time: ",Sys.time()))
        data_out = import_owner_data(input)
        DT::datatable(data_out,options=list(lengthMenu =c(25,50,100),fixedColumns = TRUE,autoWidth = TRUE))
    })

    #############################
    #-------股东变化--------#
    #############################
    output$table_owner_change<- DT::renderDataTable({
        #source("task_important_owner.r")
        data_out = read.csv("/home/davidyu/stock/data/shiny_data/data/all_owner.csv")
        #print("-----------")
        print(input$change_type)
        if(input$gudong_type!="all"){
            data_out = filter(data_out,gudong_type==input$gudong_type)
        }
        if(input$change_type!="all"){
            data_out = filter(data_out,change_type%in%input$change_type)
        }

        #data_out = filter(data_out,gudong_type==input$gudong_type)
        print(paste0("login time: ",Sys.time()))
       data_out = data_out[,input$gudongbianhua]
        DT::datatable(data_out,options=list(lengthMenu =c(25,50,100),fixedColumns = TRUE,autoWidth = TRUE,
                      columnDefs = list(list( className = 'dt-center', targets = "_all", width = '100px'  ))))
    })
    #############################
    #---------大宗交易----------#
    #############################
    output$table_dzjy <- DT::renderDataTable({
        source("task_dazongjiaoyi.r")
        df2 = dazongjiaoyi_data(input)
        DT::datatable(df2, options = list(orderClasses = TRUE))
        #DT::datatable(dzjy, options = list(orderClasses = TRUE))
    })

    #############################
    #-----------trend-----------#
    #############################
    output$pl_trend <- renderPlotly({
        source("task_trend.r")
        return_val = trend_plot(input)
        p_close=return_val$p_out
        p_turnover = return_val$p2
        p_gudong_num = return_val$p_gudong_num
        subplot(p_close,p_turnover,p_gudong_num,nrows=3,margin=0.08,shareX=FALSE) %>% layout(title="",height=1200,margin=1)
        #p
    })
    
    #############################
    #-----------MACD-----------#
    #############################
    output$pl_macd <- renderPlotly({
        source("task_macd.r")
        return_val = trend_plot(input)
        p_close = return_val$p_out
        p_macd1 = return_val$p2
        p_macd2 = return_val$p_macd2
        p_macd3 = return_val$p_macd3
        subplot(p_close,p_macd1,p_macd2,p_macd3,nrows=4,margin=0.05,shareX=TRUE) %>% layout(title="",height=1200,margin=1)
        #p
    })
    #############################
    #-----------技术指标--------#
    #############################
    
    output$table_tech_index<- DT::renderDataTable({
        #source("task_important_owner.r")
        data_out = read.csv("/home/davidyu/stock/data/shiny_data/data/hs300_tech_index.csv")
        data_out$stock_index = formatC(data_out$stock_index,width=6,flag='0')
        DT::datatable(data_out,width="30px",extensions = c('FixedColumns'),rownames= FALSE,
                        options=list(lengthMenu =c(15,50,100),autoWidth = TRUE,scrollX = TRUE,
                                        fixedColumns = list(leftColumns = 2, rightColumns = 0),
                                        columnDefs = list(list( className = 'dt-center', targets = "_all", width = '100px' ))
                                            )) %>%
                          formatStyle(c(0:30), `border-right` = "solid 2px")
    })
    
    #############################
    #----------主力控盘---------#
    #############################
    
    output$table_zhulikongpan<- DT::renderDataTable({
        #source("task_important_owner.r")
        data_out = read.csv("../../data/zhulikongpan.csv")
        data_out$stock_index = formatC(data_out$stock_index,width=6,flag='0')
        DT::datatable(data_out, options = list(orderClasses = TRUE,lengthMenu =c(25,50,100),columnDefs = list(list( className = 'dt-center', 
                                    targets = "_all", width = '10px'  )))) %>% formatStyle(c(0:30), `border-right` = "solid 2px")
        #DT::datatable(data_out,width="3px",rownames= FALSE)
                        #options=list(lengthMenu =c(15,50,100),autoWidth = TRUE,scrollX = TRUE,
                        #                columnDefs = list(list( className = 'dt-center', targets = "_all", width = '10px' ))
                                           # )) 
    })
    #############################
    #-----------板块 -----------#
    #############################
    # change bankuai select
    outVar = reactive({
        df1 = df_out()
        area = unique(df1$bankuai_name)
        area
    })
    
    observe({
        updateSelectInput(session,"bankuai1",
            choices = outVar())
    })

    df_out = reactive({
        source("task_bankuai.r")
        data1 = bankuai_data(input)
        data1
    })
    ###
    output$table_bankuai <- DT::renderDataTable({
        source("task_bankuai.r")
        df1 = df_out()
        df2 = bankuai_table_data(df1,input)
        DT::datatable(df2, options = list(orderClasses = TRUE))
    })
    
    output$pl_bankuai <- renderPlotly({
	    data1 = df_out()
        #print(input$bankuai1)
	    data2 = filter(data1,bankuai_name== input$bankuai1)
        data2 = data2[order(data2$dt),]
        p = plot_ly(data=data2,x=data2$dt,y=data2$change_ratio,type="scatter",mode="markers+lines")
        p
    
    })

    #############################
    #------------大单-----------#
    #############################
    
    v <- reactiveValues(data = NULL)
    observeEvent(input$button2, {
        print("click the button")
        v$data=1
        print(v$data)
    })

    output$pl_dadan <- renderPlotly({
        #print(randomVals())
        #if_plot = randomVals()
        if(v$data == 1){
            #y = data1[,y_col]
	        source('task_dadan.r')
            return_val=data_dadan(input)
            data1=return_val$data
            stock_name = return_val$stock_name
            rt = plot_dadan(data1)
            subplot(rt$p1,rt$p2,rt$p3,rt$p4,rt$p5,nrows=5,margin=0.03,shareX=TRUE) %>% layout(title=paste0(stock_name,"  ","大单流入(单位:百万元)"),height=800,margin=10)
        }
    })


    #############################
    #-------- 量价分布--------#
    #############################

    source('task_price_value_distribution.r')
    output$pl_pv_distribution <- renderPlotly({
        return_val=pv_data(input)
        dates=return_val$dates
        data1=return_val$data
        new_x_min=return_val$new_x_min
        new_x_max=return_val$new_x_max
        new_y_min=return_val$new_y_min
        new_y_max=return_val$new_y_max
        dick=round((as.numeric(new_y_max)-as.numeric(new_y_min))/5,2)
        k=-1
        substr_raw="subplot("
        for(dts in dates){
            k=k+1
            loop_date=as.character(dts)
            #print(loop_date)
            data2 = filter(data1,dt==loop_date,price>0,vol>0)
            if(nrow(data2)>0){
	            #print(data2)
            #x = data2[,"vol"]
            #y =  data2[,"price"]
                x_assign = paste0("x",k,"=data2[,'vol']")
                y_assign = paste0("y",k,"=data2[,'price']")
                eval(parse(text=x_assign))
                eval(parse(text=y_assign))
                pString<-sprintf("plot_ly(data=data1,x=~x%d,y=y%d,type='bar',orientation='h',name='%s')",k,k,dts) 
                layOut = sprintf("layout(xaxis=list(title='%s',titlefont=list(size=10),tickvals =0,range=c(%s,%s)),
                                 yaxis=list(range=c(%s,%s),tickfont=list(size=10),dtick=%s,autorange = FALSE))",dts,new_x_min,new_x_max,new_y_min,new_y_max,dick)
                layOut=gsub('[\r\n]','',layOut)
                pString = paste0(pString,"%>%",layOut)
                #print(pString)
                substr_raw = paste0(substr_raw,pString,",")
            }
        }
        substr_raw = paste0(substr_raw,"nrows=2,margin=0.03,shareX=F,shareY=F,titleX=T,titleY=T)%>% layout(height=800,showlegend=F)")
        #substr_raw = paste0(substr_raw,"nrows=3,margin=0.06)")
        #print(substr_raw)
        eval(parse(text=substr_raw))
        #print(substr_raw)
    })

    #############################
    #-------- fin report--------#
    #############################
    output$pl_fin_report <- renderPlotly({
	    source("task_fin_report.r")
        p = fin_report_plot(input)
        p
    
    })

    #############################
    #----------机构调研---------#
    #############################
    output$table_diaoyan<-DT::renderDataTable({
        #source("task_important_owner.r")
        data_out = read.csv("/home/davidyu/stock/data/shiny_data/data/jigoudiaoyan.csv")
        DT::datatable(data_out,options=list(lengthMenu =c(25,50,100),columnDefs = list(list(className = 'dt-center', targets = "_all")))) %>%
                  formatStyle(c(0:10), `border-right` = "solid 2px")
    })

    #############################
    #----------实时大单---------#
    #############################
    output$realtime_dadan<-DT::renderDataTable({
        #source("task_important_owner.r")
        data_out_real_dadan = read.csv("/home/davidyu/stock/data/shiny_data/data/realtime_dadan_stat.csv")
        DT::datatable(data_out_real_dadan,options=list(lengthMenu =c(25,50,100),columnDefs = list(list(className = 'dt-center', targets = "_all")))) %>%
                  formatStyle(c(0:10), `border-right` = "solid 2px")
    })
}
