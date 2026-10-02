import numpy as np, pandas as pd
out = "/home/claude/openfraudlab-tiktok/data/projects/"
sig = lambda z: 1 / (1 + np.exp(-z))

# ---------- Project 1: credit applications (finance) ----------
rng = np.random.default_rng(31)
n = 3000
region = rng.choice(["Lagos", "Abuja", "Kano", "Rivers", "Oyo", "Enugu", "Kaduna", "Edo"], n, p=[.30, .15, .12, .10, .09, .08, .08, .08])
employment = rng.choice(["Salaried", "Self-employed", "Business owner", "Contract"], n, p=[.42, .28, .18, .12])
age = rng.integers(21, 64, n)
income = np.round(np.exp(rng.normal(12.35, .45, n)) / 1000) * 1000
income = np.clip(income, 45000, 2_500_000)
months_emp = np.clip(rng.gamma(2.2, 18, n).astype(int), 0, 360)
existing_debt = np.where(rng.random(n) < .45, 0, np.round(rng.gamma(1.6, income * .6) / 1000) * 1000)
purpose = rng.choice(["Business", "School fees", "Rent", "Medical", "Asset purchase", "Personal"], n, p=[.30, .18, .16, .08, .14, .14])
tenure = rng.choice([3, 6, 9, 12, 18, 24], n, p=[.08, .25, .12, .30, .15, .10])
amount = np.round(income * rng.uniform(.4, 4.0, n) / 5000) * 5000
amount = np.clip(amount, 30000, 6_000_000)
monthly_payment = np.round(amount * (1 + 0.045 * tenure) / tenure / 100) * 100
dti = (monthly_payment + existing_debt / 12) / income
prev_loans = rng.poisson(1.4, n)
prev_late = np.array([rng.binomial(k, .18) for k in prev_loans])
salary_acct = (rng.random(n) < np.where(employment == "Salaried", .8, .35)).astype(int)
mm_txn = np.clip(rng.poisson(np.where(employment == "Salaried", 18, 30)), 0, None)
guarantor = (rng.random(n) < .4).astype(int)
z = (-2.75 + 3.0 * (dti - .35) + 0.8 * prev_late - 0.35 * salary_acct - 0.006 * (months_emp - 30)
     - 0.25 * guarantor + 0.35 * (employment == "Contract") + 0.18 * (purpose == "Personal")
     - 0.008 * (age - 38) + 0.12 * (tenure >= 18) - 0.004 * (mm_txn - 22) + rng.normal(0, .3, n))
default = (rng.random(n) < sig(z)).astype(int)
dates = pd.Timestamp("2024-01-01") + pd.to_timedelta(rng.integers(0, 731, n), unit="D")
df = pd.DataFrame({"application_id": [f"A{i:05d}" for i in range(1, n + 1)], "application_date": dates.strftime("%Y-%m-%d"),
    "region": region, "age": age, "employment_type": employment, "months_at_employer": months_emp,
    "monthly_income_ngn": income.astype(int), "existing_debt_ngn": existing_debt.astype(int), "loan_purpose": purpose,
    "loan_amount_ngn": amount.astype(int), "tenure_months": tenure, "monthly_repayment_ngn": monthly_payment.astype(int),
    "previous_loans": prev_loans, "previous_late_payments": prev_late, "has_salary_account": salary_acct,
    "mobile_money_txn_per_month": mm_txn, "has_guarantor": guarantor, "defaulted": default})
df = df.sort_values("application_date").reset_index(drop=True)
m = rng.random(n); df.loc[m < .04, "months_at_employer"] = np.nan
df.loc[rng.random(n) < .03, "mobile_money_txn_per_month"] = np.nan
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
insurance = rng.choice(["NHIA", "Private HMO", "None"], n, p=[.38, .22, .40])
chronic = (rng.random(n) < np.where(age > 45, .45, .12)).astype(int)
rain = rng.choice([0, 1], n, p=[.7, .3])
z = (-1.9 + 0.045 * lead - 0.9 * sms + 0.9 * np.where(prev_appts > 0, prev_ns / np.maximum(prev_appts, 1) * 3, 0)
     + 0.035 * dist - 0.35 * (insurance == "Private HMO") + 0.2 * (insurance == "None") - 0.3 * chronic
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

# ---------- Project 3: Lagos rental listings (real estate) ----------
rng = np.random.default_rng(33)
n = 2500
areas = {"Ikoyi": 3.4, "Victoria Island": 3.0, "Lekki Phase 1": 2.3, "Ikeja GRA": 1.9, "Lekki (Chevron-Ajah)": 1.35, "Gbagada": 1.15,
         "Yaba": 1.1, "Surulere": 1.0, "Ikeja": 1.05, "Ajah": 0.75, "Ikorodu": 0.5, "Egbeda": 0.55}
area = rng.choice(list(areas), n, p=[.05, .06, .12, .06, .12, .08, .09, .1, .1, .1, .06, .06])
ptype = rng.choice(["Self-contain", "Mini flat", "Flat", "Terrace duplex", "Detached duplex"], n, p=[.16, .2, .38, .14, .12])
beds = np.select([ptype == "Self-contain", ptype == "Mini flat", ptype == "Flat", ptype == "Terrace duplex"],
                 [np.ones(n), np.ones(n), rng.choice([2, 3], n, p=[.5, .5]), rng.choice([3, 4], n, p=[.6, .4])], rng.choice([4, 5, 6], n, p=[.55, .35, .1])).astype(int)
baths = np.clip(beds + rng.choice([-1, 0, 0, 1], n), 1, None)
size = np.round(np.where(ptype == "Self-contain", rng.normal(28, 5, n), np.where(ptype == "Mini flat", rng.normal(45, 7, n), 38 * beds + rng.normal(15, 18, n) + np.where(ptype == "Detached duplex", 60, 0))))
size = np.clip(size, 15, None)
serviced = (rng.random(n) < np.where(np.isin(area, ["Ikoyi", "Victoria Island", "Lekki Phase 1"]), .55, .15)).astype(int)
furnished = (rng.random(n) < .12).astype(int)
parking = np.where(ptype == "Self-contain", rng.choice([0, 1], n, p=[.7, .3]), rng.choice([0, 1, 2, 3], n, p=[.15, .4, .3, .15]))
year = rng.integers(1985, 2025, n)
road = np.round(np.clip(rng.gamma(1.5, .6, n), .05, 6), 2)
mult = np.array([areas[a] for a in area])
base = 9_000 * size ** 1.02
rent = base * mult * (1 + .25 * serviced) * (1 + .18 * furnished) * (1 + .03 * parking) * (1 - .004 * (2024 - year)) * (1 - .04 * road) * np.exp(rng.normal(0, .18, n))
rent = np.round(rent / 50_000) * 50_000
listed = pd.Timestamp("2025-01-01") + pd.to_timedelta(rng.integers(0, 270, n), unit="D")
df = pd.DataFrame({"listing_id": [f"R{i:05d}" for i in range(1, n + 1)], "listed_date": listed.strftime("%Y-%m-%d"), "area": area,
    "property_type": ptype, "bedrooms": beds, "bathrooms": baths, "size_sqm": size, "serviced": serviced, "furnished": furnished,
    "parking_spaces": parking, "year_built": year, "distance_to_main_road_km": road, "annual_rent_ngn": rent.astype(int)})
df = df.sort_values("listed_date").reset_index(drop=True)
df.loc[rng.random(n) < .05, "size_sqm"] = np.nan
df.loc[rng.random(n) < .03, "year_built"] = np.nan
dup = df.sample(12, random_state=33); df = pd.concat([df, dup]).sort_values("listed_date").reset_index(drop=True)
df.to_csv(out + "lagos_rentals.csv", index=False)
print("rentals", df.shape, df.annual_rent_ngn.median(), df.groupby("area").annual_rent_ngn.median().sort_values().to_dict())
