
from google_play_scraper import reviews
import pandas as pd
def fetch_reviews(app_id, count=200):
    result,_=reviews(app_id, count=count)
    return pd.DataFrame(result)
