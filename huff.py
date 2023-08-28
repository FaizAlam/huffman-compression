from HuffmanCoding import HuffmanCoding

if __name__=="__main__":
    path_txt = "sample-2mb-text-file.txt"
    H = HuffmanCoding(path_txt)
    H.compress()
    print("compressed")
    path_bin = "sample-2mb-text-file.bin"
    H.decompress(path_bin)