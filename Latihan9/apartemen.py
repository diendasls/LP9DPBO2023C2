# Saya Adinda Salsabilla 2005319 mengerjakan Latihan 5 dalam mata kuliah Desain dan Pemrograman Berorientasi Objek 
# untuk keberkahanNya maka saya tidak melakukan kecurangan seperti yang telah dispesifikasikan. Aamiin*/

from hunian import Hunian

class Apartemen(Hunian):
    # constructor
    def __init__(self, nama_pemilik, jml_penghuni, jml_kamar, image):
        super().__init__("Apartemen", jml_penghuni, jml_kamar)
        self.jenis_hunian = "Apartemen"
        self.nama_pemilik = nama_pemilik
        self.image = image
        self.listrik = 100000
        self.total_listrik = 0
    
    # Get data
    def get_dokumen(self):
        return "Sertifikat Hak Milik Atas Satuan Rumah Susun (SHMSRS) a/n " + self.nama_pemilik + "."

    def get_nama_pemilik(self):
        return self.nama_pemilik
    
    def get_image(self):
        return self.image
    
    # total listrik
    def get_total_listrik (self):
        self.total_listrik = (self.jml_penghuni * 75000) + self.listrik
        return self.total_listrik
    
    def get_detail(self):
        return "Jenis Hunian : " + self.jenis_hunian + "\n" + "Pemilik : " + self.nama_pemilik + "\nJumlah Kamar : " + str(self.jml_kamar) + "\n" + "Biaya Listrik : " + str(self.get_total_listrik()) + "\n"
