setwd("/home/davidyu/stock/scripts/davidyu_stock/scripts/R_run")
library(dplyr)

df1 = read.csv("/home/davidyu/stock/scripts/davidyu_stock/scripts/analysis/baostock/portfolio_data/portf_v2.csv")
df <- as.data.frame(df1)

last_col = ncol(df)-1

a2=xts(df[,1:last_col], order.by=as.Date(df$dates))

VaR(a2,p=.95,method="historical")
HurstIndex(a2)


chart.Boxplot(a2)

data(managers)
chart.CaptureRatios(a2[,1:6], a2[,7,drop=FALSE])

chart.RollingPerformance(a2[, 1:3], width = 24)

plot(density(a2$row_sum))

sd(a2$row_sum)

apply(df1,1,sd)


data(managers)
chart.VaRSensitivity(a2[,11,drop=FALSE],
                     methods=c("HistoricalVaR", "ModifiedVaR", "GaussianVaR"),
                     colorset=bluefocus, lwd=2)


data(managers)
chart.VaRSensitivity(managers[,1,drop=FALSE],
                     methods=c("HistoricalVaR", "ModifiedVaR", "GaussianVaR"),
                     colorset=bluefocus, lwd=2)



data(edhec)
Return.portfolio(edhec["1997",1:5], rebalance_on="quarters") # returns time series
Return.portfolio(edhec["1997",1:5], rebalance_on="quarters", verbose=TRUE) # returns list
# with a weights object
data(weights) # rebalance at the beginning of the year to various weights through time
chart.StackedBar(weights)
x <- Return.portfolio(edhec["2000::",1:11], weights=weights,verbose=TRUE)
chart.CumReturns(x$returns)
chart.StackedBar(x$BOP.Weight)
chart.StackedBar(x$BOP.Value)



