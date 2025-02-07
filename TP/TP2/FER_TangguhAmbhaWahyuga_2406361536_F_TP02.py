def main_menu():
    '''Display the main menu options to the user'''
    print('Choose an option:\n'
    '[1] Compute a reverse complement of a k-mer pattern\n'
    '[2] Count a k-mer pattern\n'
    '[3] Find most frequent k-mer patterns\n')

def reverse_complement(genome):
    '''Convert the characters in genome to their reverse complement'''
    reverse_genome = ""
    for char in genome:
        # Map each char to its complement
        if char == 'A':
            reverse_genome += 'T'
        elif char == 'T':
            reverse_genome += 'A'
        elif char == 'C':
            reverse_genome += 'G'
        else:
            reverse_genome += 'C'
    # Return the reverse of the complemented genome
    reversed_genome = ''
    for i in range(len(reverse_genome)):
        reversed_genome += reverse_genome[-i-1]
    return reversed_genome
    # return reverse_genome[::-1]

def count_k_mer(pattern):
    '''Count occurrences of a pattern and its reverse complement in the genome'''
    count = 0
    reverse_pattern = reverse_complement(pattern)
    for i in range(len(content)):
        # Melakukan slicing sepanjang panjang dari pattern
        sub_genome = content[i:len(pattern)+i]
        if sub_genome == pattern or sub_genome == reverse_pattern:
            count += 1
    return count
    
def modus_k_mer(k_mer):
    '''Find the most frequent k-mers in the genome'''
    list_genome = [] # List untuk keseluruhan
    list_pattern = [] # List untuk polanya
    for i in range(len(content)-k_mer):
        sub_genome = content[i:k_mer+i]
        if sub_genome not in list_genome:# Append Unique Words to list_pattern
            list_pattern.append(sub_genome)
            list_genome.append(sub_genome) 
        else:
            list_genome.append(sub_genome)

    # Count occurrences of each k-mer and its reverse complement
    list_frequent_pattern = []
    for j in range(len(list_pattern)):
        patterns = list_pattern[j]
        reverse_pattern = reverse_complement(patterns)
        frequent = list_genome.count(patterns)
        frequent += list_genome.count(reverse_pattern) # to add the frequency of its reverse
        list_frequent_pattern.append(frequent)
    
    # Find the k-mers with the highest frequency
    modus_pattern = [] # Yang nantinya akan menampung indeks dari pattern
    # modus = max(list_frequent_pattern)
    modus = list_frequent_pattern[0]
    for numb in list_frequent_pattern:
        if numb > modus:
            modus = numb
    for k in range(len(list_frequent_pattern)):
        value = list_frequent_pattern[k]
        if value == modus:
            # Menambahkan ke list, index dari frequency modus
            modus_pattern.append(k)
    
    for l in modus_pattern:
        # Looping print untuk pattern dalam index di dalam modus_pattern
        print(list_pattern[l])        

# Main Program
valid = True
while valid == True:
    try: # Memvalidasi Input File Name
        file_name = input('Genome file name: ')
        with open(file_name, 'r') as file:
            content = file.read()
        valid = False
    except FileNotFoundError:
        print(f'File name with name {file_name} not found\n')
    except:
        print('Error')

main_menu()
interaction = input('Selcet an option [1/2/3]: ')
if interaction == '1':
    pattern_of_genome = input('Input your pattern: ')
    reverse_genome = reverse_complement(pattern_of_genome)
    print(reverse_genome)

elif interaction == '2':
    pattern = input('Input your pattern: ')
    count = count_k_mer(pattern)
    print(count)

elif interaction == '3':
    while True: # Memvalidasi input integer
        try:
            k = int(input('Input value of k: '))
            modus_k_mer(k)
            break
        except ValueError:
            print('Input must be integer')
else:
    print('Option not Found')