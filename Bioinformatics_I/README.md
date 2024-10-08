# **RProject**: Transcriptional and proteomic insights into the host response in fatal COVID-19 cases

### Bioinformatics I

**Author:** Ilaria Coratella


## Introduction

![immagine](https://github.com/user-attachments/assets/98861fa6-070e-4f89-aeda-d21601e6eb0b)

I chose this article, which analyzes pathways related to neutrophil activation and pulmonary fibrosis among the major up-regulated transcriptional signatures in lung tissue obtained from patients who died of COVID-19 in Wuhan, China. Examination of the colonic transcriptome of these patients suggested that SARS-CoV-2 impacted host responses even at a site with no obvious pathogenesis.

## Covid 19

SARS-CoV-2, the etiologic agent for coronavirus disease 2019 (COVID-19), emerged in Wuhan, China, in late December 2019. Since then, more than 29.5 million people have been infected worldwide, with over 933,000 deaths as of September 15, 2020. Although research into the clinical and scientific features of SARS-CoV-2 pathogenesis has progressed at a dizzying pace, pathogenesis of COVID-19 is still incompletely understood.

## What is the aim of this project?

The aim of this presentation is to show the results of two differential expression analysis, hence to find DEGs in lung and colon tissues of diseased patients. I preferred to perform two simultaneous analysis for the two tissues in order to obtain a more precise result.

## Filtering of the original dataset

Firstly, I have filtered my original experimental design dataset for tissue, and I did it both for lung and colon.

```r
setwd("C:/Users/Ilaria/Desktop/UNI/not_passed/BI1/ProjectR")
library(readxl)
library(writexl)

df <- read_excel("E-ENAD-46-experiment-design - Copiaexcel.xlsx")
df_lung <- df[df$`Sample Characteristic[organism part]` == 'lung', ]
write_xlsx(df_lung, "new_experiment_design_lung_R.xlsx")

df_colon <- df[df$`Sample Characteristic[organism part]` == 'colon', ]
write_xlsx(df_colon, "new_experiment_design_colon_R.xlsx")
```

## Filtered dataset for lung
![immagine](https://github.com/user-attachments/assets/e04b7a6c-8a53-4b2d-9799-a672ea3a5cbd)


## Filtered dataset for colon
![immagine](https://github.com/user-attachments/assets/e218ae59-a214-45e9-8be6-8fd031cabecc)


## Filtering of the genes

Once I have separated the samples on the basis of the tissue type, I divided the counts of the genes. This filtering operation has been carried out on the basis of the names of the samples previously divided:

```r
lung_design <- readxl::read_excel("new_experiment_design_lung_R.xlsx")
colon_design <- readxl::read_excel("new_experiment_design_colon_R.xlsx")

lung_sample <- lung_design$Run
colon_sample <- colon_design$Run

count <- readxl::read_excel("E-ENAD-46-raw-counts.xlsx")

lung_counts <- count[,c("Gene ID","Gene Name",lung_sample)]
colon_counts <- count[,c("Gene ID","Gene Name",colon_sample)]

write.table(lung_counts, file = "lung_counts.tsv", quote = F, row.names = F, sep = "\t")
write.table(colon_counts,file = "colon_counts.tsv", quote = F, row.names = F, sep = "\t")

write.table(lung_design, file = "design_lung.tsv", quote = F, row.names = F, sep = "\t")
write.table(colon_design, file = "design_colon.tsv", quote = F, row.names = F, sep = "\t")
```

## Differential expression analysis

### Importing data as matrices

I obtained a total of 19 samples, 9 diseased and 10 healthy. First of all, I have uploaded the data of the study, both the study design and the gene counts. I did it both for LUNG and COLON:

#### LUNG
```r
coldata <- read.delim('design_lung.tsv', header = TRUE, row.names = 1) 
# Export as a matrix: it creates a matrix with the data of the experiment design file.

rowcounts <- read.delim('lung_counts.tsv', header = TRUE, row.names = 1)
# Export as a matrix: it creates a matrix with the data of the raw counts file.
```

#### COLON
```r
coldata1 <- read.delim('design_colon.tsv', header = TRUE, row.names = 1) 
# Export as a matrix: it creates a matrix with the data of the experiment design file.

rowcounts1 <- read.delim('colon_counts.tsv', header = TRUE, row.names = 1)
# Export as a matrix: it creates a matrix with the data of the raw counts file.
```

### Removing the 'extra' column

Since I noticed that there were two columns to identify the genes, I removed one. In fact, just one column is necessary to perform the Differential Expression Analysis. This is the code to remove the column `Gene.Name`:

#### LUNG
```r
countData <- as.matrix(subset(rowcounts, select = c(-Gene.Name)))
```

#### COLON
```r
countData1 <- as.matrix(subset(rowcounts1, select = c(-Gene.Name)))
```

### Specify the Sample Type

This function is used to specify to the program in which column of the `coldata` (experiment design file) it is indicated whether the samples are disease or control.

#### LUNG
```r
designFormula <- "~ Sample.Characteristic.disease."
```

#### COLON
```r
designFormula <- "~ Sample.Characteristic.disease."
```

### RNAseq analysis

These lines of code can create a DESeq dataset object from the count matrix and the colData, which I named `dds`. As it can easily be observed from the output, I have 58375 genes. `As.formula()` can be used to convert the string into a formula object, which can be useful in order to perform statistical analysis.

#### LUNG
```r
dds <- DESeqDataSetFromMatrix(countData = countData,
                              colData = coldata,
                              design = as.formula(designFormula))
print(dds)
```

#### COLON
```r
dds1 <- DESeqDataSetFromMatrix(countData = countData1,
                               colData = coldata1,
                               design = as.formula(designFormula))
print(dds1)
```

In order to obtain a more precise result in the end, I decide to filter the genes, keeping only the ones which are expressed more than once. This function saves the genes with 0 expression in all the samples as `FALSE`, and all the others as `TRUE`:

#### LUNG
```r
expressed <- rowSums(counts(dds)) > 1
table(expressed)
```

#### COLON
```r
expressed1 <- rowSums(counts(dds1)) > 1
table(expressed1)
```

Then, I removed my FALSE values from my `dds`, so that now it will contain only the genes that I have selected. To be more precise.

#### LUNG
If previously I had 58375 genes, now I have 41449 genes:
```r
dds <- dds[expressed, ]
print(dds)
```

#### COLON
If previously I had 58375 genes, now I have 42367 genes:
```r
dds1 <- dds1[expressed1, ]
print(dds1)
```

Afterward, I continued with the pipeline by applying `DESeq()`, which performs count normalization and estimates dispersion values:

#### LUNG
```r
dds <- DESeq(dds)
```

#### COLON
```r
dds1 <- DESeq(dds1)
```

It carries out the analysis, and then overwrites the results in `dds`.

Then, I proceeded to create a PCA plot by utilizing the `vst()` function for normalization. I saved it into another object, called `rld`.

#### LUNG
```r
rld <- vst(dds)
```

#### COLON
```r
rld1 <- vst(dds1)
```

Then I can obtain a PCA plot the normalized values I obtain thanks to the previous lines of code:

#### LUNG
```r
DESeq2::plotPCA(rld, intgroup = 'Sample.Characteristic.disease.')
```
![immagine](https://github.com/user-attachments/assets/f8e32e8d-caa5-4e73-a4eb-4ffe7018b358)

As it is possible to observe, almost all of the samples seem to be correctly classified, with the exception of one sample classified as COVID-19 patient. It may be the result of an error, since it shows a considerable high variance with respect to the other samples.

#### COLON
```r
DESeq2::plotPCA(rld1, intgroup = 'Sample.Characteristic.disease.')
```
![immagine](https://github.com/user-attachments/assets/b75c57f2-6721-4470-9f47-dcea06e1de2a)

This PCA plot is messier than the previous one. We can observe a certain kind of separation between the two categories of genes, but the variance is high and COVID-19 and normal samples are close to one another. It is probable that, affecting COVID-19 mainly lungs, a difference in gene expression can be easily detected in lungs, but less easily in the colon. However, it is interesting that a slight difference in gene expression does still exist, and this is one of the main points of the paper.

To create an object which describes how different are couples of samples, it is important to build the heatmap of sample-sample distance:

#### LUNG
```r
SampleDists <- dist(t(assay(rld)))
SampleDistMatrix <- as.matrix(SampleDists)
```
![immagine](https://github.com/user-attachments/assets/64a88084-34ed-4fe0-acf5-de74968714dc)

#### COLON
```
SampleDists1 <- dist(t(assay(rld1)))
SampleDistMatrix1 <- as.matrix(SampleDists1)
```
![immagine](https://github.com/user-attachments/assets/ca2aae05-1390-4819-9500-6e581e047259)

Now I can plot my heatmap:

#### LUNG
```r
library(viridis)
pheatmap(SampleDistMatrix,
         main = "Heatmap of sample-sample distance",
         clustering_distance_rows = SampleDists,
         clustering_distance_cols = SampleDists,
         col = magma(9))
```
![immagine](https://github.com/user-attachments/assets/cf09141d-72dd-409e-877a-206929b802f9)

However, we can easily observe a sample, SRR12816735, which is dissimilar to every other sample, and it may be the same we observed before in the PCA plot. Since it is highly possible that it is misclassified, I prefer proceeding by removing it.

```r
coldata <- coldata[-18, ]
rowcounts <- rowcounts[, -19]
```

## RNAseq analysis

Now I obtained the same graphs, but without SRR12816735:
```r
DESeq2::plotPCA(rld, intgroup = 'Sample.Characteristic.disease.')
```
![immagine](https://github.com/user-attachments/assets/c2af979a-8ca8-42f1-8b47-670d0973b047)
Heatmap:

```r
#plot an Heatmap of the sample-to-sample distances
#sample sample distance
SampleDists <- dist(t(assay(rld)))
SampleDistMatrix <- as.matrix(SampleDists)
library(viridis)  
pheatmap(SampleDistMatrix,
         main = "LUNG Heatmap of sample-sample distance",
         clustering_distance_rows = SampleDists,
         clustering_distance_cols = SampleDists,
         col = magma(9))
```
![immagine](https://github.com/user-attachments/assets/23d2c57d-170b-4717-bf38-9018cc9616be)

We can observe a more homogeneous PCA and heatmap.

**COLON**

```r
library(viridis)  
pheatmap(SampleDistMatrix1,
         main = "COLON Heatmap of sample-sample distance",
         clustering_distance_rows = SampleDists1,
         clustering_distance_cols = SampleDists1,
         col = magma(9))
```
![immagine](https://github.com/user-attachments/assets/7d1b51b1-41d8-43a9-a217-6b2dd547a888)

The heatmap of the colon does not show very clean results.

## RNAseq analysis

Then I performed the comparison between the two groups. I specified the column of sample data (experimental design) that has the group classification: COVID-19 vs normal.

**LUNG**

3447 genes are overexpressed in dds while 4556 underexpressed.

```r
res <- results(dds, contrast = c("Sample.Characteristic.disease.", 'COVID-19', 'normal'))
summary(res)
```

**COLON**

3447 genes are overexpressed in DS while 4556 underexpressed (update!).

```r
res1 <- results(dds1, contrast = c("Sample.Characteristic.disease.", 'COVID-19', 'normal'))
summary(res1)
```

## VOLCANO PLOT

**LUNG**

```r
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
```
![immagine](https://github.com/user-attachments/assets/1413f87b-25d1-4056-8747-51aba4c6df43)

**COLON**

```r
EnhancedVolcano(
  as.data.frame(res1),
  labSize = 2.5,
  title = "VolcanoPlot",
  subtitle = "COVID-19 vs normal",
  lab = rownames(res1),
  FCcutoff = 2,
  x = 'log2FoldChange',
  y = 'pvalue',
  col = c("#b4ddd4", "#f8a0b1", "#088490", "#f92e5d")  
)
```
![immagine](https://github.com/user-attachments/assets/cbd8f3cd-7b3d-4516-9d6c-55bc05eeeba1)

## MAPLOT

**LUNG**

```r
DESeq2::plotMA(object = res, 
               main ='MAPlot Result',
               colSig = "#f8a0b1",
               colNonSig = "#f92e5d",
               colLine = "#b4ddd4",
               xlab="mean of normalized counts", 
               ylab="log2FoldChange",
               ylim = c(-12, 12))
```
![immagine](https://github.com/user-attachments/assets/281d21ab-387a-44d4-9152-6e03029d2362)

**COLON**

```r
DESeq2::plotMA(object = res1, 
               main ='MAPlot Result',
               colSig = "#f8a0b1",
               colNonSig = "#f92e5d",
               colLine = "#b4ddd4",
               xlab="mean of normalized counts", 
               ylab="log2FoldChange",
               ylim = c(-12, 12))
```
![immagine](https://github.com/user-attachments/assets/faf6e057-f4aa-4a74-9960-90f929595b25)

## Comparison with Expression Atlas results: DOWN-regulated **LUNG** genes

C2orf91

As it is observable, we can see a log2foldchange of -8.27, while in the result of the experiment in Expression Atlas it is -7.1

```r
res['ENSG00000205086',]
```

UPK3B

As it is observable, we can see a log2foldchange of -8.25, while in the result of the experiment in Expression Atlas it is -6.8

```r
res['ENSG00000243566',]
```

## Comparison with Expression Atlas results: UP-regulated **LUNG** genes

SERPINB4

As it is observable, we can see a log2foldchange of 8.34, while in the result of the experiment in Expression Atlas it is 6.4:

```r
res['ENSG00000206073',]
```

CYP19A1

As it is observable, we can see a log2foldchange of 6.96, while in the result of the experiment in Expression Atlas it is 5.7:

```r
res['ENSG00000137869',]
```

# Some questions on DEGs

## How many genes are differentially expressed at the thresholds of padj < 0.1?

**LUNG**

```r
new_res <- res[!is.na(res$padj),]
summary(new_res[new_res$padj < 0.1 & abs(new_res$log2FoldChange) > 0 ,])
```

We can observe 8003 Differentially Expressed Genes with an adjusted p-value of 0.1.

**COLON**

```r
new_res1 <- res1[!is.na(res1$padj),]
summary(new_res1[new_res1$padj < 0.1 & abs(new_res1$log2FoldChange) > 0 ,])
```

We can observe 10330 Differentially Expressed Genes with an adjusted p-value of 0.1.

## How many genes are differentially expressed at the thresholds of padj < 0.05?

**LUNG**

```r
summary(new_res[new_res$padj < 0.05 & abs(new_res$log2FoldChange) > 0 ,])
```

We can observe 6037 Differentially Expressed Genes with an adjusted p-value of 0.05.

**COLON**

```r
summary(new_res1[new_res1$padj < 0.05 & abs(new_res1$log2FoldChange) > 0 ,])
```

We can observe 7934 Differentially Expressed Genes with an adjusted p-value of 0.05.

## How many genes at the thresholds of padj < 0.05 are UP-regulated ( > 1)?

**LUNG**

```r
summary(new_res[new_res$padj < 0.05 & new_res$log2FoldChange > 1  ,])
```

At a padj of 0.05 and using as log2FoldChange threshold the value 1, we can observe 1539 UP-regulated genes.

**COLON**

```r
summary(new_res1[new_res1$padj < 0.05 & new_res1$log2FoldChange > 1  ,])
```

At a padj of 0.05 and using as log2FoldChange threshold the value 1, we can observe 1232 UP-regulated genes.

## How many genes at the thresholds of padj < 0.05 are DOWN-regulated ( < -1)?

**LUNG**

```r
summary(new_res[new_res$padj < 0.05 & new_res$log2FoldChange < -1  ,])
```

At a padj of 0.05 and using as log2FoldChange threshold the value -1, we can observe 2930 DOWN-regulated genes.

**COLON**

```r
summary(new_res1[new_res1$padj < 0.05 & new_res1$log2FoldChange < -1  ,])
```

At a padj of 0.05 and using as log2FoldChange threshold the value -1, we can observe 5551 DOWN-regulated genes.

```markdown
# Gene Ontology (GO) Enrichment Analysis

## UP-REGULATED - LUNG

### Finding the Gene Symbol Column
```R
resSig <- subset(new_res, padj < 0.1)
upReg <- subset(resSig, log2FoldChange > 1)
upReg$symbol <- mapIds(org.Hs.eg.db,
                       keys=rownames(upReg),
                       column="SYMBOL",
                       keytype="ENSEMBL",
                       multiVals="first")
```

## Gene Ontology (GO) Enrichment Analysis

### Performing Enrichment Analysis
We perform the Enrichment analysis for Biological Process (BP) and Molecular Function (MF) using the `enrichGO()` function.

```R
GO_BP_UP <- enrichGO(upReg$symbol, OrgDb = "org.Hs.eg.db", 
                     keyType = "SYMBOL", ont = "BP")
GO_MF_UP <- enrichGO(upReg$symbol, OrgDb = "org.Hs.eg.db", 
                     keyType = "SYMBOL", ont = "MF")
```

### Dot Plots for Up-Regulated Genes

#### Biological Process (BP) - LUNG
```R
dotplot(GO_BP_UP, title = "UpBioProcess")
```
![immagine](https://github.com/user-attachments/assets/d14c5bc6-cabc-4e32-9043-f56425ecf0b0)

#### Molecular Function (MF) - LUNG
```R
dotplot(GO_MF_UP, title = "UpMolFunctions")
```
![immagine](https://github.com/user-attachments/assets/61de7c3b-22ea-4e76-b838-7069f68cd2ba)

#### Biological Process (BP) - COLON
```R
dotplot(GO_BP_UP1, title = "UpBioProcess")
```
![immagine](https://github.com/user-attachments/assets/b65fe184-743f-4c60-a5fa-c8638b90dc41)

#### Molecular Function (MF) - COLON
```R
dotplot(GO_MF_UP1, title = "UpMolFunctions")
```
![immagine](https://github.com/user-attachments/assets/5fd5e831-a200-455b-95dc-c519ca5a4635)

## DOWN-REGULATED - LUNG

### Identifying Down-Regulated Genes
```R
downReg <- subset(resSig, log2FoldChange < -1)
downReg$symbol <- mapIds(org.Hs.eg.db,
                         keys=rownames(downReg),
                         column="SYMBOL",
                         keytype="ENSEMBL",
                         multiVals="first")
```

### GO Enrichment for Down-Regulated Genes
```R
GO_BP_DOWN <- enrichGO(downReg$symbol, OrgDb = "org.Hs.eg.db", 
                       keyType = "SYMBOL", ont = "BP")
GO_MF_DOWN <- enrichGO(downReg$symbol, OrgDb = "org.Hs.eg.db", 
                       keyType = "SYMBOL", ont = "MF")
```

#### Biological Process (BP) - LUNG
```R
dotplot(GO_BP_DOWN, title = "Downregualted Biological Process")
```
![immagine](https://github.com/user-attachments/assets/2e4ea2ac-9fc1-4c98-b035-59c421eb6c20)

#### Molecular Function (MF) - LUNG
```R
dotplot(GO_MF_DOWN, title = "Downregualted Molecular Functions")
```
![immagine](https://github.com/user-attachments/assets/177e79b3-afb7-4700-8b1b-0267922be755)

### COLON

#### Identifying Down-Regulated Genes - COLON
```R
downReg1 <- subset(resSig1, log2FoldChange < -1)
downReg1$symbol <- mapIds(org.Hs.eg.db,
                         keys=rownames(downReg1),
                         column="SYMBOL",
                         keytype="ENSEMBL",
                         multiVals="first")
```

#### GO Enrichment for Down-Regulated Genes - COLON
```R
GO_BP_DOWN1 <- enrichGO(downReg1$symbol, OrgDb = "org.Hs.eg.db", 
                        keyType = "SYMBOL", ont = "BP")
GO_MF_DOWN1 <- enrichGO(downReg1$symbol, OrgDb = "org.Hs.eg.db", 
                        keyType = "SYMBOL", ont = "MF")
```

#### Biological Process (BP) - COLON
```R
dotplot(GO_BP_DOWN1, title = "Downregualted Biological Process")
```
![immagine](https://github.com/user-attachments/assets/f3f48b27-7787-45c3-9e8e-c2eb7a02f32e)

#### Molecular Function (MF) - COLON
```R
dotplot(GO_MF_DOWN1, title = "Downregualted Molecular Functions")
```
![immagine](https://github.com/user-attachments/assets/7f3538a5-2ce0-4ab7-a85f-b443118f44ee)


```
