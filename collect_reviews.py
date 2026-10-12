
import pandas as pd
from google_play_scraper import reviews, Sort
import time

APP_ID = "com.moveinsync.ets"
all_reviews = []
token = None

print("Starting MoveInSync review collection...")

for page in range(5):
    try:
        batch, token = reviews(
            APP_ID,
            lang="en",
            country="in",
            sort=Sort.NEWEST,
            count=200,
            continuation_token=token
        )

        if not batch:
            break

        all_reviews.extend(batch)
        print(f"Collected {len(all_reviews)} reviews")

        if token is None:
            break

        time.sleep(1)

    except Exception as error:
        print("Collection error:", error)
        break

if all_reviews:
    df = pd.DataFrame(all_reviews)

    columns = [
        "reviewId",
        "score",
        "content",
        "at",
        "thumbsUpCount",
        "reviewCreatedVersion"
    ]

    df = df[[column for column in columns if column in df.columns]]
    df = df.drop_duplicates(subset="reviewId")
    df.to_csv("moveinsync_reviews.csv", index=False)

    print("\nCollection complete!")
    print("Total reviews saved:", len(df))
    print("File: moveinsync_reviews.csv")
    print("\nRating distribution:")
    print(df["score"].value_counts().sort_index())

else:
    print("No reviews collected. Check the app ID or connection.")
