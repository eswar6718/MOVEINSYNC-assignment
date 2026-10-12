
import pandas as pd

df = pd.read_csv("moveinsync_reviews.csv")

negative = df[df["score"].isin([1, 2])].copy()
negative["content"] = negative["content"].fillna("").str.lower()

categories = {
    "App Stability": [
        "crash", "crashing", "not opening", "reinstall",
        "update", "loading", "stuck"
    ],
    "Booking Problems": [
        "booking", "booked", "cancel", "failed"
    ],
    "ETA and Delays": [
        "eta", "delay", "late", "waiting", "arrival"
    ],
    "Routing and Pickup": [
        "route", "routing", "pickup", "drop", "detour"
    ],
    "OTP and Safety": [
        "otp", "seat belt", "safety", "driver"
    ],
    "Notifications": [
        "notification", "alert", "reminder"
    ],
    "Login Problems": [
        "login", "log in", "sign in", "password"
    ]
}

results = []

for category, keywords in categories.items():
    matches = negative["content"].apply(
        lambda text: any(word in text for word in keywords)
    )

    results.append({
        "Category": category,
        "Matching Reviews": int(matches.sum())
    })

results_df = pd.DataFrame(results)
results_df = results_df.sort_values(
    "Matching Reviews", ascending=False
)

print("\nNEGATIVE REVIEW ANALYSIS")
print("=" * 45)
print(results_df.to_string(index=False))
print("\nTotal negative reviews analyzed:", len(negative))

results_df.to_csv("complaint_category_counts.csv", index=False)
print("\nSaved results to complaint_category_counts.csv")
