# stock-sentiment-prediction

## Background
In the rapidly evolving landscape of machine learning, we're now capable of performing analyses and making predictions that were previously beyond human capabilities. Machine learning offers us the power to identify relationships between dependent variables, forecast time-series data, and much more.

For this particular project, we're venturing into the realm of unstructured data interpretation. Our focus is on various sources of such data, including news articles and social media commentary. We aim to harness this unstructured data and apply it in the context of stock market predictions. 

## Details of our project

We aim to use unstructured data such as social media and news and turn it into a feature in stock opening price change forecasting. We used NLTK's VADER Sentiment Model fine-tuned with finance phrase bank to perform sentiment analysis. We built a web scraper that scrapes out the news of a particular time frame and take random sample according to Central Limit Theorem to represent the data. This returned a compound sentiment score in the range of \[-1, 1\] inclusive. We tested two types of model, including Random Forest Regressor and XGBoost Linear Regressor, and we will be focusing on the results of Random Forest.

### Findings 

We have three types of model, including only opening price change data, sentiment included and  sentiment + sentiment volatility included.
| Pure Data | Sentiment Included | Sentiment and Volatility |
|---------|-----|-----------|
| 0.350 | 0.382 | 0.409 |

Prediction Graphs as below:

#### Pure Data
![output1](https://github.com/pvpswaghd/stock-sentiment-prediction/assets/44018990/b93d562e-95bc-40e0-bd33-46d16c90f8f4)


#### Sentiment Included
![output](https://github.com/pvpswaghd/stock-sentiment-prediction/assets/44018990/131dd048-b270-4376-9fd9-23f1e630fe59)


#### Sentiment and Volatility
![output2](https://github.com/pvpswaghd/stock-sentiment-prediction/assets/44018990/ee9b5107-c229-4263-9f3c-7ad7f8331a10)




