# Saya Adinda Salsabilla 2005319 mengerjakan Latihan 5 dalam mata kuliah Desain dan Pemrograman Berorientasi Objek 
# untuk keberkahanNya maka saya tidak melakukan kecurangan seperti yang telah dispesifikasikan. Aamiin*/

class Hunian():
    # constructor
    def __init__(self, jenis, jml_penghuni = 1, jml_kamar = 1, image = ""):
        self.jenis = jenis
        self.jml_penghuni = jml_penghuni
        self.jml_kamar = jml_kamar
        self.image = image
        self.listrik = 100000
        self.total_listrik = 0

    # Get data
    def get_jenis(self):
        return self.jenis

    def get_jml_penghuni(self):
        return self.jml_penghuni

    def get_jml_kamar(self):
        return self.jml_kamar
    
    def get_image(self):
        return self.image

    def get_dokumen(self):
        pass

    # total listrik
    def get_total_listrik(self):
        # return "total listrik"
        if self.jenis.__eq__("Apartemen"):
            self.total_listrik = (self.jml_penghuni * 75000) + self.listrik
            return self.total_listrik
        elif self.jenis.__eq__("Indekos"):
            self.total_listrik = 200000
            return self.total_listrik
        elif self.jenis.__eq__("Rumah"):
            self.total_listrik = (self.jml_penghuni * 50000) + self.listrik
            return self.total_listrik
        

    def get_summary(self):
        return "\nHunian "+ self.jenis +", ditempati oleh " + str(self.jml_penghuni) + " orang."
    