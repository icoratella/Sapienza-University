# RProject: Transcriptional and Proteomic Insights into the Host Response in Fatal COVID-19 Cases

This project aims to replicate and extend the differential expression analysis presented in the study:

*Transcriptional and Proteomic Insights into the Host Response in Fatal COVID-19 Cases*

Authors: Meng Wu, Yaobing Chen, Han Xia, Changli Wang, Chin Yee Tan, Xunhui Cai, Yufeng Liu, Fenghu Ji, Peng Xiong, Ran Liu, Yuanlin Guan, Yaqi Duan, Dong Kuang, Sanpeng Xu, Hanghang Cai, Qin Xia, Dehua Yang, Ming-Wei Wang, Isaac M. Chiu, Chao Cheng, Philip P. Ahern, Liang Liu, Guoping Wang, Neeraj K. Surana, Tian Xia, Dennis L. Kasper.
The analysis focuses on identifying differentially expressed genes (DEGs) in lung and colon tissues of COVID-19 patients compared to healthy controls. By performing comprehensive bioinformatics analyses, we explore the transcriptional changes and underlying biological processes associated with SARS-CoV-2 infection.

### Table of Contents:

    0. Introduction
    1. Data Acquisition and Preprocessing
    2. Differential Expression Analysis
    3. Results
        3.1 Differentially Expressed Genes
        3.2 Visualization
    4. Gene Ontology Enrichment Analysis
        4.1 Up-regulated Genes
        4.2 Down-regulated Genes
    5. Comparison with Expression Atlas
    6. Conclusion
    7. References

## 0. Introduction

The COVID-19 pandemic, caused by SARS-CoV-2, has prompted extensive research to understand the disease's pathogenesis. This project investigates the host transcriptional response in lung and colon tissues from fatal COVID-19 cases. By performing differential expression analysis and functional enrichment, we aim to uncover key biological pathways and molecular functions altered during infection.
Data Acquisition and Preprocessing
Filtering the Original Dataset

    Data Source: Experimental design and raw counts were obtained from the original study's dataset.
    Sample Selection: I have separated the samples on the basis of the tissue type, then I divided also  the counts of the genes. 
    Uploading of the data: I have uploaded the data of the study, both the study design and the gene counts. I did it both for LUNG and COLON.

    Normalization: Count data were normalized using the DESeq2 package to account for library size differences and other technical variations.
    Removal of Unnecessary Columns: Extra columns, such as duplicate gene identifiers, were removed to streamline the dataset.

Differential Expression Analysis
Methodology

    Software Used: DESeq2 package in R.
    Design Formula: Specified to compare COVID-19 patients versus healthy controls.
    Filtering Lowly Expressed Genes: Genes with low counts across all samples were excluded to reduce noise.
    Normalization and Dispersion Estimation: Performed using DESeq2's internal functions to prepare data for differential expression testing.

Quality Control and Outlier Detection

    Variance Stabilizing Transformation (VST): Applied to stabilize the variance across the mean values.
    Principal Component Analysis (PCA):
        Purpose: To visualize sample clustering and identify outliers.
        Findings: An outlier sample in the lung tissue dataset was identified, showing high variance compared to other samples.
    Sample Distance Heatmap:
        Purpose: To assess the similarity between samples.
        Findings: Confirmed the presence of the outlier detected in the PCA plot.
    Outlier Removal: The identified outlier sample was removed from the lung tissue dataset to improve analysis accuracy.

Results
Differentially Expressed Genes

Differential expression analysis was performed to identify DEGs between COVID-19 patients and healthy controls.

    Thresholds Applied:
        Adjusted p-value (padj) < 0.05.
        Log2 fold change (log2FC) thresholds of >1 (up-regulated) and <-1 (down-regulated).
    Lung Tissue Results:
        Up-regulated Genes:
            Number: 3447 genes.
            Notable up-regulated genes included those involved in inflammatory responses and immune activation.
        Down-regulated Genes:
            Number: 4556 genes.
            Included genes associated with metabolic processes and cellular respiration.
    Colon Tissue Results:
        Up-regulated Genes: 2805 genes.
        Down-regulated Genes: 7525 genes.

Visualization
Principal Component Analysis (PCA)

    Lung Tissue:
        Post outlier removal, PCA plots showed clear separation between COVID-19 patients and healthy controls.
    Colon Tissue:
        PCA plots indicated less distinct separation, suggesting subtler transcriptional differences in colon tissue.

Heatmaps

    Sample-to-Sample Distance Heatmaps:
        Visualized the clustering of samples based on expression profiles.
        Lung tissue samples clustered according to disease status after outlier removal.
        Colon tissue samples showed more variability.

Volcano and MA Plots

    Volcano Plots:
        Displayed the distribution of DEGs based on statistical significance and magnitude of change.
        Highlighted genes with significant up-regulation or down-regulation.
    MA Plots:
        Showed the relationship between mean expression and log2 fold change.
        Aided in identifying genes with large fold changes across expression levels.

Gene Ontology Enrichment Analysis
Up-regulated Genes

Performed Gene Ontology (GO) enrichment analysis to identify biological processes and molecular functions overrepresented among up-regulated genes.

    Biological Processes:

    Molecular Functions:
        Cytokine activity.
        Chemokine receptor binding.

Down-regulated Genes

Analyzed down-regulated genes to uncover suppressed pathways and functions.

    Biological Processes:
        Cellular respiration.
        Oxidative phosphorylation.
        Metabolic processes.
    Molecular Functions:
        Enzyme binding.
        Structural constituent of ribosome.

Comparison with Expression Atlas

To validate our findings, selected DEGs were compared with results from the Expression Atlas.

    C2orf91:
        Our Log2FC: -8.27.
        Expression Atlas Log2FC: -7.1.
    UPK3B:
        Our Log2FC: -8.25.
        Expression Atlas Log2FC: -6.8.
    SERPINB4:
        Our Log2FC: 8.34.
        Expression Atlas Log2FC: 6.4.
    CYP19A1:
        Our Log2FC: 6.96.
        Expression Atlas Log2FC: 5.7.

Conclusion: The close agreement in log2 fold changes confirms the reliability and accuracy of our differential expression analysis.
Conclusion

This comprehensive analysis successfully replicated key findings from the original study, identifying significant DEGs and enriched biological processes associated with COVID-19 in lung and colon tissues.

    Key Findings:
        Up-regulation of genes involved in immune response and inflammation in lung tissue.
        Down-regulation of genes associated with metabolic processes.
        Subtle transcriptional changes in colon tissue, suggesting systemic effects of SARS-CoV-2 infection.
    Bioinformatics Proficiency:
        Demonstrated expertise in data preprocessing, normalization, outlier detection, differential expression analysis, and functional enrichment.
        Utilized advanced R packages and statistical methods to derive meaningful biological insights.

References

    Original Study: Transcriptional and Proteomic Insights into the Host Response in Fatal COVID-19 Cases.
    DESeq2: Love MI, Huber W, Anders S (2014). Moderated estimation of fold change and dispersion for RNA-seq data with DESeq2. Genome Biology.
    clusterProfiler: Yu G, Wang LG, Han Y, He QY (2012). clusterProfiler: an R package for comparing biological themes among gene clusters. OMICS: A Journal of Integrative Biology.
    org.Hs.eg.db: Carlson M (2019). org.Hs.eg.db: Genome wide annotation for Human. R package version 3.8.2.


