import requests
import concurrent.futures
import time


my_urls = [
    'https://images.unsplash.com/photo-1516117172878-fd2c41f4a759',
    'https://images.unsplash.com/photo-1532009324734-20a7a5813719',
    'https://images.unsplash.com/photo-1524429656589-6633a470097c',
]


def download_image(url):
    local_filename = url.split('/')[-1]
    print(f'Image {local_filename} is downloading.')
    r = requests.get(url)
    with open(local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:  # filter out keep-alive new chunks
                f.write(chunk)
    return f'Image {local_filename} has been downloaded.'


start = time.perf_counter()

with concurrent.futures.ThreadPoolExecutor() as executor:
    results = executor.map(download_image, my_urls)

    for result in results:
        print(result)


finish = time.perf_counter()

print(f'Finished in {round(finish - start, 2)} seconds.')

