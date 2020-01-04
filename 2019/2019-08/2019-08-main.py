
def read_input():
    with open("input.txt") as f:
        pixels = [str(line) for line in f][0]
        return [int(p) for p in pixels if p != '\n']

pixels = read_input()
W = 25
H = 6
images = [pixels[i: i + (H * W)] for i in range(0, len(pixels), W * H)]

max_zeros_cnt = float('inf')

for image in images:
    zeros_cnt = image.count(0)
    if max_zeros_cnt > zeros_cnt:
        max_zeros_cnt = zeros_cnt
        max_zeros_img = image

ones_cnt = max_zeros_img.count(1)
twos_cnt = max_zeros_img.count(2)
print("First solution, 2*1 = %d"%(ones_cnt * twos_cnt))

BLACK = 0
WHITE = 1
TRANSPARENT = 2

img_len = H * W
result_img = []
for pix_idx in range(0, img_len):
    print("pix_idx:%d"%pix_idx)
    value = TRANSPARENT
    offset = 0
    while pix_idx + offset < len(pixels) and value == TRANSPARENT:
        pixel = pixels[pix_idx + offset]
        offset += img_len
        if value == TRANSPARENT:
            value = pixel
    result_img.append(value)
    
piece_of_art = [' ' if pix == BLACK else '#' for pix in result_img]

for row in range(0, H):
    line = piece_of_art[W * row : W * (row+1)]
    print("".join(line))
