#CLUSTER on Cities_Data

#Set the directory
setwd("D:/Great Lakes/Data Mining/Data")
getwd()
#Read the save file 
data1 <- read.spss("cities.sav",use.valuelable=TRUE,to.data.frame=T)

#check structure 
str(data1)

#Check the few records
head(data1)

# To put every variable on scale use Scale matrix
# Scaled Variable - Use [2:4] - Infeix operartor 
scaled.data1 <- scale(data1[,2:4])

# Check the few records 
head(scaled.data1)

# uSE Euclidiean  Method and calculate Distance From Euclidiean metrix 
d.col1 <- dist(x=scaled.data1, method ="euclidean") 
d.col1

clus4 <- hclust(d.col1,method="average")
clus4

# Create Cluster Dendrogram
plot(clus4,labels=as.character(data1[,1]))

rect.hclust(clus4,k=3,border="green")

data1$clusters1 <-cutree(clus4,k=3)
# This will be tell  that which college is tagged to which Clusters
data1$clusters1

# To find the what is characteristics of each Colleg
# This Aggregation will tell the property of each variable in each cluster


aggr1 <- aggregate(data1[,-c(1)],list(data1$clusters1) , mean)
aggr1



