# Stock Sentiment Prediction

## Background

In the constantly evolving field of machine learning, we now have the capability to carry out analyses and make predictions that were once thought impossible. Machine learning empowers us to identify relationships between dependent variables, forecast time-series data, and much more.

In this project, we delve into the domain of unstructured data interpretation, with a focus on data from various sources such as news articles and social media commentary. The objective is to leverage this unstructured data and apply it in the context of stock market predictions.

## Project Outline

Our goal is to convert unstructured data from sources like social media and news into a feature for forecasting changes in stock opening prices. We utilized the VADER Sentiment Model from NLTK, fine-tuned with a finance phrase bank, to perform sentiment analysis. We also developed a web scraper to extract news within a specified timeframe and utilized random samples according to the Central Limit Theorem to represent the data. The sentiment analysis returned a compound sentiment score in the range of [-1, 1] inclusive. We experimented with two types of models, the Random Forest Regressor and the XGBoost Linear Regressor, focusing primarily on the results from the Random Forest model.

## Findings

We tested three types of models: one using only opening price change data, one with sentiment included, and one with sentiment and sentiment volatility included. The results were as follows:

| Model Type | R-Squared Score |
|------------|----------------|
| Pure Data | 0.350 |
| Sentiment Included | 0.382 |
| Sentiment and Volatility | 0.409 |

Here are the prediction graphs for each model:

### Pure Data
![Pure Data](https://github.com/pvpswaghd/stock-sentiment-prediction/assets/44018990/b93d562e-95bc-40e0-bd33-46d16c90f8f4)

### Sentiment Included
![Sentiment Included](https://github.com/pvpswaghd/stock-sentiment-prediction/assets/44018990/131dd048-b270-4376-9fd9-23f1e630fe59)

### Sentiment and Volatility
![Sentiment and Volatility](https://github.com/pvpswaghd/stock-sentiment-prediction/assets/44018990/ee9b5107-c229-4263-9f3c-7ad7f8331a10)

As evident from the graphs, the model incorporating sentiment and sentiment volatility offers a better fit. This suggests that converting unstructured data, such as news, into structured data that humans and machines can interpret, could potentially enhance tasks like stock prediction.

## Potential Improvements

1. Testing more advanced models designed to handle time-series data, such as LSTM, could yield improved results.
2. The sentiment analysis could be enhanced by incorporating OpenAI's GPT-3.5 API, potentially providing a better-fitted sentiment score.
3. As the VADER model lacks subjective opinions and only offers an out-of-the-box compound score without human tagging, it may misinterpret some articles and is incapable of classification. These limitations could be addressed in future iterations of the project.
