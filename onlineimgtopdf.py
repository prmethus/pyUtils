import os, requests
import PIL.Image


def url_inp():
    urls = []
    i = 1
    while True:
        inp = input(str(r"|type 'cancel' to cancel| Enter url of image file no.{} :".format(i)))
        if inp.strip().lower() == "cancel":
            break
        else:
            urls.append(inp)
            i += 1
    return urls

def download_imgs(urls):
    img_files = []
    i = 1
    for url in urls:
        r = requests.get(url)
        img_files.append(str(i) + ".jpg")
        with open(img_files[-1], "wb") as f:
            f.write(r.content)
            i += 1
    return img_files

def images_to_pdf(img_files):
    images = []
    for img_file in img_files:
        newimg = PIL.Image.open(img_file).convert("RGB")
        imgfile = PIL.Image.new("RGB", newimg.size, (0,0,0))
        imgfile.paste(newimg, mask=newimg.split()[3])
        images.append(imgfile)
	
    images[0].save(input(str("Enter PDF file name: ")), save_all=True, append_images=images[1:])

def rm_imgs():
    inp = input(str(r"| Remove the images from your hard drive? [y/n]:"))

def main():
    urls = url_inp()
    img_files = download_imgs(urls)
    images_to_pdf(img_files)

main()
