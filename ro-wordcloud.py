rom wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd


#Citim fișierul csv, ce conține o coloană denumită CONTINUT, cu diverse întrebări
df = pd.read_csv(r"Intrebari_diverse.csv", encoding="latin-1")

comment_words = ''
#lista de cuvinte ce nu vor fi luate in calcul la crearea wordcloud-ului
STOPWORDS = {'si', 'pentru', 'in', 'ff', 'fif', 'cont', 'cu', 'catev', 'catr', 'ave', 'alt', 'spune', 'ce',
                    'ace', 'acel', 'aceleas', 'acest', 'al', 'ale', 'ai', 'aib', 'aic', '?', '!', '\'\'', ',', '.',
                    '[', ']', '3', '4', '7', '``', 'a-mi', ' a ', 'acel', 'acei', 'eu', 'acum', 'ai', 'ca', 'cand', 'care', 'ce', 'cel',
                    'chiar', 'cu', 'cum', 'din', 'dintr', 'dintr-un', 'este', 'eu', 'fi', 'fiecare', 'fiu', 'frumos',
                    'il', 'imi', 'inainte', 'la', 'le', 'ma', 'mai', 'mea', 'meu', 'mi', 'mie', 'mult', 'ne', 'nimic',
                    'nu', 'ori', 'patra', 'patru', 'pe', 'pentru', 'peste', 'pana', 'poate', 'prin', 'sa', 'se',
                    'sunt', 'suntem', 'sunteti', 'suta', 'ta', 'te-a', 'tau', 'tai', 'tale', 'te', 'timp', 'toata',
                    'toate', 'tu', 'un', 'una', 'unde', 'unei', 'uneia', 'unele', 'uneori', 'unul', 'unu', 'unui',
                    'unuia', 'voi', 'zi-mi', 'te', 'rog', 'o', 'de'}
stopwords = set(STOPWORDS)
#print(STOPWORDS)

# iteram coloana CONTINUT a csv-ului
for val in df.CONTINUT: 
    #fiecare rand devine string si este tokenizat
    val = str(val)
    tokens = val.split()
    # toate cuvintele devin cu litera mica
    for i in range(len(tokens)):
        tokens[i] = tokens[i].lower()
    comment_words += " ".join(tokens) + " "

wordcloud = WordCloud(width=1980, height=1080,
                      background_color='white',
                      stopwords=stopwords,
                      min_font_size=10).generate(comment_words)

plt.figure(figsize=(8, 8), facecolor=None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad=0)

plt.show()
