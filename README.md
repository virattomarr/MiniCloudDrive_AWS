# ☁️ MiniCloudDrive (AWS S3 Edition)

A simple cloud file upload and download system using Flask and Amazon S3. Acts like a mini Google Drive backed by cloud storage.

---

## 🚀 Features

- Upload files via web interface
- Files stored on AWS S3 bucket
- Generate download links using presigned URLs
- View all uploaded files on homepage

---

## 🧱 Project Structure

```
MiniCloudDrive_AWS/
├── app.py
├── templates/
│   └── index.html
├── requirements.txt
└── README.md
```

---

## 🛠 Setup Instructions

1. Replace the following placeholders in `app.py`:
    - `your-s3-bucket-name`
    - `your-region`
    - `your-access-key`
    - `your-secret-key`

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the server:
```bash
python app.py
```

4. Open browser:
```
http://127.0.0.1:5000
```

---

## 💡 Requirements

- AWS S3 Bucket (Free Tier)
- IAM User with S3 access
- Flask, Boto3

---

## 🧑‍💻 Author

Virat Tomar

---

## 🪪 License

MIT License
