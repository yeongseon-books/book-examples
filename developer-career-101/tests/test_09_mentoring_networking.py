from tests.test_01_what_is_developer_career import load


def test_09_recommends_oldest_contact():
    mod = load("09-mentoring-networking.py")
    contacts = [
        mod.Contact("A", priority=5, days_since_touch=10),
        mod.Contact("B", priority=3, days_since_touch=45),
        mod.Contact("C", priority=10, days_since_touch=20),
    ]
    recommended = mod.recommend_follow_up(contacts)
    assert recommended.name == "B"
