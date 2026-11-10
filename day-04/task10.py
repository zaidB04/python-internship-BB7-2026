def make_greeting(language):

    def greet(name):

        if language == "english":
            print("Good morning,", name)

        elif language == "hindi":
            print("subprabhat,", name)

        else:
            print("Language not supported")

    return greet


english_greeting = make_greeting("english")
hindi_greeting = make_greeting("hindi")

english_greeting("zaid")
hindi_greeting("Zaid")