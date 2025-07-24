from flask import Flask, render_template, request, redirect
import boto3
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
S3_BUCKET = "your-s3-bucket-name"
S3_REGION = "your-region"  # e.g., us-east-1

s3 = boto3.client(
    "s3",
    aws_access_key_id="your-access-key",
    aws_secret_access_key="your-secret-key",
    region_name=S3_REGION
)

@app.route('/')
def index():
    objects = s3.list_objects_v2(Bucket=S3_BUCKET).get("Contents", [])
    files = [obj["Key"] for obj in objects]
    return render_template("index.html", files=files)

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    if file:
        filename = secure_filename(file.filename)
        s3.upload_fileobj(file, S3_BUCKET, filename)
    return redirect('/')

@app.route('/download/<filename>')
def download(filename):
    url = s3.generate_presigned_url(
        'get_object',
        Params={'Bucket': S3_BUCKET, 'Key': filename},
        ExpiresIn=3600
    )
    return redirect(url)

if __name__ == "__main__":
    app.run(debug=True)
