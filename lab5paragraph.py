text = input("Enter a Paragraph:")

characters = len(text)

spaces = text.count(" ")

words = len(text.split())

vowels ="aeiouAEIOU"
vowel_count = 0

for i in text:
    if i in vowels:
        vowel_count += 1

        print("\n___Total Analysis___")
        print("Total characters:",characters)
        print("Total words:",words)
        print("Total spaces:",spaces)
        print("Total vowels:",vowels)

        if len(text) >0:
            print("\n First character(Indexing):",text[0])
            print("\n Last character(Indexing):",text[-1])

            print("\nFirst 10 characters(slicing):",text[+10])
            print("\nLast 10 characters(slicing):",text[-10])


