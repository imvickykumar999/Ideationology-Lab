
# Download Library...
# --------------------------------------

# pip install spacy
# python -m spacy download en_core_web_sm


import spacy
nlp = spacy.load('en_core_web_sm') 

file_name = '0001_arina.txt'
about_text = open(file_name).read()

a = about_text.split('U:')
d = {}

for i in range(1, len(a)):
    b = a[i].split('B:')
    d.update({b[0].strip() : b[1].strip()})
    
# query = 'What happens with turbine when wind exceeds 25 m/s?'
# query = 'VAWT, what does it mean?'
# query = 'I need to know how much does cost energy for Multi-MW wind plant'
query = input('Write your question : ')

try:
    ans = nlp(query).ents[0]
    s=[]

    for i in d:
        for j in nlp(i).ents:
            if (str(ans).strip() == str(j).strip()):       
                s.append(d[i])

    ans = list(set(s))[0]
    print(ans)
except:
    print('Sorry, Unable to answer this query...')