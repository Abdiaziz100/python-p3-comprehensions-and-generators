def return_evens(num_list):
    # Return only numbers divisible by 2
    return [n for n in num_list if n % 2 == 0]


def make_exclamation(sentence_list):
    # Add "!" to the end of each sentence
    return [sentence + "!" for sentence in sentence_list]
