model = Prophet(
    changepoint_prior_scale=CURRENT_SCALE,
    yearly_seasonality=True,
    weekly_seasonality=True,
    daily_seasonality=False
)