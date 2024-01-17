"""
4. Write a Python script to accept string/sentences from the user till the user enters “END”.
Save the data in a text file and then display only those sentences which begin with ‘T’.
"""

def save_and_filter_sentences():
    # Initialize an empty list to store sentences
    sentences = []

    # Prompt the user to enter sentences
    while True:
        sentence = input("Enter a sentence or END to stop: ")

        # Check if the user entered "END"
        if sentence == "END":
            break

        # Add the sentence to the list
        sentences.append(sentence)

    # Write the sentences to a text fileS
    with open("sentences.txt", "w") as w_file:
        for sentence in sentences:
            w_file.write(sentence + "\n")    #"\n" adds a new line character at the end of every sentence

    # Filter and display sentences starting with 'T'
    filtered_sentences = [sentence for sentence in sentences if sentence.startswith("T")]
    print("\nSentences starting with 'T':")
    for sentence in filtered_sentences:
        print(sentence)

# Call the function to save and filter sentences
save_and_filter_sentences()
