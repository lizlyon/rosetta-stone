
def load_rosetta_stone_data():
    """
    This function loads the rosetta stone data
    """

    import pandas as pd
    rosetta_stone_data = pd.read_csv("https://github.com/connoralydon/rosetta_stone_final/raw/main/data/rosetta_stone_clean.csv")

    rosetta_stone_data["language"] = rosetta_stone_data["language"].astype("category")
    rosetta_stone_data["subscription_type"] = rosetta_stone_data["subscription_type"].astype("category")
    rosetta_stone_data["subscription_event_type"] = rosetta_stone_data["subscription_event_type"].astype("category")
    rosetta_stone_data["purchase_store"] = rosetta_stone_data["purchase_store"].astype("category")
    rosetta_stone_data["country"] = rosetta_stone_data["country"].astype("category")
    rosetta_stone_data["user_type"] = rosetta_stone_data["user_type"].astype("category")

    rosetta_stone_data["subscription_start_date"] = pd.to_datetime(rosetta_stone_data["subscription_start_date"])

    rosetta_stone_data["demo_user"] = rosetta_stone_data["demo_user"].astype("bool")
    rosetta_stone_data["free_trial_user"] = rosetta_stone_data["free_trial_user"].astype("bool")
    rosetta_stone_data["auto_renew"] = rosetta_stone_data["auto_renew"].astype("bool")
    rosetta_stone_data["email_subscriber"] = rosetta_stone_data["email_subscriber"].astype("bool")
    rosetta_stone_data["push_notifications"] = rosetta_stone_data["push_notifications"].astype("bool")

    rosetta_stone_data["send_count"] = rosetta_stone_data["send_count"].astype("int64")
    rosetta_stone_data["unique_open_count"] = rosetta_stone_data["unique_open_count"].astype("int64")
    rosetta_stone_data["unique_click_count"] = rosetta_stone_data["unique_click_count"].astype("int64")
    rosetta_stone_data["purchase_amount_usd"] = rosetta_stone_data["purchase_amount_usd"].astype("int64")
    rosetta_stone_data["subscription_length_days"] = rosetta_stone_data["subscription_length_days"].astype("int64")
    rosetta_stone_data["total_app_interactions"] = rosetta_stone_data["total_app_interactions"].astype("int64")
    rosetta_stone_data["launch_app_interactions"] = rosetta_stone_data["launch_app_interactions"].astype("int64")
    rosetta_stone_data["purchase_amount_usd_imputed"] = rosetta_stone_data["purchase_amount_usd_imputed"].astype("int64")
    return rosetta_stone_data

rosetta_stone_data = type_rosetta_data()