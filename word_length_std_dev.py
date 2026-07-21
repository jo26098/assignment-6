def word_length_std_dev(words_str):
    """
    Determines the standard deviation of the lengths of all words contained in the argument.

    Arguments: 
        words_str (string): A string that can contain any words.

    Returns:
        std_dev (float): The standard deviation of the lengths of all words that were in the words_str argument.
    """
    word_list = []
    current_word = ""
    for i in words_str:
        a = i
        if a != " ":
            current_word += a
        elif current_word != "" and current_word != " ":
            word_list.append(current_word)
            current_word = ""
    if a != " ":
        word_list.append(current_word)
    
    lengths_list = []
    for i in word_list:
        lengths_list.append(len(i))
    
    mean = 0
    for i in lengths_list:
        mean += i
    mean /= len(lengths_list)
    
    sum = 0
    for i in lengths_list:
        sum += (i - mean)**2
    sum /= (len(lengths_list) - 1)

    std_dev = sum**0.5
    return std_dev



#print("The standard deviation of the lengths of all words given is", word_length_std_dev(str(input("Enter anything: "))) + ".")
usr_input = "Hello Worlds"
print("The standard deviation of the lengths of all words given is", str(word_length_std_dev(usr_input)) + ".")