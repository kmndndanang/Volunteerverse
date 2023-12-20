import streamlit as st

def volunteerverse_dashboard():
    st.title("Dashboard")
    st.image("/Users/dananghilalkurniawan/Downloads/VolunteerVerse!Banner.png", use_column_width=True)
    st.header("Kuota Volunteer Verse")
    st.dataframe({
        'Penempatan': ['Student Volunteering', 'Volunteer Goes to School', 'Pelatihan Manajemen Kerelawanan', 'Orientasi Relawan'],
        'Jumlah Pendaftar': [25, 20, 50, 30]
    })
    st.header("Pemberitahuan Penting")
    st.warning("Penting: Deadline Pendaftaran Volunteer Verse Gelombang 3 pada 10 Desember 2023")

def volunteerverse_program():
    st.title("Volunteer Development")

    volunteer_list = [
        {
            "judul": "Student Volunteering",
            "deskripsi": "Program edukasi kerelawanan dengan sasaran anak berusia 7-10 tahun untuk belajar mengenai kerelawanan. Kegiatan SV terdiri dari materi dan praktek langsung yang dikemas secara menarik dan menyenangkan sehingga anak dapat menangkap tujuan dan nilai yang disampaikan. Kegiatan ini berlangsung selama 2 atau 3 hari di Sekolah Relawan dengan jadwal regulernya saat waktu libur anak sekolah.\n\nMuatan Edukasi:\n\n- Leadership\n- Creative Communication\n- Pengabdian Masyaeakat\n- Basic Kedermawanan",
            "gambar": "/Users/dananghilalkurniawan/Downloads/gambar1.jpeg",
            "link_daftar": "https://forms.gle/iJhjdujyLXUC3uuW6"
        },
        {
            "judul": "Volunteer Goes to School",
            "deskripsi": "Program edukasi kerelawanan dengan sasaran anak sekolah dasar untuk mengenal dunia kerelawanan dari hal terkecil hingga hal besar yang sama bermanfaatnya untuk orang lain dan diri sendiri. Para relawan berkunjung berbagi ilmu dan pengalaman ke sekolah-sekolah. Kegiatan dilakukan berdasarkan nilai kerelawanan yang dapat menjadi pengetahuan baru untuk mereka yang dikemas dengan menyenangkan dan interaktif.\n\nMuatan Edukasi:\n\n- Sharing Aksi Kerelawanan\n- Games Leadership\n- Video Edukasi Kerelawanan",
            "gambar": "/Users/dananghilalkurniawan/Downloads/gambar2.jpeg",
            "link_daftar": "https://forms.gle/HTABTobruAVvkymQA"
        },
        {
            "judul": "Pelatihan Manajemen Kerelawanan",
            "deskripsi": "Pelatihan manajemen kerelawanan secara offline selama dua hari bagi para manajer atau koordinator lembaga, organisasi, instansi maupun komunitas. Pelatihan ini bertujuan untuk membedah 13 materi mengenai pengetahuan dan keterampilan dasar dalam mengembangkan sistem manajemen kerelawanan yang efektif agar proyek dan program kesukarelawanan yang dimiliki mempunyai dampak lebih besar terhadap pembangunan masyarakat.\n\nMateri yang akan dibahas mencakup :\n\n- Relawan dan Pembangunan\n- Memahami Komunitas\n- Relawan dan Organisasi\n- Kontribusi Relawan\n- Peran Relawan\n- Perencanaan Program\n- Kapasitas Organisasi\n- Perjalanan Relawan\n- Pengembangan Program & Kegiatan\n- Memasarkan Kesempatan Relawan\n- Memilih dan Mencocokkan Relawan\n- Analisa Stakeholder\n- Dukungan, Supervisi",
            "gambar": "/Users/dananghilalkurniawan/Downloads/gambar3.jpeg",
            "link_daftar": "https://forms.gle/15HdVJvoavcRgynx8"
        },
        {
            "judul": "Orientasi Relawan",
            "deskripsi": "Sharing dan diskusi aktif untuk menyatukan frekuensi tentang kerelawanan. Kegiatan ini dikemas dengan metode workshop selama 6 jam. Bertujuan untuk memahami arti relawan, mengetahui modal awal yang harus dimiliki relawan, memiliki kesamaan visi serta sebagai langkah awal untuk merancang program-program kerelawanan.\n\nMateri yang akan dibahas mencakup:\n\n- Pengertian Kerelawanan\n- Inspirasi Kerelawanan\n\n- Motivasi Kerelawanan\n- Visi Kerelawanan\n- Pengenalan Fundraising",
            "gambar": "/Users/dananghilalkurniawan/Downloads/gambar4.png",
            "link_daftar": "https://forms.gle/1vXsA7k8UQ6CrN9J7"
        },
    ]
    for volunteer in volunteer_list:
        if st.button(f"Details: {volunteer['judul']}"):
            volunteerverse_details(volunteer)

def volunteerverse_details(volunteer):
    st.title(volunteer["judul"])
    st.image(volunteer["gambar"], use_column_width=True)
    st.write(volunteer["deskripsi"])

    if st.button("Back to Volunteer Verse Development"):
        volunteerverse_program()

    markdown_str = f"[Join Volunteer ({volunteer['judul']})]({volunteer['link_daftar']})"
    st.markdown(markdown_str, unsafe_allow_html=True)

def volunteerverse_dompetsesama():
    st.title("Dompet Sesama")

    sub_bab_list = [
        {
            "judul": "Bantuan Uang Tunai",
            "definisi": "Bantuan berupa uang tunai yang diberikan kepada individu atau keluarga yang membutuhkan.",
            "tujuan": "Memenuhi kebutuhan dasar sehari-hari, seperti makanan, kebutuhan medis, dan keperluan sehari-hari lainnya.",
            "image_path": "/Users/dananghilalkurniawan/Downloads/qrvol.png"
        },
        {
            "judul": "Bantuan Pakaian",
            "definisi": "Bantuan berupa pakaian yang diberikan kepada individu atau keluarga yang membutuhkan.",
            "tujuan": "Memberikan perlindungan dan kenyamanan melalui penyediaan pakaian yang layak.",
            "link_daftar": "https://forms.gle/ZH9aVjLv5cDg9v179"
        },
        {
            "judul": "Bantuan Bahan Pokok",
            "definisi": "Bantuan berupa bahan pokok seperti makanan atau bahan baku dan kebutuhan dapur lainnya.",
            "tujuan": "Membantu memenuhi kebutuhan pangan sehari-hari untuk keluarga yang kurang mampu.",
            "link_daftar": "https://forms.gle/ZH9aVjLv5cDg9v179"
        },
        {
            "judul": "Bantuan Pendidikan",
            "definisi": "Bantuan berupa dukungan pendidikan seperti,seragam sekolah yang masih layak, buku, alat tulis, dan biaya pendidikan.",
            "tujuan": "Mendukung akses pendidikan dan pengembangan potensi bagi anak-anak dan remaja.",
            "link_daftar": "https://forms.gle/ZH9aVjLv5cDg9v179"
        },
    ]

    for sub_bab in sub_bab_list:
        st.header(sub_bab["judul"])
        st.write(f"**Definisi:** {sub_bab['definisi']}")
        st.write(f"**Tujuan:** {sub_bab['tujuan']}")
 
        if sub_bab["judul"] == "Bantuan Uang Tunai":
            if st.button(f"Donasi ({sub_bab['judul']})"):
                show_donation_image(sub_bab['image_path'])
        else:
            if st.button(f"Donasi ({sub_bab['judul']})"):
                st.markdown(f"Silahkan lanjutkan pada link berikut ({sub_bab['judul']})({sub_bab['link_daftar']})")
        st.write("---")

def show_donation_image(image_path):
    st.image(image_path, width=300)
    st.success("Terima kasih telah Berdonasi, semoga amal dan kebaikan Anda dibalas yang Maha Kuasa Aamiin")

def volunteerverse_tentangkami():
    st.image("/Users/dananghilalkurniawan/Downloads/voluntering.jpeg")
    st.title("Tentang Kami")

    st.header("Sejarah")
    st.write("Aplikasi Volunteer Verse kami lahir dari mahasiswa yang peduli terhadap keberlanjutan kegiatan kegiatan sosial di tengah masyarakat. Dibentuk sebagai bagian dari tugas kuliah untuk merespon kebutuhan masyarakat, aplikasi ini bertujuan untuk memberikan wadah yang inovatif dan efektif bagi individu yang ingin memberikan kontribusi positif kepada masyarakat sekitar. Dengan semangat kolaborasi dan kepedulian, kami berusaha membentuk perubahan nyata dan merayakan kekuatan aksi sukarela dalam menciptakan dampak yang berarti.")

    st.header("Visi dan Misi")
    st.subheader("Visi:")
    st.write("Mewujudkan Lingkungan yang Lebih Bermakna dan Kemanusiaan Melalui Kolaborasi Volunteer Verse.")

    st.subheader("Misi:")
    st.write("Menyediakan Platform Inovatif yang Menghubungkan Para Relawan dan Dermawan untuk Memberikan Dampak Positif pada Masyarakat. Kami Berkomitmen untuk Membangun Jembatan Kemanusiaan, Mendorong Pertumbuhan Pribadi, dan Merayakan Keberagaman melalui Tindakan Sederhana yang Membawa Perubahan Besar.")

    st.header("Kontak Kami")
    st.subheader("Alamat:")
    st.write("Jalan Menuju Kebenaran Part 100. Isekai")

    st.subheader("Email:")
    st.write("info@volunteerverseapp.com")

    st.subheader("Telepon:")
    st.write("(021) 8989-8989")
    st.write("[WhatsApp](https://wa.me/6287864547740)")

    names = ["ganiya syazwa", "renisa putri giani", "dananghk", "redra eka prayoga", "dhafin razaqa luthfi"]
    st.subheader("Developed By:")
    for name in names:
        st.write(name)

def main():
    st.sidebar.title("VOLUNTEER VERSE")
    menu_options = ["Dashboard", "Program", "Dompet Sesama", "Tentang Kami"]
    selected_option = st.sidebar.selectbox("Pilih Menu", menu_options)
    if selected_option == "Dashboard":
        volunteerverse_dashboard()
    elif selected_option == "Program":
        volunteerverse_program()
    elif selected_option == "Dompet Sesama":
        volunteerverse_dompetsesama()
    elif selected_option == "Tentang Kami":
        volunteerverse_tentangkami()

if __name__ == "__main__":
    main()