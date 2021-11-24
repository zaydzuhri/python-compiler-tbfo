class Coba:
    def __init__(self, nama):
        self.nama = nama
    def cetak(self):
        print(self.nama)
    def __str__(self):
        return self.nama