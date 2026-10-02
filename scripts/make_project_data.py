import numpy as np, pandas as pd
out = "/home/claude/openfraudlab-tiktok/data/projects/"
sig = lambda z: 1 / (1 + np.exp(-z))

# ---------- Project 1: credit applications (finance) ----------
rng = np.random.default_rng(31)
n = 3000
region = rng.choice(["Capital", "North", "South", "East", "West", "Central", "Coastal", "Highlands"], n, p=[.30, .15, .12, .10, .09, .08, .08, .08])
employment = rng.choice(["Salaried", "Self-employed", "Business owner", "Contract"], n, p=[.42, .28, .18, .12])
age = rng.integers(21, 64, n)
income = np.round(np.exp(rng.normal(8.15, .45, n)) / 10) * 10
income = np.clip(income, 900, 40_000)
months_emp = np.clip(rng.gamma(2.2, 18, n).astype(int), 0, 360)
existing_debt = np.where(rng.random(n) < .45, 0, np.round(rng.gamma(1.6, income * .6) / 10) * 10)
purpose = rng.choice(["Business", "Education", "Home improvement", "Medical", "Car", "Personal"], n, p=[.30, .18, .16, .08, .14, .14])
tenure = rng.choice([3, 6, 9, 12, 18, 24], n, p=[.08, .25, .12, .30, .15, .10])
amount = np.round(income * rng.uniform(.4, 4.0, n) / 50) * 50
amount = np.clip(amount, 500, 100_000)
monthly_payment = np.round(amount * (1 + 0.012 * tenure) / tenure, 2)
dti = (monthly_payment + existing_debt / 12) / income
prev_loans = rng.poisson(1.4, n)
prev_late = np.array([rng.binomial(k, .18) for k in prev_loans])
salary_acct = (rng.random(n) < np.where(employment == "Salaried", .8, .35)).astype(int)
mm_txn = np.clip(rng.poisson(np.where(employment == "Salaried", 18, 30)), 0, None)
guarantor = (rng.random(n) < .4).astype(int)
z = (-2.45 + 3.0 * (dti - .35) + 0.8 * prev_late - 0.35 * salary_acct - 0.006 * (months_emp - 30)
     - 0.25 * guarantor + 0.35 * (employment == "Contract") + 0.18 * (purpose == "Personal")
     - 0.008 * (age - 38) + 0.12 * (tenure >= 18) - 0.004 * (mm_txn - 22) + rng.normal(0, .3, n))
default = (rng.random(n) < sig(z)).astype(int)
dates = pd.Timestamp("2024-01-01") + pd.to_timedelta(rng.integers(0, 731, n), unit="D")
df = pd.DataFrame({"application_id": [f"A{i:05d}" for i in range(1, n + 1)], "application_date": dates.strftime("%Y-%m-%d"),
    "region": region, "age": age, "employment_type": employment, "months_at_employer": months_emp,
    "monthly_income_usd": income.astype(int), "existing_debt_usd": existing_debt.astype(int), "loan_purpose": purpose,
    "loan_amount_usd": amount.astype(int), "tenure_months": tenure, "monthly_repayment_usd": monthly_payment,
    "previous_loans": prev_loans, "previous_late_payments": prev_late, "has_salary_account": salary_acct,
    "digital_payments_per_month": mm_txn, "has_guarantor": guarantor, "defaulted": default})
df = df.sort_values("application_date").reset_index(drop=True)
m = rng.random(n); df.loc[m < .04, "months_at_employer"] = np.nan
df.loc[rng.random(n) < .03, "digital_payments_per_month"] = np.nan
df.loc[rng.random(n) < .02, "employment_type"] = np.nan
df.to_csv(out + "credit_applications.csv", index=False)
print("credit", df.shape, df.defaulted.mean().round(3))

# ---------- Project 2: clinic appointments (health) ----------
rng = np.random.default_rng(32)
n = 5000
age = np.clip(rng.gamma(2.6, 14, n).astype(int), 0, 92)
sex = rng.choice(["F", "M"], n, p=[.58, .42])
dept = rng.choice(["General practice", "Antenatal", "Paediatrics", "Diabetes clinic", "Dental", "Eye clinic", "Physiotherapy"], n, p=[.32, .14, .14, .12, .10, .10, .08])
book = pd.Timestamp("2025-01-06") + pd.to_timedelta(rng.integers(0, 330, n), unit="D")
lead = np.clip(rng.gamma(1.4, 9, n).astype(int), 0, 120)
appt = book + pd.to_timedelta(lead, unit="D")
appt = appt + pd.to_timedelta(np.where(appt.weekday == 6, 1, np.where(appt.weekday == 5, 2, 0)), unit="D")
lead = (appt - book).days
sms = (rng.random(n) < .62).astype(int)
prev_appts = rng.poisson(3, n)
prev_ns = np.array([rng.binomial(k, .2) for k in prev_appts])
dist = np.round(np.clip(rng.gamma(2, 4.5, n), .3, 60), 1)
insurance = rng.choice(["Public", "Private", "None"], n, p=[.38, .22, .40])
chronic = (rng.random(n) < np.where(age > 45, .45, .12)).astype(int)
rain = rng.choice([0, 1], n, p=[.7, .3])
z = (-1.9 + 0.045 * lead - 0.9 * sms + 0.9 * np.where(prev_appts > 0, prev_ns / np.maximum(prev_appts, 1) * 3, 0)
     + 0.035 * dist - 0.35 * (insurance == "Private") + 0.2 * (insurance == "None") - 0.3 * chronic
     + 0.25 * rain + 0.35 * ((age >= 18) & (age <= 30)) - 0.3 * (dept == "Antenatal") + 0.25 * (dept == "Dental")
     + 0.15 * (appt.weekday == 0) + rng.normal(0, .3, n))
no_show = (rng.random(n) < sig(z)).astype(int)
df = pd.DataFrame({"appointment_id": [f"P{i:05d}" for i in range(1, n + 1)], "patient_age": age, "patient_sex": sex,
    "department": dept, "booking_date": book.strftime("%Y-%m-%d"), "appointment_date": appt.strftime("%Y-%m-%d"),
    "sms_reminder_sent": sms, "previous_appointments": prev_appts, "previous_no_shows": prev_ns, "distance_km": dist,
    "insurance": insurance, "chronic_condition": chronic, "rain_forecast": rain, "no_show": no_show})
df = df.sort_values("appointment_date").reset_index(drop=True)
df.loc[rng.random(n) < .025, "distance_km"] = np.nan
df.loc[rng.random(n) < .015, "insurance"] = np.nan
df.to_csv(out + "clinic_appointments.csv", index=False)
print("clinic", df.shape, df.no_show.mean().round(3))

# ---------- Project 3: city rental listings (real estate) ----------
rng = np.random.default_rng(33)
n = 2500
areas = {"Old Town": 1.55, "Harbourfront": 1.8, "Midtown": 1.45, "University District": 1.1, "Riverside": 1.25, "Northgate": 0.95,
         "Westfield": 0.9, "Eastside": 0.8, "Lakeview": 1.3, "Southpark": 0.75, "Hillcrest": 1.15, "Airport Fringe": 0.65}
area = rng.choice(list(areas), n, p=[.07, .06, .1, .1, .09, .1, .1, .1, .07, .08, .07, .06])
ptype = rng.choice(["Studio", "1-bed apartment", "Apartment", "Townhouse", "Detached house"], n, p=[.16, .2, .38, .14, .12])
beds = np.select([ptype == "Studio", ptype == "1-bed apartment", ptype == "Apartment", ptype == "Townhouse"],
                 [np.zeros(n), np.ones(n), rng.choice([2, 3], n, p=[.6, .4]), rng.choice([2, 3, 4], n, p=[.3, .5, .2])], rng.choice([3, 4, 5], n, p=[.45, .4, .15])).astype(int)
baths = np.clip(np.maximum(beds, 1) + rng.choice([-1, 0, 0, 1], n), 1, None)
size = np.round(np.where(ptype == "Studio", rng.normal(32, 5, n), np.where(ptype == "1-bed apartment", rng.normal(50, 7, n), 30 * np.maximum(beds, 1) + rng.normal(25, 15, n) + np.where(ptype == "Detached house", 55, 0))))
size = np.clip(size, 18, None)
furnished = (rng.random(n) < .25).astype(int)
balcony = (rng.random(n) < np.where(ptype == "Detached house", .1, .45)).astype(int)
parking = np.where(np.isin(ptype, ["Studio", "1-bed apartment"]), rng.choice([0, 1], n, p=[.6, .4]), rng.choice([0, 1, 2], n, p=[.2, .5, .3]))
year = rng.integers(1950, 2025, n)
transit = np.round(np.clip(rng.gamma(1.6, .45, n), .05, 5), 2)
pets = (rng.random(n) < .4).astype(int)
mult = np.array([areas[a] for a in area])
rent = 24 * size ** .97 * mult * (1 + .12 * furnished) * (1 + .04 * balcony) * (1 + .03 * parking) * (1 - .002 * (2024 - year)) * (1 - .06 * transit) * np.exp(rng.normal(0, .14, n))
rent = np.round(rent / 10) * 10
listed = pd.Timestamp("2025-01-01") + pd.to_timedelta(rng.integers(0, 270, n), unit="D")
df = pd.DataFrame({"listing_id": [f"R{i:05d}" for i in range(1, n + 1)], "listed_date": listed.strftime("%Y-%m-%d"), "neighbourhood": area,
    "property_type": ptype, "bedrooms": beds, "bathrooms": baths, "size_sqm": size, "furnished": furnished, "balcony": balcony,
    "parking_spaces": parking, "year_built": year, "distance_to_transit_km": transit, "pets_allowed": pets, "monthly_rent_usd": rent.astype(int)})
df = df.sort_values("listed_date").reset_index(drop=True)
df.loc[rng.random(n) < .05, "size_sqm"] = np.nan
df.loc[rng.random(n) < .03, "year_built"] = np.nan
dup = df.sample(12, random_state=33); df = pd.concat([df, dup]).sort_values("listed_date").reset_index(drop=True)
df.to_csv(out + "city_rentals.csv", index=False)
print("rentals", df.shape, df.monthly_rent_usd.median(), df.groupby("neighbourhood").monthly_rent_usd.median().sort_values().to_dict())
