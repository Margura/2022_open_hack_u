import os
from flask import Flask, flash, request, redirect ,send_file, render_template
from werkzeug.utils import secure_filename
from glob import glob
from io import BytesIO
from zipfile import ZipFile

from src.main import main

XLSX_MIMETYPE = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
UPLOAD_FOLDER = "/tmp"
DOWNLOAD_FOLDER = "/tmp"
TMP_FOLDER = "/tmp"
ALLOWED_EXTENSIONS = {"jpg", "jpeg", "png"}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = b'(\xf8\x17w\x10\xf6\x1bS`\x0f\xe3\xaa\x9az\x10\x1d'

def remove_old_files():
    for f in glob(os.path.join(UPLOAD_FOLDER, "*.jpg")):
        os.remove(f)
    for f in glob(os.path.join(DOWNLOAD_FOLDER, "*.jpeg")):
        os.remove(f)
    for f in glob(os.path.join(TMP_FOLDER, "*.png")):
        os.remove(f)
    for f in glob(os.path.join(TMP_FOLDER, "*.midi")):
        os.remove(f)
    for f in glob(os.path.join(TMP_FOLDER, "*.mp3")):
        os.remove(f)

@app.route("/")
def index():
    return render_template("upload.html") 

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/generate",methods=["POST"])
def upload():
    if "file" not in request.files :
        redirect("/")
    file = request.files["file"]
    if file.filename == "" :
        flash("No selected file")
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        
        main(UPLOAD_FOLDER, filename)

        stream = BytesIO()
        with ZipFile(stream, 'w') as zf:
            for f in glob(os.path.join(DOWNLOAD_FOLDER, "*.mp3")):
                zf.write(f, os.path.basename(f))
        stream.seek(0)

        remove_old_files()
        
        zipname = "music.zip"
        
        return send_file(
            stream,
            as_attachment=True,
            download_name=zipname,
            mimetype = XLSX_MIMETYPE
        )    
        
if __name__ == "__main__":
    app.run(debug=True)