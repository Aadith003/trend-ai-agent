
from agents.crawler_agent import fetch_reviews
from agents.filter_agent import clean
from agents.reasoning_agent import infer_topic
from agents.ontology_agent import normalize
from agents.trend_agent import build
import json,datetime

df=fetch_reviews("in.swiggy.android")
ontology=json.load(open("vector_db/ontology.json"))
df['clean']=df['content'].apply(clean)
df['topic']=df['clean'].apply(infer_topic)
df['topic']=df['topic'].apply(lambda x: normalize(x,ontology))
json.dump(ontology, open("vector_db/ontology.json","w"), indent=2)
df['date']=df['at'].astype(str).str[:10]
report=build(df)
report.to_csv("output/trend_report.csv")
print(report)
