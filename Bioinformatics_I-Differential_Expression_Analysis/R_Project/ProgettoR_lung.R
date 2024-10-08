library(DESeq2)
library(pheatmap)
library(RColorBrewer)
library(EnhancedVolcano)
library(ggplot2)
library(AnnotationDbi)
library(org.Hs.eg.db)
library(clusterProfiler)
suppressMessages(suppressWarnings(library(clusterProfiler)))

coldata <- read.delim('design_lung.tsv', header = TRUE, row.names = 1)
rowcounts <- read.delim('lung_counts.tsv', header = TRUE, row.names = 1)

#export as a matrix
#the second column contains the Gene Name, (letters-9 so should be removed)
#since the counts must have only columns with the counts values
#as indicated in the instructions
countData <- as.matrix(subset(rowcounts, select = c(-Gene.Name)))
#toglie genename (colonna) perché non ci serve. è una matrice e non df.

#Design formula.salvare il nome della colonna di coldata dove sono salvati cases and diseases.
#serve a specificare al programma in quale colonna di coldata (experiment design file) è salvata se sono sample o control
designFormula <- "~ Sample.Characteristic.disease."

#create a DESeq dataset object from the count matrix and the colData
dds <- DESeqDataSetFromMatrix(countData = countData,
                              colData = coldata,
                              design = as.formula(designFormula))
print(dds)
#filter Genes
#filter Low Expressed genes with "RowSums(Counts(dds)) > 1" si salva i geni che hanno zero espressione in tutti i sample come FALSE, vice versa come TRUE
expressed <-rowSums(counts(dds)) > 1
dds <- dds[expressed, ] 

#display results #13358 fALSE #45377 TRUE
table(expressed)

#DESeq Pipeline
#run DESeq2 pipeline #IL COMANDO Deseq ti fa l'analisi. ho sovrascritto i risultati in dds.
dds <- DESeq(dds)

#PCA of the normalized values using the vst() function. normalizzazione.e l'ho salvata in un altro oggetto
rld <- vst(dds)
DESeq2::plotPCA(rld, intgroup = 'Sample.Characteristic.disease.')


#Heatmap ----
#plot an Heatmap of the sample-to-sample distances
#sample sample distance
SampleDists <- dist(t(assay(rld)))
SampleDists

# to create an object which describes how different are couples of samples.
SampleDistMatrix <- as.matrix(SampleDists)


library(viridis)  

pheatmap(SampleDistMatrix,
         main = "Heatmap of sample-sample distance",
         clustering_distance_rows = SampleDists,
         clustering_distance_cols = SampleDists,
         col = magma(9))





###############################################################################
coldata <- coldata[-18, ]
rowcounts <- rowcounts[, -19]

##############################################################################

#export as a matrix
#the second column contains the Gene Name, (letters-9 so should be removed)
#since the counts must have only columns with the counts values
#as indicated in the instructions
countData <- as.matrix(subset(rowcounts, select = c(-Gene.Name)))
#toglie genename (colonna) perché non ci serve. è una matrice e non df.

#Design formula.salvare il nome della colonna di coldata dove sono salvati cases and diseases.
#serve a specificare al programma in quale colonna di coldata (experiment design file) è salvata se sono sample o control
designFormula <- "~ Sample.Characteristic.disease."

#create a DESeq dataset object from the count matrix and the colData
dds <- DESeqDataSetFromMatrix(countData = countData,
                              colData = coldata,
                              design = as.formula(designFormula))
print(dds)
#filter Genes
#filter Low Expressed genes with "RowSums(Counts(dds)) > 1" si salva i geni che hanno zero espressione in tutti i sample come FALSE, vice versa come TRUE
expressed <-rowSums(counts(dds)) > 1
dds <- dds[expressed, ] 

#display results #13358 fALSE #45377 TRUE
table(expressed)

#DESeq Pipeline
#run DESeq2 pipeline #IL COMANDO Deseq ti fa l'analisi. ho sovrascritto i risultati in dds.
dds <- DESeq(dds)

#PCA of the normalized values using the vst() function. normalizzazione.e l'ho salvata in un altro oggetto
rld <- vst(dds)
DESeq2::plotPCA(rld, intgroup = 'Sample.Characteristic.disease.')

#Heatmap ----
#plot an Heatmap of the sample-to-sample distances
#sample sample distance
SampleDists <- dist(t(assay(rld)))
SampleDists

# to create an object which describes how different are couples of samples.
SampleDistMatrix <- as.matrix(SampleDists)


library(viridis)  

pheatmap(SampleDistMatrix,
         main = "Heatmap of sample-sample distance",
         clustering_distance_rows = SampleDists,
         clustering_distance_cols = SampleDists,
         col = magma(9))
##########################################################################

  

#Comparison between groups ----
#perform the comparisons between the groups with the following code
#res <- results(dds)
#res <- results(dds)
res <- results(dds, contrast = c("Sample.Characteristic.disease.", 'COVID-19', 'normal'))
summary(res)

res['ENSG00000205086',]
res['ENSG00000243566',]
res['ENSG00000206073',]
res['ENSG00000137869',]

###################################################################################
#Questions

new_res <- res[!is.na(res$padj),]
summary(new_res[new_res$padj < 0.1 & abs(new_res$log2FoldChange) > 0 ,]) 

## How many genes are differentially expressed at the thresholds of padj < 0.05?

summary(new_res[new_res$padj < 0.05 & abs(new_res$log2FoldChange) > 0 ,])

## How many genes at the thresholds of padj < 0.05 are up regulated ( > 1)?
summary(new_res[new_res$padj < 0.05 & new_res$log2FoldChange > 1  ,])
summary(new_res[new_res$padj < 0.05 & new_res$log2FoldChange < -1  ,])
###########################################################################


EnhancedVolcano(
  as.data.frame(res),
  labSize = 2.5,
  title = "VolcanoPlot",
  subtitle = "COVID-19 vs normal",
  lab = rownames(res),
  FCcutoff = 2,
  x = 'log2FoldChange',
  y = 'pvalue',
  col = c("#b4ddd4", "#f8a0b1", "#088490", "#f92e5d")  
)


#MaPlot
DESeq2::plotMA(object = res, 
               main ='MAPlot Result',
               colSig = "#f8a0b1",
               colNonSig = "#f92e5d",
               colLine = "#b4ddd4",
               xlab="mean of normalized counts", 
               ylab="log2FoldChange",
               ylim = c(-12, 12))

resSig <- subset(new_res, padj < 0.05)

#upregulated with log2FoldChange > 0 ti salvi quanti sono upregulated
upReg <- subset(resSig, log2FoldChange > 1)
dim(upReg)
#downregulated with log2FoldChange < 0 ti salvi quanti sono downregulated
downReg <- subset(resSig, log2FoldChange < -1)

dim(downReg)
#-- aggiungi una colonna chiamata SYMBOL, dove salvi il gene symbol
upReg$symbol <- mapIds(org.Hs.eg.db,
                       keys=rownames(upReg),
                       column="SYMBOL",
                       keytype="ENSEMBL",
                       multiVals="first")

GO_BP_UP <- enrichGO(upReg$symbol, OrgDb = "org.Hs.eg.db", 
                     keyType = "SYMBOL", ont = "BP")
GO_df <- as.data.frame(GO_BP_UP) 
summary(GO_df[GO_df$p.adjust < 0.1,]) 
GO_df <- GO_df[order(-GO_df$Count), ]
View(GO_df)

GO_MF_UP <- enrichGO(upReg$symbol, OrgDb = "org.Hs.eg.db", 
                       keyType = "SYMBOL", ont = "MF")
GO_MF_df <- as.data.frame(GO_MF_UP) 
summary(GO_MF_df[GO_MF_df$p.adjust < 0.1,]) 
GO_MF_df <- GO_MF_df[order(-GO_MF_df$Count), ]
View(GO_MF_df)

dotplot(GO_BP_UP, title = "UpBioProcess")
dotplot(GO_MF_UP, title = "UpMolFunctions")

#DOWNREGULATED
downReg$symbol <- mapIds(org.Hs.eg.db,
                         keys=rownames(downReg),
                         column="SYMBOL",
                         keytype="ENSEMBL",
                         multiVals="first")

GO_BP_DOWN <- enrichGO(downReg$symbol, OrgDb = "org.Hs.eg.db", 
                       keyType = "SYMBOL", ont = "BP")
GO_MF_DOWN <- enrichGO(downReg$symbol, OrgDb = "org.Hs.eg.db", 
                       keyType = "SYMBOL", ont = "MF")
dotplot(GO_BP_DOWN, title = "Downregualted Biological Process")
dotplot(GO_MF_DOWN, title = "Downregualted Molecular Functions")
