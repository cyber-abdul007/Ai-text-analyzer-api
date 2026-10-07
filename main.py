from fastapi import FastAPI
from pydantic import BaseModel
from http.client import HTTPException

app=FastAPI()
{
    "text": "Artificial intelligence is changing the world"

}
class TextReq(BaseModel):
    text: str
def text_action(text: str):
    words=text.split()
    word_count=len(words)
    char_count=len(text)
    unique_words=len(set(words))
    sentence_count=text.count('.')+text.count('!')+text.count('?')
    avg_word_length=round(sum(len(word) for word in words)/word_count,2) 
    Cap_let=text.upper()
    Small_let=text.lower()

    return{
        "word_count": word_count,
        "char_count": char_count,
        "unique_words": unique_words,
        "sentence_count": sentence_count,
        "avg_word_length": avg_word_length,
        "Capital_letters": Cap_let,
        "Small_letterss": Small_let
    }
@app.post("/analyze")
def analyze_text(req: TextReq):
    return text_action(req.text)

@app.post("/analyze")
def analyze_text(req: TextReq):
    if not req.text.strip():
        raise HTTPException(status_code=400, detail="The textt field cannot be empty.")
    return text_action(req.text)