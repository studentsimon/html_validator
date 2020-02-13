#!/bin/python3


def validate_html(html):
    '''
    This function performs a limited version of html validation by checking whether every opening tag $
    >>> validate_html('<strong>example</strong>')
    True
    >>> validate_html('<strong>example')
    False
    '''
    list1 = _extract_tags(html);

    for i in list1:
        tag1 = "<" + "/" + i[1:]
        print(i + tag1)
        if tag1 in list1:
            
            list1.remove(tag1)
        else:
            return False
    return True
    

    # HINT:
    # use the _extract_tags function below to generate a list of html tags without any extra text;
    # then process these html tags using the balanced parentheses algorithm from the book
    # the main difference between your code and the book's code will be that you will have to keep tra$
    # but arbitrary text located between the html tags


def _extract_tags(html):
    '''
    This is a helper function for `validate_html`.
    By convention in Python, helper functions that are not meant to be used directly by the user are p$
    This function returns a list of all the html tags contained in the input string,
    stripping out all text not contained within angle brackets.
    >>> _extract_tags('Python <strong>rocks</strong>!')
    ['<strong>', '</strong>']
    '''

    list1 = list(html)
    list_out = []

    i = 0

    while i < len(list1):

        thing = list1[i]
        
        if thing == '<':
            
           
            
            word1 = ""
            
            while list1[i] != '>':
                word1 = word1 + list1[i]
                
                i = i+1
            word1 = word1 + list1[i]
            
            list_out.append(word1)
            
            
        i = i + 1

    return list_out

    

