import speech_recognition as sr 
import os 
from pydub import AudioSegment
from pydub.silence import split_on_silence

# create a speech recognition object
r = sr.Recognizer()

def generateTranscript(path, folderPath):
    """
    Splitting the large audio file into chunks
    and apply speech recognition on each of these chunks
    """
    sound = AudioSegment.from_wav(path)  

    chunks = split_on_silence(sound,
        min_silence_len=500,
        silence_thresh=sound.dBFS-14,
        keep_silence=500,
    )

    if not os.path.isdir(folderPath):
        os.makedirs(folderPath)

    textMap = {}
    for i, audio_chunk in enumerate(chunks, start=1):
        chunk_filename = os.path.join(folderPath, "speech_chunk{}.wav".format(i))
        audio_chunk.export(chunk_filename, format="wav")
        
        with sr.AudioFile(chunk_filename) as source:
            audio_listened = r.record(source)
            try:
                text = r.recognize_google(audio_listened)
                text = "{}. ".format(text.capitalize())
                textMap[chunk_filename] = text
            except sr.UnknownValueError as e:
                print("Error in chunk {}: {}".format(i, str(e)))
                
    return textMap