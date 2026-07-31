import json
import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
NEXTDNS_KEY = os.environ.get("NEXTDNS_KEY", "")
# NextDNS is enabled by default only when an API key is configured.
# Set NEXTDNS_ENABLED=false to explicitly disable it even when a key exists.
NEXTDNS_ENABLED = bool(NEXTDNS_KEY) and os.environ.get(
    "NEXTDNS_ENABLED", "true"
).strip().lower() in {"1", "true", "yes", "on"}

def _load_token_sets():
    raw_value = os.environ.get("TOKEN_SETS_JSON", "").strip()
    if not raw_value:
        return [
            {
                "fetch_token": "",
                "app_transaction": "",
                "hash_params": "",
                "hash_headers": "",
                "is_sandbox": True,
            }
        ]

    try:
        token_sets = json.loads(raw_value)
    except json.JSONDecodeError as exc:
        raise RuntimeError("TOKEN_SETS_JSON must be valid JSON") from exc

    if not isinstance(token_sets, list) or not token_sets:
        raise RuntimeError("TOKEN_SETS_JSON must be a non-empty JSON array")

    normalized_sets = []
    for index, token_set in enumerate(token_sets, start=1):
        if not isinstance(token_set, dict):
            raise RuntimeError(f"TOKEN_SETS_JSON item #{index} must be an object")

        normalized_sets.append(
            {
                "fetch_token": str(token_set.get("fetch_token", "")),
                "app_transaction": str(token_set.get("app_transaction", "")),
                "hash_params": str(token_set.get("hash_params", "")),
                "hash_headers": str(token_set.get("hash_headers", "")),
                "is_sandbox": token_set.get("is_sandbox", True) is True,
            }
        )

    return normalized_sets


TOKEN_SETS = _load_token_sets()

ADMIN_ID = int(os.environ.get("ADMIN_ID", "6581326766"))
MAX_USERS = int(os.environ.get("MAX_USERS", "0"))
NUM_WORKERS = len(TOKEN_SETS)
DONATE_PHOTO = "AgACAgUAAxkBAAEhBOdpjtu4_D_90mzmM3ax-jLUQbW7HwACjA5rGyK6eFQz2Vzy6zHTMwEAAwIAA3kAAzoE"

E_LOADING = '<tg-emoji emoji-id="5350752364246606166">✍️</tg-emoji>'
E_LIMIT   = '<tg-emoji emoji-id="5424857974784925603">🚫</tg-emoji>'
E_SUCCESS = '<tg-emoji emoji-id="5260463209562776385">✅</tg-emoji>'
E_ERROR   = '<tg-emoji emoji-id="5318840353510408444">🔴</tg-emoji>'
E_TIP     = '<tg-emoji emoji-id="4968003407315993509">💡</tg-emoji>'
E_MENU    = '<tg-emoji emoji-id="5449601904147440135">👑</tg-emoji>'

E_USER    = '<tg-emoji emoji-id="5974048815789903111">👤</tg-emoji>'
E_ID      = '<tg-emoji emoji-id="5974526806995242353">🆔</tg-emoji>'
E_TAG     = '<tg-emoji emoji-id="5240228673738527951">🏷️</tg-emoji>'
E_STAT    = '<tg-emoji emoji-id="4967519884192777037">📊</tg-emoji>'
E_GLOBE   = '<tg-emoji emoji-id="5231489647946768652">🌐</tg-emoji>'
E_SOS     = '<tg-emoji emoji-id="6301027265899661025">🆘</tg-emoji>'
E_SHIELD  = '<tg-emoji emoji-id="5352888345972187597">🛡️</tg-emoji>'
E_CALENDAR = '<tg-emoji emoji-id="5413879192267805083">📅</tg-emoji>'
E_IOS     = '<tg-emoji emoji-id="5350556204500263431">🍏</tg-emoji>'
E_ANDROID = '<tg-emoji emoji-id="5303145396254563405">🤖</tg-emoji>'


DEFAULT_LANG = "VI"

TEXTS = {
    "VI": {
        "welcome": f"{E_SUCCESS} <b>Locket Gold Activator</b>\n\nChào mừng! Vui lòng chọn ngôn ngữ hoặc sử dụng menu bên dưới.",
        "menu_msg": f"{E_MENU} <b>Bảng Điều Khiển</b>\n\n👇 Bấm nút bên dưới để nhập Username kích hoạt Gold.",
        "btn_input": "🔑 Nhập User Locket",
        "btn_lang": "🌐 Đổi Ngôn Ngữ",
        "btn_help": "🆘 Hỗ Trợ",
        "prompt_input": f"{E_LOADING} Vui lòng nhập <b>Username</b> hoặc <b>Link Locket</b> của bạn vào tin nhắn trả lời bên dưới:",
        "lang_select": "🌐 Vui lòng chọn ngôn ngữ / Please select language:",
        "lang_set": f"{E_SUCCESS} Đã cài đặt ngôn ngữ: Tiếng Việt",
        "help_msg": (
            f"<b>{E_MENU} Danh Sách Lệnh:</b>\n\n"
            f"/start - Khởi động bot & Menu chính\n"
            f"/setlang - Đổi ngôn ngữ (VI/EN)\n"
            f"/help - Xem trợ giúp này\n\n"
            f"<b>{E_TIP} Cách dùng:</b>\n"
            f"1. Bấm nút '🔑 Nhập User Locket'\n"
            f"2. Điền Username hoặc Link\n"
            f"3. Bot sẽ kiểm tra và kích hoạt Gold.\n\n"
            f"⚠️ <b>Lưu ý:</b> Mỗi người dùng chỉ được kích hoạt tối đa <b>5 lần/ngày</b>."
        ),
        "resolving": f"{E_LOADING} <b>Đang phân giải UID...</b>",
        "not_found": f"{E_ERROR} Không tìm thấy User.",
        "limit_reached": (
            f"{E_LIMIT} Đã đạt giới hạn tối đa 5/5 lần hôm nay.\n"
            f"Vui lòng quay lại vào ngày mai nhé!\n\n"
            f"💬 Nếu muốn tăng giới hạn, hãy <a href='tg://user?id={ADMIN_ID}'>Liên hệ Admin</a>."
        ),
        "queue_almost": f"{E_LOADING} <b>Sắp đến lượt bạn!</b>\nCòn <b>2 người</b> nữa là đến lượt bạn. Hãy chuẩn bị sẵn sàng! 🚀",
        "admin_noti_sent": f"{E_SUCCESS} Đã gửi thông báo đến tất cả user.",
        "admin_reset": f"{E_SUCCESS} Đã reset lượt dùng cho user {{}}.",
        "admin_only": f"{E_ERROR} Bạn không có quyền sử dụng lệnh này.",
        "checking_status": f"{E_LOADING} <b>Đang kiểm tra Entitlement...</b>",
        "free_status": "Free (Chưa Active)",
        "gold_active": f"{E_SUCCESS} <b>Gold Đã Active</b> (Hết hạn: {{}})",
        "user_info_title": f"{E_USER} <b>User Information</b>",
        "btn_upgrade": "🚀 KÍCH HOẠT NGAY",
        "queued": f"{E_LOADING} <b>Đã thêm vào hàng chờ</b>\nTarget: <code>{{0}}</code>\nVị trí: <b>#{{1}}</b> (Còn {{2}} người trước bạn)...",
        "processing": (
            f"{E_LOADING} <b>⚡ SYSTEM EXPLOIT RUNNING...</b>\n"
            f"<pre>"
            f"[*] Target:  {{}}\n"
            f"[*] Method:  RevenueCat_Bypass_v2\n"
            f"[>] Action:  Injecting Malicious Receipt\n"
            f"[>] Status:  Bypassing Validation...\n"
            f"[?] Waiting: Server Response..."
            f"</pre>"
        ),
        "success_title": f"{E_SUCCESS} <b>KÍCH HOẠT THÀNH CÔNG</b>",
        "generating_dns": f"{E_SHIELD} Đang tạo Anti-Revoke DNS...",
        "fail_title": f"{E_ERROR} <b>Kích hoạt thất bại</b>",
        "dns_msg": (
            f"{E_SHIELD} <b>HƯỚNG DẪN CHỐNG VĂNG GOLD</b>:\n"
            f"Để giữ Gold ổn định và không bị văng, bạn nên cài DNS này:\n\n"
            f"{E_IOS} <b>iOS</b>: <a href='{{}}'>Nhấn vào đây để Cài</a>\n"
            f"(Mở bằng <b>Safari</b> -> Cho phép -> Cài đặt cấu hình)\n\n"
            f"{E_ANDROID} <b>Android</b>: <code>{{}}.dns.nextdns.io</code>\n"
            f"(Cài đặt → Mạng → DNS cá nhân)\n\n"
            f"{E_TIP} <b>Lưu ý</b>: Nếu không cài DNS, bạn có thể dùng nút <b>🔄 Làm Mới Gold</b> khi bị văng, nhưng chỉ được tối đa 5 lần/ngày!"
        ),
        "bot_full": (
            f"🚫 <b>Hệ thống đã đầy!</b>\n"
            f"Bot đã đạt giới hạn tối đa số lượng người dùng thử nghiệm.\n\n"
            f"💬 Vui lòng <a href='tg://user?id={ADMIN_ID}'>Liên hệ Admin</a> để được hỗ trợ thêm."
        ),
        "coche_msg": (
            f"🛠 <b>CƠ CHẾ HOẠT ĐỘNG CỦA HỆ THỐNG</b>\n\n"
            f"<b>1. Tại sao lại lên được Gold?</b>\n"
            f"Bên mình dùng chung một biên lai mua hàng hợp lệ từ Apple. Khi bạn nhập Locket, bot sẽ gửi biên lai này lên máy chủ Locket thay cho bạn. Locket nhận diện thành công và cấp Gold. Hoàn toàn không cần tài khoản iCloud của bạn!\n\n"
            f"<b>2. Tại sao cần cài NextDNS?</b>\n"
            f"Thỉnh thoảng app Locket sẽ kiểm tra chéo với máy chủ Apple xem iCloud của bạn có thật sự đã mua gói không. Nếu kiểm tra thất bại, bạn sẽ mất Gold. NextDNS hoạt động như một lá chắn, chặn app Locket gọi về Apple. Nhờ vậy, trạng thái Gold của bạn sẽ được giữ vĩnh viễn!"
        )
    },
    "EN": {
        "welcome": f"{E_SUCCESS} <b>Locket Gold Activator</b>\n\nWelcome! Please select your language or use the menu below.",
        "menu_msg": f"{E_MENU} <b>Control Panel</b>\n\n👇 Click the button below to enter Username.",
        "btn_input": "🔑 Input Locket User",
        "btn_lang": "🌐 Change Language",
        "btn_help": "🆘 Help",
        "prompt_input": f"{E_LOADING} Please enter your <b>Username</b> or <b>Locket Link</b> in the reply below:",
        "lang_select": "🌐 Please select language:",
        "lang_set": f"{E_SUCCESS} Language set: English",
        "help_msg": (
            f"<b>{E_MENU} Commands:</b>\n\n"
            f"/start - Main Menu\n"
            f"/setlang - Change Language\n"
            f"/help - Show this help\n\n"
            f"<b>{E_TIP} How to use:</b>\n"
            f"1. Click '🔑 Input Locket User'\n"
            f"2. Enter Username or Link\n"
            f"3. Bot will activate Gold.\n\n"
            f"⚠️ <b>Note:</b> You can only activate max <b>5 times/day</b>."
        ),
        "resolving": f"{E_LOADING} <b>Resolving UID...</b>",
        "not_found": f"{E_ERROR} User not found.",
        "limit_reached": (
            f"{E_LIMIT} You have reached the daily limit (5/5).\n"
            f"Please come back tomorrow!\n\n"
            f"💬 To increase your limit, please <a href='tg://user?id={ADMIN_ID}'>Contact Admin</a>."
        ),
        "queue_almost": f"{E_LOADING} <b>Almost your turn!</b>\n<b>2 people</b> ahead of you. Get ready! 🚀",
        "admin_noti_sent": f"{E_SUCCESS} Notification sent to all users.",
        "admin_reset": f"{E_SUCCESS} Usage reset for user {{}}.",
        "admin_only": f"{E_ERROR} You don't have permission.",
        "checking_status": f"{E_LOADING} <b>Checking Entitlements...</b>",
        "free_status": "Free (Inactive)",
        "gold_active": f"{E_SUCCESS} <b>Gold Active</b> (Exp: {{}})",
        "user_info_title": f"{E_USER} <b>User Information</b>",
        "btn_upgrade": "🚀 ACTIVATE NOW",
        "queued": f"{E_LOADING} <b>Added to Queue</b>\nTarget: <code>{{0}}</code>\nPosition: <b>#{{1}}</b> ({{2}} people ahead)...",
        "processing": (
            f"{E_LOADING} <b>⚡ SYSTEM EXPLOIT RUNNING...</b>\n"
            f"<pre>"
            f"[*] Target:  {{}}\n"
            f"[*] Method:  RevenueCat_Bypass_v2\n"
            f"[>] Action:  Injecting Malicious Receipt\n"
            f"[>] Status:  Bypassing Validation...\n"
            f"[?] Waiting: Server Response..."
            f"</pre>"
        ),
        "success_title": f"{E_SUCCESS} <b>ACTIVATION SUCCESSFUL</b>",
        "generating_dns": f"{E_SHIELD} Generating Anti-Revoke DNS...",
        "fail_title": f"{E_ERROR} <b>Activation Failed</b>",
        "dns_msg": (
            f"{E_SHIELD} <b>ANTI-REVOKE INSTRUCTIONS</b>:\n"
            f"To keep Gold stable and prevent frequent revokes, you should install this DNS:\n\n"
            f"{E_IOS} <b>iOS</b>: <a href='{{}}'>Click to Install</a>\n"
            f"(Open in <b>Safari</b> -> Allow -> Install Profile)\n\n"
            f"{E_ANDROID} <b>Android</b>: <code>{{}}.dns.nextdns.io</code>\n"
            f"(Settings → Network → Private DNS)\n\n"
            f"{E_TIP} <b>Note</b>: If you don't install DNS, you can use the <b>🔄 Refresh Gold</b> button when revoked, but it's limited to 5 times/day!"
        ),
        "bot_full": (
            f"🚫 <b>System Full!</b>\n"
            f"The bot has reached its maximum capacity of test users.\n\n"
            f"💬 Please <a href='tg://user?id={ADMIN_ID}'>Contact Admin</a> for support."
        ),
        "coche_msg": (
            f"🛠 <b>SYSTEM MECHANISM</b>\n\n"
            f"<b>1. How do you get Gold?</b>\n"
            f"We use a shared valid Apple receipt. The bot submits this receipt to Locket's servers on your behalf to unlock Gold. We do NOT need your iCloud account!\n\n"
            f"<b>2. Why do you need NextDNS?</b>\n"
            f"Sometimes the Locket app cross-checks with Apple servers. If it does, you will lose Gold. NextDNS acts as a shield, blocking Locket from reaching Apple. This ensures your Gold status remains permanent!"
        )
    }
}


def T(key, lang=None):
    if not lang:
        lang = DEFAULT_LANG
    return TEXTS.get(lang, TEXTS["VI"]).get(key, key)
