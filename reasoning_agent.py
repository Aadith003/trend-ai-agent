
from openai import OpenAI
client=OpenAI()
def infer_topic(text):
    r=client.chat.completions.create(model="gpt-4o-mini",
    messages=[{"role":"system","content":"Give 2-4 word issue/request topic"},
              {"role":"user","content":text}])
    return r.choices[0].message.content.strip()
