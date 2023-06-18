from os import path
from pydub import AudioSegment
import audioop
import os
import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv
from vosk import Model, KaldiRecognizer
import wave
import json
import soundfile as sf
import os

global model
model = Model(r"vosk-model-en-us-librispeech-0.2")
def Voice_rec():

    fs = 96000

    # seconds
    duration = 6
    myrecording = sd.rec(int(duration * fs),
                         samplerate=fs, channels=2);print('start now ')
    sd.wait()

    # Save as FLAC file at correct sampling rate
    sf.write('my_Audio_file.wav', myrecording, fs)

def to_mono_audio():
    Voice_rec()


    inFileName='my_Audio_file.wav'
    outFileName='file_for_convertion.wav'

    inFile = wave.open(inFileName,'rb')
    outFile = wave.open(outFileName,'wb')

    try:

        outFile.setnchannels(1)

        outFile.setsampwidth(inFile.getsampwidth())
        outFile.setframerate(inFile.getframerate())

        soundBytes = inFile.readframes(inFile.getnframes())
        print("frames read: {} length: {}".format(inFile.getnframes(),len(soundBytes)))

        monoSoundBytes = audioop.tomono(soundBytes, inFile.getsampwidth(), 1, 1)
        outFile.writeframes(monoSoundBytes)

    except Exception as e:
        print(e)

    finally:
        inFile.close()
        outFile.close()
        ##########################


def converting_to_text():

    inFileName = 'file_for_convertion.wav'
    outfileText = 'M1S3-Text.json'

    wf = wave.open(inFileName, "rb")

    # initialize a str to hold results
    results = ""
    textResults = []

    # build the model and recognizer objects.

    recognizer = KaldiRecognizer(model, wf.getframerate())
    recognizer.SetWords(True)

    while True:
        data = wf.readframes(4000)
        if len(data) == 0:
            break
        if recognizer.AcceptWaveform(data):
            recognizerResult = recognizer.Result()
            results = results + recognizerResult
            # convert the recognizerResult string into a dictionary
            resultDict = json.loads(recognizerResult)
            # save the 'text' value from the dictionary into a list
            textResults.append(resultDict.get("text", ""))

    # process "final" result
    results = results + recognizer.FinalResult()
    resultDict = json.loads(recognizer.FinalResult())
    textResults.append(resultDict.get("text", ""))


    # write text portion of results to a file
    with open(outfileText, 'w') as output:
        print(json.dumps(textResults, indent=4), file=output)

    #to_mono_audio()
    #converting_to_text()
