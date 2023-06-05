from docSimilarity import docSimilarity
import argparse
import sys


def main():
        
        parser = argparse.ArgumentParser(
                        prog='Document Similarity Checker',
                        description='This program checks for similarity on two documents takes documents as input and returns similarity results',
                        epilog='Similarity Checker')
        # document file
        parser.add_argument('-d', '--document', help='source document for similarity checking', type=str)

        # source file
        parser.add_argument('-t', '--target', help='target document file')
        
        args = parser.parse_args()
        
        if args.document and args.target:
            dc = docSimilarity()
            
            doc1 = open(args.document, 'r')
            doc1_text= doc1.read()
            
            doc1.close()
            
            doc2 = open(args.target, 'r')
            doc2_text= doc2.read()
            doc2.close()
                        
            similar = dc.get_similarity(doc1_text, doc2_text)

            if similar :
                print ("similar documents")
                sys.exit(1)
            else :
                print("dissimilar documents")
                sys.exit(1)
        
        elif not args.document:
            parser.error("Document is Missing") 
            

         
        elif not args.target: 
            parser.error("Target Document is Missing") and sys.exit(1)


        else:
            parser.print_help()


if __name__ == '__main__':
    
    main()