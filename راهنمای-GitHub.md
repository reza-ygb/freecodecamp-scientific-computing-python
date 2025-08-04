# فایل آماده‌سازی GitHub

## مراحل نصب Git و آپلود پروژه

### مرحله 1: نصب Git
دو راه برای نصب Git:
1. از لینک بالا دانلود کنید و نصب کنید
2. یا منتظر بمانید تا Chocolatey نصب شود و بعد دستور زیر را اجرا کنید:

```powershell
choco install git -y
```

### مرحله 2: تنظیم Git
بعد از نصب Git:

```bash
git config --global user.name "اسم شما"
git config --global user.email "your-email@example.com"
```

### مرحله 3: ساخت Repository در GitHub
1. برو به GitHub.com
2. روی + کلیک کن و New repository انتخاب کن
3. نام: `freecodecamp-scientific-computing-python`
4. توضیحات: `My solutions for FreeCodeCamp Scientific Computing with Python`
5. Public انتخاب کن
6. README اضافه نکن (چون خودمون داریم)
7. Create repository کلیک کن

### مرحله 4: آپلود کردن
دستورات زیر را در ترمینال اجرا کن:

```bash
cd "r:\freecodecamp\projrct1"
git init
git add .
git commit -m "🎉 Initial commit: Arithmetic Formatter project

✨ Features:
- Professional arithmetic problem formatter
- Comprehensive input validation
- Clean code with documentation
- Part 1 of 5 FreeCodeCamp projects

📚 FreeCodeCamp Scientific Computing with Python certification"

git branch -M main
git remote add origin https://github.com/USERNAME/freecodecamp-scientific-computing-python.git
git push -u origin main
```

### آماده است! 🚀
همه چیز آماده شده:
- کد حرفه‌ای و تمیز ✅
- مستندات کامل ✅  
- ساختار پروژه ✅
- LICENSE ✅
- README های جامع ✅

فقط Git نصب کن و دستورات بالا را اجرا کن!
