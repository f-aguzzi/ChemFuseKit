
Francisco Julián Cuevas, Gema Pereira-Caro, José Manuel Moreno-Rojas, José Manuel Muñoz-Redondo, María José Ruiz-Moreno,
Assessment of premium organic orange juices authenticity using HPLC-HR-MS and HS-SPME-GC-MS combining data fusion and chemometrics,
Food Control,
Volume 82,
2017,
Pages 203-211,
ISSN 0956-7135,
https://doi.org/10.1016/j.foodcont.2017.06.031.
(https://www.sciencedirect.com/science/article/pii/S0956713517303304)

**Abstract**: This study aims to develop a robust chemometric approach to make it possible to authenticate European premium organic orange juices. The metabolomic fingerprinting and the volatile profile of commercial orange juices were analyzed by HPLC-HR-MS and HS-SPME-GC-MS. These data were used for authentication (classification of orange juices) purposes, using principal component analysis, hierarchical cluster analysis and partial least squares discriminant analysis, which provided acceptable results. Some flavonoids, fatty acids, aldehydes and esters were identified as potential markers involved in the differentiation of organic juices. Data fusion strategies were tested and 'mid-level' data fusion achieved an optimal model for classifying organic or conventional orange juices with a sensitivity and specificity of 100%, thus improving the individual models. This approach, combining mass spectrometry techniques, chemometrics and data fusion, likely provides a new framework for the authentication of organic foodstuffs.

Keywords: Organic farming; Data fusion; Authentication; Foodomics; Chemometrics

---

Mid-level data fusion anche qui. Va proprio tentata anche nel progetto.

Il problema è che ai fini della ricerca ho a disposizione solo un dataset piccolissimo con tre sensori, e l'altro ne ha solo due. Online non si trova nulla di utilizzabile a questo fine.

---

Data fusion involves using different instrumental techniques and combining the data they generate. [Borràs et al. (2015)](https://www.sciencedirect.com/science/article/pii/S0956713517303304#bib6) proposed grouping the strategies into three categories: 'Low-level', 'Mid-level' and 'High-level'. To find an optimal classification model for the classes selected (organic or conventional), low-level and mid-level data fusion were tested for the two blocks (LC and GC matrices) obtained from the [mass spectrometry](https://www.sciencedirect.com/topics/agricultural-and-biological-sciences/mass-spectrometry "Learn more about mass spectrometry from ScienceDirect's AI-generated Topic Pages")techniques. The objective of the data fusion was to obtain the maximum number of correctly classified samples. In low-level fusion, data are simply concatenated sample-wise into a unique matrix containing all the information from the different instruments (with as many rows as the number of samples and as many columns as the number of variables from all the instruments) before building the model. The PLS-DA model developed can extract correlations between variables of different blocks (or instruments) weighing the importance of each instrument to the objective evaluated. The predominance of one data source over the others (dimensional distortion) can be avoided using pre-processing techniques ([Borràs et al., 2015](https://www.sciencedirect.com/science/article/pii/S0956713517303304#bib6)). A limitation of this strategy is that the increase in useful information given by each apparatus cannot compensate for the amount of irrelevant data added by each instrument. In the mid-level fusion, relevant features were selected from the individual PLS-DA models (GC-MS and LC-MS). These features can be obtained by variable selection procedures ([Borràs et al., 2015](https://www.sciencedirect.com/science/article/pii/S0956713517303304#bib6)) and concatenated into a single matrix or through the multi-way methods ([Smilde, van der Werf, Bijlsma, van der Werff-van der Vat, & Jellema, 2005](https://www.sciencedirect.com/science/article/pii/S0956713517303304#bib37)). With this technique, dimensional distortion is avoided, while the main disadvantage is the need to build a preliminary model of the individual blocks that will determine the goodness of the mid-level data fusion approach.

---

^^^ Qui spiega come mai mid-level data fusion è superiore.

Insomma si può andare diretti con la PLSDA oppure ci sono tecniche di selezione vera e propria. L'idea generale è che se non si fa feature selection prima di unire, i regressori in più potrebbero portare più rumore che segnale.

Nel mid-level pesano di più le singole scelte dei singoli algoritmi di feature selection, nel low-level contano le dimensioni dei dataset.