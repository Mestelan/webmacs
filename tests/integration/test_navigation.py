from webmacs import buffers, current_window

from PyQt5.QtTest import QTest


def test_navigate_new_buffer(session):
    """
    navigate in new buffer.
    """
    session.load_page("navigation")

    def sorted_buff_titles():
        return sorted(b.title() for b in buffers())

    assert sorted_buff_titles() == ["navigation"]

    session.wkeyclicks("C-u f")

    session.check_js_follow_element_selected(
        "document.getElementById('link1')"
    )

    session.wkeyclicks("Enter")

    def new_buffer_loaded():
        return sorted_buff_titles() == ["link one", "navigation"]

    assert session.wait_until(new_buffer_loaded, 5.0)
