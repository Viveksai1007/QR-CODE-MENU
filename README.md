# 🍽️ Digital Restaurant Menu QR Code Generator

A simple Django web application that allows restaurant owners to generate a QR code for their digital menu URL.  
The generated QR code can be downloaded and used for contactless dining.

---

## 🚀 Project Overview

This project allows users to:

- Enter a **Restaurant Name**
- Enter a **Menu URL**
- Generate a **QR Code**
- View the QR Code on a result page
- Download the QR Code image

The QR code is generated dynamically and saved inside the `media/` directory.

---

## 🛠️ Technologies Used

- Python  
- Django  
- Bootstrap 5  
- qrcode Python library  
- HTML5  
- CSS3  

---


## 📂 Project Structure

```
qr_project/
│
├── qr_app/
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   └── templates/
│       ├── generate_qr_code.html
│       └── qr_result.html
│
├── media/
├── settings.py
└── manage.py
```

---

## ⚙️ How It Works (Step-by-Step Explanation)

### 1️⃣ User Input Form

The user fills out a form containing:

- Restaurant Name  
- Menu URL  

This form is created using Django Forms (`forms.py`).

```python
class QRCodeForm(forms.Form):
    restaurant_name = forms.CharField(...)
    url = forms.URLField(...)
```

---
## 2️⃣ Form Submission

When the user submits the form:

```python
if request.method == 'POST':
    form = QRCodeForm(request.POST)
```

Django validates the form using:

```python
if form.is_valid():
```

---

## 3️⃣ QR Code Generation

The QR code is generated using the `qrcode` Python library:

```python
qr = qrcode.make(url)
```

The file name is created dynamically using the restaurant name:

```python
file_name = restaurant_name.replace(" ", "_").lower() + '_menu.png'
```

---

## 4️⃣ Saving QR Code

The image is saved inside the `media/` folder:

```python
file_path = os.path.join(settings.MEDIA_ROOT, file_name)
qr.save(file_path)
```

---

## 5️⃣ Displaying QR Code

The QR image is displayed on the result page using:

```html
<img src="{{ qr_url }}" alt="qr_code">
```

A download button is also provided:

```html
<a href="{{ qr_url }}" download="{{ file_name }}">
```

---

# 🖥️ Setup Instructions (How to Run This Project)

## Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/your-repo-name.git
```

---

## Step 2: Navigate to Project Folder

```bash
cd your-repo-name
```

---

## Step 3: Create Virtual Environment

```bash
python -m venv env
```

### Activate the Environment

**Windows:**

```bash
env\Scripts\activate
```

**Mac/Linux:**

```bash
source env/bin/activate
```

---

## Step 4: Install Dependencies

```bash
pip install django
pip install qrcode
pip install pillow
```

### Or Create a requirements.txt File

```bash
pip freeze > requirements.txt
```

Install using:

```bash
pip install -r requirements.txt
```

---

## Step 5: Configure MEDIA Settings

Add this in `settings.py`:

```python
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

---

## Step 6: Run Server

```bash
python manage.py runserver
```

Open in your browser:

```
http://127.0.0.1:8000/
```

---

# 📸 Features

- ✅ Simple UI using Bootstrap  
- ✅ Dynamic QR Code Generation  
- ✅ Download QR Code Option  
- ✅ Clean and Beginner-Friendly Django Project  
- ✅ Media File Handling  

---

# 🔮 Future Improvements

- Add logo inside QR code  
- Add QR code customization (color, size)  
- Store generated QR codes in database  
- Add user authentication  
- Deploy to cloud (Render / Railway / PythonAnywhere)  

---

# 🎯 Learning Outcomes

Through this project, I learned:

- Django Form Handling  
- Media File Management  
- Working with Third-Party Libraries  
- Dynamic File Generation  
- Bootstrap Integration  
- URL Routing in Django  

---

# 👨‍💻 Author

**Vivek Sai**

If you like this project, feel free to ⭐ the repository!

