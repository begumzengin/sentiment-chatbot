import random
from textblob import TextBlob
from textblob.np_extractors import ConllExtractor
extractor = ConllExtractor()

def main():
    print("hello, i am begbot, the simple robot\n"
          "you can end this conversation any time by typing \"bye\"\n"
          "after typing each answer, press 'enter'\n"
          "how are you today?")

    while True:
        user_input = input("> ")
        if user_input.lower() == "bye":
            break
        else:
            user_input_blob = TextBlob(user_input, np_extractor=extractor)
            np = user_input_blob.noun_phrases
            response = ""
            if user_input_blob.polarity <= -0.5:
                response = "oh dear that sounds bad :("
            elif user_input_blob.polarity <= 0:
                response = "hmm that's not great :/"
            elif user_input_blob.polarity <= 0.5:
                response = "well that sounds positive :)"
            elif user_input_blob.polarity <= 1:
                response = "wow that sounds great :D"

            if len(np) != 0:
                #there was at least one noun phrase detected,
                #so ask about that and pluralise it
                response = response + "\ncan you tell more about " + np[0].pluralize() + "?"
            else:
                response = response + "\ncan you tell me more?"
            print(response)

    print("it was nice talking to you, goodbye")

def translator():
    bookBlob = TextBlob("It is a truth universally acknowledged, that a single man in "
                        "possession of a good fortune, "
                        "must be in want of a wife!")
    print(bookBlob.translate(from_lang="en", to="fr"))

def sentimentFinder():
    quote1 = """Two things are infinite: the universe and human stupidity; and I'm not sure about the universe."""

    sentiment1 = TextBlob(quote1).sentiment

    print(quote1 + "\nhas a sentiment of " + str(sentiment1))


sentimentFinder()

translator()

main()







