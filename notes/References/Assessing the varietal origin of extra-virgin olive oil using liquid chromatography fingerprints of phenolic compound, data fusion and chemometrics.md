Aadil Bajoub, Santiago Medina-Rodríguez, María Gómez-Romero, El Amine Ajal, María Gracia Bagur-González, Alberto Fernández-Gutiérrez, Alegría Carrasco-Pancorbo,
Assessing the varietal origin of extra-virgin olive oil using liquid chromatography fingerprints of phenolic compound, data fusion and chemometrics,
Food Chemistry,
Volume 215,
2017,
Pages 245-255,
ISSN 0308-8146,
https://doi.org/10.1016/j.foodchem.2016.07.140.
(https://www.sciencedirect.com/science/article/pii/S0308814616311736)

**Abstract**: High Performance Liquid Chromatography (HPLC) with diode array (DAD) and fluorescence (FLD) detection was used to acquire the fingerprints of the phenolic fraction of monovarietal extra-virgin olive oils (extra-VOOs) collected over three consecutive crop seasons (2011/2012-2013/2014). The chromatographic fingerprints of 140 extra-VOO samples processed from olive fruits of seven olive varieties, were recorded and statistically treated for varietal authentication purposes. First, DAD and FLD chromatographic-fingerprint datasets were separately processed and, subsequently, were joined using “Low-level” and “Mid-Level” data fusion methods. After the preliminary examination by principal component analysis (PCA), three supervised pattern recognition techniques, Partial Least Squares Discriminant Analysis (PLS-DA), Soft Independent Modeling of Class Analogies (SIMCA) and K-Nearest Neighbors (k-NN) were applied to the four chromatographic-fingerprinting matrices. The classification models built were very sensitive and selective, showing considerably good recognition and prediction abilities. The combination “chromatographic dataset+chemometric technique” allowing the most accurate classification for each monovarietal extra-VOO was highlighted.
Keywords: Monovarietal extra-virgin olive oils; High performance liquid chromatography; Phenolic compounds fingerprints; Data fusion; Chemometrics; Varietal origin

---

Cose rilevanti: low-level e mid-level data fusion, PCA + PLSDA, SIMCA, KNN. Diversità nel tipo di sensori.

**Domanda: cos'è mid-level data fusion?**

Risposta: sezione 2.4

In the “Low-level” data fusion strategy, the original data matrices from HPLC-DAD and HPLC-FLD analyses were concatenated and appropriately pretreated, and then the resulting fused data array was analyzed as if it was a simple data block. Prior to concatenation, each block was preprocessed using the data [pretreatment](https://www.sciencedirect.com/topics/agricultural-and-biological-sciences/pretreatment "Learn more about pretreatment from ScienceDirect's AI-generated Topic Pages") reported in [Table 1, supplementary](https://www.sciencedirect.com/science/article/pii/S0308814616311736#s0105). Moreover, to take into account the possible difference of variance between blocks as well as an unbalanced number of variables, together with the simple mean centering, a block variance scaling was also applied to the fused data array.

On the same dataset, the “Mid-level” data fusion strategy (which consists in concatenating features extracted from the original data blocks) was tested. In the present study, “Mid-level” data fusion was carried out concatenating the scores matrices of the optimal PLS-DA models calculated on the different individual data blocks (i.e., those whose parameters are reported in [Table 1 supplementary](https://www.sciencedirect.com/science/article/pii/S0308814616311736#s0105)).

--> MID-LEVEL DATA FUSION: data fusion eseguito sulle matrici riscalate con PCA o PLSDA. 

=====>> PLSDA è una tecnica di decomposizione e non di regressione! Ecco perché funziona in modo così strano!

Il paper spiega bene come funziona:

PLS-DA performs a reduction in the dimension of the predictor variables using an approach similar to principal component analysis. PLS-DA is based on the PLS2 algorithm ([Wold et al., 1983](https://www.sciencedirect.com/science/article/pii/S0308814616311736#b0205)) that searches for latent variables with a maximum covariance with the Y-variables. Of course, the main difference is related to the dependent variables, since these represent qualitative (and not quantitative) values when dealing with classification. In PLS-DA, the Y-block describes which objects are in the classes of interest. When dealing with N classes, the class vector is unfolded and the PLS2 algorithm is applied. For each object, PLS-DA will return the prediction as a vector of size N, with values between 0 and 1: an _n-th_ value closer to zero indicates that the object does not belong to the _n-th_ class while a value closer to one indicates the opposite. Since predicted vectors will not have the form (0,0,…,1,…0) but real values in the range between 0 and 1, a classification rule must be applied. The object can be assigned to the class with the maximum value in the Y vector or, alternatively, a threshold between 0 and 1 can be determined for each class on the basis of the Bayes theorem. The class threshold is selected at the point where the number of false positives and false negatives is minimized ([Barker & Rayens, 2003](https://www.sciencedirect.com/science/article/pii/S0308814616311736#b0010)). The latter was the one chosen in this study as decision rule.
