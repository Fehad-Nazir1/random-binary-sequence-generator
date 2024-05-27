import random
import streamlit as st
import os

def create_bin_file(num_ones, num_zeros, bin_filename, txt_filename):
    num_bits = num_ones + num_zeros
    bits = [1] * num_ones + [0] * num_zeros
    random.shuffle(bits)

    byte_array = bytearray()
    bit_string = ""
    for i in range(0, len(bits), 8):
        byte = 0
        for bit in bits[i:i+8]:
            byte = (byte << 1) | bit
        byte_array.append(byte)
        bit_string += ''.join(map(str, bits[i:i+8]))

    with open(bin_filename, 'wb') as bin_file:
        bin_file.write(byte_array)

    with open(txt_filename, 'w') as txt_file:
        txt_file.write(bit_string)

def bin_to_txt(bin_filename, txt_filename):
    with open(bin_filename, 'rb') as bin_file:
        byte = bin_file.read(1)
        bit_string = ""
        while byte:
            byte = ord(byte)
            bits = bin(byte)[2:].zfill(8)
            bit_string += bits
            byte = bin_file.read(1)

    with open(txt_filename, 'w') as txt_file:
        txt_file.write(bit_string)

def main():
    st.title('Random Binary Sequence Generator and Converter')

    # Binary file generation
    st.header('Generate Binary File')
    num_ones = st.number_input('Enter the number of 1s:', min_value=0)
    num_zeros = st.number_input('Enter the number of 0s:', min_value=0)

    if st.button('Generate Binary File'):
        bin_filename = 'output.bin'
        txt_filename = 'output.txt'
        create_bin_file(num_ones, num_zeros, bin_filename, txt_filename)
        st.success('Binary file and its text counterpart created successfully.')
        st.download_button('Download Binary File', data=open(bin_filename, 'rb'), file_name=bin_filename)
        st.download_button('Download Text File', data=open(txt_filename, 'r'), file_name=txt_filename)

    # Binary to text file conversion
    st.header('Convert Binary File to Text File')
    uploaded_file = st.file_uploader("Upload a binary file", type=["bin"])

    if uploaded_file is not None:
        with open("uploaded_file.bin", "wb") as f:
            f.write(uploaded_file.getbuffer())

        if st.button('Convert to Text File'):
            bin_to_txt('uploaded_file.bin', 'uploaded_file.txt')
            st.success('Binary file converted to text file successfully.')
            st.download_button('Download Text File', data=open('uploaded_file.txt', 'r'), file_name='uploaded_file.txt')

    # Clean up files
    if os.path.exists('output.bin'):
        os.remove('output.bin')
    if os.path.exists('output.txt'):
        os.remove('output.txt')
    if os.path.exists('uploaded_file.bin'):
        os.remove('uploaded_file.bin')
    if os.path.exists('uploaded_file.txt'):
        os.remove('uploaded_file.txt')

if __name__ == '__main__':
    main()
