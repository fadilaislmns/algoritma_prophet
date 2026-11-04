from flask import Flask, request, jsonify
import pandas as pd
from prophet import Prophet

app = Flask(__name__)

@app.route('/forecast', methods=['POST'])
def forecast():
    data = request.json

    df = pd.DataFrame(data)
    df['ds'] = pd.to_datetime(df['ds'])

    model = Prophet()
    model.fit(df)

    future = model.make_future_dataframe(periods=7)
    forecast = model.predict(future)

    result = forecast[['ds', 'yhat']].tail(7)

    return jsonify(result.to_dict(orient='records'))
    print(data)
if __name__ == '__main__':
    app.run(port=5000)