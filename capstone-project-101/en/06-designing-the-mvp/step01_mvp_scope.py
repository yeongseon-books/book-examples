from __future__ import annotations
from common import assert_offline

def run() -> dict[str, object]:
    assert_offline({'use_network': False})
    return {'flow': 'register -> upload -> share', 'out': ['payment', 'i18n', 'admin'], 'demo': ['login_demo_user', 'upload_sample', 'show_share_link'], 'success': {'happy_path': '<= 60s', 'errors': 0}, 'form': ['clarity', 'speed', 'value']}

if __name__ == '__main__':
    print(run())
