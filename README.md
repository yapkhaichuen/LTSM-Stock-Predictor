# **LTSM Stock Predictor**
[![Model Training](https://github.com/yapkhaichuen/LTSM-Stock-Predictor/actions/workflows/model-training.yml/badge.svg)](https://github.com/yapkhaichuen/LTSM-Stock-Predictor/actions/workflows/model-training.yml) [![Generate Report](https://github.com/yapkhaichuen/LTSM-Stock-Predictor/actions/workflows/generate-report.yml/badge.svg?event=workflow_dispatch)](https://github.com/yapkhaichuen/LTSM-Stock-Predictor/actions/workflows/generate-report.yml)

Predicting different stock prices using Long Short-Term Memory Recurrent Neural Network in Python using TensorFlow 2 and Keras. Highly customizable for different stock tickers. Current ticker: AMZN (Amazon).

View deployment here: <br>
[GitHub Pages](https://yapkhaichuen.github.io/LTSM-Stock-Predictor)

## **Basic Usage**
1. Install the required libraries by running ***pip install -r requirements.txt***.
1. Run ***train.py*** to train our model. (This will take some time approx. 4 hours)
2. After training ends, run ***tensorboard --logdir="logs"*** to view the Huber loss as specified in the LOSS parameter, the curve is the validation loss. You can also increase the number of epochs to get much better results.
3. Run ***test.py*** to test the model and to output the result

Note: the project is currently running on GitHub Actions, you can take a look at the example output down below. GitHub Actions allows the code to be ran offsite hence freeing up your development computer.

## **Raw data**
<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=https://raw.githubusercontent.com/yapkhaichuen/LTSM-Stock-Predictor/main/data.json) -->
<!-- The below code snippet is automatically added from https://raw.githubusercontent.com/yapkhaichuen/LTSM-Stock-Predictor/main/data.json -->
```json
[
    {
        "Ticker": "AMZN",
        "Future price after": "1 day",
        "Predicted price for 2022-06-04": "2504.44$",
        "Mean absolute error": 10.630584475929423,
        "Accuracy score": 0.5091926458832934,
        "Total buy profit": 831.4678506851188,
        "Total sell profit": -383.82859086990385,
        "Total profit": 447.639259815215,
        "Profit per trade": 0.3578251477339848,
        "Generated": "2022-06-03 20:11:34.615186+08:00"
    }
]
```
<!-- The below code snippet is automatically added from https://raw.githubusercontent.com/yapkhaichuen/LTSM-Stock-Predictor/main/data.json -->
<!-- MARKDOWN-AUTO-DOCS:END -->

## **Generated report**
<!-- MARKDOWN-AUTO-DOCS:START (JSON_TO_HTML_TABLE:src=./data.json) -->
<table class="JSON-TO-HTML-TABLE"><thead><tr><th class="ticker-th">Ticker</th><th class="future-price-after-th">Future price after</th><th class="predicted-price-for-2022-06-04-th">Predicted price for 2022-06-04</th><th class="mean-absolute-error-th">Mean absolute error</th><th class="accuracy-score-th">Accuracy score</th><th class="total-buy-profit-th">Total buy profit</th><th class="total-sell-profit-th">Total sell profit</th><th class="total-profit-th">Total profit</th><th class="profit-per-trade-th">Profit per trade</th><th class="generated-th">Generated</th></tr></thead><tbody ><tr ><td class="ticker-td td_text">AMZN</td><td class="future-price-after-td td_text">1 day</td><td class="predicted-price-for-2022-06-04-td td_text">2504.44$</td><td class="mean-absolute-error-td td_num">10.630584475929423</td><td class="accuracy-score-td td_num">0.5091926458832934</td><td class="total-buy-profit-td td_num">831.4678506851188</td><td class="total-sell-profit-td td_num">-383.82859086990385</td><td class="total-profit-td td_num">447.639259815215</td><td class="profit-per-trade-td td_num">0.3578251477339848</td><td class="generated-td td_text">2022-06-03 20:11:34.615186+08:00</td></tr></tbody></table>
<!-- MARKDOWN-AUTO-DOCS:END -->

## **Graphs**
![graph](./graphs/prediction.png)


Disclaimer: This is **not** finanical advice. Please don't bet your life savings on this.
