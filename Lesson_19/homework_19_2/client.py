import requests

image_path = '/Users/serhii.ravliuk/PycharmProjects/Lesson_2_1/Lesson_19/homework_19_2/mars_photo1.jpg'

def upload_image(image_path):
    url = 'http://127.0.0.1:8080/upload'
    with open(image_path, 'rb') as image_file:
        files = {'image': image_file}
        response = requests.post(url, files=files)
        if response.status_code == 201:
            return response.json()['image_url']
        else:
            print("Error uploading image:", response.text)
            return None

def get_image(image_filename):
    url = f'http://127.0.0.1:8080/image/{image_filename}'
    headers = {'Content-Type': 'image'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        print("Image retrieved successfully.")
        with open(image_filename, 'wb') as f:
            f.write(response.content)
        print(f"Image saved as {image_filename}.")
    else:
        print("Error retrieving image:", response.text)

def delete_image(image_filename):
    url = f'http://127.0.0.1:8080/delete/{image_filename}'
    response = requests.delete(url)
    if response.status_code == 200:
        print("Image deleted successfully.")
    else:
        print("Error deleting image:", response.text)

if __name__ == '__main__':
    image_url = upload_image(image_path)
    if image_url:
        print("Uploaded image URL:", image_url)
        filename = image_url.split('/')[-1]

        get_image(filename)

        delete_image(filename)
