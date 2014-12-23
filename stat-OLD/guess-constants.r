argv=commandArgs(trailingOnly = TRUE)
r=read.csv(argv[1])
s=split(r,r$Sample)

michael=function(x) {
  b=c(kcat=max(x$kobs),km=mean(x$S)) 
  try(summary(nls(kobs~kcat*S/(km+S),x,start=b)))
}

si=function(x) {
  b=c(kcat=max(x$kobs),km=mean(x$S),ki=km)
  try(summary(nls(kobs~kcat*S/(km+S+S^2/ki),x,start=b)))
}

lapply(s, function(x) { michael(x) })

print('---666---')

lapply(s, function(x) { try(summary(lm(kobs~S,x))) })

library(ggplot2)
ggplot(r, aes(S, kobs)) + 
theme_minimal() + 
geom_point() + 
stat_smooth(method="lm", se=F, color="green") + 
facet_wrap(~Sample,scales="free") +
geom_smooth(method="nls",
formula=y~kcat*x/(km+2*x),
start=c(kcat=1,km=0.01),se=F) + 
ggsave("out.pdf")

