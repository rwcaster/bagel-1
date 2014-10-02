argv <- commandArgs(trailingOnly = TRUE)
r=read.csv(argv[1], header=T)

x=subset(r, select=-c(X,description,kcat))
y=r$kcat

library(e1071)
m=svm(x,y)

print(m)
pred=predict(m,x,decision.values=T)
plot(pred)
