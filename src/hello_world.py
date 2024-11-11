class Greeting:
    """
    Created with a greeting text.
    Writes the text to stdout.

    """
    
    def __init__(self, greeting):
        self.greeting: str = greeting

    def greet(self, name: str ="") -> None:
        if name != "":
            utterance = self.greeting + ", " + name + "!" 
        else:
            utterance = self.greeting + "!"
        print(utterance)

