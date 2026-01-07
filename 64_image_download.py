import requests
import asyncio
# For image
async def download_image1():
    print("Start downloading_1...")
    
    url = ("https://img.freepik.com/free-vector/laptop-with-program-code-isometric-icon-software-development-programming-applications-dark-neon_39422-971.jpg")
    
    response = requests.get(url)
  
    with open("4K_Image1.jpg", 'wb')as f: 
        f.write(response.content)
    
    print("Download finished1")
    

async def download_image2():
    await asyncio.sleep(3)
    print("Start downloading_2...")
    
    url = ("https://i.pinimg.com/736x/36/35/c6/3635c64646cb17f59993b1102188cbde.jpg")
    
    response = requests.get(url)
    # open("4K_Image2.jpg", "wb").write(response.content)
    with open("4K_Image2.jpg", 'wb')as f: 
        f.write(response.content)
    print("Download finished2")
    
async def main():
    # await download_image1()
    # await download_image2()
    # return
    await asyncio.gather(
        download_image2(),
        download_image1(),
    )

asyncio.run(main())