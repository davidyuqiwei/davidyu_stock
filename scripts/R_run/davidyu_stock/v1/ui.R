library(shiny)
library(ggplot2)
library(DT)
library(plotly)


import_owner = read.csv("/home/davidyu/stock/data/shiny_data/data/important_owner.csv")
#names(import_owner)=c("stock_index","stock_name","owner_name","type","date","volume")
dzjy = read.csv("/home/davidyu/stock/data/daily_report/2021-02-02/dazongjiaoyi_report_pos_2021-02-02.csv")
bankuai = read.csv("/home/davidyu/stock/scripts/davidyu_stock/scripts/analysis/bankuai/bankuai_zde.csv")

## dfcf all owner
gudong_change=read.csv("/home/davidyu/stock/data/shiny_data/data/all_owner.csv")
gudong_type_list = c("all",as.character(unique(gudong_change$gudong_type)))
change_type_list = c("all",as.character(unique(gudong_change$change_type)))

source("col_names.r")
now_date = Sys.Date()
#df1 = read.csv("/home/davidyu/stock/data/daily_report/2021-02-02")
# Define UI for app that draws a histogram ----
inline = function (x) {
    tags$div(style="display:inline-block;", x)          
}
textInputRow<-function(inputId, label, value = ""){
    div(style="display:inline-block",
    tags$label(label, `for` = inputId), 
    tags$input(id = inputId, type = "text", value = value,class="input-small"))

}
ui <- fluidPage(
    #tags$head(includeScript("google-analytics.js")),
    #tags$head(includeScript("matomo.js")),
    #print(paste0("login time:",Sys.Time()))
    tags$head(includeScript("ip.js")),
  # App title ----
  #titlePanel("Hello Shiny!"),


  title =  "DavidYu's Lab",
  # Sidebar layout with input and output definitions ----
  sidebarLayout(
    
    #df1 = read.csv("/home/davidyu/stock/data/daily_report/2021-02-02/important_owner_today_report_2021-02-02.csv")
    # Sidebar panel for inputs ----
    sidebarPanel(

        width = 2,
        #----------------- 重要股东
        # Input: Slider for the number of bins ----
        conditionalPanel(
            'input.dataset === "重要股东"',
            checkboxGroupInput("show_vars", "Columns in diamonds to show:",
                           names(import_owner), selected = names(import_owner))
        ),
        ###############
        # 股东变化    #
        ###############
        conditionalPanel(
            'input.dataset === "股东变化"',
            selectInput('gudong_type',label="股东类型(社保 | QFII)",
                    selected = "all",choices = gudong_type_list),
            
            checkboxGroupInput('change_type',"变化类型(增加 | 减少)",
                    change_type_list,selected = "all"),

           checkboxGroupInput("gudongbianhua", "股东变化",
                    names(gudong_change), selected = names(gudong_change)),
           
            tags$style("input[type=checkbox] {
                transform: scale(1.5);
            }")
        ),


        #-------------------------------------------------------------------------------------------------#
        #---------------------------------------------  板块
	     conditionalPanel(
	       'input.dataset === "板块"',
	        selectInput('bankuai_tab',label="大板块",
	                selected = "行业",choices = c("板块","地域","行业"))
	    ),
	       
	     conditionalPanel(
	        'input.dataset === "板块"',
	        selectInput('bankuai1',label="选择",choices = NULL),
	        dateRangeInput("date", "Date range:",
	                       start  = as.character(Sys.Date()-1),
	                       end    = Sys.Date(),
	                       min    = now_date-360,
	                       max    = "2050-10-01",
	                       format = "dd/mm/yy",
	                       separator = " - ")
	     ), 
    #----------------------------------------大宗交易-----------------------------------#
	     conditionalPanel(
	       'input.dataset === "大宗交易"',
	        selectInput('dazongjiaoyi_type',label="大宗交易类型",
	                selected = "",choices = c("全部","正溢价","明细"))
	    ),
    


    #--------------------------------------------trend------------------------------------------------#

      conditionalPanel(
        'input.dataset === "Trend"',
        textInput("tr_stock_index", "input stock index",value="601398"),
        textInput("tr_start_date", "start_date",value="2020-12-01"),
        textInput("tr_end_date", "end_date",value=as.character(Sys.Date())),
        ),
    #######################
    #-------技术指标------#
    #######################
      conditionalPanel(
        'input.dataset === "技术指标"',
	    selectInput("tech_index",label="指标范围",
	                selected = "沪深300",choices = c("沪深300","地域","行业")),
        textInputRow(inputId="tr_tech_index", label="min",value="h"),
        textInputRow(inputId="tr_tech1_index", label="max",value="h"),
        
        ),

    #######################
    #-------主力控盘------#
    #######################
      conditionalPanel(
        'input.dataset === "主力控盘"',
	    ##selectInput("tech_index",label="指标范围",
	    #           selected = "沪深300",choices = c("沪深300","地域","行业")),
        #textInputRow(inputId="tr_tech_index", label="min",value="h"),
        #textInputRow(inputId="tr_tech1_index", label="max",value="h"),
        
        ),
    #######################
    #-------技术指标------#
    #######################
      conditionalPanel(
        'input.dataset === "MACD"',
        textInput("macd_stock_index", "input stock index",value="601398"),
        textInput(inputId="macd_start_date", label="min",value="2020-01-01"),
        textInput(inputId="macd_end_date", label="max",value=now_date),
        
        ),
    #-------------------------------------------------------------------------------------------------#
    #------------------------------------------大单----------------------------------------------------#
    conditionalPanel(
        'input.dataset === "大单"',
        #actionButton("button2", "Action 2"),
        textInput("stock_index_dadan", "input stock index",value="601398"),
        #textInput("y", "input y column",value=now_date),
        textInput("start_date_dadan", "start_date",value="2020-12-01"),
        textInput("end_date_dadan", "end_date",value=now_date),
        br(),
        actionButton("button2", "提交"),
        #plotlyOutput('pl_dadan', width='100%', height='400px')
        ),
               
        conditionalPanel(
            'input.dataset === "实时大胆"',
            checkboxGroupInput("realtime_dadan", "Columns in diamonds to show:",
                           names(import_owner), selected = names(import_owner))
        ),
    
      ##------------------------------- 量价分布 -------------------------------------------#
      conditionalPanel(
        'input.dataset === "量价分布"',
        textInput("pv_stock_index", "input stock index",value="601398"),
        textInput("pv_start_date", "start_date"),
        textInput("pv_end_date", "end_date"),
        textInput("reset_date", "重新定义日期",value="0"),
        #textInput("pv_x_max", "x最大值",value="10000000"),
        #textInput("pv_y_min", "y最小值",value="4.8"),
        #textInput("pv_y_max", "y最大值",value="5.9"),
      ),
     #------------------------------- 财务报表 ---------------------------------------#
      conditionalPanel(
        'input.dataset === "财务报表"',
        textInput("fin_report_stock_index", "input stock index",value="601398"),
        checkboxGroupInput("fin_report_para", "财务报表指标:",
                name_fin_report, selected = "摊薄每股收益(元)"),

        textInput("pv_start_date", "start_date"),
        textInput("pv_start_date", "end_date"),
        textInput("pv_x_min", "x最小值",value="1000000"),
        textInput("pv_x_max", "x最大值",value="10000000"),
        textInput("pv_y_min", "y最小值",value="4.8"),
        textInput("pv_y_max", "y最大值",value="5.9"),
      )
    ),   

    # Main panel for displaying outputs ----
    mainPanel(
        tabsetPanel(
            id = 'dataset',
            tabPanel("重要股东", DT::dataTableOutput("table_import_owner")),
            tabPanel("股东变化", DT::dataTableOutput("table_owner_change")),
            #tabPanel("板块", DT::dataTableOutput("mytable3")),
            tabPanel("板块", fluidRow(plotlyOutput('pl_bankuai', width='100%', height='400px')),
                     DT::dataTableOutput("table_bankuai")),
            tabPanel("大宗交易", DT::dataTableOutput("table_dzjy")),
            #tabPanel("trend", DT::dataTableOutput("mytable3"))
            tabPanel("Trend", plotlyOutput('pl_trend', width='100%', height='400px')),
            tabPanel("MACD", plotlyOutput('pl_macd', width='100%', height='400px')),
            tabPanel("技术指标", DT::dataTableOutput("table_tech_index")),
            tabPanel("主力控盘", DT::dataTableOutput("table_zhulikongpan")),
            tabPanel("大单", plotlyOutput('pl_dadan', width='100%', height='400px'),DT::dataTableOutput("tt")),
            tabPanel("实时大单", DT::dataTableOutput("realtime_dadan")),
            tabPanel("量价分布", plotlyOutput('pl_pv_distribution', width='100%', height='400px')),
            tabPanel("财务报表", plotlyOutput('pl_fin_report', width='100%', height='400px')),
            tabPanel("机构调研",  DT::dataTableOutput("table_diaoyan"))
            )
        )
    )
)
