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

{'photos': [{'id': 102693, 'sol': 1000, 'camera': {'id': 20, 'name': 'FHAZ', 'rover_id': 5, 'full_name': 'Front Hazard Avoidance Camera'}, 'img_src': 'http://mars.jpl.nasa.gov/msl-raw-images/proj/msl/redops/ods/surface/sol/01000/opgs/edr/fcam/FLB_486265257EDR_F0481570FHAZ00323M_.JPG', 'earth_date': '2015-05-30', 'rover': {'id': 5, 'name': 'Curiosity', 'landing_date': '2012-08-06', 'launch_date': '2011-11-26', 'status': 'active', 'max_sol': 4102, 'max_date': '2024-02-19', 'total_photos': 695670, 'cameras': [{'name': 'FHAZ', 'full_name': 'Front Hazard Avoidance Camera'}, {'name': 'NAVCAM', 'full_name': 'Navigation Camera'}, {'name': 'MAST', 'full_name': 'Mast Camera'}, {'name': 'CHEMCAM', 'full_name': 'Chemistry and Camera Complex'}, {'name': 'MAHLI', 'full_name': 'Mars Hand Lens Imager'}, {'name': 'MARDI', 'full_name': 'Mars Descent Imager'}, {'name': 'RHAZ', 'full_name': 'Rear Hazard Avoidance Camera'}]}}, {'id': 102694, 'sol': 1000, 'camera': {'id': 20, 'name': 'FHAZ', 'rover_id': 5, 'full_name': 'Front Hazard Avoidance Camera'}, 'img_src': 'http://mars.jpl.nasa.gov/msl-raw-images/proj/msl/redops/ods/surface/sol/01000/opgs/edr/fcam/FRB_486265257EDR_F0481570FHAZ00323M_.JPG', 'earth_date': '2015-05-30', 'rover': {'id': 5, 'name': 'Curiosity', 'landing_date': '2012-08-06', 'launch_date': '2011-11-26', 'status': 'active', 'max_sol': 4102, 'max_date': '2024-02-19', 'total_photos': 695670, 'cameras': [{'name': 'FHAZ', 'full_name': 'Front Hazard Avoidance Camera'}, {'name': 'NAVCAM', 'full_name': 'Navigation Camera'}, {'name': 'MAST', 'full_name': 'Mast Camera'}, {'name': 'CHEMCAM', 'full_name': 'Chemistry and Camera Complex'}, {'name': 'MAHLI', 'full_name': 'Mars Hand Lens Imager'}, {'name': 'MARDI', 'full_name': 'Mars Descent Imager'}, {'name': 'RHAZ', 'full_name': 'Rear Hazard Avoidance Camera'}]}}]}
