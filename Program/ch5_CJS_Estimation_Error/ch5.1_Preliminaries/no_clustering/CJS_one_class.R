library(marked)
library(readr)

args = commandArgs(trailingOnly=TRUE)
# read file
capturing_history = read_lines(args[1], n_max = -1)
ch <- c(capturing_history)

#ip_cluster = read_lines(args[2], n_max = -1)
#cluster <- c(ip_cluster)

#cluster <- factor(cluster)
#DT <- data.frame("ch" = ch, "cluster" = cluster)
DT <- data.frame("ch" = ch)
DT$ch <- as.character(DT$ch)

start_time <- Sys.time()
#DT.proc <- process.data(DT, groups="cluster")
DT.proc <- process.data(DT)
DT.ddl <- make.design.data(DT.proc)

# no cluster
Phi.time <- list(formula=~time)
p.time <- list(formula=~time)
cjs.m2 <- crm(DT.proc, DT.ddl, model.parameters = list(Phi = Phi.time, p = p.time), accumulate = FALSE)
cjs.m2 <- cjs.hessian(cjs.m2)
print(predict(cjs.m2))

end_time <- Sys.time()
print(end_time-start_time)