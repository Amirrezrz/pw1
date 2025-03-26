# راهنمای مهاجر | Persian Migrant Guide

🌍 یک وب‌سایت فارسی برای مهاجرین در ایتالیا و اروپا. امکانات سایت شامل راهنمایی، ثبت‌نام کاربران، ارسال آگهی اجاره و بارگذاری تصویر می‌باشد.

---

## 📦 ویژگی‌ها

- ثبت‌نام و ورود کاربران
- داشبورد شخصی برای مدیریت آگهی‌ها
- فرم ارسال آگهی اجاره با امکان بارگذاری تصویر
- طراحی راست‌چین (RTL) با Tailwind CSS
- پشتیبانی از زبان فارسی و فونت مناسب
- استفاده از پایگاه داده SQLite

---

## 🛠 مراحل نصب و اجرا

### 1. دانلود و استخراج پروژه

```bash
unzip persian_guide_with_images.zip
cd persian_guide_with_images
```

### 2. ساخت محیط مجازی

```bash
python -m venv env
env\Scripts\activate  # ویندوز
# یا
source env/bin/activate  # لینوکس / مک
```

### 3. نصب وابستگی‌ها

```bash
pip install django
```

### 4. اعمال مایگریشن و ساخت دیتابیس

```bash
python manage.py migrate
```

### 5. ساخت ادمین (اختیاری)

```bash
python manage.py createsuperuser
```

### 6. اجرای سرور

```bash
python manage.py runserver
```

سپس مرورگر را باز کنید:

📍 http://127.0.0.1:8000/

---

## 🧩 ساختار پروژه

```
persian_guide_with_images/
│
├── manage.py                  # فایل اصلی اجرای پروژه
├── db.sqlite3                 # پایگاه داده SQLite
├── mysite/                    # تنظیمات پروژه
│   └── settings.py            # تنظیمات اصلی Django
│
├── main/                      # اپلیکیشن اصلی پروژه
│   ├── models.py              # مدل‌ها (آگهی‌ها)
│   ├── forms.py               # فرم ثبت آگهی
│   ├── views.py               # کنترلرها
│   ├── urls.py                # آدرس‌های URL
│   └── templates/             # قالب‌های HTML
│       ├── base.html          # قالب پایه
│       ├── main/              # صفحات داخلی
│       └── registration/      # ورود و ثبت‌نام
│
└── media/                     # محل ذخیره عکس‌های آپلودی (پس از اجرا ساخته می‌شود)
```

---

## 🖼 بارگذاری عکس

- تصاویر آگهی‌ها در پوشه `media/rent_images/` ذخیره می‌شوند.
- آدرس دهی خودکار در حالت توسعه (`DEBUG = True`) فعال است.

---

✨ طراحی و توسعه با عشق برای مهاجرین
