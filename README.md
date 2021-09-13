# Covid Sentiment Analysis

I used the [Coronavirus Tweet Data](https://www.kaggle.com/datatattle/covid-19-nlp-text-classification) from Kaggle to perform sentiment analysis...

## Structure of the data

│
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-jqp-initial-data-exploration`.
│
└─── requirements.txt   <- The requirements file for reproducing the analysis environment
│
└─── src                <- Source code for use in this project.
   │
   └── data             <- Scripts to download or generate data
       └── fetch_data.py