import PIL.Image as Image

class ImageCrypt:
    def __init__(self, imageFile):
        self.imageFile = imageFile # handle image file variable
        self.image = Image.open(self.imageFile).convert("RGB") # Open image file in rgba mode
        self.pixels = [(x, y) for y in range(self.image.height) for x in range(self.image.width)] # Get a list of all pixels in the image

    def encodeBytes(self, byteList):
        byteLength = format(len(byteList), "032b")
        byteLength = [byteLength[i:i+8] for i in range(0, len(byteLength), 8)]
        byteList = ["10101010"] + byteLength + byteList
        if (len(self.pixels) <= len(byteList)): raise Exception("The bytes could not be hidden in the image because the image is too small!")
        for byteNumber, byte in enumerate(byteList):
            for bitNumber, bit in enumerate(byte):
                bit = int(bit)
                totalBitNumber = byteNumber * 8 + bitNumber
                currentPixelCoordinate = self.pixels[totalBitNumber]
                currentPixelValue = list(self.image.getpixel(currentPixelCoordinate))
                currentPixelValue = tuple(value + (bit * (1 - value % 2) or (1 - bit) * (value % 2)) for value in currentPixelValue)
                self.image.putpixel(currentPixelCoordinate, currentPixelValue)
        self.image.save(self.imageFile)
        return self.image
    
    def decodeBytes(self):
        byteLength = int("".join(map(str, [0 if int(list(self.image.getpixel(pixel))[0])%2==0 else 1 for pixel in self.pixels[:40][8:]])), 2)
        if ("".join(map(str, [0 if int(list(self.image.getpixel(pixel))[0])%2==0 else 1 for pixel in self.pixels[:8]]))!="10101010"): raise ValueError("The file could not be decrypted as no bytes were hidden in it!")
        array = self.pixels[40:]
        byteList = []
        byte = ""
        for totalBitNumber, pixel in enumerate(array):
            if (totalBitNumber/8>=byteLength): break
            bitNumber = totalBitNumber % 8 + 1
            bitValue = 0 if self.image.getpixel(pixel)[0]%2==0 else 1
            byte += str(bitValue)
            if (bitNumber == 8):
                byteList.append(byte)
                byte = ""
        return byteList
    
    def encodeText(self, text):
        byteList = [format(byte, "08b") for byte in bytes(text, "utf-8")]
        return self.encodeBytes(byteList)

    def decodeText(self):
        byteList = self.decodeBytes()
        text = "".join([chr(int(byte, 2)) for byte in byteList])
        return text
    
    def encodeFile(self, filePath):
        with open(filePath, "rb") as f: content = f.read()
        byteList = [format(byte, "08b") for byte in content]
        return self.encodeBytes(byteList)

    def decodeFile(self, fileName):
        byteList = self.decodeBytes()
        byte_data = bytearray()
        for b in byteList: byte_data.append(int(b, 2))
        with open(fileName, "wb") as f: f.write((byte_data))
        return fileName