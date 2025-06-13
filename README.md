วิธีการใช้งาน

1.Download https://visualstudio.microsoft.com/visual-cpp-build-tools<br>
&nbsp;-เลือก "Download Build Tools"<br>
&nbsp;-ในหน้าติดตั้งให้ติ๊ก:<br>
&nbsp;&nbsp;-Desktop development with C++ ✅\n<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-MSVC v143 ✅<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-Windows 11 SDK ✅<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-C++ CMake tools ✅<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-C++ build tools core features ✅<br>

2.Download Git https://git-scm.com/downloads

3.ทำการ Git Clone โดยเปิด Terminal<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;รัน git clone 

4.จากนั้นเข้าไปใน Folder ที่ Clone มารัน .\setup.bat <br>

5.เมิ้อติดตั้ง Lib เสร็จให้รัน .\venv\Scripts\activate.bat <br>

6.ถ้า lib ติดตั้งไม่สำเร็จลอง .\venv\Scripts\activate.bat แล้วติดตั้ง lib แบบ manual <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;รัน pip install ultralytics insightface onnxruntime opencv-python numpy <br>
7.ให้ทำการสร้าง Folder เปล่า weights และ data <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;โดยโหลด https://drive.google.com/drive/folders/10rvqs55VgQZqcP0v5W6xElDyUAPNyCFu?usp=sharing แล้วนำไฟล์ .pt ไปใ่ส่ใน Folder weigths <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ส่วน Folder data ปล่อยว่างไว้

8.รันโปรแกรม python .\main.py <br>

Etc ...
Folder must be like this:

![image_alt]()
