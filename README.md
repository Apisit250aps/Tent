# Tent

## ตารางข้อมูลหลัก

- รถ: เก็บข้อมูลเกี่ยวกับรถ เช่น ยี่ห้อ รุ่น ปี เลขไมล์ สี สภาพ ราคา รูปภาพ สถานะ (เตรียมขาย จอง ขายแล้ว)
- ลูกค้า: เก็บข้อมูลเกี่ยวกับลูกค้า เช่น ชื่อ เบอร์โทร ที่อยู่ อีเมล ข้อมูลเครดิต
- พนักงาน: เก็บข้อมูลเกี่ยวกับพนักงาน เช่น ชื่อ เบอร์โทร ตำแหน่ง
- การจอง: เก็บข้อมูลเกี่ยวกับการจองรถ เช่น ลูกค้า รถ วันที่จอง เงินมัดจำ สถานะ (จอง รอชำระ ยกเลิก)
- ไฟแนนซ์: เก็บข้อมูลเกี่ยวกับการจัดไฟแนนซ์ เช่น ลูกค้า ยอดจัด ยอดผ่อน ระยะเวลา สถานะ (รออนุมัติ อนุมัติ ปฏิเสธ)
- การขาย: เก็บข้อมูลเกี่ยวกับการขายรถ เช่น ลูกค้า รถ ราคา รูปแบบการชำระ สถานะ (รอชำระ ชำระแล้ว)

## ความสัมพันธ์ระหว่างตาราง
- รถ:
   - มีความสัมพันธ์แบบ 1:N กับตาราง การจอง
   - มีความสัมพันธ์แบบ 1:N กับตาราง การขาย
- ลูกค้า:
   - มีความสัมพันธ์แบบ 1:N กับตาราง การจอง
   - มีความสัมพันธ์แบบ 1:N กับตาราง ไฟแนนซ์
   - มีความสัมพันธ์แบบ 1:N กับตาราง การขาย
- พนักงาน:
   - มีความสัมพันธ์แบบ 1:N กับตาราง การขาย
- การจอง:
   - มีความสัมพันธ์แบบ 1:1 กับตาราง ไฟแนนซ์ (รถบางคันอาจไม่ใช้ไฟแนนซ์)
- การขาย:
   - มีความสัมพันธ์แบบ 0:N กับตาราง ไฟแนนซ์ (รถบางคันอาจไม่ใช้ไฟแนนซ์)
  

## ฟังก์ชันการทำงาน
- จัดการสต็อกรถ:
    - เพิ่ม/แก้ไข/ลบ ข้อมูลรถ
    - ค้นหารถตามยี่ห้อ รุ่น ปี เลขไมล์ สี สภาพ ราคา สถานะ
    - แสดงรายการรถ
    - แสดงรายการรถที่ใกล้ถึงกำหนดเข้าตรวจเช็ค
- จัดการการจองรถ:
    - เพิ่ม/แก้ไข/ลบ ข้อมูลการจอง
    - ค้นหาการจองตามลูกค้า รถ วันที่จอง สถานะ
    - แสดงรายการรถที่ถูกจอง
    - แจ้งเตือนลูกค้าเมื่อถึงกำหนดจอง
- จัดการการจัดไฟแนนซ์:
    - เพิ่ม/แก้ไข/ลบ ข้อมูลการจัดไฟแนนซ์
    - ค้นหาข้อมูลการจัดไฟแนนซ์ตามลูกค้า ยอดจัด ยอดผ่อน ระยะเวลา สถานะ
    - แสดงรายการการจัดไฟแนนซ์ที่รออนุมัติ
    - แจ้งเตือนลูกค้าเมื่อสถานะการจัดไฟแนนซ์มีการเปลี่ยนแปลง
- จัดการการอนุมัติของแถม ส่วนลด:
    - กำหนดเงื่อนไข ระยะเวลา ของส่วนลด ของแถม
    - อนุมัติส่วนลด ของแถม ให้กับลูกค้า
- จัดการการขายรถ:
    - เพิ่ม/แก้ไข/ลบ ข้อมูลการขาย
    - ค้นหาข้อมูลการขายตามลูกค้า รถ ราคา รูปแบบการชำระ สถานะ
    - ออกใบเสร็จ/ใบกำกับภาษี
    - แสดงรายงานการขาย
  
