Huan Liu, Yi Chen, Ce Shi, Xinting Yang, Donghai Han,
FT-IR and Raman spectroscopy data fusion with chemometrics for simultaneous determination of chemical quality indices of edible oils during thermal oxidation,
LWT,
Volume 119,
2020,
108906,
ISSN 0023-6438,
https://doi.org/10.1016/j.lwt.2019.108906.
(https://www.sciencedirect.com/science/article/pii/S0023643819312484)
**Abstract**: A rapid, non-destructive and robust method for measuring peroxide values (PVs) and acid values (AVs) of common edible oils (soybean, rapeseed, sunflower and peanut) simultaneously under various thermal oxidation was explored by FT-IR and Raman spectroscopy data fusion strategy. Uninformative variable elimination (UVE) and successive projections algorithm (SPA) methods were used for feature variables extraction, quantitative models for prediction of chemical quality indices were established using partial least squares regression (PLSR) algorithm. The bands associated with vibration of C=O and C=C stretching were highly correlated with PVs and AVs, data fusion of the two spectra showed the best modeling results when variables identified by SPA were used. For modeling of PVs, the resulting Rc2 and Rp2 were 0.964 and 0.939, RMSEC and RMSEP were 0.060 and 0.080. For modeling of AVs, the resulting Rc2 and Rp2 were 0.955 and 0.919, RMSEC and RMSEP were 0.025 and 0.027.
Keywords: Data fusion strategy; Feature variables extraction; SPA-PLS; Quality indices; Edible oils


Anche questi analizzano l'olio.

Usano PLS.

Usano mid-level data fusion:

Data fusion is divided into three levels, in this study, mid-level data fusion strategy was implemented, in which a previous variable selection step was independently performed over the spectral data obtained from each kind of technique, so only the most relevant variables were fused. Since FT-IR and Raman spectra have different dimensions, in order to eliminate dimensional effects between each kind of spectra, z-score method was used to standardize spectral data ([Márquez, López, Ruisánchez, & Callao, 2016](https://www.sciencedirect.com/science/article/pii/S0023643819312484#bib22)). The original variables were normalized to the [−1, 1] range to obtain similar numerical weights through the following Eq. [(5)](https://www.sciencedirect.com/science/article/pii/S0023643819312484#fd5)(5)where _x__ij_ is the _i_th variable (i.e. spectral intensity value at frequency i) for the _j_th sample,‾_x__i_ and _σ__i_ are the mean and standard deviation.

The XIR-Raman matrix was then obtained from all the samples and all variables for both FT-IR and Raman spectra. Its magnitude is indicative of the variables characteristic of oxidation. The raw variables selected from each data source were then fused (concatenated), and PLS algorithm was performed. Z-score standardization was analyzed by employing statistical software of the SPSS 19.0 (SPSS Institute, Chicago, USA).