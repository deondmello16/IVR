#Team Code to combine everything
import convert_to_text as deon
import match as harsh
import text_to_speech_win as enock
import question_set_db as jamin
import read_json as ej
import unanswered_question as anagha


#Main class that runs all the module files in one
class Main:

    #constructor of Main file with display texts
    def __init__(self):
        self.speak="Listening..."
        self.think="Thinking..."
        self.oops_error="Oops Something went wrong say it again..."
        self.oops_unavailable="Oops I can't figure it out..."


    """
    This function is used to take the audio convert it to
    text and match it with the database questions and run it back
    """
    def main(self):

        intro=enock.TextToSpeech()
        intro.intro()
        #to display speak text
        print(self.speak)
        #speech to text
        deon.to_mono_audio()
        #to display thinking
        print(self.think)
        deon.converting_to_text()

        #read json
        read_json=ej.ReadJson()
        text=read_json.read_json("M1S3-Text.json")
        #print(text)

        #check if string is empty or not
        if text[0] != " " or text[0] != "":

            #mongodb
            #get the question set from mongodb
            question_answer=jamin.QuestionSet()
            question_set=question_answer.get_question_set()

            #matching words with the input and database set
            match_tup=harsh.closests_match(question_set,text)

            #check if match was done or not
            if match_tup[0] == True:
                tts=enock.TextToSpeech()
                tts.to_speech(tts.frame_word(tts.create_list(match_tup[1])))
                #run the module back
                main=Main()
                main.main()
            else:
                #if question is not found upload it to database and run thr module back
                tts=enock.TextToSpeech()
                tts.to_speech(self.oops_unavailable)
                anagha.insert_question(match_tup[1])
                #run the module back
                main=Main()
                main.main()

        #if text is found empty
        else:
            #calling main
            tts=enock.TextToSpeech()
            tts.to_speech(self.oops_error)
            main=Main()
            main.main()
