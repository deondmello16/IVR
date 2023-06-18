#pyttsx3 module to work on speech drivers
import pyttsx3

#This class contains all the functions to run the TTS
class TextToSpeech:


    #This is a constructor that is used to initialize all the required vairables and objects for TTS
    def __init__(self):
        #callback topics for engine
        self.start_topic="started-utterance"
        self.word_topic="started-word"
        self.finish_topic="finished-utterance"
        self.error="error"
        #speech driver on the OS
        self.speech_driver="sapi5"
        #speech driver engine object
        self.engine=pyttsx3.init(driverName=self.speech_driver,debug=True)

    """
    This is a function that is used to take a complete string and convert it into
    pieces of words and append it on a list
    """
    def create_list(self,sentence):
        word_list=[]
        #converting a string into a list of words
        for word in sentence.split(' '):
            word_list.append(word)
        return word_list

    """
    This is a function is used to take a list of words and concat them with spaces
    to create a sentence
    """
    def frame_word(self,word_list):
        text=None
        #combining all words into sentence
        for word in word_list:
            if text!=None:
                text=text+word+' '
            else:
                text=word+' '
        return text

    """
    This is a callback function that is called during a
    start of a utterance or speech
    """
    def on_start(self,name):
        print('Starting: '+name)

    """
    This is a callback function that is called during a
    error occured during the utterance or speech
    """
    def on_error(self,name,exception):
        print(name+' Failed with Exception: '+exception)
        self.engine.endLoop()

    """
    This is a function that is used to print all the list
    of voices in the speech driver
    """
    def list_of_voices(self):
        engine=pyttsx3.init(driverName=self.speech_driver,debug=True)
        #listing all voices
        for voice in engine.getProperty('voices'):
            print(voice.id)

    def intro(self):
        engine=self.engine
        engine.say('Hi I a Mercury, welcome to reva university how can i help you')
        engine.runAndWait()

    """
    This is a function that is used to the text pass it to the engine
    and all callback functions are called and a queue command is started
    for speech
    """
    def to_speech(self,text):
        engine=self.engine
        engine.setProperty('rate',200-40)
        engine.setProperty('volume',1.0)
        #engine.connect(self.start_topic,self.on_start)
        #engine.connect(self.error,self.on_error)
        engine.say(text,text)
        engine.runAndWait()
