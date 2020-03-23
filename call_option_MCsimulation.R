
library(reshape2)
suppressPackageStartupMessages(library(RODBC, quietly = TRUE))
suppressPackageStartupMessages(library(ggplot2, quietly = TRUE))
suppressPackageStartupMessages(library(ggthemes, quietly = TRUE))
suppressPackageStartupMessages(library(shiny, quietly = TRUE))
suppressPackageStartupMessages(library(plotly, quietly = TRUE))
suppressPackageStartupMessages(library(tidyverse, quietly = TRUE))
suppressPackageStartupMessages(library(shinydashboard, quietly = TRUE))
suppressPackageStartupMessages(library(DT, quietly = TRUE))
suppressPackageStartupMessages(library(doParallel, quietly = TRUE))
suppressPackageStartupMessages(library(foreach, quietly = TRUE))
suppressPackageStartupMessages(library(sendmailR, quietly = TRUE))
#suppressPackageStartupMessages(library(RDCOMClient, quietly = TRUE)) # this does not work in the new R version, probably it will soon
suppressPackageStartupMessages(library(tcltk, quietly = TRUE))
suppressPackageStartupMessages(library(highcharter, quietly = TRUE))
suppressPackageStartupMessages(library(data.table, quietly = TRUE))
suppressPackageStartupMessages(library(openxlsx, quietly = TRUE))
#suppressPackageStartupMessages(library(scales, quietly = TRUE))
suppressPackageStartupMessages(library(dplyr, quietly = TRUE))

mu <- 0.05
vol <- 0.15
S0 <- 100
paths <- 3000
maturity <- 1
dt <- 1 / 252

stock <- matrix(nrow = maturity / dt, ncol = paths)
stock[1, ] <- S0


for (path in 1:paths) {
  for (date in 2:(maturity / dt)) {
    stock[date, path] <- stock[date - 1, path] * exp((mu - 0.5 * vol * vol)* dt  + vol * sqrt(dt) * rnorm(1, 0, 1))
  }
}

plot(seq(1 / 252, maturity, dt), stock[, 1], type = "l") 

call_price <- exp(-mu * maturity) * mean(max(stock[maturity / dt, ] - 75, 0)) 
call_price # discounted average price today on a 1y call option (across 3000 paths) on the underlying with strike 75 
          # so you take the last row (in 252 days and compute the present value)


melt(stock) %>% ggplot(aes(x = Var1, y = value, group = Var2, color = Var2)) +
  geom_line() +
  theme_minimal() 



prova <-  exp((mu - 0.5 * vol * vol) * dt + vol * sqrt(dt) * rnorm(1, 0, 1))
