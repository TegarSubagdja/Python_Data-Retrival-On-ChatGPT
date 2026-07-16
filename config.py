ADDRESS_IP = "127.0.0.1:9222"

MIN_SAMPLES = 5

MAX_LEN = 10

AVG_RESPONSE_TIME_LIMIT = 60

AVG_RESPONSE_TIME_LIMIT_BOTTOM = 10

STOP_FLAG = False

CHATGPT_URL = "chatgpt.com"

PROMPT_TEXTAREA_ID = "prompt-textarea"

VOICE_BUTTON_SELECTOR = (
    'button[aria-label="Start Voice"]'
)

COPY_BUTTON_SELECTOR = (
    'button[aria-label="Copy response"]'
)

COMPANY_KNOWLEDGE_SELECTOR = (
    'button[aria-label="Company knowledge, click to remove"]'
)

LIMIT_KEYWORDS = [
    "reach the maximum",
    "you've reached the maximum",
    "starting a new chat",
    "our systems have detected unusual activity",
    "unusual activity"
]

EXCEL_FILE = "Data/data.xlsx"
EXCEL_SHEET = "Sheet1"

EXCEL_FILE_2 = "Data/data2.xlsx"
EXCEL_SHEET_2 = "Sheet1"

PROMPT_BASE = """
Tugas CP08062026:

Tarik data dari company knowledge berdasarkan nama/kode produk THK yang akan saya berikan.

Aturan keluaran WAJIB:

Keluaran harus berupa plain text murni.
Jangan gunakan markdown apa pun.
Jangan gunakan code block.
Jangan gunakan format bash.
Jangan gunakan tabel.
Jangan gunakan emoji, ikon, simbol dekoratif, atau karakter khusus.
Hasil harus siap copy-paste langsung ke Excel atau CSV.
Gunakan urutan format persis seperti yang ditentukan.
Pada bagian "Data teknis", tampilkan hanya field yang relevan dengan kategori produk.
Gunakan seluruh spesifikasi yang tersedia pada company knowledge selengkap mungkin.
Jangan menghilangkan spesifikasi penting hanya karena tidak ada pada contoh.
Untuk produk dengan kategori yang sama, gunakan nama field yang konsisten.
Jangan membuat spesifikasi yang tidak terdapat pada company knowledge.
Jika suatu informasi tidak ditemukan, isi dengan "Tidak ditemukan".
Jika kode produk tidak ditemukan sama sekali, tetap tampilkan seluruh format dan jelaskan pada bagian catatan bahwa data produk tidak ditemukan di company knowledge.
Jangan menambahkan penjelasan, disclaimer, ataupun kalimat pembuka maupun penutup.

Format keluaran:

[NAMA PRODUK]

Deskripsi marketplace:

[Deskripsi dalam bahasa marketplace yang menjelaskan:

jenis produk,
fungsi utama,
prinsip kerja,
aplikasi penggunaan,
kompatibilitas dengan komponen lain bila ada,
keunggulan produk,
serta hal-hal yang perlu diperiksa customer sebelum membeli.]

Data teknis:

Brand: ...
Kode produk: ...
Kategori: ...
Seri: ...
Jenis produk: ...

[Lanjutkan dengan spesifikasi teknis yang benar-benar relevan terhadap kategori produk. Gunakan seluruh spesifikasi yang tersedia pada company knowledge. Jangan batasi hanya pada contoh di bawah.]

Aturan pembentukan field teknis:

Nama field harus mengikuti istilah teknis yang digunakan pada company knowledge.
Untuk kategori produk yang sama, gunakan nama field yang konsisten.
Jangan menampilkan field yang tidak relevan.
Jika suatu field memang relevan tetapi nilainya tidak ditemukan, isi "Tidak ditemukan".
Urutkan field dari informasi umum menuju informasi yang lebih spesifik.

Contoh field yang dapat digunakan (sesuaikan kategori produk):

Dimensi:
Ukuran nominal
Diameter
Diameter poros
Diameter luar
Diameter dalam
Panjang
Stroke
Lead
Pitch
Lebar
Tinggi
Panjang blok
Lebar blok
Lebar rel
Tinggi rakitan
Panjang rel
Diameter bola

Konstruksi:
Jenis nut
Jenis block
Jenis rail
Jenis bearing
Tipe flange
Tipe mounting
Preload
Accuracy Grade
Precision Grade
Clearance
Seal
Grease nipple
Jumlah sirkulasi bola
Material
Surface treatment
Drive system
Thread direction
Configuration
Mounting orientation

Kapasitas:
Beban dinamis
Beban statis
Moment load
Maximum speed
Maximum acceleration
Maximum load
Maximum thrust
Rated load
Torque
Power
Voltage
Current
Resolution
Repeatability

Kompatibilitas:
Rail pasangan
Nut pasangan
Bearing pasangan
Motor kompatibel
Encoder kompatibel
Controller kompatibel
Referensi pengganti
Kompatibilitas referensi

Informasi aplikasi:
Aplikasi
Fungsi
Keunggulan
Catatan pemilihan produk

Catatan:

[keterangan tambahan atau "Tidak ada"]

Pedoman konsistensi kategori:

Untuk LM Guide:
Gunakan field seperti Ukuran nominal, Tinggi rakitan, Lebar blok, Panjang blok, Lebar rel, Beban dinamis, Beban statis, Rail pasangan, dan field lain yang tersedia.

Untuk Ball Screw:
Gunakan field seperti Diameter screw, Lead, Stroke, Jenis nut, Accuracy Grade, Preload, Direction, Beban dinamis, Beban statis, serta spesifikasi lain yang tersedia.

Untuk Cross Roller Ring:
Gunakan field seperti Diameter dalam, Diameter luar, Tinggi, Tipe, Seal, Clearance, Akurasi, Beban, dan spesifikasi lain yang tersedia.

Untuk Linear Actuator:
Gunakan field seperti Stroke, Maximum Speed, Maximum Load, Motor Type, Drive System, Encoder, Voltage, Repeatability, Mounting, dan spesifikasi lain yang tersedia.

Untuk kategori lainnya:
Bentuk field berdasarkan spesifikasi yang tersedia pada company knowledge dengan tetap menjaga konsistensi penamaan untuk produk dalam kategori yang sama.

Prioritas utama:

Akurasi terhadap company knowledge.
Kelengkapan spesifikasi.
Konsistensi nama field pada kategori produk yang sama.
Jangan memaksakan field dari kategori lain.

"""