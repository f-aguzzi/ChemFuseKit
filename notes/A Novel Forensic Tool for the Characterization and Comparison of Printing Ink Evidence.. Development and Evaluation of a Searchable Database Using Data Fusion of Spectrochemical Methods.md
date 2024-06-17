
TY  - JOUR
AU  - Trejos, Tatiana
AU  - Torrione, Peter
AU  - Corzo, Ruthmara
AU  - Raeva, Ana
AU  - Subedi, Kiran
AU  - Williamson, Rhett
AU  - Yoo, Jong
AU  - Almirall, Jose
TI  - A Novel Forensic Tool for the Characterization and Comparison of Printing Ink Evidence: Development and Evaluation of a Searchable Database Using Data Fusion of Spectrochemical Methods
JO  - Journal of Forensic Sciences
JA  - J Forensic Sci
VL  - 61
IS  - 3
SN  - 0022-1198
UR  - https://doi.org/10.1111/1556-4029.13109
DO  - https://doi.org/10.1111/1556-4029.13109
SP  - 715
EP  - 724
KW  - forensic science
KW  - ink
KW  - document examination
KW  - database
KW  - spectrochemical
KW  - data fusion
PY  - 2016
AB  - Abstract A searchable printing ink database was designed and validated as a tool to improve the chemical information gathered from the analysis of ink evidence. The database contains 319 samples from printing sources that represent some of the global diversity in toner, inkjet, offset, and intaglio inks. Five analytical methods were used to generate data to populate the searchable database including FTIR, SEM-EDS, LA-ICP-MS, DART-MS, and Py-GC-MS. The search algorithm based on partial least-squares discriminant analysis generates a similarity ?score? used for the association between similar samples. The performance of a particular analytical method to associate similar inks was found to be dependent on the ink type with LA-ICP-MS performing best, followed by SEM-EDS and DART-MS methods, while FTIR and Py-GC-MS were less useful in association but were still useful for classification purposes. Data fusion of data collected from two complementary methods (i.e., LA-ICP-MS and DART-MS) improves the classification and association of similar inks.
ER  - 


---

Questo è importante perché è l'unico esempio facilmente individuabile di data fusion chemiometrica in ambito forense, anche se con un obiettivo diverso rispetto a quello di RISEN.

---

The PLSDA algorithm is an appropriate choice for inclusion because it (i) has very few parameters (the number of PLSDA components), (ii) generally provides very good performance, (iii) works across multiple different sensor types with minimal changes in preprocessing, (iv) is fast to train on very large databases, and (v) is very fast to evaluate on test samples [22](https://onlinelibrary.wiley.com/doi/full/10.1111/1556-4029.13109#jfo13109-bib-0022).

Data fusion is a powerful tool for improving the results by combining information across a number of different analytical techniques. Decisions made using data fusion across multiple techniques are often significantly better than decisions made using any of the techniques in isolation, because the mistakes made by different techniques tend to be independent of one another.

**Alternative a data fusion**

A number of different approaches to data fusion are possible, including data-level, confidence-level, and decision-level fusion. The developed software makes use of confidence-level fusion as this provides a good middle ground between the power of data-level fusion and the simplicity of decision-level fusion. The database makes use of a simple but robust “average-confidence” metric for combining outputs from the PLSDA confidences across up to five different analytical techniques. The average-confidence metric does not rely on having the same number of replicates in each sensor modality, and is simple to implement and interpret, and can be considered a simple approach to noise reduction from multiple independent measurements.

**SPECTRAL OVERLAY**

Comparison between the samples to estimate the discrimination power of each method by ink type was made using spectral overlay of the relevant variables present above the assigned threshold levels. Then, a pairwise comparison matrix was created to determine the overall discrimination potential. The spectral overlay allows a visual comparison of the spectral shapes and relative peak heights of the questioned and known sample spectra. Each pair comparison was made using at least three replicate spectra per sample to address the variability within the sample. Therefore, for each variable, the range of the questioned sample replicates was compared to the range of the known sample replicates. If the ranges of one or more elements in the questioned and known samples did not overlap, it was concluded that the samples were printed from a different source. For each spectral overlay, two examiners independently reviewed the data and grouped or discriminated the samples according to the differences and similarities of the replicate spectra.

**PLSDA e KNN**

These results indicate relatively robust performance for object classification using most of the proposed techniques together with PLSDA-based classification, particularly for those datasets that contained larger number of training sets or duplicate controls.

An ink was considered to be classified correctly if the correct duplicate was listed as one of top five selections provided by the PLSDA algorithm. The reasoning behind this match criteria decision is that in many cases, for inks with very similar chemical compositions, the true ink type may be the second or third most likely ink found by PLSDA. Likewise, for the KNN spectral comparisons, a correct classification was determined if any of the top 10 nearest spectra identified by KNN as possible match for the control sample had the same label as the test spectra.

Table [3](https://onlinelibrary.wiley.com/doi/full/10.1111/1556-4029.13109#jfo13109-tbl-0003 "Link to table") summarizes the performance of each technique by assessing the “correct association” of duplicate controls when the duplicates are analyzed on different days and/or by different operators or instruments.

Although preliminary, these results indicate relatively robust performance for ink classification using the proposed techniques. The performance of PLSDA vs. KNN algorithms seems to be dependent on the technique and can be improved in the future with larger training sets and duplicate controls for each ink type.