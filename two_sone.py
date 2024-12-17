def two_sum(liste_numb, target):
    cpt=0
    for index_number, number in enumerate(liste_numb):
        for index_other_numb, number_other in enumerate(liste_numb[index_number + 1 :], start = index_number+1):
            cpt = number + number_other
            if cpt == target:
                return [index_number, index_other_numb]
    
    return None

test = two_sum([5, 5], 10)
print(test)