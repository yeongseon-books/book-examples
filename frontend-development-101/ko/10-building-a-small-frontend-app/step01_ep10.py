"""Frontend Development 101 - 10편: building a small frontend app 예제."""

from __future__ import annotations

from common import BundleSimulator, ComponentSim, FormValidator, MockFetch, RouterSim


def render_note(props: dict[str, object], state: dict[str, object]) -> str:
    """Render note."""
    return f"notes={len(state['notes'])} title={props['title']}"


def run_demo() -> dict[str, object]:
    """데모를 실행합니다."""
    router = RouterSim({"/": lambda _: "notes", "/notes/:id": lambda p: p["id"]})
    fetch = MockFetch({"/notes": {"items": [{"id": "1", "title": "A"}]}})
    data = fetch.get("/notes")
    comp = ComponentSim(
        props={"title": "notes"}, state={"notes": data["items"]}, renderer=render_note
    )
    validator = FormValidator()
    bundle = BundleSimulator()
    out = bundle.minify(bundle.concat(["const app=1;", "console.log(app);"]))
    return {
        "route": router.navigate("/notes/1"),
        "render": comp.render(),
        "email_error": validator.validate_email("user@example.com"),
        "bundle_size": len(out),
    }
