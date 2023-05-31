# Saya Adinda Salsabilla 2005319 mengerjakan Latihan 5 dalam mata kuliah Desain dan Pemrograman Berorientasi Objek 
# untuk keberkahanNya maka saya tidak melakukan kecurangan seperti yang telah dispesifikasikan. Aamiin*/

from hunian import Hunian

class Indekos(Hunian):
    # constructor
    def __init__(self, nama_pemilik, nama_penghuni, image):
        super().__init__("Indekos")
        self.jenis_hunian = "Indekos"
        self.nama_pemilik = nama_pemilik
        self.nama_penghuni = nama_penghuni
        self.image = image
        self.listrik = 150000

    # Get data
    def get_dokumen(self):
        return "Bukti kontrak indekos oleh " + self.nama_penghuni + " dari " + self.nama_pemilik + "."

    def get_nama_pemilik(self):
        return self.nama_pemilik
    
    def get_image(self):
        return self.image

    def get_nama_penghuni(self):
        return self.nama_penghuni
    
    # listrik
    def get_listrik(self):
        return self.listrik

    def get_summary(self):
        return "Hunian Indekos."
    
    def get_detail(self):
        return "Jenis Hunian : " + self.jenis_hunian + "\n" + "Pemilik : " + self.nama_pemilik + "\nNama Penghuni : " + self.nama_penghuni + "\nBiaya Listrik : " + str(self.get_listrik()) + "\n\n"
