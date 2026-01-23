import json
import pandas as pd
import numpy as np
from catboost import CatBoostRegressor, Pool

# ---------------- LOAD MODEL ----------------
model = CatBoostRegressor()
model.load_model("catboost_model.cbm")

# ---------------- LOAD FEATURE SCHEMA ----------------
with open("feature_schema.json", "r") as f:
    FEATURE_COLUMNS = list(json.load(f).keys())

# 🔥 GET CATEGORICAL FEATURES FROM MODEL ITSELF
CAT_FEATURE_INDICES = model.get_cat_feature_indices()
CAT_COLS = [FEATURE_COLUMNS[i] for i in CAT_FEATURE_INDICES]

# ---------------- PREPROCESS ----------------
def preprocess_input(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    # datetime parsing
    df["trip_creation_time"] = pd.to_datetime(df["trip_creation_time"])
    df["od_start_time"] = pd.to_datetime(df["od_start_time"])
    df["od_end_time"] = pd.to_datetime(df["od_end_time"])

    # derived time features
    df["trip_hour"] = df["trip_creation_time"].dt.hour
    df["trip_weekday"] = df["trip_creation_time"].dt.weekday
    df["is_weekend"] = (df["trip_weekday"] >= 5).astype(int)

    df["od_time_diff_hour"] = (
        (df["od_end_time"] - df["od_start_time"])
        .dt.total_seconds() / 60
    )

    df["hour_x_distance"] = df["trip_hour"] * df.get("osrm_distance", 0)
    df["hour_x_osrm"] = df["trip_hour"] * df.get("osrm_time", 0)

    return df


# ---------------- PREDICTION ----------------
def predict_delivery_time(input_df: pd.DataFrame) -> float:
    df = preprocess_input(input_df)

    # create full feature vector (exact schema)
    full_df = pd.DataFrame(
        np.zeros((1, len(FEATURE_COLUMNS))),
        columns=FEATURE_COLUMNS
    )

    # ✅ FIX: cast categorical columns before assignment
    for col in CAT_COLS:
        full_df[col] = full_df[col].astype(str)

    

    # fill known values
    for col in df.columns:
        if col in full_df.columns:
            full_df.at[0, col] = df[col].values[0]

    # 🔥 categorical columns MUST be string
    for col in CAT_COLS:
        if col in full_df.columns:
            full_df[col] = full_df[col].astype(str).fillna("missing")

    # numeric safety
    for col in full_df.columns:
        if col not in CAT_COLS:
            full_df[col] = pd.to_numeric(full_df[col], errors="coerce").fillna(0)

    pool = Pool(
        data=full_df,
        cat_features=CAT_FEATURE_INDICES
    )

    log_pred = model.predict(pool)
    pred = np.expm1(log_pred)

    return float(pred[0])
