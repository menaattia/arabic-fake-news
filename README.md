# Arabic Fake News Detection

This is the repository of our NLP701 course project at MBZUAI.

This repository contains the implementation and experiments for detecting fake news in Arabic. The focus is on understanding the characteristics of fake news and developing models to effectively differentiate between fake and real news, leveraging diverse datasets such as satirical articles, BBC news, and COVID-19 tweets.


## Installation
Run the following to setup the conda environment and install the requirements:
<pre>
<code>
git clone https://github.com/your_username/arabic-fake-news.git
cd arabic-fake-news
</code>
<button onclick="copyToClipboard(this.previousElementSibling.innerText)"></button>
</pre>

## Usage 
To Run the experiments please run the following code, 
- 

<pre>
<code>

</code>
<button onclick="copyToClipboard(this.previousElementSibling.innerText)"></button>
</pre>




## Experiments
For our paper, we ran the following experiments with each model (SVM, XGBoost, LSTM, and CNN) to perform consistent comparisons

| Train | Test  | 
|-----------------|--------------------------|
| Articles   | Articles  | 
| Articles   | Tweets    | 
| Tweets     | Tweets    | 
| Tweets     | Articles  | 


## Acknowledgements
A large part of the idea was inspired by Saadany's [ _Fake or Real? A Study of Arabic Satirical Fake News_](https://aclanthology.org/2020.rdsm-1.7/). Many thanks for their wonderful work.
<pre>
<code>
@inproceedings{saadany-etal-2020-fake,
    title = "Fake or Real? A Study of {A}rabic Satirical Fake News",
    author = "Saadany, Hadeel  and
      Orasan, Constantin  and
      Mohamed, Emad",
    editor = "Aker, Ahmet  and
      Zubiaga, Arkaitz",
    booktitle = "Proceedings of the 3rd International Workshop on Rumours and Deception in Social Media (RDSM)",
    month = dec,
    year = "2020",
    address = "Barcelona, Spain (Online)",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2020.rdsm-1.7",
    pages = "70--80",
    abstract = "One very common type of fake news is satire which comes in a form of a news website or an online platform that parodies reputable real news agencies to create a sarcastic version of reality. This type of fake news is often disseminated by individuals on their online platforms as it has a much stronger effect in delivering criticism than through a straightforward message. However, when the satirical text is disseminated via social media without mention of its source, it can be mistaken for real news. This study conducts several exploratory analyses to identify the linguistic properties of Arabic fake news with satirical content. It shows that although it parodies real news, Arabic satirical news has distinguishing features on the lexico-grammatical level. We exploit these features to build a number of machine learning models capable of identifying satirical fake news with an accuracy of up to 98.6{\%}. The study introduces a new dataset (3185 articles) scraped from two Arabic satirical news websites ({`}Al-Hudood{'} and {`}Al-Ahram Al-Mexici{'}) which consists of fake news. The real news dataset consists of 3710 articles collected from three official news sites: the {`}BBC-Arabic{'}, the {`}CNN-Arabic{'} and {`}Al-Jazeera news{'}. Both datasets are concerned with political issues related to the Middle East.",
}
</code>
</pre>
