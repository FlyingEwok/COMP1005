import pygame

src_img = pygame.image.load('comp1405_live_demo_18_sample_picture.png')
(wid, hgt) = src_img.get_size()
src_img = pygame.transform.scale(src_img, (wid, hgt))
(wid, hgt) = src_img.get_size()
win_sfc = pygame.display.set_mode((wid, hgt))
win_sfc.blit(src_img, (0, 0))

# by request, the ASCII art will also appear in an external file
external_file = open("ascii_art_result.txt", "w")

for y in range(hgt):
	for x in range(wid):

		(r, g, b, _) = win_sfc.get_at((x, y))

		luminance = (0.2126 * r + 0.7152 * g + 0.0722 * b) / 255

		if luminance > 0.875:
			next_character = "@"
		elif luminance > 0.750:
			next_character = "#"
		elif luminance > 0.625:
			next_character = "*"
		elif luminance > 0.500:
			next_character = "+"
		elif luminance > 0.375:
			next_character = "="
		elif luminance > 0.250:
			next_character = "-"
		elif luminance > 0.125:
			next_character = ":"
		else:
			next_character = "."

		print(next_character, end="")
		print(next_character, file=external_file, end="")

	print()
	print(file=external_file)
	
external_file.close()

pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()	