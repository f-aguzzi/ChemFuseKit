
Corrado Di Natale, Manuela Zude-Sasse, Antonella Macagnano, Roberto Paolesse, Bernd Herold, Arnaldo D’Amico,
Outer product analysis of electronic nose and visible spectra: application to the measurement of peach fruit characteristics,
Analytica Chimica Acta,
Volume 459, Issue 1,
2002,
Pages 107-117,
ISSN 0003-2670,
https://doi.org/10.1016/S0003-2670(02)00107-1.
(https://www.sciencedirect.com/science/article/pii/S0003267002001071)


---
## Abstract

Visual aspect and aroma are among the most important features of fruit that determine consumer preferences. Electronic nose and spectroscopic techniques have shown positive results in evaluating some basic analytical parameters of fruit and global features such as the cultivar.

In this paper, we illustrate and discuss a study aimed at evaluating the improvement derived by the fusion of visible spectra and electronic nose data. These experiments were performed on a population of yellow peaches belonging to two cultivars. Each sample was measured by visible optical spectroscopy and by electronic nose. In addition, a number of reference parameters were also measured by conventional destructive methodologies.

Collected data were analysed individually and then fused together in order to classify the two cultivars and to estimate the reference parameters. Data fusion was performed building the outer product matrix for each measurement. The set of matrices was then successively unfolded and analysed by conventional chemometrics tools.

Results were improved using outer products, for instance in classification average percentage errors of 25, 10, and 7 for electronic nose, spectra, and outer product, respectively was achieved. Regression analysis provides the evidence of a substantial orthogonal appearance of the datasets, which offer former hidden information on fruit classification.

---

Data were analysed using chemometrics tools, in particular partial least squares (PLS) was utilised both for classification of cultivars and quantitative regression of reference parameters. In the case of classification PLS is used as a method to solve discriminant analysis (PLS/DA). Generalisation error of models was evaluated through a cross-validation procedure using the leave-one-out method [[28]](https://www.sciencedirect.com/science/article/pii/S0003267002001071#BIB28). All calculations were performed in Matlab©.

---

As it is evident, no particular structure appears from a simple inspection of data, and hidden relevant information can be extracted only through a proper multivariate data analysis technique. The spectra taken at the opposite sides of the fruits are 
quite similar, it is worth to remind that the terms red and green-sides were only conventional and they were not very different in the explored wavelength range, in the case here measured.

The capability of the three datasets to correctly classify the two populations of fruits was tested applying PLS/DA. The performance was expressed through the measure of the percentage of the samples correctly classified in a leave-one-out cross validation procedure. The three datasets obtained the following percentages: spectra from red-side 97.5%, spectra from green-side 77.5%, and finally electronic nose 95.0%.

It has to be remarked the difference of information contained in the two spectra sets. This can be explained by the largest variance exhibited by the pigment contents in the samples. Later the relationship between reference parameters and cultivar discrimination will be shown and discussed. It is important here to put in evidence the scarcity of information that, in this case, the green-side of the fruits gives to the partial transmittance spectra. For this reason electronic nose data were fused only with the red-side spectra.

Data of electronic nose and visible spectroscopy are very different with each other. For each measurement electronic nose gives a vector of dimension seven. Each value is expressed in Hertz, and it is proportional to the increase of the amount of molecules adsorbed in the coating film from the gaseous phase when the sensor is exposed to the sample headspace.

On the other hand, for each measure the visible spectroscopy provides a vector of dimension 120. Each component is the attenuation of light transmitted and reflected, by the skin surface and the portion of flesh probed, at a certain wavelength, or better in a range of wavelength defined by the resolution power of the spectrometer. These values are normally dimensionless being the result of the ratio between the intensities of the transmitted light and a blank calibration.

In this paper, the outer product was chosen as a method of fusing the two different datasets. Outer product consists, for each measurement, in the Cartesian product of one vector for the other [[26]](https://www.sciencedirect.com/science/article/pii/S0003267002001071#BIB26). In this way a matrix, dimension 7×120, represent the composed measurement of each single sample. Each component of the spectra is multiplied by each component of the electronic nose. Therefore, the outer product matrix will contain all the possible combination of the intensity values of both signals. Finally, we can say that each instrument data are weighted by the other instrument data. [Fig. 2](https://www.sciencedirect.com/science/article/pii/S0003267002001071#FIG2) shows an example of one of these outer product matrices.
