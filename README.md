# Arabic Fake News Detection

This is the repository of our NLP701 course project at MBZUAI.

This repository contains the implementation and experiments for detecting fake news in Arabic. The focus is on understanding the characteristics of fake news and developing models to effectively differentiate between fake and real news, leveraging diverse datasets such as satirical articles, BBC news, and COVID-19 tweets.

## Installation

Run the following to clone this repository:

<pre>
<code>
git clone https://github.com/your_username/arabic-fake-news.git
cd arabic-fake-news
</code>
<button onclick="copyToClipboard(this.previousElementSibling.innerText)"></button>
</pre>

### Installing Requirements

All dependencies used in the project are listed in the `requirements.txt` file and can be installed using the terminal command `pip install -r requirements.txt`.

<!--## Usage
To Run the experiments please run the following code,
-

<pre>
<code>

</code>
<button onclick="copyToClipboard(this.previousElementSibling.innerText)"></button>
</pre> -->

<!-- ## Experiments

For our paper, we ran the following experiments with each model (SVM, XGBoost, LSTM, and CNN) to perform consistent comparisons

| Train    | Test     |
| -------- | -------- |
| Articles | Articles |
| Articles | Tweets   |
| Tweets   | Tweets   |
| Tweets   | Articles |
| Both     | Both     | -->

## Codebase

- `Comparative_text_Analysis` contains the python notebook involving all the analysis done in our report related to the topics of the text in the datasets, and the associated graphs and figures.
- `dataset_preprocessing` contains the code for preprocessing the tweets and articles in the two seperate folders, as well as the code for combining them into one dataset in `combine_final_datasets.ipynb`.
- `final_datasets` contains the three final preprocessed datasets that were used in our experiments: `articles_dataset.csv`, `combined_dataset.csv`, `tweets_dataset.csv`. In training the different models, a random state of 42 was used to ensure a consistent train-test split across models.
- `Models` contains the `Experiment results` folder which includes .txt files of the results outputted by the different models. Additionally, it contains the implementations of the four different models we trained:

  1. `lstm.ipynb` contains code related to the LSTM deep learning model.
  2. `CNN_Fake_news.ipynb` contains code related to the CNN deep learning model.
  3. `Machine_Learning_Models.ipynb` contains code for the SVM and XGBoost machine learning models.
     Additionally, `testing_features_hyperparameter` and `Machine_Learning_Models_grid_search.ipynb` are related to tuning the hyperparameters of the SVM and XGBoost models.

## Datasets

- The ArCOV-19 Rumors dataset that we used (before preprocessing) can be found in the `Tweets.txt` file found [here.](https://gitlab.com/bigirqu/ArCOV-19/-/tree/master/ArCOV19-Rumors/tweet_verification?ref_type=heads)
- The Satirical fake news dataset GitHub repo can be found [here.](https://github.com/sadanyh/Arabic-Satirical-Fake-News-Dataset)
- The BBC and CNN data came from [this]() dataset.

## Acknowledgements

Our project idea was motivated by Saadany et al's [ _Fake or Real? A Study of Arabic Satirical Fake News_](https://aclanthology.org/2020.rdsm-1.7/). Many thanks for their wonderful work.

## References

<pre>
<!-- <code> -->
@inproceedings{saadany2020fake, title={Fake or Real? A Study of Arabic Satirical Fake News},
author={Saadany, Hadeel and Orasan, Constantin and Mohamed, Emad},
booktitle={Proceedings of the 3rd International Workshop on Rumours and Deception in Social Media (RDSM)},
pages={70--80},
year={2020} }


@inproceedings{covid_tweets,
    title = "{A}r{COV}19-Rumors: {A}rabic {COVID}-19 {T}witter Dataset for Misinformation Detection",
    author = "Haouari, Fatima  and
      Hasanain, Maram  and
      Suwaileh, Reem  and
      Elsayed, Tamer",
    booktitle = "Proceedings of the Sixth Arabic Natural Language Processing Workshop",
    month = apr,
    year = "2021",
    address = "Kyiv, Ukraine (Virtual)",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2021.wanlp-1.8",
    pages = "72--81",
}

<!-- </code> -->
</pre>
