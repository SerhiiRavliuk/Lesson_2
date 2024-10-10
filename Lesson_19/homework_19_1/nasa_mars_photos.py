import requests

url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'
params = {'sol': 1000, 'camera': 'fhaz', 'api_key': 'DEMO_KEY'}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    if 'photos' in data:
        photos = data['photos']
        for index, photo in enumerate(photos):
            photo_url = photo['img_src']
            img_response = requests.get(photo_url)
            if img_response.status_code == 200:
                file_name = f'mars_photo{index + 1}.jpg'
                with open(file_name, 'wb') as img_file:
                    img_file.write(img_response.content)
                print(f'Збережено: {file_name}')
            else:
                print(f'Помилка при скачуванні: {photo_url}')
    else:
        print('Фото не знайдені.')
else:
    print('Помилка при отриманні даних:', response.status_code)
