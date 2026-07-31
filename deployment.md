# Hướng Dẫn Triển Khai Locket Gold Bot (Deployment Guide)

Tài liệu này hướng dẫn chi tiết cách để deploy (triển khai) Bot Locket Gold lên một máy chủ (VPS) như Ubuntu hoặc CentOS để bot có thể hoạt động liên tục 24/7.

## Yêu cầu hệ thống (Prerequisites)
- **Hệ điều hành**: Linux (Khuyên dùng Ubuntu 20.04 hoặc 22.04)
- **Phần mềm**: Python 3.8+ (khuyên dùng 3.10+), `pip`, `git`, và `screen` (hoặc `tmux`/`systemd`)
- **Tài khoản**: Đã có sẵn Bot Token (từ @BotFather) và danh sách Token Apple (để bypass).

---

## Bước 1: Cập nhật hệ thống và Cài đặt Python
Kết nối SSH vào VPS của bạn và chạy lệnh sau để cài đặt các công cụ cơ bản:

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install python3 python3-pip python3-venv git screen -y
```

## Bước 2: Tải mã nguồn về máy chủ
Clone (tải) kho lưu trữ của bạn về VPS:

```bash
git clone https://github.com/your-username/Locket-Gold.git
cd Locket-Gold
```
*(Thay thế URL trên bằng link Github thực tế của bạn nếu bạn để private).*

## Bước 3: Cài đặt môi trường Ảo (Virtual Environment)
Cài đặt các thư viện cần thiết độc lập trong môi trường ảo để không bị xung đột với hệ thống:

```bash
# Tạo môi trường ảo
python3 -m venv venv

# Kích hoạt môi trường ảo
source venv/bin/activate

# Cài đặt thư viện từ requirements
pip install -r requirements.txt
```

## Bước 4: Cấu hình hệ thống (File .env)
Sao chép file cấu hình mẫu và điền thông tin của bạn vào:

```bash
cp .env.example .env
nano .env
```
Cấu hình các thông số sau trong trình chỉnh sửa `nano`:
- `BOT_TOKEN`: Điền Token của Telegram Bot.
- `ADMIN_ID`: Điền ID Telegram của bạn (để dùng lệnh Admin không giới hạn).
- `MAX_USERS`: Giới hạn số lượng Tester (Điền `0` để không giới hạn).
- `NEXTDNS_KEY` & `NEXTDNS_ENABLED`: Để trống hoặc setup nếu dùng NextDNS.
- `TOKEN_SETS_JSON`: Điền cấu trúc JSON chứa các token bypass Locket (Có thể cấu hình bao nhiêu Token tuỳ thích, bot sẽ tự động chia đều tải trọng).

Bấm `Ctrl + X`, sau đó nhấn `Y` và `Enter` để lưu lại.

## Bước 5: Chạy Bot 24/7 với Screen
Sử dụng công cụ `screen` để tạo một phiên làm việc chạy ngầm, giúp bot không bị tắt khi bạn tắt máy tính.

```bash
# Tạo một screen mới tên là locket-bot
screen -S locket-bot

# Khởi chạy bot bằng file bash có sẵn (sẽ tự động activate venv và chạy main.py)
chmod +x run.sh
./run.sh
```

- Nếu bot báo **"Bot is running..."**, hệ thống đã hoạt động thành công!
- Để thoát ra khỏi màn hình screen (ẩn bot xuống nền chạy 24/7): **Bấm tổ hợp phím `Ctrl + A` sau đó bấm phím `D`**.

### Lệnh hữu ích với Screen:
- Mở lại màn hình bot để xem log: `screen -r locket-bot`
- Tắt hoàn toàn bot: Vào trong screen, bấm `Ctrl + C`.

---

## Quản trị viên (Admin)
Mở Telegram, truy cập vào Bot của bạn và bấm `/start`. Các lệnh Admin sẽ được hiện lên vì bạn đã điền `ADMIN_ID`:
- `/stats` - Xem tổng số user, số truy vấn và tỷ lệ thành công.
- `/noti [nội dung]` - Gửi tin nhắn Broadcast (thông báo) đến toàn bộ những người đang dùng bot.
- `/setdonate` - Trả lời một bức ảnh với lệnh này để đổi ảnh khi bot gửi thông báo kích hoạt thành công.
- `/rs [id]` - Reset lại số lượt dùng (giới hạn 5 lần/ngày) cho 1 user nào đó.

Chúc bạn triển khai thành công! 🚀
