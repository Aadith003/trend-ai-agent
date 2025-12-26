
import re
def clean(text):
    text=text.lower()
    text=re.sub(r"[^a-z ]","",text)
    return text.strip()
