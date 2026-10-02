"""Synthetic, global practice datasets for lessons 10-30 (fixed seeds). Not real people, companies or prices."""
import numpy as np, pandas as pd
OUT = "/home/claude/openfraudlab-tiktok/data/global/"
sig = lambda z: 1 / (1 + np.exp(-z))

# ---- Online store: customers + orders (retail / e-commerce) ----
rng = np.random.default_rng(101)
countries = ["United States", "United Kingdom", "Germany", "India", "Brazil", "Canada", "Australia", "France", "Japan", "Nigeria", "Mexico", "South Africa"]
cp = [.24, .11, .09, .12, .07, .06, .05, .06, .06, .05, .05, .04]
nc = 2000
cust = pd.DataFrame({"customer_id": [f"C{i:04d}" for i in range(1, nc + 1)],
    "signup_date": (pd.Timestamp("2023-01-01") + pd.to_timedelta(rng.integers(0, 730, nc), unit="D")).strftime("%Y-%m-%d"),
    "country": rng.choice(countries, nc, p=cp), "age": np.clip(rng.normal(36, 11, nc).round(), 18, 80).astype(int),
    "segment": rng.choice(["Consumer", "Small business", "Corporate"], nc, p=[.72, .2, .08]),
    "acquisition_channel": rng.choice(["Search", "Social media", "Referral", "Email", "Direct"], nc, p=[.3, .25, .15, .1, .2])})
cats = {"Electronics": (180, .8), "Home & kitchen": (45, .6), "Clothing": (35, .5), "Books": (14, .3), "Beauty": (22, .4), "Sports & outdoors": (55, .6), "Toys": (25, .5)}
no = 12000
cid = rng.choice(cust.customer_id, no, p=None)
cat = rng.choice(list(cats), no, p=[.16, .17, .2, .14, .12, .11, .1])
price = np.array([round(np.exp(np.log(cats[c][0]) + rng.normal(0, cats[c][1])), 2) for c in cat])
units = rng.choice([1, 1, 1, 2, 2, 3, 4], no)
disc = rng.choice([0, 0, 0, 0.05, 0.1, 0.15, 0.2, 0.3], no)
ship = np.clip(rng.gamma(2.2, 1.6, no).round(), 1, 21).astype(int)
odate = pd.Timestamp("2024-01-01") + pd.to_timedelta(rng.integers(0, 366, no), unit="D")
# seasonal bump in Nov-Dec
bump = rng.random(no) < .12
odate = odate.where(~bump, pd.Timestamp("2024-11-15") + pd.to_timedelta(rng.integers(0, 45, no), unit="D"))
ret_p = sig(-2.6 + .9 * (cat == "Clothing") + .4 * (cat == "Electronics") + .08 * (ship - 4) + 1.2 * (disc >= .3))
returned = (rng.random(no) < ret_p).astype(int)
rating = np.clip(np.round(4.4 - .12 * (ship - 4) - 1.4 * returned + rng.normal(0, .7, no)), 1, 5).astype(int)
orders = pd.DataFrame({"order_id": [f"O{i:05d}" for i in range(1, no + 1)], "order_date": odate.strftime("%Y-%m-%d"), "customer_id": cid,
    "category": cat, "units": units, "unit_price_usd": price, "discount": disc, "shipping_days": ship, "returned": returned, "rating": rating})
orders = orders.sort_values("order_date").reset_index(drop=True)
orders["order_id"] = [f"O{i:05d}" for i in range(1, no + 1)]
orders.loc[rng.random(no) < .03, "rating"] = np.nan
cust.to_csv(OUT + "customers.csv", index=False); orders.to_csv(OUT + "orders.csv", index=False)
print("orders", orders.shape, "returned", orders.returned.mean().round(3))

# ---- City bike rentals (transport / weather) ----
rng = np.random.default_rng(102)
days = pd.date_range("2023-01-01", "2024-12-31", freq="D"); nd = len(days)
doy = days.dayofyear.values
temp = np.round(12 + 10 * np.sin((doy - 105) / 365 * 2 * np.pi) + rng.normal(0, 3.5, nd), 1)
hum = np.clip(np.round(65 - .6 * (temp - 12) + rng.normal(0, 12, nd)), 20, 100).astype(int)
wind = np.round(np.clip(rng.gamma(3, 4, nd), 0, 60), 1)
rain = np.round(np.where(rng.random(nd) < .3, rng.gamma(1.5, 4, nd), 0), 1)
holiday = (rng.random(nd) < .03).astype(int)
weekend = (days.dayofweek >= 5).astype(int)
season = np.select([np.isin(days.month, [12, 1, 2]), np.isin(days.month, [3, 4, 5]), np.isin(days.month, [6, 7, 8])], ["Winter", "Spring", "Summer"], "Autumn")
growth = 1 + .18 * (days.year == 2024)
rent = (900 + 155 * temp - 4.2 * np.maximum(temp - 26, 0) ** 2 - 6 * (hum - 60) - 14 * wind - 70 * rain - 250 * holiday + 180 * weekend) * growth + rng.normal(0, 480, nd)
rent = np.clip(rent, 40, None).round().astype(int)
bikes = pd.DataFrame({"date": days.strftime("%Y-%m-%d"), "season": season, "temperature_c": temp, "humidity_pct": hum, "wind_kmh": wind,
    "rain_mm": rain, "is_holiday": holiday, "is_weekend": weekend, "rentals": rent})
# ice cream style confounder: daily ice-cream kiosk sales also follow temperature
bikes["kiosk_ice_cream_sales"] = np.clip((40 + 9 * temp + rng.normal(0, 25, nd)).round(), 0, None).astype(int)
bikes.to_csv(OUT + "bike_rentals.csv", index=False)
print("bikes", bikes.shape, bikes[["temperature_c", "rentals"]].corr().iloc[0, 1].round(3))

# ---- Subscription service customers (churn) ----
rng = np.random.default_rng(103)
n = 4000
regions = ["North America", "Europe", "Asia-Pacific", "Latin America", "Africa", "Middle East"]
region = rng.choice(regions, n, p=[.3, .27, .2, .1, .08, .05])
plan = rng.choice(["Basic", "Standard", "Premium"], n, p=[.42, .38, .2])
fee = np.select([plan == "Basic", plan == "Standard"], [8.99, 14.99], 22.99) * np.where(np.isin(region, ["Latin America", "Africa", "Asia-Pacific"]), .7, 1)
fee = np.round(fee, 2)
contract = rng.choice(["Monthly", "Annual"], n, p=[.64, .36])
tenure = np.clip(rng.gamma(1.6, 11, n).round(), 1, 72).astype(int)
usage = np.round(np.clip(rng.gamma(2.5, 2.4, n), 0, 40), 1)
tickets = rng.poisson(np.where(usage < 3, 1.4, .8))
pay = rng.choice(["Card", "Mobile wallet", "Bank transfer", "PayPal"], n, p=[.5, .18, .12, .2])
auto = (rng.random(n) < np.where(contract == "Annual", .85, .55)).astype(int)
age = np.clip(rng.normal(34, 12, n).round(), 16, 80).astype(int)
devices = rng.choice([1, 2, 3, 4], n, p=[.4, .3, .2, .1])
z = (-1.0 + 1.3 * (contract == "Monthly") - .035 * tenure - .16 * usage + .38 * tickets - .7 * auto + .25 * (plan == "Premium")
     + .3 * (pay == "Bank transfer") - .15 * (devices - 1) + .008 * (age - 34) + rng.normal(0, .4, n))
churn = (rng.random(n) < sig(z)).astype(int)
subs = pd.DataFrame({"customer_id": [f"S{i:05d}" for i in range(1, n + 1)], "region": region, "age": age, "plan": plan, "monthly_fee_usd": fee,
    "contract": contract, "tenure_months": tenure, "avg_weekly_hours": usage, "devices": devices, "support_tickets_90d": tickets,
    "payment_method": pay, "auto_renew": auto, "churned": churn})
subs.loc[rng.random(n) < .03, "avg_weekly_hours"] = np.nan
subs.to_csv(OUT + "subscribers.csv", index=False)
print("subs", subs.shape, "churn", subs.churned.mean().round(3))

# ---- Card transactions (fraud, highly imbalanced) ----
rng = np.random.default_rng(104)
n = 20000
amount = np.round(np.exp(rng.normal(3.6, 1.0, n)), 2)
hour = rng.integers(0, 24, n)
online = (rng.random(n) < .45).astype(int)
foreign = (rng.random(n) < .08).astype(int)
new_merchant = (rng.random(n) < .2).astype(int)
dist = np.round(np.clip(rng.gamma(1.2, 15, n), 0, 3000), 1)
prev_24h = rng.poisson(2.2, n)
z = (-8.7 + .55 * np.log1p(amount) + 1.1 * foreign + .8 * online + .9 * new_merchant + .012 * dist ** .8
     + 1.0 * ((hour <= 5)) + .18 * prev_24h + rng.normal(0, .5, n))
fraud = (rng.random(n) < sig(z)).astype(int)
tx = pd.DataFrame({"transaction_id": [f"T{i:06d}" for i in range(1, n + 1)], "amount_usd": amount, "hour": hour, "is_online": online,
    "is_foreign": foreign, "new_merchant": new_merchant, "distance_from_home_km": dist, "transactions_last_24h": prev_24h, "is_fraud": fraud})
tx.to_csv(OUT + "transactions.csv", index=False)
print("tx", tx.shape, "fraud", tx.is_fraud.mean().round(4), tx.is_fraud.sum())
