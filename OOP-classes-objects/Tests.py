def run_tests (shirt_one, shirt_two, total_cost, total_discount):
    # unit test to check the working of shirt class.
    assert shirt_one.price == 10, 'shirt one price is 10'
    assert shirt_one.color == 'red', 'shirt one should be red'
    assert shirt_one.style == 'long-sleeve', 'shirt one should be long sleeve in color'
    assert shirt_one.size == 'S', 'shirt one should be of Size S'

    assert shirt_two.price == 10, 'shirt two price is 10'
    assert shirt_two.color == 'orange', 'shirt two is orange'
    assert shirt_two.style == 'short_sleeve', 'shirt two is short_sleeve'
    assert shirt_two.size == 'L', 'shirt two is of size L'

    assert total_cost == 20, 'The total cost should be 20'
    assert round(total_discount) == 18, 'total discount should be 18.0'