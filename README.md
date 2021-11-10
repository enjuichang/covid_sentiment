#  Covid Sentiment Analysis with SpaCy

*First time creating a NLP classification project? Want to have hands-on experience with SpaCy? Want to work with tweet datasets?*

In this article, we will go through the main concepts of NLP project, including the data selection, exploratory data analysis, 
NLP preprocessing, NLP models (statistical/neural language models), metrics selection, and implementation on another dataset. 
The dataset of interest is the COVID-19 tweet dataset on Kaggle, while all NLP-related tasks are performed using SpaCy.

The data source is the [Coronavirus Tweet Data](https://www.kaggle.com/datatattle/covid-19-nlp-text-classification) dataset 
from Kaggle.

## Structure of the data
```
│
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── raw            <- The original, immutable data dump.
│   └── processed      <- The final, canonical data sets for modeling.
│
├── config             <- Config files for training in spaCy.
│
├── models             <- Trained and serialized models, model predictions, or model summaries.
│
├── images             <- Images for the notebooks.
│
├── notebooks          <- Serialized Jupyter notebooks created in the project.
│   ├── All            <- Notebook that includes all codes.
│   ├── EDA            <- Exploratory data analysis process.
│   ├── Traditional    <- The training of traditional statistical models.
│   └── Neural         <- The training of neural network models.
│
└─── requirements.txt  <- The requirements file for reproducing the analysis environment.

```
