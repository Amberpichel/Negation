{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "'geen' occurred 2992 times\n",
      "'niet' occurred 1243 times\n",
      "'niets' occurred 17 times\n",
      "'nooit' occurred 35 times\n",
      "'niks' occurred 3 times\n",
      "'zonder' occurred 286 times\n",
      "'niemand' occurred 1 times\n",
      "'weigeren' occurred 1 times\n",
      "'prevent' occurred 0 times\n",
      "'noch' occurred 25 times\n",
      "'afzien' occurred 0 times\n",
      "'zag af' occurred 0 times\n",
      "'af te zien' occurred 0 times\n",
      "'ziet af' occurred 0 times\n",
      "'zie af' occurred 0 times\n",
      "'zien af' occurred 0 times\n",
      "'zagen af' occurred 0 times\n",
      "'afgezien' occurred 4 times\n",
      "'blanco' occurred 15 times\n",
      "'nee' occurred 28 times\n",
      "'negatief' occurred 152 times\n",
      "'niet aanwezig' occurred 0 times\n",
      "'niet meer' occurred 0 times\n",
      "'noch, noch' occurred 0 times\n",
      "'ontbreken' occurred 9 times\n",
      "'ontbreek' occurred 0 times\n",
      "'ontbreekt' occurred 1 times\n",
      "'ontbrak' occurred 0 times\n",
      "'opheffen' occurred 4 times\n",
      "'hef op' occurred 0 times\n",
      "'heft op' occurred 0 times\n",
      "'opgeheven' occurred 9 times\n",
      "'staken' occurred 9 times\n",
      "'staak' occurred 0 times\n",
      "'staakt' occurred 0 times\n",
      "'gestaakt' occurred 13 times\n",
      "'staakte' occurred 0 times\n",
      "'staakten' occurred 0 times\n",
      "'stop' occurred 15 times\n",
      "'stoppen' occurred 29 times\n",
      "'stopt' occurred 3 times\n",
      "'gestopt' occurred 33 times\n",
      "'stopte' occurred 0 times\n",
      "'stopten' occurred 0 times\n",
      "'sluit uit' occurred 0 times\n",
      "'sluiten uit' occurred 33 times\n",
      "'uitgesloten' occurred 19 times\n",
      "'sloot uit' occurred 0 times\n",
      "'sloten uit' occurred 0 times\n",
      "'uitsluiten' occurred 8 times\n",
      "'verdwijn' occurred 0 times\n",
      "'verdwijnt' occurred 3 times\n",
      "'verdwijnen' occurred 2 times\n",
      "'verdween' occurred 2 times\n",
      "'verdwenen' occurred 42 times\n",
      "'verdwijnen' occurred 2 times\n",
      "'vervangen' occurred 6 times\n",
      "'vervang' occurred 0 times\n",
      "'vervangt' occurred 0 times\n",
      "'verving' occurred 0 times\n",
      "'vervingen' occurred 0 times\n",
      "'verwijderen' occurred 48 times\n",
      "'verwijder' occurred 0 times\n",
      "'verwijdert' occurred 0 times\n",
      "'verdwijderden' occurred 0 times\n",
      "'verwijderde' occurred 3 times\n",
      "'weigeren' occurred 1 times\n",
      "'weiger' occurred 0 times\n",
      "'weigert' occurred 0 times\n",
      "'weigerde' occurred 0 times\n",
      "'weigerden' occurred 0 times\n",
      "'geweigerd' occurred 3 times\n",
      "'zonder' occurred 286 times\n",
      "'ontbraken' occurred 0 times\n",
      "'hefte op' occurred 0 times\n",
      "'hefde op' occurred 0 times\n",
      "'hefden op' occurred 0 times\n",
      "'nog niet' occurred 0 times\n",
      "'nog geen' occurred 0 times\n",
      "'negatief' occurred 152 times\n"
     ]
    }
   ],
   "source": [
    "import nltk\n",
    "from collections import Counter\n",
    "import sys\n",
    "import glob\n",
    "import os\n",
    "import spacy\n",
    "import csv\n",
    "import sys\n",
    "\n",
    "def count_negcues():\n",
    "    \"\"\"count negation cues from VUmc corpus from given corpus\"\"\"\n",
    "\n",
    "    corpus = sys.argv[1]\n",
    "    txt = glob.glob(os.path.join(corpus + sys.argv[2]))\n",
    "    count = Counter()\n",
    "    \n",
    "    for infile in txt:\n",
    "        with open(infile, errors='ignore') as doc:\n",
    "            counts = nltk.word_tokenize(doc.read().lower())\n",
    "            count.update(counts)\n",
    "\n",
    "    print (\"'geen' occurred\", count['geen'], \"times\")\n",
    "    print (\"'niet' occurred\", count['niet'], \"times\")\n",
    "    print (\"'niets' occurred\", count['niets'], \"times\")\n",
    "    print (\"'nooit' occurred\", count['nooit'], \"times\")\n",
    "    print (\"'niks' occurred\", count['niks'], \"times\")\n",
    "    print (\"'zonder' occurred\", count['zonder'], \"times\")\n",
    "    print (\"'niemand' occurred\", count['niemand'], \"times\")\n",
    "    print (\"'weigeren' occurred\", count['weigeren'], \"times\")\n",
    "    print (\"'prevent' occurred\", count['prevent'], \"times\")\n",
    "    print (\"'noch' occurred\", count['noch'], \"times\")\n",
    "    print (\"'afzien' occurred\", count['afzien'], \"times\")\n",
    "    print (\"'zag af' occurred\", count['zag af'], \"times\")\n",
    "    print (\"'af te zien' occurred\", count['af te zien'], \"times\")\n",
    "    print (\"'ziet af' occurred\", count['ziet af'], \"times\")\n",
    "    print (\"'zie af' occurred\", count['zie af'], \"times\")\n",
    "    print (\"'zien af' occurred\", count['zien af'], \"times\")\n",
    "    print (\"'zagen af' occurred\", count['zagen af'], \"times\")\n",
    "    print (\"'afgezien' occurred\", count['afgezien'], \"times\")\n",
    "    print (\"'blanco' occurred\", count['blanco'], \"times\")\n",
    "    print (\"'nee' occurred\", count['nee'], \"times\")\n",
    "    print (\"'negatief' occurred\", count['negatief'], \"times\")\n",
    "    print (\"'niet aanwezig' occurred\", count['niet aanwezig'], \"times\")\n",
    "    print (\"'niet meer' occurred\", count['niet meer'], \"times\")\n",
    "    print (\"'noch, noch' occurred\", count['noch, noch'], \"times\")\n",
    "    print (\"'ontbreken' occurred\", count['ontbreken'], \"times\")\n",
    "    print (\"'ontbreek' occurred\", count['ontbreek'], \"times\")\n",
    "    print (\"'ontbreekt' occurred\", count['ontbreekt'], \"times\")\n",
    "    print (\"'ontbrak' occurred\", count['ontbrak'], \"times\")\n",
    "    print (\"'opheffen' occurred\", count['opheffen'], \"times\")\n",
    "    print (\"'hef op' occurred\", count['hef op'], \"times\")\n",
    "    print (\"'heft op' occurred\", count['heft op'], \"times\")\n",
    "    print (\"'opgeheven' occurred\", count['opgeheven'], \"times\")\n",
    "    print (\"'staken' occurred\", count['staken'], \"times\")\n",
    "    print (\"'staak' occurred\", count['staak'], \"times\")\n",
    "    print (\"'staakt' occurred\", count['staakt'], \"times\")\n",
    "    print (\"'gestaakt' occurred\", count['gestaakt'], \"times\")\n",
    "    print (\"'staakte' occurred\", count['staakte'], \"times\")\n",
    "    print (\"'staakten' occurred\", count['staakten'], \"times\")\n",
    "    print (\"'stop' occurred\", count['stop'], \"times\")\n",
    "    print (\"'stoppen' occurred\", count['stoppen'], \"times\")\n",
    "    print (\"'stopt' occurred\", count['stopt'], \"times\")\n",
    "    print (\"'gestopt' occurred\", count['gestopt'], \"times\")\n",
    "    print (\"'stopte' occurred\", count['stopte'], \"times\")\n",
    "    print (\"'stopten' occurred\", count['stopten'], \"times\")\n",
    "    print (\"'sluit uit' occurred\", count['sluit uit'], \"times\")\n",
    "    print (\"'sluiten uit' occurred\", count['sluiten'], \"times\")\n",
    "    print (\"'uitgesloten' occurred\", count['uitgesloten'], \"times\")\n",
    "    print (\"'sloot uit' occurred\", count['sloot uit'], \"times\")\n",
    "    print (\"'sloten uit' occurred\", count['sloten uit'], \"times\")\n",
    "    print (\"'uitsluiten' occurred\", count['uitsluiten'], \"times\")\n",
    "    print (\"'verdwijn' occurred\", count['verdwijn'], \"times\")\n",
    "    print (\"'verdwijnt' occurred\", count['verdwijnt'], \"times\")\n",
    "    print (\"'verdwijnen' occurred\", count['verdwijnen'], \"times\")\n",
    "    print (\"'verdween' occurred\", count['verdween'], \"times\")\n",
    "    print (\"'verdwenen' occurred\", count['verdwenen'], \"times\")\n",
    "    print (\"'verdwijnen' occurred\", count['verdwijnen'], \"times\")\n",
    "    print (\"'vervangen' occurred\", count['vervangen'], \"times\")\n",
    "    print (\"'vervang' occurred\", count['vervang'], \"times\")\n",
    "    print (\"'vervangt' occurred\", count['vervangt'], \"times\")\n",
    "    print (\"'verving' occurred\", count['verving'], \"times\")\n",
    "    print (\"'vervingen' occurred\", count['vervingen'], \"times\")\n",
    "    print (\"'verwijderen' occurred\", count['verwijderen'], \"times\")\n",
    "    print (\"'verwijder' occurred\", count['verwijder'], \"times\")\n",
    "    print (\"'verwijdert' occurred\", count['verwijdert'], \"times\")\n",
    "    print (\"'verdwijderden' occurred\", count['verwijderden'], \"times\")\n",
    "    print (\"'verwijderde' occurred\", count['verwijderde'], \"times\")\n",
    "    print (\"'weigeren' occurred\", count['weigeren'], \"times\")\n",
    "    print (\"'weiger' occurred\", count['weiger'], \"times\")\n",
    "    print (\"'weigert' occurred\", count['weigert'], \"times\")\n",
    "    print (\"'weigerde' occurred\", count['weigerde'], \"times\")\n",
    "    print (\"'weigerden' occurred\", count['weigerden'], \"times\")\n",
    "    print (\"'geweigerd' occurred\", count['geweigerd'], \"times\")\n",
    "    print (\"'zonder' occurred\", count['zonder'], \"times\")\n",
    "    print (\"'ontbraken' occurred\", count['ontbraken'], \"times\")\n",
    "    print (\"'hefte op' occurred\", count['hefte op'], \"times\")\n",
    "    print (\"'hefde op' occurred\", count['hefde op'], \"times\")\n",
    "    print (\"'hefden op' occurred\", count['hefden op'], \"times\")\n",
    "    print (\"'nog niet' occurred\", count['nog niet'], \"times\")\n",
    "    print (\"'nog geen' occurred\", count['nog geen'], \"times\")\n",
    "    print (\"'negatief' occurred\", count['negatief'], \"times\")\n",
    "    \n",
    "count_negcues()\n",
    "\n",
    "def count_tokens_sentences():\n",
    "\"\"\"count the number of tokens and sentences in a given corpus\"\"\"\n",
    "\n",
    "    corpus = sys.argv[1]\n",
    "\n",
    "    with open(corpus) as f:\n",
    "        content = f.read()\n",
    "        tokenized = nltk.word_tokenize(content)\n",
    "        sents = nltk.sent_tokenize(tokenized)\n",
    "        print(len(tokenized))\n",
    "        print(len(sents))\n",
    "\n",
    "count_tokens_sentences()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "LaDKernel",
   "language": "python",
   "name": "ladkernel"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
