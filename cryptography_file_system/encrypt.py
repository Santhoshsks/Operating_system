import numpy as np
from PIL import Image
import pickle 

def image_splitting(image, block_size):
    # Split the image into non-overlapping blocks
    height, width = image.shape
    blocks = [image[i:i+block_size, j:j+block_size] for i in range(0, height, block_size) for j in range(0, width, block_size)]
    return blocks

def confusion(blocks):
    # Apply zigzag pattern and rotation to blocks
    # Generate a random vector r
    r = np.random.randint(0, 256, len(blocks))
    # Random permutation of image blocks based on r
    scrambled_blocks = [blocks[i] for i in np.argsort(r)]

    return scrambled_blocks

def key_generation(plain_image):
    # Calculate the initial value of the logistic map
    Y0 = np.sum(plain_image) / (plain_image.size * 255.0)
    
    # Iterate the chaotic map
    M, N = plain_image.shape
    sequence_size = M * N
    chaotic_map = logistic_map(Y0, sequence_size)
    
    # Calculate the key
    key = [int(chaotic_map[i] * 1e14) % 256 for i in range(sequence_size)]
    
    return key

def logistic_map(Y0, size):
    # Logistic map iteration
    Y = Y0
    a = 3.8  # You can adjust the control parameter 'a' as needed
    chaotic_sequence = []
    
    for _ in range(size):
        Y = a * Y * (1 - Y)
        chaotic_sequence.append(Y)
    
    return chaotic_sequence

def diffusion(scrambled_blocks, key):
    # Bit-wise XOR operation between key and scrambled image
    encrypted_blocks = [np.bitwise_xor(scrambled_blocks[i].ravel(), key[i]) for i in range(len(scrambled_blocks))]
    encrypted_image = np.concatenate(encrypted_blocks)

    return encrypted_image.reshape(plain_image.shape)

def save_image(image, filename):
    # Save the encrypted image
    encrypted_image = Image.fromarray(image.astype(np.uint8))
    encrypted_image.save(filename)

def encrypt_image(plain_image, block_size):
    # Plain image splitting
    blocks = image_splitting(plain_image, block_size)
    
    # Confusion
    scrambled_blocks = confusion(blocks)
    
    # Key generation
    key = key_generation(plain_image)
    with open("key.bat",'wb+') as f:
        pickle.dump(key,f)
    # Diffusion
    encrypted_image = diffusion(scrambled_blocks, key)

    return encrypted_image

# Load the plain image
plain_image_path = "image.jpeg"
plain_image = np.array(Image.open(plain_image_path).convert('L'))

# Block size for image splitting
block_size = 16  # You can choose 16, 32, or 64

# Encrypt the image
encrypted_image = encrypt_image(plain_image, block_size)

# Save the encrypted image
save_image(encrypted_image, "encrypted.jpeg")