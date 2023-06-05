from docSimilarity.docSimilarity import docSimilarity

if __name__ == '__main__':
    
    docSimilarity = docSimilarity()
    
    similar = docSimilarity.get_similarity("", "")

    if similar :
        print ("doc1 & doc2 similar")
    else :
        print("not similar")