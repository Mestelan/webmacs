from webmacs import buffers


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


def test_navigate_follow_hinting(session):
    session.load_page("navigation")

    assert session.buffer.title() == "navigation"

    session.wkeyclicks("f")

    # wait for the first element to be selected
    session.check_js_follow_element_selected(
        "document.getElementById('link1')"
    )

    session.keyclicks("two")

    # now wait for the second element to be selected
    session.check_js_follow_element_selected(
        "document.getElementById('link2')"
    )

    session.wkeyclicks("Enter")

    assert session.wait_until(
        lambda: session.buffer.title() == "link two"
    )


def test_navigate_follow_hinting_numbers(session):
    session.load_page("navigation")

    assert session.buffer.title() == "navigation"

    session.wkeyclicks("f")

    # wait for the first element to be selected
    session.check_js_follow_element_selected(
        "document.getElementById('link1')"
    )

    session.keyclicks("2")

    # now wait for the second element to be selected
    session.check_js_follow_element_selected(
        "document.getElementById('link2')"
    )

    session.wkeyclicks("Enter")

    assert session.wait_until(
        lambda: session.buffer.title() == "link two"
    )
