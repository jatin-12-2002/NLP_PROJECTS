import os
from wsgiref import simple_server
from flask import Flask, request, render_template, jsonify
from flask_cors import CORS
import shutil

from com_in_ineuron_ai_speech_to_text.transcriptGenerator import generateTranscript
from com_in_ineuron_ai_spellingcorrector.spellcorrector import spell_corrector
from com_in_ineuron_ai_keywordspotter.keywordSpotter import AddMultiKeywords

app = Flask(__name__)
CORS(app)

app.config['DEBUG'] = True

class ClientService:
    def __init__(self):
        self.FolderPath = "InputFiles"
        self.fileList = os.listdir(self.FolderPath)
        self.separatedOutputFiles = "./SeparatedOutputFiles"
        self.outputText = {}

    def processAudioFile(self):
        outputResponseObj = {}
        for val in self.fileList:
            inputFileTranscriptedOp = generateTranscript(os.path.join(self.FolderPath, val), self.separatedOutputFiles)
        outputResponseObj["inputFileTranscriptedOp"] = inputFileTranscriptedOp

        spellCorrectedOpMap = {}
        for val in inputFileTranscriptedOp.keys():
            spellcorrectedOp = spell_corrector(inputFileTranscriptedOp[val])
            spellCorrectedOpMap[val] = spellcorrectedOp
        outputResponseObj["spellCorrectedOpMap"] = spellCorrectedOpMap

        extractedKeywordMap = {}
        for val in inputFileTranscriptedOp.keys():
            adding = AddMultiKeywords(inputFileTranscriptedOp[val], {"place": ["england"], "team": ["manchester united"], "game": ["football"]})
            result = adding.addkey()
            extractedKeywordMap[val] = result
        outputResponseObj["extractedKeywors"] = extractedKeywordMap

        return outputResponseObj


inputFileDir = "./InputFiles"
archiveDir = './ArchivedInputFiles'


def archiveOldInputFiles():
    files = os.listdir(inputFileDir)
    for f in files:
        if os.path.exists(os.path.join(archiveDir, f)):
            os.remove(os.path.join(archiveDir, f))
        shutil.move(os.path.join(inputFileDir, f), archiveDir)


@app.route("/", methods=["GET"])
def homePage():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def getInputFile():
    try:
        inputFile = request.files.get('file')
        archiveOldInputFiles()
        inputFile.save(os.path.join("InputFiles", inputFile.filename))
        return jsonify({"output": "Successfully uploaded the file"})
    except Exception as e:
        return jsonify({"outputError": str(e)})


@app.route("/startprocessing", methods=["POST"])
def processInputFile():
    opResponseObj = clntApp.processAudioFile()
    return jsonify(opResponseObj)


if __name__ == "__main__":
    clntApp = ClientService()
    host = '0.0.0.0'
    port = 5000
    httpd = simple_server.make_server(host, port, app)
    print("Serving on %s %d" % (host, port))
    httpd.serve_forever()