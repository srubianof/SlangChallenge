
def calculateNGrams(text, n):
    """Obtain the n-grams given a string TEXT and a number N to subdivide it
    
    Keyword arguments:
    text -- the word where the n-gram operation would be applied
    n    -- number of characters per n-gram

    As the complexity of the python operation for slicing is
    O(K) being K number of characters per n-gram and its within a loop we can conclude that the resulting
    complexity would be O(K*n) being n the size of the given string
    """

    return ([text[i:i+n] for i in range(len(text)-n+1)])

def mostFrequentNGram(text,n):
    """Obtain the most frequent n-gram from an n-gram list where given a string TEXT and a number N
    the operation will be executed
    
    Keyword arguments:
    text -- the word where the n-gram operation would be applied
    n    -- number of characters per n-gram

    As the complexity of the function calculateNGrams(text,n) is O(K*n) and counterFrequency(ngram) is linear,
    the resulting complexity of the entire function will be O(n^2) in the worst case scenario
    """

    ngram = calculateNGrams(text,n)
    return counterFrequency(ngram)
     
  
def counterFrequency(text):
    """Obtain the most frequent item from a given string TEXT
    
    Keyword arguments:
    text -- the word

    As the fuction contains a loop where it iterates within a text on n lenght the resulting complexity would be
    O(n) or linear as the operations performed with the dictionary are O(1) or constant 
    """
    dictText = {}
    maxN = 0
    mostFrequent = ""
    for item in text:
        if (item not in dictText):
            dictText[item] = 1
        else: 
            dictText[item] +=1
        
        if (dictText[item] > maxN):
            mostFrequent = item
            maxN = dictText[item]
    return mostFrequent

