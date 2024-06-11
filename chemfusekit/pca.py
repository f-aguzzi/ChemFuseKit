'''Principal Component Analysis Module'''
from copy import copy
from functools import cached_property
from typing import Optional

import numpy as np
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

from sklearn.decomposition import PCA as PC

import scipy.stats

from chemfusekit.__utils import print_table, GraphMode
from .__base import BaseDataModel


class PCADataModel(BaseDataModel):
    '''Data model for the PCA outputs.'''
    def __init__(self, x_data: pd.DataFrame, x_train: pd.DataFrame, y: np.ndarray, array_scores: np.ndarray,
                 components: int):
        super().__init__(x_data, x_train, y)
        self.array_scores = array_scores
        self.components = components


class PCASettings:
    '''Holds the settings for the PCA object.'''
    def __init__(self, target_variance: float = 0.95,
                 confidence_level: float = 0.05,
                 initial_components: int = 10, output: GraphMode = GraphMode.NONE):
        if target_variance < 0:
            raise ValueError("Target variance should be positive or null.")
        if confidence_level < 0 or confidence_level > 1:
            raise ValueError("Confidence level should be between 0 and 1.")
        if initial_components < 3:
            raise ValueError("Initial components should be at least 3.")
        self.target_variance = target_variance
        self.confidence_level = confidence_level
        self.initial_components = initial_components
        self.output = output


class PCA:
    '''A class to store the data, methods and artifacts for Principal Component Analysis'''
    def __init__(self, settings: PCASettings, data: BaseDataModel):
        self.data = data
        self.components = 0
        self.pca_model: Optional[PC] = None
        self.settings = settings
        self.array_scores: Optional[np.ndarray] = None

    def pca(self):
        '''Performs Principal Component Analysis.'''

        # Read from the data fusion object
        x_data = self.data.x_data

        # Run PCA producing the reduced variable Xreg and select the first 10 components
        pca = PC(self.settings.initial_components)
        pca.fit(x_data)

        # Define the class vector (discrete/categorical variable)
        # y_dataframe = pd.DataFrame(self.fused_data.y, columns=['Substance'])
        # classes = y_dataframe.astype('category') (a cosa serve?)
        out_sum = np.cumsum(pca.explained_variance_ratio_)

        # Autoselect the number of components
        for i, x in enumerate(out_sum):
            if x >= self.settings.target_variance:
                self.components = i
                break
        self.components = max(self.components, 3)

        compsexpv = [[(i+1), pca.explained_variance_ratio_[i]] for i in np.arange(pca.n_components_)]
        comps, expv = zip(*compsexpv)
        print_table(
            ["Components", "Explained Variance"],
            [comps, expv],
            "Proportion of Variance Explained",
            mode=self.settings.output
        )

        if self.settings.output is GraphMode.GRAPHIC:
            # PCA scree plot
            pc_values = np.arange(pca.n_components_) + 1
            plt.plot(pc_values, pca.explained_variance_ratio_, 'ro-', linewidth=2)
            plt.title('Scree Plot')
            plt.xlabel('Principal Component')
            plt.ylabel('Proportion of Variance Explained')
            plt.show()

        compsexpv = [[(i+1), out_sum[i]] for i in np.arange(pca.n_components_)]
        comps, expv = zip(*compsexpv)
        print_table(
            ["Components", "Cumulative Explained Variance"],
            [comps, expv],
            "Cumulative Proportion of Variance Explained",
            mode=self.settings.output
        )

        if self.settings.output is GraphMode.GRAPHIC:
            # Cumulative explained variance ratio
            plt.plot(pc_values, out_sum, 'ro-', linewidth=2)
            plt.title('Scree Plot (cumulative)')
            plt.xlabel('Principal Component')
            plt.ylabel('Cumulative Proportional Variance Explained')
            plt.show()

        # Run PCA producing the pca_model with a proper number of components
        pca = PC(n_components=self.components)
        self.pca_model = pca
        self.pca_model.fit(x_data)

    def pca_stats(self):
        '''Produces PCA-related statistics.'''
        x_data = self.data.x_data
        x_train = self.data.x_train

        # Prepare the Scores dataframe (and concatenate the original 'Region' variable)
        pc_cols = [f"PC{i+1}" for i in range(self.components)]
        scores = pd.DataFrame(data=self.pca_model.fit_transform(x_data), columns=pc_cols)
        scores.index = x_data.index
        scores = pd.concat([scores, x_train.Substance], axis = 1)
        
        print_table(
            pc_cols + ['Substance'],
            [scores.iloc[:,i] for i in range(scores.shape[1])],
            "PCA scores for each component",
            self.settings.output
        )

        # Prepare the loadings dataframe
        loadings = pd.DataFrame(
            self.pca_model.components_.T,
            columns=pc_cols,
            index=x_data.columns
        )
        loadings["Attributes"] = loadings.index
    
        print_table(
            pc_cols + ['Retention Time'],
            [loadings.iloc[:,i] for i in range(loadings.shape[1])],
            "PCA Loadings",
            self.settings.output
        )

        if self.settings.output is GraphMode.GRAPHIC:
            # View the scores plot using plotly library
            fig = px.scatter(
                scores,
                x="PC1",
                y="PC2",
                color="Substance",
                hover_data=['Substance'],
                hover_name=x_data.index
            )
            fig.update_xaxes(zeroline=True, zerolinewidth=1, zerolinecolor='Black')
            fig.update_yaxes(zeroline=True, zerolinewidth=1, zerolinecolor='Black')
            fig.update_layout(
                height=600,
                width=800,
                title_text='PCA Scores Plot colored by Substance')
            fig.show()

            # Plot 3D scores
            fig = px.scatter_3d(
                scores,
                x='PC1',
                y='PC2',
                z='PC3',
                color='Substance',
                hover_data=['Substance'],
                hover_name=x_data.index
            )
            fig.show()

        # Get PCA scores
        t = scores.iloc[:,0:self.components]
        # Get PCA loadings
        p = loadings.iloc[:,0:self.components]
        # Calculate error array
        err = x_data - np.dot(t,p.T)
        # Calculate Q-residuals (sum over the rows of the error array)
        q= np.sum(err**2, axis=1)
        # Calculate Hotelling's T-squared (note that data are normalised by default)
        tsq = np.sum((t/np.std(t, axis=0))**2, axis=1)

        def mean_confidence_interval(data, confidence=self.settings.confidence_level):
            a = 1.0 * np.array(data)
            n = len(a)
            m, se = np.mean(a), scipy.stats.sem(a)
            h = se * scipy.stats.t.ppf((1 + confidence) / 2., n-1)
            return m, m-h, m+h

        tsq_conf = (mean_confidence_interval(
            tsq.values,
            confidence=self.settings.confidence_level)
        )[2]
        q_conf = (mean_confidence_interval(
            q.values,
            confidence=self.settings.confidence_level)
        )[2]

        # Create a dataframe using only T2 and Q-residuals
        hot_q_data = pd.DataFrame(
            {'T2': tsq, 'Qres': q, 'Substance': x_train.Substance},
            index = x_data.index
        )

        if self.settings.output is GraphMode.GRAPHIC:
            # Plot the Hotelling T2 vs Q-residuals plot
            fig = px.scatter(
                hot_q_data,
                x="T2",
                y="Qres",
                hover_data={'Sample': (hot_q_data.index)},
                color = "Substance"
            )
            fig.add_hline(y=abs(q_conf),line_dash="dot", line_color='Red')
            fig.add_vline(x=tsq_conf,line_dash="dot", line_color='Red')
            fig.update_traces(textposition='top center')
            fig.update_layout(
                height=600,
                width=800,
                title_text="Hotelling's T2 vs Q-residuals")
            fig.show()

        # Normalize Q-residuals and Hotelling's T-squared
        normalized_q = q / np.max(q)
        normalized_tsq = tsq / np.max(tsq)

        # Create a DataFrame with normalized values
        normalized_hot_q_data = {
            'T2': normalized_tsq,
            'Qres': normalized_q,
            'Substance': x_train.Substance
        }
        normalized_hot_q_data = pd.DataFrame(normalized_hot_q_data, index=x_data.index)

        if self.settings.output is GraphMode.GRAPHIC:
            # Plot the normalized Hotelling T2 vs Q-residuals plot
            fig_normalized = px.scatter(
                normalized_hot_q_data,
                x="T2",
                y="Qres",
                hover_data={'Sample': (normalized_hot_q_data.index)},
                color="Substance"
            )
            fig_normalized.add_hline(y=abs(q_conf / np.max(q)), line_dash="dot", line_color='Red')
            fig_normalized.add_vline(x=tsq_conf / np.max(tsq), line_dash="dot", line_color='Red')
            fig_normalized.update_traces(textposition='top center')
            fig_normalized.update_layout(
                height=600,
                width=800,
                title_text="Normalized Hotelling's T2 vs Q-residuals"
            )
            fig_normalized.show()

        # Assuming 'scores' is your DataFrame with the 'class' column
        # Drop the 'class' column before converting to NumPy array
        array_scores = scores.drop('Substance', axis=1).values

        print_table(
            pc_cols,
            [array_scores[:,i] for i in range(array_scores.shape[1])],
            "Array without 'Substance' column",
            self.settings.output
        )

        self.array_scores = array_scores

    def export_data(self) -> PCADataModel:
        '''Export data artifacts.'''
        if self.pca_model is None or self.array_scores is None:
            raise RuntimeError("Run both pca() and pca_stats() methods before exporting data!")

        return PCADataModel(
            self.data.x_data,
            self.data.x_train,
            self.data.y,
            self.array_scores,
            self.components
        )

    @cached_property
    def rescaled_data(self) -> PCADataModel:
        if self.array_scores is None:
            settings_backup = copy(self.settings)
            self.settings.output = GraphMode.NONE
            if self.pca_model is None:
                self.pca()
            self.pca_stats()

        x_data = pd.DataFrame(self.pca_model.transform(self.data.x_data))
        y_dataframe = pd.DataFrame(self.data.y, columns=['Substance'])
        x_train = pd.concat(
            [y_dataframe, x_data],
            axis=1
        )

        return PCADataModel(
            x_data,
            x_train,
            self.data.y,
            self.array_scores,
            self.components
        )
