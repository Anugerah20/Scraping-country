import requests
import csv
from bs4 import BeautifulSoup

name = input("Masukkan nama negara: ").strip()

formatted_name = name.replace(" ", "_")
target_url = "https://id.wikipedia.org/wiki/" + formatted_name

response = requests.get(target_url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    paragraphs = soup.find_all('p')
    info = "Informasi tidak ditemukan"

    for paragraph in paragraphs:
        text = paragraph.get_text()
        if name.lower() in text.lower():
            info = text.strip()
            break

    with open("name_country.csv", mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        file.seek(0, 2)
        if file.tell() == 0:
            writer.writerow(['Nama Negara', 'Deskripsi'])
        writer.writerow([name, info])
        print(f"Data berhasil ditambahkan ke file CSV.")
else:
    print("Halaman tidak ditemukan di Wikipedia.")
