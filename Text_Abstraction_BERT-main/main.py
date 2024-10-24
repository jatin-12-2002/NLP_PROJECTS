from flask import Flask, request, render_template, Response, jsonify
import os
from werkzeug.utils import secure_filename
import shutil
from zipfile import ZipFile
from wsgiref import simple_server
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/')
def upload():
    return render_template("upload.html")


@app.route('/predict', methods=['POST'])
def success():
    if request.method == 'POST':
        userInput = (request.form['fileName'])  # get value from dropdown
        testStoryFileName = userInput.split(",")[0]
        testSummaryFileName = userInput.split(",")[1]
        f = request.files['uploadFile']
        models = "models"
        try:
            # shutil.rmtree("models")
            # uploads_dirModelData = os.path.join(userDetail, 'InputModelFolder')
            # os.makedirs(userDetail)
            os.makedirs(models)
            # os.unlink("/models")
        except FileNotFoundError:
            print("fileNotFouncError")
        except FileExistsError:
            print("FileExistsError")
        except Exception as e:
            print("Exception", e)
        try:
            # f.save(os.path.join(userDetail, secure_filename(f.filename)))
            f.save(os.path.join(models, secure_filename(f.filename)))
        except Exception:
            print("Not able to save input files")

        with ZipFile('models/' + f.filename, 'r') as zipObj:
            # Extract all the contents of zip file in current directory
            zipObj.extractall()
            os.remove('models/' + f.filename)
        try:
            from com_in_ineuron_ai_predict.predictionFile import results

            responseDict = results(testStoryFileName, testSummaryFileName)
        except FileNotFoundError:
            return Response("Uploaded model File is not proper. Please see the instructions about requirements.")

        return jsonify(responseDict)


# port = int(os.getenv("PORT"))
if __name__ == "__main__":
    # clntApp = ClientApi()
    host = '0.0.0.0'
    port = 5000
    httpd = simple_server.make_server(host, port, app)
    print("Serving on %s %d" % (host, port))
    httpd.serve_forever()