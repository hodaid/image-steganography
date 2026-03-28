import cv2

def encode_image(cover_path, secret_path, output_path):
    cover = cv2.imread(cover_path)
    secret = cv2.imread(secret_path)

    secret = cv2.resize(secret, (cover.shape[1], cover.shape[0]))

    stego = (cover & 254) | (secret >> 7)
    cv2.imwrite(output_path, stego)

def decode_image(stego_path, output_path):
    stego = cv2.imread(stego_path)
    extracted = (stego & 1) * 255
    cv2.imwrite(output_path, extracted)
