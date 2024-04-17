import numpy as np
import pandas as pd

# COSE DA FARE: SCELTA PREPROCESSING, TESTARE EXPORT

def snv(input_data):
  
    # Define a new array and populate it with the corrected data  
    output_data = np.zeros_like(input_data)
    for i in range(input_data.shape[0]):
 
        # Apply correction
        output_data[i,:] = (input_data[i,:] - np.mean(input_data[i,:])) / np.std(input_data[i,:])
 
    return output_data

class LLDF_Model:
    def __init__(self, X_data, Y_dataframe, X_train, Y):
        self.X_data = X_data
        self.Y_dataframe = Y_dataframe
        self.X_train = X_train
        self.Y = Y

class LLDF:
    def __init__(self, preprocessing='snv'):
        self.preprocessing = preprocessing

    def lldf(self):
        path = input("Insert the QEPAS file path:")
        sheet = input("Insert the QEPAS sheet name:")
        spectra = pd.read_excel(path, sheet_name=sheet, index_col=0, header=0)
        path = input("Insert the GC file path:")
        sheet = input("Insert the GC sheet name:")
        ret_time = pd.read_excel(path, sheet_name=sheet, index_col=0, header=0)

        # select only numerical attributes
        X_spectra = spectra.iloc[:, 1:]
        X_time = ret_time.iloc[:, 1:]

        #Selection of classes from the spectra database
        Y = spectra.loc[:, 'Substance'].values

        Y_dataframe = pd.DataFrame(Y, columns=['Substance'])

        # It is necessary to convert the column names as string to select them
        spectra.columns = spectra.columns.astype(str) # to make the colnames as text

        #wavelenghts for plots (variables)
        # Your string with numbers separated by spaces
        numbers_string = "8 8,0126	8,0253 8,038	8,0507	8,0635	8,0763	8,0892	8,1021	8,115	8,128	8,141	8,1541	8,1672	8,1804	8,1935	8,2068	8,2201	8,2334	8,2468	8,2602	8,2736	8,2871	8,3007	8,3142	8,3279	8,3415	8,3553	8,369	8,3828	8,3967	8,4106	8,4245	8,4385	8,4526	8,4667	8,4808	8,495	8,5092	8,5235	8,5378	8,5522	8,5666	8,5811	8,5956	8,6102	8,6248	8,6395	8,6542	8,6689	8,6838	8,6986	8,7136	8,7285	8,7435	8,7586	8,7737	8,7889	8,8042	8,8194	8,8348	8,8502	8,8656	8,8811	8,8967	8,9123	8,9279	8,9437	8,9594	8,9753	8,9912	9,0071	9,0231	9,0391	9,0553	9,0714	9,0877	9,1039	9,1203	9,1367	9,1532	9,1697	9,1863	9,2029	9,2196	9,2364	9,2532	9,2701	9,287	9,304	9,3211	9,3382	9,3554	9,3727	9,39	9,4074	9,4249	9,4424	9,46	9,4776	9,4953	9,5131	9,531	9,5489	9,5669	9,5849	9,603	9,6212	9,6395	9,6578	9,6762	9,6947	9,7132	9,7318	9,7505	9,7692	9,7881	9,8069	9,8259	9,845	9,8641	9,8833	9,9025	9,9219	9,9413	9,9608	9,9804	10"
        
        # Replace commas with points and join the numbers with a space
        wl = np.array(list(map(lambda x: float(x.replace(',', '.')), numbers_string.split())))

        # Preprocessing
        if self.preprocessing == 'snv':
            # Compute the SNV on spectra
            preprocessed_spectra = snv(X_spectra.values)
        elif self.preprocessing == 'savgol':
            # Preprocessing with Savitzki-Golay - smoothing, defining the window, the order and the use of derivatives
            from scipy.signal import savgol_filter
            preprocessed_spectra = savgol_filter(X_spectra, 7, polyorder = 2, deriv=0)
        elif self.preprocessing == 'savgol+snv':
            # We can also combine the preprocessing strategies together: Savitzki-Golay - smoothing + SNV
            X_savgol = savgol_filter(X_spectra, 7, polyorder = 2, deriv=0)
            preprocessed_spectra = snv(X_savgol)
        else:
            raise Exception(f"LLDF: this type of preprocessing does not exist ({self.preprocessing=})")


        # Create a new DataFrame with the processed numerical attributes
        processed_dataframe_spectra = pd.DataFrame(preprocessed_spectra, columns=spectra.columns[1:])
        processed_dataframe_spectra.head()

        X_RT_array = X_time.values

        # Create a new DataFrame with the processed numerical attributes
        processed_dataframe_rt = pd.DataFrame(X_RT_array, columns=ret_time.columns[1:])

        # X training set
        X_train = pd.concat([Y_dataframe, processed_dataframe_spectra, processed_dataframe_rt], axis = 1)

        # select only numerical attributes
        X_data = X_train.iloc[:, 1:]

        self.fused_data = LLDF_Model(X_data, Y_dataframe, X_train, Y)

    def export_data(self):
        path = input("Insert the output file path: ")
        pd.DataFrame(self.fused_data).to_excel(path)