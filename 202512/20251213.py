# https://leetcode.com/problems/coupon-code-validator/


class Solution:
    """3606. Coupon Code Validator

    You are given three arrays of length `n` that describe the properties of `n`
    coupons: `code`, `business_line`, and `is_active`. The `ith` coupon has:

    * `code[i]`: a **string** representing the coupon identifier.

    * `business_line[i]`: a **string** denoting the business category of the coupon.

    * `is_active[i]`: a **boolean** indicating whether the coupon is currently active.

    A coupon is considered **valid** if all of the following conditions hold:

    1. `code[i]` is non-empty and consists only of alphanumeric characters (a-z, A-Z,
    0-9) and underscores (`_`).

    2. `business_line[i]` is one of the following four categories: `"electronics"`,
    `"grocery"`, `"pharmacy"`, `"restaurant"`.

    3. `is_active[i]` is **true**.

    Return an array of the **codes** of all valid coupons, **sorted** first by their
    **business_line** in the order: `"electronics"`, `"grocery"`, `"pharmacy",
    "restaurant"`, and then by **code** in lexicographical (ascending) order within each
    category."""

    def validate_coupons(
        self, code: list[str], business_line: list[str], is_active: list[bool]
    ) -> list[str]: ...

    validateCoupons = validate_coupons
