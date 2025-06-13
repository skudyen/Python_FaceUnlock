วิธีการใช้งาน

1.Download https://visualstudio.microsoft.com/visual-cpp-build-tools
  เลือก "Download Build Tools"
  ในหน้าติดตั้งให้ติ๊ก:
    Desktop development with C++ ✅
      -MSVC v143 ✅
      -Windows 11 SDK ✅
      -C++ CMake tools ✅
      -C++ build tools core features ✅

2.Download Git https://git-scm.com/downloads

3.ทำการ Git Clone โดยเปิด Terminal
  รัน git clone 

4.จากนั้นเข้าไปใน Folder ที่ Clone มารัน .\setup.bat

5.เมิ้อติดตั้ง Lib เสร็จให้รัน .\venv\Scripts\activate.bat

6.ถ้า lib ติดตั้งไม่สำเร็จลอง .\venv\Scripts\activate.bat แล้วติดตั้ง lib แบบ manual

  รัน pip install ultralytics insightface onnxruntime opencv-python numpy
7.ให้ทำการสร้าง Folder เปล่า weights และ data 
  โดยโหลด https://drive.google.com/drive/folders/10rvqs55VgQZqcP0v5W6xElDyUAPNyCFu?usp=sharing แล้วนำไฟล์ .pt ไปใ่ส่ใน Folder weigths
  ส่วน Folder data ปล่อยว่างไว้

8.รันโปรแกรม python .\main.py

Etc ...
Folder must be like this:

![image_alt]()
