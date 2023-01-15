#levenshtein 
def levenshtein_distance(s1, s2):
    # base cases
    if s1 == s2:
        return 0
    if len(s1) == 0:
        return len(s2)
    if len(s2) == 0:
        return len(s1)
    
    # recursive case
    cost = 0 if s1[-1] == s2[-1] else 1
    return min(levenshtein_distance(s1[:-1], s2) + 1,
               levenshtein_distance(s1, s2[:-1]) + 1,
               levenshtein_distance(s1[:-1], s2[:-1]) + cost)
