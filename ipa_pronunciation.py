import nltk
import re

arpabet = {
	'AA': {'ipa':'ɑ', 'type':'V', 'keyword':'balm, bot'},
	'AE': {'ipa':'æ', 'type':'V', 'keyword':'bat'},
	'AH': {'ipa':'ʌ', 'type':'V', 'keyword':'butt'},
	'AO': {'ipa':'ɔ', 'type':'V', 'keyword':'bought'},
	'AW': {'ipa':'aʊ', 'type':'V', 'keyword':'bout'},
	'AY': {'ipa':'aɪ', 'type':'V', 'keyword':'bite'},
	'B': {'ipa':'b', 'type':'C', 'keyword':'buy'},
	'CH': {'ipa':'tʃ', 'type':'C', 'keyword':'China'},
	'D': {'ipa':'d', 'type':'C', 'keyword':'die'},
	'DH': {'ipa':'ð', 'type':'C', 'keyword':'thy'},
	'EH': {'ipa':'ɛ', 'type':'V', 'keyword':'bet'},
	'ER': {'ipa':'ɝ', 'type':'V', 'keyword':'bird'},
	'EY': {'ipa':'eɪ', 'type':'V', 'keyword':'bait'},
	'F': {'ipa':'f', 'type':'C', 'keyword':'fight'},
	'G': {'ipa':'ɡ', 'type':'C', 'keyword':'guy'},
	'HH': {'ipa':'h', 'type':'C', 'keyword':'high'},
	'IH': {'ipa':'ɪ', 'type':'V', 'keyword':'bit'},
	'IY': {'ipa':'i', 'type':'V', 'keyword':'beat'},
	'JH': {'ipa':'dʒ', 'type':'C', 'keyword':'jive'},
	'K': {'ipa':'k', 'type':'C', 'keyword':'kite'},
	'L': {'ipa':'l', 'type':'C', 'keyword':'lie'},
	'M': {'ipa':'m', 'type':'C', 'keyword':'my'},
	'N': {'ipa':'n', 'type':'C', 'keyword':'nigh'},
	'NG': {'ipa':'ŋ', 'type':'C', 'keyword':'sing'},
	'OW': {'ipa':'oʊ', 'type':'V', 'keyword':'boat'},
	'OY': {'ipa':'ɔɪ', 'type':'V', 'keyword':'boy'},
	'P': {'ipa':'p', 'type':'C', 'keyword':'pie'},
	'R': {'ipa':'ɹ', 'type':'C', 'keyword':'rye'},
	'S': {'ipa':'s', 'type':'C', 'keyword':'sigh'},
	'SH': {'ipa':'ʃ', 'type':'C', 'keyword':'shy'},
	'T': {'ipa':'t', 'type':'C', 'keyword':'tie'},
	'TH': {'ipa':'θ', 'type':'C', 'keyword':'thigh'},
	'UH': {'ipa':'ʊ', 'type':'V', 'keyword':'book'},
	'UW': {'ipa':'u', 'type':'V', 'keyword':'boot'},
	'V': {'ipa':'v', 'type':'C', 'keyword':'vie'},
	'W': {'ipa':'w', 'type':'C', 'keyword':'wise'},
	'Y': {'ipa':'j', 'type':'C', 'keyword':'yacht'},
	'Z': {'ipa':'z', 'type':'C', 'keyword':'zoo'},
	'ZH': {'ipa':'ʒ', 'type':'C', 'keyword':'pleasure'},
    '0': {'ipa': '', 'type': 'C', 'keyword': 'no stress'},
    '1': {'ipa': 'ˈ', 'type': 'C', 'keyword': 'primary stress'},
    '2': {'ipa': 'ˌ', 'type': 'C', 'keyword': 'secondary stress'}
}


pronounceDict = {}

def encodeWord(p_word):
    head = p_word[0]
    value = ''
    for syllable in p_word[1]:
        parts = re.split('(\d+)',syllable) # split off stress
        for component in parts:
            if component in arpabet.keys():
                value = value + arpabet[component]['ipa']
    return (head,value)


print('loading words...')

extras = [('hypotenuse','HH AH0 P AA1 T AH N Y UW2 Z'.split(' ')),
          ('quadratical','K W AA2 D R AE1 T IH K AH L'.split(' '))]

for thisWord in list(nltk.corpus.cmudict.entries()) + extras:
    if thisWord[0] in pronounceDict.keys():
        continue # keep only the first instance
    thisWord = encodeWord(thisWord)
    pronounceDict[thisWord[0]]=thisWord[1]
print()


#print('finished loading...')

paragraph = '''I am the very model of a modern Major-General,
I've information vegetable, animal, and mineral,
I know the kings of England, and I quote the fights historical
From Marathon to Waterloo, in order categorical;
I'm very well acquainted, too, with matters mathematical,
I understand equations, both the simple and quadratical,
About binomial theorem I'm teeming with a lot o' news,
With many cheerful facts about the square of the hypotenuse.'''

print(paragraph)
print()

paragraph = paragraph.lower()

# ignore this punctuation
paragraph = paragraph.replace('-',' ')
paragraph = paragraph.replace(',',' ')
paragraph = paragraph.replace('  ',' ')
paragraph = re.sub('[ ]+',' ', paragraph) # compress spaces

# sentence ending punctuation
paragraph = paragraph.replace("\n",'.')
paragraph = paragraph.replace(';','.')
paragraph = paragraph.replace('?','.')
paragraph = paragraph.replace('!','.')
paragraph = re.sub('[.]+','.', paragraph) # compress sentence-enders


sentences = paragraph.split('.')

for sentence in sentences:
    if sentence == '':
        continue
    #print(sentence)
    sentence = sentence.lower().strip().split(' ')

    #print('/ ', end='')
    for w in sentence:
        if w in pronounceDict.keys():
            print(pronounceDict[w], end=' ')
        else:
            print(w.upper(), end= ' ')
    print()

#
#
#
# wordlist = set(w.lower() for w in nltk.corpus.words.words())
#
# puzzle_letters = nltk.FreqDist('egivrvonl')
# [w for w in wordlist if len(w) >= 6 and obligatory in w and nltk.FreqDist(w) >- puzzle_letters]
