from ko.ep01_design_overview import bad_order_processor, good_order_processor


def test_ep01_bad_and_good_same_output() -> None:
    order = {"id": "A1", "items": [{"price": 100, "qty": 2}, {"price": 50, "qty": 1}]}
    assert bad_order_processor(order) == good_order_processor(order)
