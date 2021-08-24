# About

This repository is inspired by James Tauber's [vocabulary-tools](https://github.com/jtauber/vocabulary-tools) but is for the Hebrew Bible. The API is virutally identical to vocabulary-tools with a few exceptions. The data is taken with thanks from the Open Scriptures Hebrew Bible Project (See "Sources" below).

Available chunk types are:

* book
* chapter
* verse
* paragraph
* pericope

The verses are based on the placement of the _sof pasuq_. Paragraphs are based on the _samekh_ and _pe_ markers in the MT text. Books and Chapters are based on the references from the WLC xml files.

Available token types are:

* form
* lemma
* parse
* morph_lemma (a tuple of `(parse, lemma)`)
* all (a tuple of `(form, lemma, parse)`)

## Pretty printing text

Because the _sof pasuq_, and _maqqef_ are treated as individual tokens, the `pprint_text` function takes a list tokens and returns a string with appropriate spacing for the _maqqef_ and _sof pasuq_. 

## Using the lexical data

Finally, `load_lex` returns a tuple of dictionaries `(glosses, strongs, lemmas)`, where `glosses` is a dictionary of Hebrew lemmas -> glosses, `strongs` is a dictionary of Strong's numbers -> glosses, and `lemmas` is a dictionary of Strong's numbers -> Hebrew text of the lemma.

Thus all of the following statements would be true.

```
glosses, strongs, lemmas = load_lex()

assert glosses['אָב'] == 'father'

assert strongs['1'] == 'father'

assert lemmas['1'] == 'אָב'

assert glosses[lemmas['1']] == 'אָב'
```



# Sources

## WLC Source

The source xml files are taken from the Open Scriptures Hebrew Bible Project's [Open Scriptures Hebrew Bible (OSHB)](https://github.com/openscriptures/morphhb) and the WLC text that it is based upon is in the Public Domain per the OSHB repository.



## Lexical data

The Lexical data is taken from the Open Scriptures Hebrew Bible Project's [The OSHB Hebrew Lexicon](https://github.com/openscriptures/HebrewLexicon) which is released under a [Creative Commons Attribution 4.0 International](http://creativecommons.org/licenses/by/4.0/). The text of Brown Driver, Briggs Hebrew Lexicon and Strong's Hebrew Dictionary are in the Public Domain per the OSHB Hebrew Lexicon repository. 

# License

This work is released unthe the same [Creative Commons Attribution 4.0 International](http://creativecommons.org/licenses/by/4.0/) license as its Open Scriptures Hebrew Bible sources. 


