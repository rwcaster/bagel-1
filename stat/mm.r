#argv=commandArgs(trailingOnly = TRUE)
#r=read.csv(argv[1], header=T)
r=read.csv('example.csv')
s=split(r,r$Sample)

michael=function(x) {
  b=c(kcat=max(x$kobs),km=mean(x$S))
  try(nls(kobs~kcat*S/(km+S),x,start=b))
}

print('Michaelis-Menten models')
lapply(s, function(x) { summary(michael(x)) })

print('Linear fits')
lapply(s, function(x) { summary(lm(kobs~S,x)) })

library(ggplot2)
ggplot(r, aes(S, kobs)) + 
geom_point() + 
facet_wrap(~Sample,scales="free") +
geom_smooth(method="nls",
formula=y~kcat*x/(km+x),
start=c(kcat=1,km=0.01),se=FALSE)

ggplot(r, aes(S, kobs)) +
geom_point() + 
stat_smooth(method="lm",se=F) + 
facet_wrap(~Sample,scales="free")
