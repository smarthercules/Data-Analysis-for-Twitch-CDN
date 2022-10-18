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

# # fit.DT.cjs.models <- function(){
# #   Phi.dot <- list(formula=~1)
# #   Phi.time <- list(formula=~time)
# #   Phi.subnet <- list(formula=~subnet)
# #   Phi.subnet.time <- list(formula=~subnet*time)
# # 
# #   p.dot <- list(formula=~1)
# #   p.time <- list(formula=~time)
# #   p.subnet <- list(formula=~subnet)
# #   p.subnet.time <- list(formula=~subnet*time)
# # 
# #   cml <- create.model.list(c("Phi", "p"))
# #   results <- crm.wrapper(cml,
# #                          data = DT.proc,
# #                          ddl = DT.ddl,
# #                          external = FALSE,
# #                          accumulate = FALSE,
# #                          hessian = TRUE)
# #   return(results)
# # }
# # 
# # DT.cjs.models <-fit.DT.cjs.models()
# # print(DT.cjs.models)

# with cluster
#Phi.cluster.time <- list(formula=~cluster*time)
#p.cluster.time <- list(formula=~cluster*time)
#cjs.m2 <- crm(DT.proc, DT.ddl, model.parameters = list(Phi = Phi.cluster.time, p = p.cluster.time), accumulate = FALSE)
#cjs.m2 <- cjs.hessian(cjs.m2)
#print(predict(cjs.m2))

# no cluster
Phi.time <- list(formula=~time)
p.time <- list(formula=~time)
cjs.m2 <- crm(DT.proc, DT.ddl, model.parameters = list(Phi = Phi.time, p = p.time), accumulate = FALSE)
cjs.m2 <- cjs.hessian(cjs.m2)
print(predict(cjs.m2))

end_time <- Sys.time()
print(end_time-start_time)