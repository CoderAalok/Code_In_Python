# # Coroutine
# import time
# def find_data():

#     with open("Excersise.log")as f:
#         data = f.read()
#     print(data)
#     time.sleep(2)

#     while True:
#         d = yield  #->> It preserved the execution state when reached here 
#         if d in data:
#             print(data)
#         else:
#             print("The data is not found.")

# data = find_data() #Creates generator object
# # Before it generator object print
# print(data)
# # Here iterate the generator object using next() function
# next(data) #start execution
# # After that it execute intermediate to bottom because yield holds execution state
# data.send("Alok")
# data.send(input())
# print("Done")


"""
What is Coroutine?
-->> Coroutine is a function which used to pause the execution at yield and later resume from same point when it is reached
Why do needs Coroutine?
--> It needs to handle long running task effectively.
--> It avoid blocking entire program. 
--> preform work in step by step instead of at once. 

> In working context: It use basically, in large and complex project
""" 

# def sample():
#     # Suppose read a file to check does the input name of file exist or not
#     with open("Diet.log")as f:
#         files = f.read()
#     while True:
#         file = yield  #pause point (preserved the execution state) when send value it start/resume from same point
#         if file in files:
#             print("Exist")
#         else:
#             print("Not exist")


# s = sample() #return generator object( No print yet )
# next(s) #stats execution
# s.send("Aalok") 
# s.send("Harry")



# In python, Coroutine is use to pause the execution at specific point and resume same point when it is reached
# it contains yield, async/await syntax. (Generator based) (pause/resume)


# Asynchronous in short async means non-blocking execution,
# Where a task may pauses while waiting for finish,
# allowing other task executes from the same point.
""" 
Asynchronous -> Non-blocking execution or Concurrent execution (Concurrent means in CS happening at the same time but simantaneously).
Async I/O is a powerful programming pattern that allows for high-performance and concurrent I/O operations in Python.
With the asyncio module and asynchronous functions, you can write efficient and scalable
code that can handle large amounts of data and I/O operations without blocking the main thread.
Whether you're working on web applications, network services, or data processing pipelines, async IO is an essential tool for any Python developer.
"""

# import asyncio
# async def sample1():
#     print("Starting point...")
#     await asyncio.sleep(2)
#     print("To Pythoic World")

# async def sample2():
#     print("Welcome")
#     await asyncio.sleep(1)

# async def main():
#     # task = asyncio.create_task(sample1())
#     # await task  #await -->  non-blocking execution
#     # await asyncio.sleep(2)
    
#     # await sample1()
#     # await sample2()
#     await asyncio.gather(
#                 sample1(),
#                 sample2(),                
#             )
    
# asyncio.run(main())



# import requests
# import asyncio
# # For image
# async def download_image1():
#     print("Start downloading_1...")
    
#     url = ("https://img.freepik.com/free-vector/laptop-with-program-code-isometric-icon-software-development-programming-applications-dark-neon_39422-971.jpg")
    
#     response = requests.get(url)
  
#     with open("4K_Image1.jpg", 'wb')as f: 
#         f.write(response.content)
    
#     print("Download finished1")
    

# async def download_image2():
#     await asyncio.sleep(3)
#     print("Start downloading_2...")
    
#     url = ("https://i.pinimg.com/736x/36/35/c6/3635c64646cb17f59993b1102188cbde.jpg")
    
#     response = requests.get(url)
#     # open("4K_Image2.jpg", "wb").write(response.content)
#     with open("4K_Image2.jpg", 'wb')as f: 
#         f.write(response.content)
#     print("Download finished2")
    
# async def main():
#     # await download_image1()
#     # await download_image2()
#     # return
#     await asyncio.gather(
#         download_image2(),
#         download_image1(),
#     )

# asyncio.run(main())


# For audio
# import yt_dlp

# URL of video
# url = "https://www.youtube.com/watch?v=tm9GpM3lV3s"

# # Audio format and download file name defined
# audio_format = {
#     "outtmpl": "Phonk_Music.%(ext)s",
#     "format": "bestaudio/best",
#     "postprocessors": [{
#         'key': 'FFmpegExtractAudio',
#         'preferredcodec': 'mp3',
#         'preferredquality':'200'
#     }]
# }
# # Start download
# with yt_dlp.YoutubeDL(audio_format)as music:
#     music.download([url])

# print("Download completed.")

# This example of Synchronous
# import yt_dlp
# import asyncio

# async def download_music_1():
#     # URL of video
#     await asyncio.sleep(3)
#     url = "https://www.youtube.com/watch?v=Oqwx7JQxnRY"

#     # Audio format and download file name defined
#     audio_format = {
#         "outtmpl": "Phonk_Music1.%(ext)s",
#         "format": "bestaudio/best",
#         "postprocessors": [{
#             'key': 'FFmpegExtractAudio',
#             'preferredcodec': 'mp3',
#             'preferredquality':'200'
#         }]
#     }

#     # Start download
#     with yt_dlp.YoutubeDL(audio_format)as music:
#         music.download([url])
#     print("1. Download completed")

# async def download_music_2():
#     # URL of video
#     url = "https://www.youtube.com/watch?v=0B_5moouO_U"

#     # Audio format and download file name defined
#     audio_format = {
#         "outtmpl": "Shree_Ram.%(ext)s",
#         "format": "bestaudio/best",
#         "postprocessors": [{
#             'key': 'FFmpegExtractAudio',
#             'preferredcodec': 'mp3',
#             'preferredquality':'200'
#         }]
#     }

#     # Start download
#     with yt_dlp.YoutubeDL(audio_format)as music:
#         music.download([url])
#     print("2. Download completed")

# async def start_download():
#     await asyncio.gather(
#         download_music_1(),
#         download_music_2()
#     )
    
    
#     print("\nDownload successfully completed.")

# asyncio.run(start_download())


# Asynchronous
import yt_dlp
import asyncio
from concurrent.futures import ThreadPoolExecutor

# A thread is a lightweight unit of execution inside a program.
#Python ->> run_in_executor 
# ->>function reference + args --> 
# Thread picks up -->
# Thread calls : download(url, filename)

# download -> function object
# Both args passes separately url and filename
# Thread calls with take it

# def download(url, filename):
#     audio_format = {
#         "outtmpl": f"{filename}.%(ext)s",
#         "format": "bestaudio/best",
#          "postprocessors": [{
#             'key': 'FFmpegExtractAudio',
#             'preferredcodec': 'mp3',
#             'preferredquality':'200'
#         }]
#     }
    
#     with yt_dlp.YoutubeDL(audio_format)as music:
#         music.download([url])
#     print(f"{filename} download completed.")

# async def download_music():
#     loop = asyncio.get_event_loop()
    
#     with ThreadPoolExecutor(max_workers=2) as executor:
#         tasks = [
#             loop.run_in_executor(
#                 executor,
                # download,   #function object
#                 "https://www.youtube.com/watch?v=Oqwx7JQxnRY",  #arg1
#                 "Phonk" #arg2
#             ),
#             loop.run_in_executor(
#                 executor,
#                 download,     #function object
#                 "https://www.youtube.com/watch?v=0B_5moouO_U",    #arg1
#                 "Shree_Ram"   #arg2
#             ),
            
#         ]
        
#         await asyncio.gather(*tasks)
#     print("\nDownload completed.")
    
# asyncio.run(download_music())