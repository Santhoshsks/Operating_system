"""import numpy as np
from PIL import Image
import pickle

def image_splitting(image, block_size):
    # Split the image into non-overlapping blocks
    height, width = image.shape
    blocks = [image[i:i+block_size, j:j+block_size] for i in range(0, height, block_size) for j in range(0, width, block_size)]
    return blocks

def inverse_diffusion(encrypted_blocks, key):
    # Bit-wise XOR operation between key and encrypted image
    decrypted_blocks = [np.bitwise_xor(encrypted_blocks[i].ravel(), key[i]) for i in range(len(encrypted_blocks))]
    decrypted_image = np.concatenate(decrypted_blocks)

    return decrypted_image.reshape(encrypted_image.shape)

def inverse_confusion(scrambled_blocks, r):
    # Reverse the random permutation of image blocks based on r
    blocks = [scrambled_blocks[i % len(scrambled_blocks)] for i in np.argsort(r)]
    return blocks


def inverse_image_splitting(blocks, block_size, image_shape):
    # Reverse the image splitting process
    height, width = image_shape
    original_image = np.zeros(image_shape, dtype=np.uint8)

    for i in range(0, len(blocks)):
        row_start = (i * block_size) // width * block_size
        col_start = (i * block_size) % width
        original_image[row_start:row_start+block_size, col_start:col_start+block_size] = blocks[i]

    return original_image

def decrypt_image(encrypted_image, block_size, key):
    # Decrypt the image

    # Step 1: Inverse Diffusion
    encrypted_blocks = image_splitting(encrypted_image, block_size)
    decrypted_image = inverse_diffusion(encrypted_blocks, key)

    # Step 2: Inverse Confusion
    r = np.random.randint(0, 256, len(encrypted_blocks))
    blocks = inverse_confusion(decrypted_image, r)

    # Step 3: Inverse Image Splitting
    original_image = inverse_image_splitting(blocks, block_size, encrypted_image.shape)

    return original_image

def logistic_map(Y0, size):
    # Logistic map iteration
    Y = Y0
    a = 3.8  # You can adjust the control parameter 'a' as needed
    chaotic_sequence = []
    
    for _ in range(size):
        Y = a * Y * (1 - Y)
        chaotic_sequence.append(Y)
    
    return chaotic_sequence


def save_image(image, filename):
    # Save the encrypted image
    encrypted_image = Image.fromarray(image.astype(np.uint8))
    encrypted_image.save(filename)
    
# Load the encrypted image
encrypted_image_path = "encrypted.jpeg"
encrypted_image = np.array(Image.open(encrypted_image_path).convert('L'))

with open('key.bat','rb') as f:
    key=pickle.load(f)

block_size=16
# Decrypt the image
decrypted_image = decrypt_image(encrypted_image, block_size, key)

# Save the decrypted image
save_image(decrypted_image, "decrypted.jpeg")

"""
import numpy as np
from PIL import Image
import pickle

def save_image(image, filename):
    # Save the encrypted image
    encrypted_image = Image.fromarray(image.astype(np.uint8))
    encrypted_image.save(filename)

def inverse_diffusion(encrypted_blocks, key):
    # Bit-wise XOR operation between key and encrypted image
    decrypted_blocks = [np.bitwise_xor(encrypted_blocks[i].ravel(), key[i]) for i in range(len(encrypted_blocks))]
    decrypted_image = np.concatenate(decrypted_blocks)

    return decrypted_image.reshape(encrypted_image.shape)

def inverse_confusion(scrambled_blocks, r):
    # Reverse the random permutation of image blocks based on r
    blocks = [scrambled_blocks[i % len(scrambled_blocks)] for i in np.argsort(r)]
    return blocks
def inverse_image_splitting(blocks, block_size, image_shape):
    # Reverse the image splitting process
    height, width = image_shape
    original_image = np.zeros(image_shape, dtype=np.uint8)

    for i in range(0, len(blocks)):
        row_start = (i * block_size) // width * block_size
        col_start = (i * block_size) % width
        block = blocks[i]

        # Reshape the block
        block = block.reshape((block_size, -1))

        # Resize the block to fit the specified block size
        block = np.resize(block, (block_size, block_size))

        original_image[row_start:row_start+block_size, col_start:col_start+block_size] = block

    return original_image




def image_splitting(image, block_size):
    # Split the image into non-overlapping blocks
    height, width = image.shape
    blocks = [image[i:i+block_size, j:j+block_size] for i in range(0, height, block_size) for j in range(0, width, block_size)]
    return blocks

def decrypt_image(encrypted_image, block_size, key):
    # Step 0: Read the key from the file

    # Step 1: Inverse Diffusion
    encrypted_blocks = image_splitting(encrypted_image, block_size)
    decrypted_image = inverse_diffusion(encrypted_blocks, key)

    # Step 2: Inverse Confusion
    r = np.random.randint(0, 256, len(encrypted_blocks))
    blocks = inverse_confusion(decrypted_image, r)

    # Step 3: Inverse Image Splitting
    original_image = inverse_image_splitting(blocks, block_size, encrypted_image.shape)

    return original_image

# Load the encrypted image
encrypted_image_path = "encrypted.jpeg"
encrypted_image = np.array(Image.open(encrypted_image_path).convert('L'))

# Specify the block size used during encryption
block_size = 16  # You can choose 16, 32, or 64

with open('key.bat','rb') as f:
    key=pickle.load(f)

# Decrypt the image
decrypted_image = decrypt_image(encrypted_image, block_size, key)

# Save the decrypted image
decrypted_image_path = "decrypted.jpeg"
save_image(decrypted_image, decrypted_image_path)
