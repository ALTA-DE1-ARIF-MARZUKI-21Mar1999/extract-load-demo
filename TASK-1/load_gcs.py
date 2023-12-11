from google.cloud import storage
import os
import json

def write_to_gcs(bucket_name, blob_name, data):
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(blob_name)
    blob.upload_from_string(data)

data = [
    {
        "nama": "Joko",
        "umur": 25,
        "gender": "Pria",
        "pekerjaan": "Developer",
        "tempat_tinggal": "Jakarta",
        "hobi": "Membaca"
    },
    {
        "nama": "Mawar",
        "umur": 30,
        "gender": "Wanita",
        "pekerjaan": "Designer",
        "tempat_tinggal": "Bandung",
        "hobi": "Memasak"
    },
    {
        "nama": "Budi",
        "umur": 28,
        "gender": "Pria",
        "pekerjaan": "Pilot",
        "tempat_tinggal": "Surabaya",
        "hobi": "Berenang"
    },
    {
        "nama": "Eva",
        "umur": 33,
        "gender": "Wanita",
        "pekerjaan": "Penyanyi",
        "tempat_tinggal": "Yogyakarta",
        "hobi": "Menulis"
    },
    {
        "nama": "Alan",
        "umur": 27,
        "gender": "Pria",
        "pekerjaan": "Dokter",
        "tempat_tinggal": "Lampung",
        "hobi": "Fotografi"
    },
    {
        "nama": "Melati",
        "umur": 29,
        "gender": "Wanita",
        "pekerjaan": "Guru",
        "tempat_tinggal": "Solo",
        "hobi": "Olahraga"
    },
    {
        "nama": "Marshall",
        "umur": 31,
        "gender": "Pria",
        "pekerjaan": "Presenter",
        "tempat_tinggal": "Jakarta",
        "hobi": "Traveling"
    },
    {
        "nama": "Monica",
        "umur": 26,
        "gender": "Wanita",
        "pekerjaan": "Content Creator",
        "tempat_tinggal": "Bandung",
        "hobi": "Menggambar"
    },
    {
        "nama": "Eko",
        "umur": 32,
        "gender": "Pria",
        "pekerjaan": "Data Engineer",
        "tempat_tinggal": "Medan",
        "hobi": "Bermain game"
    },
    {
        "nama": "olivia",
        "umur": 24,
        "gender": "Wanita",
        "pekerjaan": "Advokat",
        "tempat_tinggal": "Malang",
        "hobi": "Mendaki"
    }
]

json_data = json.dumps(data)

bucket_name = os.getenv('BUCKET_NAME')
blob_name = 'arif_task1.json'
write_to_gcs(bucket_name, blob_name, json_data)
