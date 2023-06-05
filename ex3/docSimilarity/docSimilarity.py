#! /usr/bin/env python

"""
    - Created At 2023-23-05

    - Description:
        this class compare the  similarity of two documents 

"""

import nltk

from nltk.corpus import wordnet as wn
from nltk import word_tokenize, pos_tag


class docSimilarity(object):
    
    def __init__(self):
        pass

    def __nl_pos_to_wn_pos(self, tag):
        tags = {"N": "n", "J": "a", "R": "r", "V": "v"}

        if tag[0] in tags.keys():
            return tags[tag[0]]

        return None

    def __to_synsets(self, w, tag):
        """
        Get the synsets of wordnet from the word and giving tag
        - word : document string format
        - tag : nltk pros tag format
        """
        wn_tag = self.__nl_pos_to_wn_pos(tag)

        if wn_tag is None:
            return None

        try:
            return wn.synsets(w, wn_tag)[0]

        except:
            None

    def get_similarity(self, doc1, doc2, threshold=0.6):
        d1 = pos_tag(word_tokenize(doc1))
        d2 = pos_tag(word_tokenize(doc2))

        synsets1 = [self.__to_synsets(*p) for p in d1 if self.__to_synsets(*p)]
        synsets2 = [self.__to_synsets(*p) for p in d2 if self.__to_synsets(*p)]

        score, count = 0.0, 0

        for synset in synsets1:
            best_score = max([synset.path_similarity(ss) for ss in synsets2])

            if best_score is not None:
                score += best_score
                count += 1

        score /= count

        similar_score = threshold

        if score > similar_score:
            return 1

        return 0

