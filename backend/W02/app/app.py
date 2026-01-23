import pickle # thư viện chuyển đổi đối tượng python thành dạng nhị phân để lưu xuống ô cứng và ngược lại
import os # thư viên kiểm tra file có tồn tại hay không

FILE_NAME = "data.pkl" # định nghĩa tên file để lưu 
menu = {} # khởi tạo biến dictionary rỗng

# danh sách loại món cố định để chọn số cho nhanh
# thay vì gõ tay, tránh sai chính tả
DS_LOAI = ["Khai vị", "Món chính", "Tráng miệng", "Đồ uống"]

# --- 1. QUẢN LÝ FILE ---
def load_data():
    global menu # báo cho python biết tôi muốn sửa biển menu toàn cục ở ngoài
    if os.path.exists(FILE_NAME): # kiểm tra data.pkl có trên máy chưa
        try:
            with open(FILE_NAME, "rb") as f: # mở file chế độ đọc dạng nhị phân
                menu = pickle.load(f) # đọc dự liệu file chuyển thành dictionary và gán vào biến menu
        except: menu = {} # phòng rủi ro, nếu ko đọc được chương trình ko bị crash mà tạo menu rỗng
    else: menu = {}

def save_data():
    with open(FILE_NAME, "wb") as f: # mở file để ghi
        pickle.dump(menu, f) # đóng gói menu và lưu xuống file f
    print(">> Đã lưu dữ liệu thành công!")

# --- 2. HÀM HỖ TRỢ (GIÚP CHỌN SỐ) ---
def chon_mon_theo_so():
    #In danh sách món và trả về tên món người dùng chọn
    if not menu: # nếu menu rỗng
        print(">> Menu trống!")
        return None
    
    keys = list(menu.keys()) # lấy toàn bộ tên món đưa vào list
    print("\n--- DANH SÁCH MÓN ---")
    for i, ten in enumerate(keys, 1): # giúp đánh số thứ tự bắt đầu từ 1
        print(f"{i}. {ten}")
    
    try:
        idx = int(input(">> Nhập số thứ tự món: ")) - 1 # người dùng thấy menu bắt đầu từ 1 mà máy tính đếm từ 0 nên trừ đi 1
        if 0 <= idx < len(keys):
            return keys[idx] # trả về tên món 
        else:
            print(">> Số không hợp lệ!")
            return None
    except ValueError:
        print(">> Phải nhập số!")
        return None

# --- 3. CÁC CHỨC NĂNG CHÍNH ---
def them_mon():
    print("\n--thêm món mới")
    ten = input("Nhập tên món: ")
    try:
        gia = float(input("Nhập giá: "))
    except:
        print(">> Giá phải là số!"); return

    # chọn loại theo số
    print("Chọn loại:")
    for i, loai in enumerate(DS_LOAI, 1): print(f"{i}. {loai}")
    try:
        chon_l = int(input(">> Nhập số loại: ")) - 1
        loai = DS_LOAI[chon_l] if 0 <= chon_l < 4 else "Khác" # lấy loại món từ danh sách dựa trên số người dùng chọn
    except: loai = "Khác"

    nl = input("Nhập nguyên liệu (cách nhau dấu phẩy): ").split(",") # cắt chuỗi tạo thành danh sách
    
    #tạo mục mới trong dictionary, dict lồng nhau
    menu[ten] = {    
        "gia": gia, "loai": loai, 
        "nguyen_lieu": [x.strip() for x in nl], # xóa khoảng trắng thừa
        "trang_thai": "Còn hàng"
    }
    print(">> Đã thêm xong!")

def xem_menu():
    print("\n---xem menu")
    if not menu: print("Menu trống."); return
    
    for i, (ten, v) in enumerate(menu.items(), 1): # duyệt qua từng món trong menu
        print(f"{i}. Tên món: {ten}")
        print(f"   Giá: {v['gia']:,.0f}đ")
        print(f"   Loại: {v['loai']}")
        print(f"   Trạng thái: {v['trang_thai']}")
        # join giúp nối list nguyên liệu thành chuỗi string
        print(f"   Nguyên liệu: {', '.join(v['nguyen_lieu'])}")
        print("-" * 30)

def cap_nhat_mon():
    print("\n---cập nhật món")
    ten = chon_mon_theo_so() # gọi hàm chọn số
    if not ten: return

    print("Bạn muốn sửa gì?")
    print("1. Giá | 2. Loại | 3. Nguyên liệu")
    chon = input(">> Chọn (1-3): ")

    if chon == '1':
        menu[ten]['gia'] = float(input("Nhập giá mới: "))
    elif chon == '2':
        # chọn loại lại theo số
        for i, loai in enumerate(DS_LOAI, 1): print(f"{i}. {loai}")
        c = int(input(">> Chọn loại mới: ")) - 1
        menu[ten]['loai'] = DS_LOAI[c]
    elif chon == '3':
        nl = input("Nhập nguyên liệu mới (cách dấu phẩy): ").split(",")
        menu[ten]['nguyen_lieu'] = [x.strip() for x in nl]
    
    print(">> Cập nhật thành công!")

def xoa_mon():
    print("\n--- XÓA MÓN ---")
    ten = chon_mon_theo_so()
    if ten:
        del menu[ten]
        print(">> Đã xóa món này!")

def loc_theo_loai():
    print("\n--- LỌC MÓN ---")
    # chọn loại cần lọc theo số
    for i, loai in enumerate(DS_LOAI, 1): print(f"{i}. {loai}")
    try:
        c = int(input(">> Muốn xem loại nào (nhập số): ")) - 1
        can_tim = DS_LOAI[c]
        
        found = False
        for ten, v in menu.items():
            if v['loai'] == can_tim:
                print(f"- {ten}: {v['gia']:,.0f}đ ({v['trang_thai']})")
                found = True
        if not found: print(">> Không có món nào thuộc loại này.")
    except: print(">> Nhập sai số!")

def tim_nguyen_lieu():
    tk = input("\nNhập tên nguyên liệu cần tìm: ").lower() # chuyển về chữ thường
    found = False
    for ten, v in menu.items():
        # kiểm tra từng nguyên liệu trong danh sách
        ds_nl_thuong = [x.lower() for x in v['nguyen_lieu']]
        if tk in ds_nl_thuong:
            print(f"- {ten} (có chứa {tk})")
            found = True
    if not found: print(">> Không tìm thấy.")

def doi_trang_thai():
    print("\n--- ĐỔI TRẠNG THÁI ---")
    ten = chon_mon_theo_so()
    if ten:
        print(f"Món: {ten} (Hiện tại: {menu[ten]['trang_thai']})")
        print("1. Còn hàng | 2. Hết hàng")
        c = input(">> Chọn trạng thái mới (1/2): ")
        if c == '1': menu[ten]['trang_thai'] = "Còn hàng"
        elif c == '2': menu[ten]['trang_thai'] = "Hết hàng"
        print(">> Đã đổi trạng thái!")

# --- 4. CHƯƠNG TRÌNH CHÍNH ---
load_data() #chạy chương trình để tải dữ liệu cũ lên

while True: # vòng lặp vô tận
    print("\n=== QUẢN LÝ QUÁN ĂN ===")
    print("1. Thêm món")
    print("2. Xem menu")
    print("3. Cập nhật món (Giá/Loại/Nguyên liệu)")
    print("4. Xóa món")
    print("5. Lọc theo loại")
    print("6. Tìm theo nguyên liệu")
    print("7. Đổi trạng thái (Còn/Hết)")
    print("8. Lưu & Thoát")
    
    chon = input(">> Mời chọn chức năng (1-8): ")
    
    if chon == '1': them_mon()
    elif chon == '2': xem_menu()
    elif chon == '3': cap_nhat_mon()
    elif chon == '4': xoa_mon()
    elif chon == '5': loc_theo_loai()
    elif chon == '6': tim_nguyen_lieu()
    elif chon == '7': doi_trang_thai()
    elif chon == '8': save_data(); break # thoát vòng lặp, lưu, kết thúc chương trình
    else: print(">> Chọn sai, vui lòng nhập lại!")