import isapi.install
import spacy
nlp = spacy.load("en_core_web_sm")

doc = nlp("He is running and she ran yesterday.He ran better than her.")
for token in doc:
    print('hi')
    # print(f"{token.text:10} | POS: {token.pos_:6} | Lemma: {token.lemma_} | parsing: {token.dep_}")

# .dep_ => depency parsing


txt = "EURUSD rose today, ADDSUB is a function, and GBPUSD stayed flat."
info=nlp(txt)


for i in info.ents:
    print(i.text +" ->"+i.label_)
