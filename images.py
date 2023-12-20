import streamlit as st
from PIL import Image

def main():
    st.title("Tampilkan Dua Gambar")

    # List path gambar
    image_paths = [
        "/Users/dananghilalkurniawan/Downloads/gambar1.jpeg",
        "/Users/dananghilalkurniawan/Downloads/gambar2.jpeg"
        "/Users/dananghilalkurniawan/Downloads/gambar3.jpeg"
        "/Users/dananghilalkurniawan/Downloads/gambar4.jpeg"
        "/Users/dananghilalkurniawan/Downloads/VolunteerVerse!Banner.jpeg"
        "/Users/dananghilalkurniawan/Downloads/qrvol.jpeg"
        "/Users/dananghilalkurniawan/Downloads/voluntering.jpeg"
    ]

    # Tampilkan gambar untuk setiap path
    for image_path in image_paths:
        # Baca file gambar dan konversi ke objek gambar
        image = Image.open(image_path)

        # Tampilkan gambar
        st.image(image, caption=f"Gambar ({image_path})", use_column_width=True)

if __name__ == "__main__":
    main()
