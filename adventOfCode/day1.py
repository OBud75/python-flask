def read_file(prompt):
    with open(prompt, 'r') as file :
        # On peut utiliser une comprehension de liste pour lire le fichier
        # return [list(map(int,line.split())) for line in file]
        # Aussi, regardez la fonction enumerate pour obtenir l'index de la ligne
        return [[int(num) for i, num in enumerate(line.split())] for line in file]

        arr = [] # Que signifie arr ?
        for line in file :
            line_numbers  = list(map(int,line.split()))
            arr.append(line_numbers)
    return arr

def get_prompt():
    return "adventOfCode/day1.txt"

def problem1() :
    prompt = '/Users/thoma/OneDrive/Documents/python-flask/adventOfCode/day1.txt'
    # Autant utiliser un chemin relatif
    prompt = get_prompt()
    file = read_file(prompt)
    unzipped_lists = list(zip(*file))

    sorted_lists = []
    for lst in unzipped_lists:
        sorted_lists.append(sorted(lst))

    rezipped_lists = zip(*sorted_lists)

    sorted_arr = [list(x) for x in rezipped_lists]

    ans = 0

    # Python a une fonction sum qui permet de sommer les éléments d'une liste
    # print(sum([abs(sorted_arr[i][0] - sorted_arr[i][j]) for i in range(len(sorted_arr)) for j in range(len(sorted_arr[i]))]))
    for i in range(len(sorted_arr)): 
        for j in range(len(sorted_arr[i])):
            ans += abs(sorted_arr[i][0] - sorted_arr[i][j])
    # Pas besoin de print à chaque fois ?
    print(ans)
    # Pas besoin de return 0 à la fin contrairement à d'autres langages
    return 0

def problem2():
    prompt = '/Users/thoma/OneDrive/Documents/python-flask/adventOfCode/day1.txt'
    prompt = get_prompt()
    file = read_file(prompt)

    # Pourquoi avoir utilisé 2 structures de données différentes pour les 2 colonnes ?
    left_column_set = set()
    right_column = []
    
    for row in file:
        left_column_set.add(row[0])  
        right_column.append(row[1])  

    sorted_left_column = sorted(left_column_set)  
    sorted_right_column = sorted(right_column)

    counter = 0
    ans = 0

    # Même remarques que pour le problème 1, prennez le temps de comprendre les
    # "list comprehension" qui permettent de pas mal simplifier et d'utiliser
    # quelque chose comme sum([f(x) for x in list if condition(x)])
    for i in range(len(sorted_left_column)):
        for j in range(len(sorted_right_column)):
            if sorted_left_column[i] == sorted_right_column[j]:
                counter += 1
            else:
                ans += sorted_left_column[i] * counter
                counter = 0

    print(ans)
    return 0




problem1()
problem2()